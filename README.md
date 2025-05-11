# 🧠 MindfulAI – AI-Powered Mental Health Support Platform

![MindfulAI Banner](https://img.shields.io/badge/Powered%20By-Gemini%20API-blueviolet?style=for-the-badge)  
> An intelligent and empathetic web application providing mental health support through advanced AI conversations, emotional analysis, and user assistance.

---

## 🌐 Live Demo

🌍 [Visit MindfulAI Now](https://mindfulai-cggh.onrender.com)



---

## ✨ Features

- 🤖 **AI-Powered Chatbot**: Mental health conversation support using Gemini API.
- 💬 **Emotion Detection**: Analyzes user inputs to assess emotional state.
- 🧾 **Insightful Recommendations**: Offers mood-based feedback and mental health tips.
- 🔐 **Secure Authentication**: User login & registration with Supabase.
- 👤 **User Dashboard**: Personalized space for users to track emotional trends and history.
- 📄 **Auto Documentation Generator**: AI-based generation of project documentation.
- 🌙 **Dark Mode + Glassmorphism UI**: Elegant and calming design theme.

---

## 📁 Tech Stack

| Layer        | Technology                           |
|--------------|---------------------------------------|
| Frontend     | HTML, CSS, JavaScript                 |
| Backend      | Python (Flask)                        |
| Database     | Supabase (PostgreSQL)                 |
| AI/ML        | Gemini API, OpenRouter                |
| Deployment   | Render                                |

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.10+
- `pip` package manager
- Supabase project & API keys
- Gemini API key

### 🛠️ Installation

```bash
# Clone the repo
git clone https://github.com/thelokesha/mindfulAI.git
cd mindfulAI

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 🔑 Set Environment Variables

Create a `.env` file in the root directory with:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
GEMINI_API_KEY=your_gemini_key
```

---

## 🧠 Usage

1. Run the Flask server:

```bash
python app.py
```

2. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.
3. Register or log in to begin chatting with the AI.

---

## 🗃️ Project Structure

```
mindfulAI/
│
├── static/                 # CSS, JS, assets
├── templates/              # HTML files (login, register, chat, etc.)
├── create_documentation.py
├── gemini_client.py        # Gemini API logic
├── openrouter_client.py    # Alternate AI integration
├── app.py                  # Main Flask application
├── main.py                 # Utility and routing
├── create_supabase_tables.py
├── requirements.txt
└── README.md
```

---

## 📄 Documentation

📘 [MindfulAI_Documentation.pdf](./MindfulAI_Documentation.pdf) – Learn more about the system architecture, logic flow, and development.

---

## 🤝 Contributing

We welcome contributions! Feel free to:

- Fork the repository
- Make your changes
- Submit a pull request

---

## 📫 Contact
📧 Email: lokesharumugam1826@gmail.com 

---

## 💖 Support

If you find this project helpful, give it a ⭐ and share it with your peers!
