from bs4 import BeautifulSoup
import requests
import openpyxl

wb = openpyxl.load_workbook('TestOpenUrlScrape.xlsx')
sheet = wb['Sheet1']  # replace 'Sheet1' with the name of your sheet

base_url = 'https://www.europarl.europa.eu/meps/en/'

for row in sheet.iter_rows(min_row=2, values_only=True):
    column_a = row[0]
    column_b = row[1]
    column_c = row[2]
    nameurl=f"{column_b}_{column_c}"
    url = f"{base_url}{column_a}/{nameurl}/home"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    time_tag = soup.find('time', {'class': 'sln-birth-date'})
    if time_tag is not None:
        date_str = time_tag['datetime'].split('T')[0]
        print(date_str)
    else:
        print(f"No birth date found for MEP {column_b} {column_c}")
