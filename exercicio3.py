def inverter_string(string):
    
    if len(string) <=1:
        return string
    return string[-1] + inverter_string(string[:-1])

print(inverter_string('o my good.'))