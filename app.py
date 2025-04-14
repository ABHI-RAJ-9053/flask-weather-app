from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = '2fe93482c24a616dd419fa9084126a4c'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city'].strip()
    if not city:
        return render_template('index.html', error="Please enter a city name.")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    print("API URL:", url)  # Debug URL

    response = requests.get(url)
    print("Status Code:", response.status_code)  # Debug status
    print("Response JSON:", response.text)       # Raw response

    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'].title(),
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'icon': data['weather'][0]['icon']  # 🔥 This line passes the icon code!
        }
        return render_template('weather.html', weather=weather)
    else:
        return render_template('index.html', error=f"City '{city}' not found. Please try again.")

if __name__ == '__main__':
    app.run(debug=True)
