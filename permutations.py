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


def permutations(
    org_string: str,
    curr_string: str = "",
    repetition: bool = True,
    all_substrings: bool = False,
    choose: bool = None,
) -> list:
    if choose is None:
        choose = len(org_string)
    elif choose > len(org_string):
        raise ValueError(
            f"Passed: ({choose}) for var 'choose', must be <= ({len(org_string)}) length of 'org_string': '{org_string}'"
        )
    if len(curr_string) == choose:
        return [curr_string]
    perms = [curr_string] if curr_string != "" and all_substrings else []
    for char in org_string:
        if repetition == False and char in curr_string:
            continue
        else:
            perms += permutations(
                org_string=org_string,
                curr_string=curr_string + char,
                all_substrings=all_substrings,
                repetition=repetition,
                choose=choose,
            )
    return perms


def combinations(
    org_string: str,
    curr_string: str = "",
    index: int = 0,
    repetition: bool = True,
    choose: int = None,
):
    if choose is None:
        choose = len(org_string)
    elif choose > len(org_string):
        raise ValueError(
            f"Passed: ({choose}) for var 'choose', must be <= ({len(org_string)}) length of 'org_string': '{org_string}'"
        )
    if len(curr_string) == choose:
        return [curr_string]
    perms = []
    for char_index, char in enumerate(org_string[index:]):
        if repetition == False and char in curr_string:
            continue
        else:
            perms += combinations(
                org_string=org_string,
                curr_string=curr_string + char,
                index=char_index + index,
                repetition=repetition,
                choose=choose,
            )
    return perms


if __name__ == "__main__":

    """
    Testing all the possible combinations
    of these functions :)
    """

    print("\n")

    string = "AB"
    perms = permutations(org_string=string)
    perms_no_rep = permutations(org_string=string, repetition=False)
    all_substrings = permutations(org_string=string, all_substrings=True)

    print(f"Permuations for '{string}' length: ({len(perms)}) {perms}")
    print(
        f"Permuations no repetition '{string}' length: ({len(perms_no_rep)}) {perms_no_rep}"
    )
    print(
        f"All substrings for '{string}' length: ({len(all_substrings)}) {all_substrings}"
    )

    string = "ABC"
    choose = len(string) - 1
    perms = permutations(org_string=string, choose=choose)
    print(
        f"Permutations for '{string}' choose {choose} with repetition length: {len(perms)} {perms}"
    )

    string = "ABC"
    choose = len(string) - 1
    perms = permutations(org_string=string, choose=choose, repetition=False)
    print(
        f"Permutations for '{string}' choose {choose} with repetition length: {len(perms)} {perms}"
    )

    print("\n")

    string = "AB"
    combs = combinations(org_string=string)
    print(f"Combinations for '{string}' length: ({len(combs)}) {combs}")

    string = "ABC"
    combs = combinations(org_string=string)
    print(f"Combinations for '{string}' length: ({len(combs)}) {combs}")

    string = "AB"
    combs = combinations(org_string=string, repetition=False)
    print(f"Combinations no repetition for '{string}' length: ({len(combs)}) {combs}")

    string = "ABC"
    combs = combinations(org_string=string, repetition=False)
    print(f"Combinations repetition for '{string}' length: ({len(combs)}) {combs}")

    string = "ABC"
    choose = len(string) - 1
    combs = combinations(org_string=string, choose=choose)
    print(
        f"Combinations repetition for '{string}' choose {choose} length: ({len(combs)}) {combs}"
    )

    string = "ABC"
    choose = len(string) - 1
    combs = combinations(org_string=string, repetition=False, choose=choose)
    print(
        f"Combinations repetition for '{string}' choose {choose} no repetition length: ({len(combs)}) {combs}"
    )

    print("\n")
