# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()


#PREDICTIONS
# Same behavior as last file as long as this file is the file being run 
# with python.exe and not via "flask run." If the file is run using the former method
# it'll be in debug mode. If it's run via "flask run" it won't be, but it also
# won't show the warning that goes along the lines of "silently ignoring app.run()..."

#Actual
# Matches our predictions