def count_negative_temperatures():
    # Read the number of products
    num_products = int(input("Enter number of products: "))

    # Read the temperatures as a list of integers
    temperatures = list(map(int, input("Enter storage temperatures: ").split()))

    # Validate input size
    if len(temperatures) != num_products:
        print("Error: Number of temperatures does not match number of products.")
        return

    # Count the number of temperatures that are negative
    negative_count =pytho

    # Print the result
    print(negative_count)

# Run the function
count_negative_temperatures()
