# Continuous Discharge Analysis

voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

max_len = 1
current_len = 1
start_val = voltages[0]
end_val = voltages[0]

curr_start = voltages[0]
curr_end = voltages[0]

for i in range(1, len(voltages)):
    if(voltages[i] < voltages[i - 1]):
        current_len += 1
        curr_end = voltages[i]
    else:
        if(current_len > max_len):
            max_len = current_len
            start_val = curr_start
            end_val = curr_end
        curr_start = voltages[i]
        curr_end = voltages[i]
        current_len = 1

if (current_len> max_len):
    max_len =current_len
    start_val = curr_start
    end_val = curr_end

print("Longest continuous drop:", max_len, "minutes")
print("Started at:", start_val, "V")
print("Ended at:", end_val, "V")
