# The Red Imposter | Daniel Sooknanan, Roshani Shrestha, Shadman Rakib
# SoftDev
# Oct 2021 
# Basics of /static folder

from flask import Flask, send_from_directory
app = Flask(__name__) 

@app.route("/")       
def main():
    return send_from_directory("static", "fixie.html")

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()