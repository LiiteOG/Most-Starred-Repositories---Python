from pydoc import resolve
from unicodedata import name
from urllib import response
import requests
import pprint

# ---- Different API Set ----
# https://randomuser.me/api
# response = requests.get("https://randomuser.me/api")

# gender = response.json()['results'][0]['gender']
# print(gender)

# fname = response.json()['results'][0]['name']['first']

# lname = response.json()['results'][0]['name']['last']

# age = response.json()['results'][0]['dob']['age']

# print(f'{fname} {lname}')
# print(f'Age: {age}')

# **********************************************************************
# response = requests.get("https://api.github.com/search/repositories?q=created:%22%3E2018-09-30%22language:python&sort=stars&order=desc&per_page=10")

# print(response.status_code)
# pprint.pprint(response.json())
# starcount = response.json()['items'][0]['stargazers_count']
# print(starcount)

mainurl = "https://api.github.com/search/repositories?q=created:%22%3E2018-09-30%22language:python&sort=stars&order=desc&per_page=10"

def main_request(mainurl):
    response = requests.get(mainurl)
    return response.json()

def parse_json(response):
    for i in response['items']:
        print(i['name'], (i['stargazers_count']))
    return

def likenums(response):
    for i in response['items']:
        print(i['stargazers_count'], len(i))
    # ---- This will print out the amount of items in the list ----
    # counter = 0
    # for i in response['items']:
    #     counter = counter + 1
    #     print(counter)  
    return

data = main_request(mainurl)

# ---- Same print, different methods ----
# print(likenums(data))
# likenums(data)

parse_json(data)

# ---- Below is method without functions ----
# name = data['items'][0]['name']
# print(name)

# for i in response.json()['items']:
#     print(i['name'])
    
# starcount = data['items'][0]['stargazers_count']
# print(starcount)

# for i in response.json()['items']:
#     print(i['stargazers_count'])
    