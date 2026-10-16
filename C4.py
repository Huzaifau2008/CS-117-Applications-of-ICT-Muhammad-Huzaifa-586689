# Loaded Voltage Divider
def loaded_divider(vs, r1, r2, rl):
    unloaded_voltage = vs * (r2 / (r1 + r2))
    
    r2_parallel_rl = (r2 * rl) / (r2 + rl)
    loaded_voltage = vs * (r2_parallel_rl / (r1 + r2_parallel_rl))
    
    return (round(unloaded_voltage, 2), round(loaded_voltage, 2))

print("loaded_divider(12, 1000, 1000, 500) =", loaded_divider(12, 1000, 1000, 500))
