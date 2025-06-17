def remove_duplicates_preserve_order(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

if __name__ == "__main__":
    # Read number of elements
    N = int(input("Enter number of elements: "))
    
    # Read list of numbers
    arr = list(map(int, input("Enter space-separated numbers: ").split()))
    
    if len(arr) != N:
        print(f"Error: Expected {N} numbers, but got {len(arr)}.")
    else:
        result = remove_duplicates_preserve_order(arr)
        print("Output:", ' '.join(map(str, result)))
