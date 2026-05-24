import os
import streamlit as st
import numpy as np
import faiss
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader
from docx import Document
from sentence_transformers import SentenceTransformer

load_dotenv()

model = SentenceTransformer("all-MiniLM-L6-v2")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="RAG Universel", page_icon="🧠", layout="wide")
st.title("🧠 RAG Universel")
st.markdown("Upload un document **PDF, DOCX ou TXT** et pose tes questions.")
st.divider()

def extraire_texte(fichier):
    nom = fichier.name.lower()
    if nom.endswith(".pdf"):
        reader = PdfReader(fichier)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    elif nom.endswith(".docx"):
        doc = Document(fichier)
        return "\n".join(p.text for p in doc.paragraphs)
    elif nom.endswith(".txt"):
        return fichier.read().decode("utf-8")
    return ""

def decouper_texte(texte, taille=500, chevauchement=50):
    mots = texte.split()
    chunks = []
    i = 0
    while i < len(mots):
        chunks.append(" ".join(mots[i:i+taille]))
        i += taille - chevauchement
    return chunks

def construire_index(chunks):
    embeddings = model.encode(chunks)
    embeddings = np.array(embeddings).astype("float32")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index

def chercher_contexte(question, chunks, index, k=4):
    q_vec = model.encode([question]).astype("float32")
    _, indices = index.search(q_vec, k)
    return "\n\n".join(chunks[i] for i in indices[0] if i < len(chunks))

def repondre(question, contexte):
    prompt = f"""Tu es un assistant expert. Réponds uniquement avec le contexte fourni.
Si la réponse n'est pas dans le contexte, dis-le clairement.

CONTEXTE:
{contexte}

QUESTION: {question}

RÉPONSE:"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    return response.choices[0].message.content

fichier = st.file_uploader("📂 Uploade ton document", type=["pdf", "docx", "txt"], key="upload_doc")

if fichier:
    with st.spinner("📖 Lecture et indexation en cours..."):
        texte = extraire_texte(fichier)
        if not texte.strip():
            st.error("❌ Impossible d'extraire le texte.")
            st.stop()
        chunks = decouper_texte(texte)
        index = construire_index(chunks)

    st.success(f"✅ Document prêt — {len(chunks)} segments créés.")

    with st.sidebar:
        st.header("📊 Infos document")
        st.write(f"**Fichier :** {fichier.name}")
        st.write(f"**Segments :** {len(chunks)}")
        st.write(f"**Caractères :** {len(texte):,}")

    st.divider()
    st.subheader("💬 Pose ta question")

    question = st.text_input("Ta question :", placeholder="Ex: Quels sont les points principaux ?")

    if question:
        with st.spinner("🤖 Génération de la réponse..."):
            contexte = chercher_contexte(question, chunks, index)
            reponse = repondre(question, contexte)

        st.markdown("### 🤖 Réponse")
        st.write(reponse)

        with st.expander("📄 Passages sources utilisés"):
            st.text(contexte)