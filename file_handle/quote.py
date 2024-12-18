import re

count = 0

with open('./data_set/365_quotes.txt', encoding='utf-8') as file:
    for line in file:
        stripped_line = line.strip()
        
        # Only print if the line has content after stripping whitespace
        if stripped_line:
           
            if stripped_line.isdigit():
                count += 1
                print()
                print(f"{'':>10}QUOTE NUMBER : {count}{'':>10}")
                print()
            elif stripped_line.lower().startswith("bonus"):
                break
            else:
                # Check if the line contains an author name with a dash (–)
                author_match = re.search(r"–(.+)$", stripped_line)
                if author_match:
                    # Extract and format the author’s name
                    author = author_match.group(1).strip().upper()
                    
                    print(f"Author: {author}")
                else:
                    # Print the quote text in uppercase
                    print(stripped_line.upper())
                
               
                
