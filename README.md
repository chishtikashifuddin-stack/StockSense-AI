# 📈 StockPulse AI

## 📌 Project Overview
StockPulse AI is a Python-based intelligent stock market monitoring system that tracks live stock data using financial APIs. The application automatically identifies the highest-performing stock of the day, generates voice-based announcements using Text-to-Speech (TTS), and triggers sound alerts for important updates.

This project combines finance, automation, AI, and voice technology into a smart assistant for traders, investors, and stock market enthusiasts.

---

# 🚀 Features

- 📊 Real-time stock market monitoring
- 📈 Tracks multiple popular US stocks
- 🔍 Automatically finds the highest-performing stock
- 🔔 Sound alert system using `winsound`
- 🗣️ Voice announcements using `pyttsx3`
- ⚡ Live financial data from APIs
- 🤖 Automated market update assistant

---

# 🛠️ Technologies Used

- Python
- Requests Library
- pyttsx3 (Text-to-Speech)
- winsound
- REST API
- JSON

---

# 📂 Project Workflow

1. Fetches stock market data using the EOD Historical Data API.
2. Reads the previous day’s stock prices.
3. Compares selected stocks automatically.
4. Identifies the highest closing stock.
5. Generates a voice announcement.
6. Triggers an alert sound notification.

---

# 📋 Stock List

- AAPL
- MSFT
- GOOGL
- TSLA
- AMZN
- META
- NVDA
- NFLX

---

# ▶️ Installation

## Install Required Libraries

```bash
pip install requests pyttsx3
