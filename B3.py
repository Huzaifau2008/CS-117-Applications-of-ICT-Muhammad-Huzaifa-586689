# Sensor Readings

readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
above_threshold_count = 0
highest_reading = readings[0]
lowest_reading = readings[0]
total_sum = 0
count = 0

for val in readings:
    if (val > 3.2):
        above_threshold_count += 1
    if (val > highest_reading):
        highest_reading = val
    if (val < lowest_reading):
        lowest_reading = val
    total_sum += val
    count += 1

average_reading = total_sum / count

print("Readings above 3.2 V:", above_threshold_count)
print("Highest:", highest_reading, "V")
print("Lowest:", lowest_reading, "V")
print("Average:", round(average_reading, 2), "V")
