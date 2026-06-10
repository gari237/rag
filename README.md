# 🧠 RAG Universel — Interrogez n'importe quel Document en Langage Naturel

> Projet de fin de cycle Bachelor · IPSA Paris · Spécialisation IA & Data Science

[![Demo Live](https://img.shields.io/badge/Demo-Live-brightgreen?style=for-the-badge)](https://a7dazunxhneyamzft4sax6.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-deployed-red?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![FAISS](https://img.shields.io/badge/Vector%20Store-FAISS-purple?style=for-the-badge)](https://faiss.ai)

---

## 📌 Présentation

**RAG Universel** est un système de Retrieval-Augmented Generation (RAG) permettant d'interroger n'importe quel document (PDF, DOCX, TXT) en langage naturel. Il combine la recherche sémantique par embeddings, un index vectoriel FAISS, et la génération LLM via Groq pour fournir des réponses précises avec citation des sources.

---

## 🏗️ Architecture RAG

```
Document (PDF / DOCX / TXT)
         │
         ▼
┌─────────────────┐
│   Extraction    │  Parsing et découpage en chunks
│   du texte      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Embeddings    │  sentence-transformers → vecteurs sémantiques
│   sémantiques   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Index FAISS    │  Stockage et recherche vectorielle rapide
└────────┬────────┘
         │
  Question utilisateur
         │
         ▼
┌─────────────────┐
│  Retrieval      │  Top-k chunks les plus pertinents
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Génération LLM │  Groq API · Llama 3.1 → réponse + sources citées
└─────────────────┘
         │
         ▼
   Interface Streamlit
```

---

## ✨ Fonctionnalités

- 📄 **Multi-formats** : PDF, DOCX et TXT acceptés
- 🔍 **Recherche sémantique** : embeddings par `sentence-transformers`
- ⚡ **Index FAISS** : recherche vectorielle rapide même sur de grands documents
- 🤖 **Génération LLM** : réponses naturelles via Groq / Llama 3.1
- 📎 **Citation des sources** : chaque réponse indique les passages du document utilisés
- 🌐 **Interface intuitive** : upload, question, réponse en quelques secondes

---

## ⚙️ Stack Technique

| Composant            | Technologie                        |
|----------------------|------------------------------------|
| Interface            | Streamlit                          |
| Embeddings           | sentence-transformers              |
| Index vectoriel      | FAISS                              |
| LLM                  | Groq API · Llama 3.1               |
| Parsing documents    | PyPDF2 · python-docx               |
| Versioning           | Git / GitHub                       |

---

## 🚀 Installation & Lancement Local

```bash
# 1. Cloner le dépôt
git clone https://github.com/gari237/rag-universel
cd rag-universel

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate   # Windows : venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer la clé API
echo "GROQ_API_KEY=your_key_here" > .env

# 5. Lancer l'application
streamlit run app.py
```

---

## 🔑 Variables d'Environnement

| Variable       | Description                      |
|----------------|----------------------------------|
| `GROQ_API_KEY` | Clé API Groq (obligatoire)       |

---

## 📁 Structure du Projet

```
rag-universel/
├── app.py                  # Interface Streamlit principale
├── rag/
│   ├── loader.py           # Extraction texte (PDF, DOCX, TXT)
│   ├── embeddings.py       # Génération des embeddings sémantiques
│   ├── index.py            # Construction et requêtage index FAISS
│   └── generator.py        # Génération LLM avec citation des sources
├── requirements.txt
├── .env.example
└── README.md
```

---

## 💡 Exemple d'Utilisation

1. Uploader un document PDF (rapport, cours, contrat…)
2. Poser une question en français ou en anglais
3. Obtenir une réponse précise avec les passages sources mis en évidence

**Exemple :**
> Document : Rapport annuel d'une entreprise (PDF, 80 pages)  
> Question : *"Quel est le chiffre d'affaires du segment cloud en 2023 ?"*  
> Réponse : *"Selon la page 34, le segment cloud a généré 2,4 Md€ en 2023, en hausse de 18% par rapport à l'exercice précédent."*

---

## 🌐 Lien

| Ressource     | URL                                                       |
|---------------|-----------------------------------------------------------|
| Demo live     | https://a7dazunxhneyamzft4sax6.streamlit.app/             |

---

## 👨‍💻 Auteur

**Garisson Willfrid Kammognie**  
Bachelor Aéronautique · Spécialisation IA & Data Science · IPSA Paris  
📧 kammogniegarissonwillfrid@gmail.com  
🔗 [Portfolio](https://gari237.github.io/garisson-willfrid.github.io-/) · [LinkedIn](https://www.linkedin.com/in/garisson-willfrid-kammognie-774a45341) · [GitHub](https://github.com/gari237)

---

*Disponible pour stage immédiat (3–4 mois) et alternance dès septembre 2026 en Île-de-France.*
