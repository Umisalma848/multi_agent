# ResearchMind – Multi-Agent AI Research Assistant

ResearchMind is a multi-agent AI research assistant built using LangChain, OpenAI, and Tavily Search API. It autonomously searches the web, extracts meaningful information, generates research reports, and reviews outputs through specialized AI agents working together in a unified pipeline.
<img width="1511" height="899" alt="Screenshot 2026-05-15 121642" src="https://github.com/user-attachments/assets/9017956f-1fa4-49e5-be7d-155455a70339" />

---

## 🚀 Features

* Multi-Agent AI Workflow
* Real-Time Web Research
* AI Generated Research Reports
* Web Scraping & Content Extraction
* Critic Review System
* LangChain LCEL Pipelines
* `.env` API Key Support

---

## 🛠️ Tech Stack

* Python
* LangChain
* OpenAI API
* Tavily Search API
* BeautifulSoup
* dotenv

---

## 📂 Project Structure

```bash
ResearchMind/
│
├── .venv/
├── __pycache__/
├── .env
├── agents.py
├── pipelines.py
├── tools.py
├── app.py
├── requirements.txt
└── README.md
```

---

## 🔄 Project Flow

```text
User Query
    ↓
Search Agent
    ↓
Reader Agent
    ↓
Writer Agent
    ↓
Critic Agent
    ↓
Final Research Report
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/multi_agent.git

cd multi_agent
```

---

### 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Create `.env` File

```env
OPENAI_API_KEY=your_openai_api_key

TAVILY_API_KEY=your_tavily_api_key
```

---

### 5️⃣ Run the Project

```bash
python app.py
```

---

## 🚫 `.gitignore`

```gitignore
.venv/
__pycache__/
.env
```

---

## 📤 Push Project to GitHub

```bash
git init

git add .

git commit -m "Initial commit"

git branch -M main

git remote add origin https://github.com/your-username/ResearchMind.git

git push -u origin main
```

---

## 💡 Use Cases

* Academic Research
* Market Trend Analysis
* AI & Tech Research
* Open Source Project Analysis
* Business Intelligence
* Automated Report Generation

---

## 🧪 Example Topics

* Future of AI Agents
* Quantum Computing
* Cybersecurity Trends
* Renewable Energy
* CRISPR Gene Editing

---

## ❌ Common Errors

### Missing API Key

```bash
OpenAIError: Missing API Key
```

Add keys inside `.env`.

---

### Environment Not Activated

```bash
ModuleNotFoundError
```

Activate `.venv` before running the project.

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 👨‍💻 Author

Built using LangChain and Agentic AI concepts.
