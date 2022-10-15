"""
When order does'nt matter we've got a combination.
When order does matter we've got a permuatation.

So a combination for a lock is permutations because different
ordering means a different outcome completely.

A group of fruit or veg is a combination. If you've got
2 apples and 1 pear no matter what way you order them
you've got the same thing.

With Permuatations you've got two types:
    - With Repetition
        - With rep is a nice one. n x n x n
    - Without Repetition
        - Without rep is a little different n x n-1 x n-2

There's another probelm that's interesting to solve and that's
all the possible substrings of a string. In the case of AB it's
not just AB BA AA BB, it would also include A and B

With combinations there are also two types:
    - With Repetition
    - Without Repetition

"""

if __name__ == "__main__":

    def permutations(org_string, curr_string="", all_substrings=False):
        if len(curr_string) == len(org_string):
            return [curr_string]
        perms = [curr_string] if curr_string != "" and all_substrings else []
        for char in org_string:
            perms += permutations(
                org_string=org_string,
                curr_string=curr_string + char,
                all_substrings=all_substrings,
            )
        return perms

    print(f'{permutations(org_string="AB")}\n')
    print(f'{permutations(org_string="AB", all_substrings=True)}\n')

    def combinations(org_string, curr_string="", index=0):
        if len(curr_string) == len(org_string):
            return [curr_string]
        perms = []
        for char_index, char in enumerate(org_string[index:]):
            perms += combinations(
                org_string=org_string,
                curr_string=curr_string + char,
                index=char_index + index,
            )
        return perms

    res = combinations(org_string="AB")
    print(f"{res}, length: {len(res)}\n")
    res = combinations(org_string="ABC")
    print(f"{res}, length: {len(res)}\n")

