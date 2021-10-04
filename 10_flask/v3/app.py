# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

#PREDICTIONS
# Same thing as the prior file. 

#ACTUAL
# Well it is like the last file in the sense that the two print statements 
# act the same, but the difference is A) Debugger is active and there's
# a Debugger Pin, B) When the file is changed, that change is detected and
# the localhost site is updated (but you have to refresh to see this change).
# Also, when using flask run, debug mode isn't active despite setting the value to True.