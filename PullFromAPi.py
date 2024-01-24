import requests
import csv

# URL of API and test to see if you get a successful response
# of 200
response = requests.get('https://randomuser.me/api')
# print(response.status_code)
# print(response.json())

# start parsing the information from API
# Parsing information from the API
data = response.json()['results'][0]
title = data['name']['title']
first_name = data['name']['first']
last_name = data['name']['last']
gender = data['gender']
age = data['dob']['age']

# Security Info
username = data['login']['username']
password = data['login']['password']
salt = data['login']['salt']
sha1 = data['login']['sha1']

# print(f'{title}. {first_name} {last_name}')
# print(f'Age:{age}')
# print(f'Sex:{gender}')
# print(f'Security Information:')
# print(f'Username:{username} and Password:{password}')
# print(f'Salt:{salt}')
# print(f'sha1:{sha1}')

# write data to CSV
with open('user_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # write the header info
    writer.writerow(['Title', 'First Name', 'Last Name', 'Age', 'Gender', 'Username', 'Password', 'Salt', 'SHA1'])
    # write the data
    writer.writerow([title, first_name, last_name, age, gender, username, password, salt, sha1])

print("Data saved to user_data.csv")
