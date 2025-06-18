def find_significant_pattern_length(n, binary_string):
    max_len = 0
    current_char = binary_string[0]
    current_count = 1

    for i in range(1, n):
        if binary_string[i] == current_char:
            current_count += 1
        else:
            # Check if the current sequence is NOT at the start or end
            start = i - current_count
            end = i - 1
            if start > 0 and end < n - 1:
                max_len = max(max_len, current_count)
            current_char = binary_string[i]
            current_count = 1

    # Check the last sequence (at the end of the loop)
    start = n - current_count
    end = n - 1
    if start > 0 and end < n - 1:
        max_len = max(max_len, current_count)

    return max_len

# 🔹 Sample Inputs
n1 = 6
binary_str1 = "101000"
print("Output:", find_significant_pattern_length(n1, binary_str1))  # Output: 1

n2 = 9
binary_str2 = "101111110"
print("Output:", find_significant_pattern_length(n2, binary_str2))  # Output: 6

# # Example Usage:
# n = int(input())
# binary_string = input()
# print(find_significant_pattern_length(n, binary_string))
