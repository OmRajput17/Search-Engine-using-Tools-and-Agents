# 🌐 LangChain – Chat with Search  

An **AI-powered conversational assistant** built with **Streamlit, LangChain, and Groq LLMs**, capable of performing real-time searches across **Google, Wikipedia, and Arxiv**. The system uses a **ReAct agent** to dynamically choose the right tool, summarize retrieved content, and maintain a natural chat flow with session-based memory.  

---

## 🚀 Features  
- 💬 Interactive **chat interface** with Streamlit.  
- 🔎 Integration with **Google Search, Wikipedia, and Arxiv** for live knowledge retrieval.  
- 🧠 **LangChain Zero-Shot ReAct Agent** for intelligent tool selection.  
- ⚡ Powered by **Groq LLaMA 3.1 model** for fast and coherent responses.  
- 📚 Summarized outputs for concise, digestible answers.  
- 🔄 Session-based memory for continuous conversation.  
- 🔐 Secure API key handling with `.env` file.  

---

## 🛠 Tech Stack  
- **LLM**: [Groq LLaMA 3.1](https://groq.com/)  
- **Framework**: [LangChain](https://www.langchain.com/)  
- **Frontend/UI**: [Streamlit](https://streamlit.io/)  
- **Tools**: Google Search, Wikipedia, Arxiv  
- **Environment Management**: `python-dotenv`  

---

## 📖 How It Works  
1. User submits a query in the chat interface.  
2. The **LangChain Agent** decides which tool to call (Google, Wikipedia, or Arxiv).  
3. Retrieved content is processed and summarized by the Groq LLM.  
4. Response is displayed in a natural conversational format, while memory is preserved for context.  

---

## ⚡ Installation  

```bash
# Clone the repository
git clone https://github.com/your-username/langchain-chat-search.git
cd langchain-chat-search

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

# Install dependencies
pip install -r requirements.txt
