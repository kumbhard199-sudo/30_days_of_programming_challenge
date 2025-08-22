def reverseWords(s: str) -> str:
    words = s.strip().split()
    
    words.reverse()
    
    return " ".join(words)

s = input("Enter a string: ")
print("Reversed string:", reverseWords(s))
