# Daniel Sooknanan, Eric Guo, Mark Zhu 

# Summary
#   The program takes the two lists of students from period 1 & 2
#   and prints out a random student's name from those lists. 
#   This is done by using randrange to randomly pick a list 
#   and then randomly pick a list index,

# Discoveries
# You can find the people in each period by viewing the submodules 
# in the repo-of-holding.

# Questions

from random import randrange

# List people for periods 1 and 2
pd1 = ["Alejandro Alonso", "Aryaman Goenka", "Christopher Liu",  "Deven Maheshwari", 
        "Emma Buller", "Ella Krechmer",  "Gavin McGinley", "Haotian Gan", "Ivan Lam", 
        "Ishraq Mahid", "Ivan Mijacika", "Julia Nelson", "Lucas Lee", "Lucas Tom Wong", 
        "Michelle Lo", "Oscar Wang", "Owen Yaggy", "Reng Zheng", "Shriya Anand", "Shyne Choi",
        "Sadid Ethun", "Tomas Acuna", "Theo Fahey", "Tina Nguyen", "Tami Takada", "William Chen", 
        "Yusuf Elsharawy", "Zhaoyu Lin"]
pd2 = ["Alif Abdullah", "Andrew Juang", "Andy Lin", "Austin Ngan", "Annabel Zhang", 
        "Daniel Sooknanan", "Eric Guo", "Eliza Knapp", "Hebe Huang", "Han Zhang",
        "Yoonah Chang", "Josephine Lee", "Jonathan Wu", "Jesse Xie", "Justin Zou", 
        "Kevin Cao", "Liesel Wong", "Michael Borczuk", "Noakai Aronesty", "Patrick Ging",
        "Qina Liu", "Rachel Xiao", "Raymond Yeung", "Sophie Liu", "Shadman Rakib",
        "Thomas Yu", "Wenhao Dong", "Yaying Liang Li", "Yuqing Wu"]

def main():
    rand_period = randrange(2)
    if (rand_period == 0):
        print( pd1[randrange(len(pd1))] )
    else:
        print( pd2[randrange(len(pd2))] )

if __name__ == "__main__":
    main()