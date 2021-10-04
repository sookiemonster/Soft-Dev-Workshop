# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

#PREDICTIONS
# Produces a website with "No hablo queso!" as text at 127.0.0.1:5000/
# Doesn't print anything into the terminal

#ACTUAL
# Matches our predictions