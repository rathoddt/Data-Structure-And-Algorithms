def cottages_not_renovated(labels):
    vowels = set('aeiouAEIOU')
    # result = ''.join(c for c in labels if c not in vowels)
    result = ''.join(c for c in labels if c in vowels)
    print(result)

# Sample input
input_string = "Mynameisanthony"
cottages_not_renovated(input_string)
