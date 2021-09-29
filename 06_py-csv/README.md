## The Red Imposter - Daniel Sooknanan, Shadman Rakib, and Roshani Shrestha
### SoftDev
&nbsp;
# K07 -- Show What You Know
### 2021-09-29

## I/O
We used `with open(filename)` to open occupations.csv and specified it to be a `csvfile`. The `with` is really important as it automatically closes the file after the block ends.
Also, we used a `Try-Except` block that catches `FileNotFoundError` just in case `occupations.csv` isn’t there.

## Dictionary
Python dictionaries are a key value data structure. Keys in the dictionary are assigned certain values. The benefit of dictionaries is constant data retrieval and modifications. 

Let’s look at a specific use case of dictionaries.

Imagine you are tasked with counting the number of times words appear in a list. You could use a dictionary to keep track of word frequency. In this case, the keys for the dictionary will be all the unique words that appear in the list, and the values will be the corresponding word frequency. 
As you loop through the list, if the word does not exist in the dictionary, set the value under with the word as its key to 1. If it does exist, then increment by 1. At the end, you will have a dictionary of the words that correspond to their word frequency.

This is important because it allows us to easily access information associated with each other, which, in our case, are job classes and percentages. 

In our program, we used `csv.DictReader(csvfile)` to insert the information on occupations.csv into a set of dictionaries called `reader`. We then read each row of `reader` and used a dictionary called `occ_dict` to set each Job Class as a key mapping to its corresponding Percentage as a value. 
We popped the last entry with this code: 
```python
if 'Total' in occ_dict.keys(): 
    occ_dict.pop('Total')
```
We did this because the last entry just contained the total percentage, so it wasn’t needed in the dictionary of occupations and their percentages. 

## List
We used `list(occ_dict.keys())` to make a list of the keys in the dictionary, which was the first argument for `random.choices()`. Then, `occ_dict.values()` automatically makes a list for the values in the dictionary, so there was no need to use `list()`. This list was used as the weights list argument for `random.choices()`. `random.choices()` returned a list of values chosen randomly based on those weights. In this case, the list only had one element because we had to print out one occupation, so that was the result that we returned and printed.

## Github-flavored markdown
Hashtags are used for different types of headings. One hashtag makes the text the most bold, while two hashtags make it less bold. Surrounding text with one backtick on each side creates inline code. Surrounding text with three backticks on each side creates code blocks. A blank line forms a paragraph. 

## Weighted randomized selection
We used `random.choices( *values_list*, *weights_list*, k=1)` to get a list length k of random choices from the `values_list`. The frequency at which a choice from the `values_list` will appear is based on the corresponding weight specified in the `weights_list`. 
Then, since we set k = 1, the list of random choices is 1 item long and the result will be the first (and only element) within it. We return and print that item, thus giving a random occupation based on the weights specified by the percentages.



