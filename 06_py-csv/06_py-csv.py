import csv

occ_dict = {}

with open('occupations.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        occ_dict[row['Job Class']] = float(row['Percentage'])

for key in occ_dict.keys():
    print("%s :  %s" % (key, occ_dict[key]))