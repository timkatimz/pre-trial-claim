import requests
from bs4 import BeautifulSoup

user_ogrn = int(input())

url = f"https://www.tinkoff.ru/business/contractor/legal/{user_ogrn}/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

company_name = soup.find('div', class_='aEYBZs').find('h1', class_='ctCsKQ').text
company_data = soup.find('div', class_='aEYBZs').findAll('div', class_='itCsKQ')
company_ogrn = company_data[0].text
company_registration_date = company_data[1].text
company_inn = company_data[2].text

print(f'Название: {company_name}')
print(f'ОГРН: {company_ogrn}')
print(f'ИНН: {company_inn}')
print(f'Дата регистрации: {company_registration_date}')





