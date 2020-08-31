import requests
import random
from termcolor import colored
import pyfiglet

print(colored(pyfiglet.figlet_format('DAD JOKE 3000', font='slant'), color='magenta'))


url = "https://icanhazdadjoke.com/search"

search_term = input("Let me tell you a joke! Give me a topic: ")

res = requests.get(
  url,
  headers={"Accept": "application/json"},
  params = {"term": search_term }

)

data = res.json()
# print(data['results'])



num_of_jokes = len(data['results'])
while len(data['results']) == 0:
  search_term = input(f'Sorry, I don\'t have any jokes about {search_term}. Please try again. ')

  res = requests.get(
  url,
  headers={"Accept": "application/json"},
  params = {"term": search_term }

  )

  data = res.json()
  
if len(data['results']) == 1:
  print(f'I\'ve got one joke about {search_term}. Here it is: ')
  for result in data['results']:
    print(result['joke'])

elif len(data['results']) > 1:
  print(f'I\'ve got {num_of_jokes} jokes about {search_term}. Here\'s one: ')
  joke = random.choice(data['results'])
  print(joke['joke'])
  


