import re

# Dictionary to store authors and their quotes
quotes_by_author = {}
author = None  # Initialize author to None to handle quotes without an author yet

with open('./data_set/365_quotes.txt', encoding='utf-8') as file:
    for line in file:
        stripped_line = line.strip()
        
        # Only process non-empty lines
        if stripped_line:
            # Check if the line is a quote number (digit)
            if stripped_line.isdigit():
                continue  # Skip quote number lines for the dictionary

            # Check if the line contains an author name with a dash (–)
            author_match = re.search(r"–(.+)$", stripped_line)
            if author_match:
                # Extract the author's name
                author = author_match.group(1).strip()
                # Ensure the author has an entry in the dictionary with an empty list
                if author not in quotes_by_author:
                    quotes_by_author[author] = []
            else:
                # If there's no author match, we assume it's part of the quote
                if author:  # Only add to quotes if there's a known author
                    quote_text = stripped_line
                    quotes_by_author[author].append(quote_text)  # Append quote to the author's list

# Print the quotes_by_author dictionary
for author, quotes in quotes_by_author.items():
    print()
    saying = f"{author.upper()} : {quotes}"
    print(saying)


# print(len(list(quotes_by_author.keys())))
