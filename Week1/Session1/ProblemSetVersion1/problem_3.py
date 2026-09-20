"""
T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() 
that accepts a string word and returns a new string that removes
 any substrings t, i, gg, and er from word. The function should be case insensitive.

def tiggerfy(word):
	pass
Example Usage:

word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)
Example Output:

"r"
"eplan"
"chor"
"""

def tiggerfy(word):
    # create a result string to append results
    result = ""
    # index to track the iteration from 0 to length of input
    index = 0 

    while index < len(word):
        if word[index] in "TtiI":
            index += 1
        elif word[index: index + 2].lower() == "gg" or word[index: index + 2].lower() == "er":
            index += 2
        else:
            result += word[index]
            index += 1
    return result.lower()


	


word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))