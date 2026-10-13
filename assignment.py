def classify(value):
    if value < 48:
        return "Below range"
    elif value <= 52:
        return "In range"
    else:
        return "Above range"

def calculate_average(total, count):
    average_snapshot = total / count
    average_result = average_snapshot
    return average_result
num_cables = int(input("Enter the number of cables: "))
total = 0
below_count = 0
in_count = 0
above_count = 0
for i in range(num_cables):
    length = int(input("Enter the cable length: "))
    result = classify(length)
    print(result)

    total += length

    if result == "Below range":
        below_count += 1
    elif result == "In range":
        in_count += 1
    else:
        above_count += 1
average = calculate_average(total, num_cables)
print(f"Total length: {total} cm")
print(f"Average length: {average} cm")
print(f"Below range: {below_count}")
print(f"In range: {in_count}")
print(f"Above range: {above_count}")