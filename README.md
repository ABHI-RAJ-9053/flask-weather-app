# 🌤️ Flask Weather App

A simple and interactive web application built with **Flask** that displays real-time weather information for any city using the **OpenWeatherMap API**. Styled with **Bootstrap 5** and includes animations like a scrolling city banner.

---

## 📖 Project Description

This Flask Weather App allows users to fetch and view live weather updates for any city in the world. It connects to the OpenWeatherMap API and returns real-time data such as temperature, weather conditions, humidity, and wind speed. The app is built with a clean and modern UI using Bootstrap, and features a smooth scrolling ticker showing major cities across the globe. It’s designed to be simple, responsive, and beginner-friendly.

This was developed as a hands-on project to learn backend integration, API consumption, and deployment practices.

---

## 🚀 Features

- 🌍 Search weather by city name
- 🌡️ Real-time temperature, humidity, wind speed & description
- 🧭 Responsive design using Bootstrap 5
- 🏙️ Scrolling list of popular cities
- 🔥 Deployed using Render (Free Hosting)

---

## 🖥️ Preview

![App Screenshot : 1](flask-weather-app/preview_01.png)

> ✅ Live Demo: [https://430c5613-d76e-48a8-9922-bb43670396a2-00-2ij5gez8vwiqe.sisko.replit.dev/)

---

## 🛠️ Tech Stack

- Python 3
- Flask
- HTML, CSS (Bootstrap 5)
- OpenWeatherMap API
- Gunicorn (for deployment)

---

## 📦 Setup Instructions

### 🔧 Prerequisites

- Python 3.x
- `pip` installed

## 🗂️ Project Structure

flask-weather-app/
│
├── static/
│   └── styles.css          # Custom CSS styles (optional)
│
├── templates/
│   ├── index.html          # Home page with city input
│   └── weather.html        # Weather results display
│
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Procfile                # For deployment on Render
└── README.md               # Project documentation


### 💻 Local Setup

```bash
git clone https://github.com/your-username/flask-weather-app.git
cd flask-weather-app
pip install -r requirements.txt
python app.py
