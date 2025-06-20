# Read input
particular_group = input("Enter your group").strip()     # e.g., '2'
participants = input("Enter participant list").strip()         # e.g., '1232238'

# Count occurrences of the group digit in the participant list
count = participants.count(particular_group)

# Print the result
print(count)
