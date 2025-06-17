def get_max_revenue_per_day(days, products, sales_data):
    max_revenues = []
    for day in range(days):
        max_revenue = max(sales_data[day])
        max_revenues.append(max_revenue)
    return max_revenues

if __name__ == "__main__":
    try:
        # Read number of days and products
        m, n = map(int, input("Enter number of days and products (space-separated): ").split())

        sales_data = []
        print(f"Enter {m} rows of sales data (each with {n} space-separated revenues):")
        for _ in range(m):
            row = list(map(int, input().split()))
            if len(row) != n:
                print("Error: Invalid number of entries in row.")
                exit(1)
            sales_data.append(row)

        result = get_max_revenue_per_day(m, n, sales_data)
        print("Output:", ' '.join(map(str, result)))

    except ValueError:
        print("Invalid input. Please enter integers only.")
