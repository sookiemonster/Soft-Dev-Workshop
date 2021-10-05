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
        print("File %s does not exist" % (filename))
    
    return dict


def getRandomKey(dictionary):

    if (len(dictionary) > 0):
        result = choices(list(dictionary.keys()), weights=dictionary.values(), k=1)[0]
        return "<h3>Selected: %s</h3>" % result
    else: 
        return "<h3>Selected: None (no occupations to select from)</h3>"

def listKeys(dictionary):
    key_list = "<div>Occupations: "
    for key in dictionary.keys():
        key_list += "<div>%s</div>" % (key)
    return key_list + "</div>"

@app.route("/") 
def main():
    occ_dict = makeDict('occupations.csv')
    header = "<h3>The Red Imposter | Daniel Sooknanan, Roshani Shrestha, Shadman Rakib</h3>"
    return header + getRandomKey(occ_dict) + listKeys(occ_dict)

if __name__ == "__main__":
    app.run()
