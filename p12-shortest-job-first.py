def calculate_avg_waiting_time():
    n = int(input())                          # Number of tasks
    request_times = list(map(int, input().split()))
    _ = int(input())                          # Confirm durations length (same as n)
    durations = list(map(int, input().split()))
    
    tasks = sorted([(request_times[i], durations[i], i) for i in range(n)])  # (request, duration, original index)
    
    current_time = 0
    waiting_time = 0
    completed = 0
    visited = [False] * n
    
    while completed < n:
        # Get available tasks
        available = []
        for i in range(n):
            if not visited[i] and tasks[i][0] <= current_time:
                available.append((tasks[i][1], tasks[i][0], i))  # (duration, request_time, index)

        if available:
            available.sort()  # sort by duration, then by request time
            duration, request, idx = available[0]
            visited[idx] = True
            waiting_time += current_time - request
            current_time += duration
            completed += 1
        else:
            # If no task is available, move time forward to next task arrival
            current_time += 1

    avg_wait = waiting_time / n
    print(f"{avg_wait:.2f}")

# Sample Run
# Input:
# 3
# 0 1 2
# 3
# 5 2 3
calculate_avg_waiting_time()
