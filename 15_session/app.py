# Red Wings | Daniel Sooknanan, Cameron Nelson, Sophie Liu
# SoftDev
# K15 Flask Session Shenaniganza
# 2021-10-18

from flask import Flask, render_template, request, redirect

app = Flask(__name__)    #create Flask object

real_username = "username"
real_password = "password"

@app.route("/", methods=['GET', 'POST'])
def welcome():
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        if real_username == username:
            if real_password == password:
                return render_template( 'response.html', username = username)
            else: 
                return render_template( 'login.html', error = "Password is incorrect")
        else: 
            return render_template( 'login.html', error = "User does not exist")
    else:
        return render_template('login.html') # Redirect users to login if there's no post request to get info from

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()