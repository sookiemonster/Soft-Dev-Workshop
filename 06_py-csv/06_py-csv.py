# The Red Imposter  || Daniel Sooknanan, Roshani Shrestha, Shadman Rakib
# SoftDev
# 06_py-csv.py: Returns a random Job Class based on their respective
# frequenies given a .csv file of Job Classes & Percentages
# 2021-09-16

# My team used the DictReader function from the csv module 
# to create rows of dictionaries where the keys are 
# "Job Class" and "Percentage". We used the choices function
# from the random module to return a key from the dictionary
# using weighted probability.

from csv import DictReader
from random import choices

def main():

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
        print(result)
        return(result)

    except FileNotFoundError: 
        print('File "%s" does not exist' % (filename)) 

if __name__ == "__main__":
    main()