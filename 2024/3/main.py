import re

corrupted_memory = ""
with open('input.txt', 'r') as file:
    corrupted_memory = file.read()

def sum_valid_multiplications(corrupted_memory):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    matches = re.findall(pattern, corrupted_memory)
    
    total = 0
    for x, y in matches:
        total += int(x) * int(y)
    
    return total

def sum_enabled_multiplications(corrupted_memory):
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    combined_pattern = fr"{do_pattern}|{dont_pattern}|{mul_pattern}"
    
    matches = re.finditer(combined_pattern, corrupted_memory)
    
    mul_enabled = True
    total = 0
    
    for match in matches:
        if match.group(0) == "do()":
            mul_enabled = True
        elif match.group(0) == "don't()":
            mul_enabled = False
        else:
            if mul_enabled:
                x, y = map(int, match.groups())
                total += x * y
    
    return total
result = sum_valid_multiplications(corrupted_memory)
print(f"Sum of valid multiplications: {result}")

result2 = sum_enabled_multiplications(corrupted_memory)
print(f"Sum of enabled multiplications: {result2}")
