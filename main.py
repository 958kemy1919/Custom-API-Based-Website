import requests
from flask import Flask, render_template, request

URL = "https://api.openbrewerydb.org/breweries"
parameters = {
    "per_page": 1000,
}
response = requests.get(url=URL,params=parameters)
breweries = response.json()


app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():
    return render_template("index.html")

@app.route('/breweries')
def find_breweries():
    return render_template("baza.html",breweries=breweries)

@app.route('/search-by-city',methods=["POST","GET"])
def search_by_city():
    if request.method == "POST":
        city = request.form.get("city")
        parameters = {
            "per_page": 100,
            "by_city": city
        }
        resp = requests.get(url=URL,params=parameters)
        breweries_by_city = resp.json()
        return render_template("cities.html",breweries_by_city=breweries_by_city)
    return render_template("index.html",breweries=breweries)

@app.route('/search-by-state',methods=["POST","GET"])
def search_by_state():
    if request.method == "POST":
        state = request.form.get("state")
        parameters = {
            "by_state": state,
            "per_page": 100
        }
        res = requests.get(url=URL, params=parameters)
        breweries_by_state = res.json()
        return render_template("states.html", breweries_by_state=breweries_by_state)
    return render_template("index.html", breweries=breweries)

if __name__ == "__main__":
    app.run(debug=True)