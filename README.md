# StockSense AI

## Project Overview

StockPulse AI is a Python-based intelligent stock market monitoring system that tracks live stock data using financial APIs. The application automatically identifies the highest-performing stock of the day, generates voice-based announcements using Text-to-Speech (TTS), and triggers sound alerts for important updates.

This project combines finance, automation, artificial intelligence, and voice technology into a single intelligent assistant designed for traders, investors, and stock market analysis.

---
## Author

**Kashifuddin Chishti**

Developer of StockPulse AI – a Python-based intelligent stock market monitoring and voice assistant system.

## Features

- Real-time stock market monitoring  
- Tracks multiple major US stocks  
- Automatically identifies the highest-performing stock  
- Audio alert system using `winsound`  
- Voice announcements using `pyttsx3`  
- Live financial data integration using APIs  
- Automated market analysis and reporting  

---

## Technologies Used

- Python  
- Requests Library  
- pyttsx3 (Text-to-Speech)  
- winsound  
- REST API  
- JSON  

---

## Project Workflow

1. Fetch stock market data using the EOD Historical Data API.  
2. Retrieve previous day stock prices.  
3. Compare selected stock performance.  
4. Identify the highest closing stock.  
5. Generate a voice-based announcement.  
6. Trigger an audio alert notification.  

---

## Stock List

- AAPL  
- MSFT  
- GOOGL  
- TSLA  
- AMZN  
- META  
- NVDA  
- NFLX  

---

## Installation

Install required dependencies:

```bash
pip install requests pyttsx3
