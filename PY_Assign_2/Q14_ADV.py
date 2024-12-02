# 2. Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa.


def convert_temperature(value, scale):
    
    if scale.upper() == 'C':
        return (value * 9/5) + 32
    elif scale.upper() == 'F':
        return (value - 32) * 5/9
    else:
        raise ValueError("Invalid scale. Use 'C' for Celsius or 'F' for Fahrenheit.")

result = convert_temperature(30, 'C')
print(result)

result = convert_temperature(80, 'F')
print(result)
