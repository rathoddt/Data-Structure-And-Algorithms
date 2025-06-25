import math

def circle_overlap_area(r1, r2, d):
    if d >= r1 + r2:
        # No overlap
        return 0.0
    if d <= abs(r1 - r2):
        # One circle is completely inside the other
        return math.pi * min(r1, r2) ** 2

    # Use geometric formula for partial overlap
    part1 = r1**2 * math.acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
    part2 = r2**2 * math.acos((d**2 + r2**2 - r1**2) / (2 * d * r2))
    part3 = 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * 
                            (d - r1 + r2) * (d + r1 + r2))
    return part1 + part2 - part3

# Example usage
r1 = 5
r2 = 3
d = 4

area = circle_overlap_area(r1, r2, d)
print(f"Overlapping area: {area:.4f}")
