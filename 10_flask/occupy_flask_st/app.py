# The Red Imposter | Daniel Sooknanan, Roshani Shrestha, Shadman Rakib
# SoftDev
# Oct 2021

from flask import Flask
from csv import DictReader
from random import choices

app = Flask(__name__)

def makeDict(filename):

    dict = {}

    try:
        with open(filename) as csvfile:
            reader = DictReader(csvfile)
            for row in reader: 
                dict[row['Job Class']] = float(row['Percentage']) 

        if 'Total' in dict.keys(): 
            dict.pop('Total')

    except FileNotFoundError: 
        pass

    return dict

def getRandomKey(dictionary):

    occ_dict = {} # Create a dictionary to be filled in
    filename = 'occupations.csv'

    try:
        with open(filename) as csvfile:
            reader = DictReader(csvfile)
            for row in reader: 
                occ_dict[row['Job Class']] = float(row['Percentage']) 

        if 'Total' in occ_dict.keys(): 
            occ_dict.pop('Total')

        result = choices(list(occ_dict.keys()), weights=occ_dict.values(), k=1)[0]
        return "<span style='display: block; margin-bottom: 10px; font-weight: bold'>Selected: %s</span>" % result

    except FileNotFoundError: 
        return 'File "%s" does not exist' % (filename)

def listKeys(dictionary):
    key_list = "<div>Occupations: "
    for key in dictionary.keys():
        key_list += "<p style='margin: 7px 20px'>%s</p>" % (key)
    return key_list + "</div>"

@app.route("/") 
def main():
    occ_dict = makeDict('occupations.csv')
    header = "<h3>The Red Imposter | Daniel Sooknanan, Roshani Shrestha, Shadman Rakib</h3>"
    return header + getRandomKey(occ_dict) + listKeys(occ_dict)

if __name__ == "__main__":
    app.run()
