import re

# Pattern to match lines containing "/2024" followed by "GET"
pattern1 = r"31/Mar/(2019|2020).*GET"
pattern2 = r"31/Mar/(2019|2020).*GET.*almhuette"
pattern3 = r"https://scrapy.org"

search_line = re.compile(pattern3)  # Compile the pattern with the new variable name

with open('./access.log') as file:
    for line in file:
        if search_line.search(line):
            print(line)
