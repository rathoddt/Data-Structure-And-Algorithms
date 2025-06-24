from collections import Counter

def find_missing_character(original, proofread):
    # Count characters in both strings
    original_count = Counter(original)
    proofread_count = Counter(proofread)
    
    # Compare character counts
    for char in original_count:
        if original_count[char] != proofread_count.get(char, 0):
            return char

# Sample input
stringSent = input("Enter original manuscript: ")
stringRec = input("Enter proofread manuscript: ")

# Output the missing character
missing_char = find_missing_character(stringSent, stringRec)
print("Missing character:", missing_char)
