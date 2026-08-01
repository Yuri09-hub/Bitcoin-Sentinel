# ₿ Bitcoin Sentinel

Bitcoin Sentinel is a Python-based cryptocurrency price monitoring tool that continuously tracks the current Bitcoin price and automatically sends an email notification whenever a price change is detected.

This project was built to practice web scraping, task scheduling, email automation, and secure credential management in Python.

## Features

* Real-time Bitcoin price monitoring
* Automated web scraping using **Requests** and **BeautifulSoup**
* Scheduled price checks using **Schedule**
* Email notifications when the Bitcoin price changes
* Secure credential management using **.env** environment variables
* Simple and lightweight implementation

## Technologies

* Python 3
* Requests
* BeautifulSoup4
* Schedule
* python-dotenv
* smtplib

## Project Structure

```text
Bitcoin-Sentinel/
│
├── main.py
├── web_scraper.py
├── notification.py
├── .env.example
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Yuri09-hub/Bitcoin-Sentinel.git
cd Bitcoin-Sentinel
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root.

Example:

```env
EMAIL=your_email@gmail.com
PASSWORD=your_app_password
```

> **Note:** If you are using Gmail, generate an **App Password** from your Google Account instead of using your regular account password.

## Usage

Run the application:

```bash
python main.py
```

The program will periodically check the current Bitcoin price and automatically send an email notification whenever a change is detected.

## Disclaimer

This project is intended for educational purposes and personal learning. Please respect the terms of service of any website you scrape.

## Author

**Yuri Rodrigues**

GitHub: https://github.com/Yuri09-hub

