def count_unique_elements():
    # Input size of first list
    n1 = int(input("Enter the size of the first list: "))
    list1 = list(map(int, input("Enter elements").split()))
    
    # Input size of second list
    n2 = int(input("Enter the size of the second list: "))
    list2 = list(map(int, input("Enter elements").split()))
    
    # Convert to sets for efficient lookup
    set1 = set(list1)
    set2 = set(list2)
    
    # Unique elements in either set
    unique_to_list1 = set1 - set2
    unique_to_list2 = set2 - set1
    
    # Total unique elements
    total_unique = len(unique_to_list1) + len(unique_to_list2)
    
    print(total_unique)

# Run the program
count_unique_elements()
