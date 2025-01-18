# server.py or main.py is a common name for the server/main module in a flask web app
from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

# make your app a Flask app
app = Flask(__name__)


# routes in Flask
@app.route("/")  # home page
# frequently, will access home page if you go to '/index' or '/index.html'
@app.route("/index")


# define a function that returns something for the route
def index():
    return render_template("index.html")


# handle weather route
@app.route("/weather")
def get_weather():
    # get the form data - city
    city = request.args.get("city")
    # get form data - country
    country = request.args.get("country")
    weather_data = get_current_weather(city, country)
    return render_template(
        "weather.html",
        title=weather_data["name"],
        country=country,
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
    )


# make it a module
if __name__ == "__main__":
    # run on locahost port 8000

    serve(app, host="0.0.0.0", port=8000)
