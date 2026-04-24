# Pomodoro Rocks 🍅💎

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Pomodoro Rocks** is a pro-active health and productivity assistant for Windows. It's not just a timer; it's an AI-driven agent that understands your personal and professional life to help you stay focused, healthy, and on track.

## 🚀 Key Features

- **Adaptive Scheduling:** Automatically recalculates Pomodoro sessions based on your Google Calendar and MS Teams meetings.
- **Hard-Block Awareness:** Native respect for fixed daily duties (e.g., family time, lunch breaks).
- **Proactive Health Routine:** AI-generated active breaks (hydration, mobility, eye exercises) to combat sedentary work.
- **Multi-LLM Intelligence:** Powered by Gemini, OpenAI, and DeepSeek with automatic fallback and rotation.
- **Minimalist UI:** Modern Dark Mode interface that lives in your System Tray, staying out of your way until needed.
- **Multimodal Context:** Upload screenshots of your schedule or chat directly with the assistant to reschedule your day.

## 🏗️ Architecture

- **Core Daemon:** Background process managing state, time, and activity monitoring.
- **Frontend:** Modern UI built with `CustomTkinter`.
- **Database:** Local SQLite with WAL mode for robust, concurrent data handling.
- **AI Router:** Intelligent enforcer for LLM API management and fallback logic.

## 🛠️ Tech Stack

- **Language:** Python 3.11+
- **Database:** SQLAlchemy 2.0 / SQLite
- **GUI:** CustomTkinter / Pystray
- **Monitoring:** pynput (Mouse/Keyboard Activity)
- **AI:** Google Generative AI, OpenAI SDK

## 📥 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/danroncallo/pomodoro-rocks.git
   cd pomodoro-rocks
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Testing

Run the suite of deterministic tests using pytest:
```bash
python -m pytest
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Created with ❤️ by **jaguardluz** - Standard Jaguar v3.1*
