def generate_task_number():
    num = input("Enter robot identification code: ")

    # Remove negative sign if present
    is_negative = num.startswith('-')
    num = num.lstrip('-')

    # Sort digits
    digits = sorted(num)

    # Ensure result doesn't start with zero
    if digits[0] == '0':
        # Find the first non-zero digit and swap it with the first position
        for i in range(1, len(digits)):
            if digits[i] != '0':
                digits[0], digits[i] = digits[i], digits[0]
                break

    task_number = ''.join(digits)

    print("Task number:", task_number)

# Run the program
generate_task_number()
