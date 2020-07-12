s = "qPxYqP:S24.L?"
count = 0 

for char in s:
    if char == ":":
        data = s[:count]
    count += 1
print(data)