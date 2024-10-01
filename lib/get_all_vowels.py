def get_all_vowels(string):
    vowels = []
    for char in string:
        if char in "aioueAIOUE":
            vowels.append(char)
    return "".join(vowels)