"""
Rabbit is collecting carrots from his garden to make a
feast for Pooh and friends. Write a function harvest() 
that accepts a 2D n x m matrix vegetable_patch and 
returns the number of of carrots that are ready to 
harvest in the vegetable patch. A carrot is ready 
 harvest if vegetable_patch[i][j] has value 'c'.

Assume n = len(vegetable_patch) and m = len(vegetable_patch[0]). 0 <= i < n and 0 <= j < m.

def harvest(vegetable_patch):
	pass
Example Usage:

vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]
harvest(vegetable_patch)
Example Output:

6
"""


def harvest(vegetable_patch):
	# variable for harvest
    harvest = 0 
    rows, cols = len(vegetable_patch), len(vegetable_patch[0])
    for r in range(rows):
        for c in range(cols):
            if vegetable_patch[r][c] == "c":
                harvest += 1
    return harvest


vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]

print(harvest(vegetable_patch))