import csv

with open('/home/stephen/Documents/web-scraping/web-scrapers/bizbuysell/details.csv', 'r') as f:
    raw_csv = f.read()
    clean_csv = raw_csv.strip(' ')
    
with open('details_clean.csv', 'w') as f:
    f.write(clean_csv)
