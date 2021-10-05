# The Red Imposter | Daniel Sooknanan, Roshani Shrestha, Shadman Rakib
# SoftDev
# Oct 2021

from flask import Flask
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
        return "<h3>Selected: %s</h3>" % result
    else:
        return "<h3>Selected: None (no occupations to select from)</h3>"

# Return a string of all the keys in the given dictionary
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
