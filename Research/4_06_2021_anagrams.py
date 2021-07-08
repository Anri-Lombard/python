def anagrams(S): # S is a set of strings
    d = {}
    for word in S:
        s = ''.join(sorted(word))
        if s in d:
            d[s].append(word)
        else:
            d[s] = word

    return [d[s] for s in d if len(d[s]) > 1]


print(anagrams(input()))
