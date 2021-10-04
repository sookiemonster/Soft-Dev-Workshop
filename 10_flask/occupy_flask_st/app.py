# The Red Imposter | Daniel Sooknanan, Roshani Shrestha, Shadman Rakib
# SoftDev
# Oct 2021

from flask import Flask
from csv import DictReader
from random import choices

app = Flask(__name__)

def getRandomOccupation():

    occ_dict = {} # Create a dictionary to be filled in
    filename = 'occupations.csv' # Specifies the target .csv file

    try:
        with open(filename) as csvfile:
            reader = DictReader(csvfile)
            for row in reader: 
                # Fill in the dictionary with Job Classes as keys & Percentages as values
                occ_dict[row['Job Class']] = float(row['Percentage']) 

        if 'Total' in occ_dict.keys(): 
            occ_dict.pop('Total') # Remove the Total at the end of the .csv file if it exists

        # Get the first item in a list that is length k (in this case 1)
        # The randomness of a key appearing is weighted based on its respective value
        result = choices(list(occ_dict.keys()), weights=occ_dict.values(), k=1)[0]
        return(result)

    except FileNotFoundError: 
        print('File "%s" does not exist' % (filename)) 
        return 'File "%s" does not exist' % (filename)


@app.route("/") 
def main():
    return str(getRandomOccupation())

if __name__ == "__main__":
    app.run()
