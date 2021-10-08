# Blue Imposter | Daniel Sooknanan (Sussy), Yoonah Chang (Yelena), Annabel Zhang (Mang)
# SoftDev
# Oct 2021

from flask import Flask, render_template
from csv import DictReader
from random import choices

app = Flask(__name__)

# Create a dictionary given the filename
def makeDict(filename):
    dict = {}
    try:
        with open(filename) as csvfile:
            reader = DictReader(csvfile)
            for row in reader: 
                # Fill in the dictionary with Job Classes as keys & Percentages as values
                dict[row['Job Class']] = float(row['Percentage']) 

        if 'Total' in dict.keys(): 
            dict.pop('Total') # Remove the Total at the end of the .csv file if it exists

    except FileNotFoundError: 
        print("File %s does not exist" % (filename))
    
    return dict

# Return a random key given the frequency at which it should appear (second column of csv)
def getRandomKey(dictionary):
    if (len(dictionary) > 0): 
        # Get the first element of a list length 1 (or k) that selects random keys based on the weights specified by the keys respective values
        result = choices(list(dictionary.keys()), weights=dictionary.values(), k=1)[0]
        return result
    else:
        return "None (no occupations to select from)"

# @app.route("/occupyflaskst") 
@app.route("/") 
def main():
    occ_dict = makeDict('occupations.csv')
    return render_template('occupations.html', selected = getRandomKey(occ_dict), occupations = occ_dict)

if __name__ == "__main__":
    app.debug = True
    app.run()
