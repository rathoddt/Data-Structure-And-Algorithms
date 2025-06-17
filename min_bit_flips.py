import sys

def count_bit_flips(num1: int, num2: int) -> int:
    # XOR highlights bits that are different
    xor_result = num1 ^ num2
    # Count the number of differing bits
    return bin(xor_result).count('1')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <num1> <num2>")
        sys.exit(1)

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("Both arguments must be integers.")
        sys.exit(1)

    result = count_bit_flips(num1, num2)
    print(f"Minimum bit flips to convert {num1} to {num2}: {result}")
