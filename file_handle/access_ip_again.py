
count = 0
with open('./access.log') as file:
    for line in file:
        count += 1
        line = line.split()
        if line:
            print(line[0])
        if count > 40:
            break
