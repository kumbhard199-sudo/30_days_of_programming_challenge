from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    
    for word in strs:
        key = "".join(sorted(word))
        anagrams[key].append(word)
    
    return list(anagrams.values())

strs = input("Enter words: ").split()

result = groupAnagrams(strs)
print("Grouped Anagrams:", result)
