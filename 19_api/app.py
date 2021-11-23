# Daniel Sooknanan (Sussy), Alif Abdullah (The Eagle in the Sand)
# SoftDev
# K19 API Shenanigans
# 2021-11-23
# time spent: 20 minutes

from flask import Flask, render_template
from json import loads
import urllib

app = Flask(__name__)

KEY_FILE = "key_nasa.txt"
API_KEY = ""

with open(KEY_FILE, "r") as file:
    API_KEY = file.read()

@app.route("/") 
def main():
    request_json = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=%s" % API_KEY).read()
    img_src = loads(request_json)['url']
    return render_template("main.html", pic = img_src)

if __name__ == "__main__":
    app.run()
