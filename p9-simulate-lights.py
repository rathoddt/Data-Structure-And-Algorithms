def simulate_lights(state, days):
    n = len(state)
    for _ in range(days):
        new_state = [0] * n
        for i in range(n):
            left = state[i - 1] if i > 0 else 0
            right = state[i + 1] if i < n - 1 else 0
            new_state[i] = 1 if left != right else 0
        state = new_state
    return state

# Read input
n = int(input())  # Always 8
initial_state = list(map(int, input().split()))
days = int(input())

# Simulate and print result
final_state = simulate_lights(initial_state, days)
print(" ".join(map(str, final_state)))
