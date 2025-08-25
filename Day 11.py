def string_permutations(s: str):
    result = []
    used = [False] * len(s)
    s = sorted(s)  

    def backtrack(path):
        if len(path) == len(s):
            result.append("".join(path))
            return

        for i in range(len(s)):
            
            if used[i]:
                continue
           
            if i > 0 and s[i] == s[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            backtrack(path + [s[i]])
            used[i] = False

    backtrack([])
    return result

s = input("Enter a string: ").strip()
permutations = string_permutations(s)

print("All unique permutations are:")
print(permutations)
