
import requests
import csv
from bs4 import BeautifulSoup

def get_character_ids():
    """Get all character ids from website
    Using requests, call this page https://www.superheroapi.com/ids.html
    to get character ids so that they can be put in a spreadsheet with the superhero
    they correspond with
    Using beautiful soup to parce the webpage and put the character ids into a list
    by finding 'table' 'tr' and 'td' which is where the character id number is
    Return the list of character ids"""

    response = requests.get('https://www.superheroapi.com/ids.html')
    print(response)
    soup = BeautifulSoup(response.content, 'html.parser')

    character_ids = []

    for table in soup.find_all('table'):
        for row in table.tbody.find_all('tr'):
            columns = row.find_all('td')
            character_ids.append(columns[0].text)

    return character_ids

def get_character_data(character_id):
    """Using the access_token and the character id number request to get the info
    Print the character id and the info of the character
    List what info I want from each character in a dictionary and show in json format
    Return the superhero"""

    access_token = '8742370349122539'
    url = f'https://superheroapi.com/api/{access_token}/{character_id}'
    response = requests.get(url)

    print(character_id, response)
    response_json = response.json()

    superhero = {
        'Character ID': response_json['id'],
        'Character Name': response_json['name'],
        'Full Name': response_json['biography']['full-name'],
        'Alter Egos': response_json['biography']['alter-egos'],
        'Place Of Birth': response_json['biography']['place-of-birth'],
        'Gender': response_json['appearance']['gender'],
        'Height': response_json['appearance']['height'][0],
        'Intelligence': response_json['powerstats']['intelligence'],
        'Strength': response_json['powerstats']['strength'],
        'Speed': response_json['powerstats']['speed'],
        'Durability': response_json['powerstats']['durability'],
        'Power': response_json['powerstats']['power'],
        'Combat': response_json['powerstats']['combat']
    }
    return superhero

def main():
    """Use the previous functions 'get_character_ids' amd 'get_character_data
     to append the info into a list
     Write a list of titles I want in the spreadsheet
     Write a csv file called superheros with all the data inside"""

    character_ids = get_character_ids()
    data = []

    for character_id in character_ids:
        superhero = get_character_data(character_id)
        data.append(superhero)

    field_names = ['Character ID', 'Character Name', 'Full Name', 'Alter Egos', 'Place Of Birth', 'Gender', 'Height',
                   'Intelligence', 'Strength', 'Speed', 'Durability', 'Power', 'Combat']

    with open('Superheros.csv', 'w+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

        spreadsheet.writeheader()
        spreadsheet.writerows(data)
