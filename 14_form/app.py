# Red Wings | Daniel Sooknanan, Cameron Nelson, Sophie Liu
# SoftDev
# Oct 2021 

from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET'])
def login():
    return render_template('login.html')

@app.route("/auth", methods=['POST'])
def welcome():
    username = request.form.get('username')
    return render_template( 'response.html', username = username)

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()