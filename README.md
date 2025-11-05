# 🧾 INSURANCE_CHATBOT

## 📖 About  
**INSURANCE_CHATBOT** is a Python-based conversational AI system designed to answer insurance-related queries.  
It loads insurance PDF documents, retrieves relevant information, and generates user-friendly responses using a **Retrieval-Augmented Generation (RAG)** approach.

---

## 🚀 Features  
- 📂 Load and process multiple insurance PDF documents  
- 🔍 Retrieve relevant sections using document embeddings  
- 💬 Generate human-like answers to user queries  
- ⚙️ Modular structure (Loader, Retriever, RAG Chain, Main)  
- 🧠 Easy to extend with new documents or models  

---

## 🧱 Project Structure  
INSURANCE_CHATBOT/
│
├── main.py # Main entry point for chatbot execution
├── pdf_loader.py # Extracts and preprocesses text from PDFs
├── retriever.py # Builds vector store and retrieves relevant info
├── rag_chain.py # Combines retrieval + generation logic
├── insurance_docs.txt # Metadata or list of insurance documents
├── CHOTGDP23004V012223.pdf
├── EDLHLGA23009V012223.pdf
├── HDFHLIP23024V072223.pdf
├── ICIHLIP22012V012223.pdf
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/Aadityaramrame/INSURANCE_CHATBOT.git
cd INSURANCE_CHATBOT
2️⃣ Create and activate a virtual environment
bash
Copy code
python -m venv venv
# Activate
venv\Scripts\activate        # (Windows)
source venv/bin/activate     # (macOS/Linux)
3️⃣ Install dependencies
(Make sure requirements.txt is present or install manually)

bash
Copy code
pip install -r requirements.txt
4️⃣ Run the chatbot
bash
Copy code
python main.py
🧩 How It Works
PDF Loading → pdf_loader.py extracts and cleans text from uploaded insurance documents.

Retrieval → retriever.py embeds and indexes the document text for efficient search.

RAG Pipeline → rag_chain.py retrieves the most relevant text chunks and combines them with a generative model to form an accurate, human-like response.

Interaction → main.py orchestrates the flow, taking user queries and returning context-aware answers.

💡 Usage Tips
Ensure your PDFs are readable (not scanned as pure images).

For better results, add more comprehensive insurance documents.

You can modify retrieval parameters for improved accuracy.

Experiment with different embedding models or chunk sizes.

🧠 Possible Enhancements
🖥️ Web UI using Flask or Streamlit

🧾 Add support for DOCX/HTML documents

💬 Maintain chat history for contextual responses

🧩 Integrate LLM APIs (like OpenAI, Cohere, or HuggingFace)

🧰 Add evaluation metrics for retrieval and generation accuracy

👥 Contributing
Contributions are welcome!

Fork the repo

Create a new branch: git checkout -b feature-name

Commit changes: git commit -m "Added new feature"

Push branch: git push origin feature-name

Submit a Pull Request 🚀

📜 License
This project is open-source. (Add your license here, e.g., MIT or Apache 2.0)

🧩 Authors
Aaditya Ramrame and contributors

⭐ If you found this helpful, consider starring the repo!
🔗 GitHub Repository
