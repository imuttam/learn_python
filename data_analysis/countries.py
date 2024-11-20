import csv

countries = set()
with open('./data_set/netflix_titles.csv', encoding='utf-8') as file:
    rows = csv.reader(file)
    headers = next(rows)

    for row in rows:
        country = row[5]
        try:
            country=country.strip().split()
            for c in country:
                if c.isalpha():
                    countries.add(c)
        except ValueError:
            continue


print(headers)
print(len(countries))



