# Blue Imposter | Daniel Sooknanan (Sussy), Yoonah Chang (Yelena), Annabel Zhang (Mang)
# SoftDev
# 2021-10-10

from flask import Flask, render_template
from csv import DictReader
from random import choices

app = Flask(__name__)

# Create a dictionary given the filename
def makeDict(filename):
    """Returns a dictionary given a .csv file structured, KEY : [Column_2, Column_3]"""
    dict = {}
    try:
        with open(filename) as csvfile:
            reader = DictReader(csvfile)
            for row in reader: 
                # Fill in the dictionary with Job Classes as keys & a list of Percentages & Links as values
                dict[row['Job Class']] = [float(row['Percentage']), row['Link']]

        if 'Total' in dict.keys(): 
            dict.pop('Total') # Remove the Total at the end of the .csv file if it exists

    except FileNotFoundError: 
        print("File %s does not exist" % (filename))
    
    return dict

# Return a random key given the frequency at which it should appear (second column of csv)
def getRandomKey(dictionary):
    """Returns a random key based on a specified frequency, given a dictionary structured KEY : [FREQUENCY, Value_2]"""
    if (len(dictionary) > 0): 
        # Get the first element of a list length 1 (or k) that selects random keys based on the weights specified by the keys respective values
        freq_list = list(dictionary.values())
        for i in range(len(freq_list)):
            freq_list[i] = freq_list[i][0]
        
        result = choices(list(dictionary.keys()), weights=freq_list, k=1)[0]
        return result
    else:
        return "None (no occupations to select from)"

@app.route("/occupyflaskst") 
def main():
    occ_dict = makeDict('data/occupations.csv')
    selected = getRandomKey(occ_dict)
    return render_template('tablified.html', selected = selected, selected_link = occ_dict[selected][1], occupations = occ_dict)

if __name__ == "__main__":
    app.debug = True
    app.run()
