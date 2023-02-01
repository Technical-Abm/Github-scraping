import requests
import os
import time
from bs4 import BeautifulSoup

github_scraping_link = "https://github.com/Technical-Abm/Github-scraping"
response_data = requests.get(github_scraping_link)
soup = BeautifulSoup(response_data.text, "html.parser")
forks = soup.find("span", {"id": "repo-network-counter"}).get_text()

class logo:
    def __init__(self):
        self.author = "Technical Abm"
        self.github = "https://github.com/Technical-Abm"
        self.page = "https://www.facebook.com/techabm"
        self.website = "https://abmportfolioweb.000webhostapp.com/"
        pass

logo_object = logo()

author = logo_object.author
github = logo_object.github
page = logo_object.page
website = logo_object.website

wrapper = """  
             d8888 888888b.   888b     d888 
            d88888 888  "88b  8888b   d8888 
           d88P888 888  .88P  88888b.d88888 
          d88P 888 8888888K.  888Y88888P888 
         d88P  888 888  "Y88b 888 Y888P 888 
        d88P   888 888    888 888  Y8P  888 
       d8888888888 888   d88P 888   "   888 
      d88P     888 8888888P"  888       888               
---------------------------------------------------
(~) Author :- {}
(~) Github :- {}
(~) Page   :- {}
(~) Abm web:- {}
(~) Forks  :- {}
---------------------------------------------------
""".format(author, github, page, website, forks)

def get_github_user_info(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    user_info = response.json()
    if response.status_code == 404:
        raise KeyError("Error 404; Username not found")
    return user_info


def get_github_followers(username):
    response = requests.get(f"https://api.github.com/users/{username}/followers")
    followers = response.json()
    return followers

os.system("clear")
print(wrapper)
username = input(" (~) Enter Github username:- ")
user_info = get_github_user_info(username)
followers = get_github_followers(username)

print(f" (~) Username: {user_info['login']}")
print(f" (~) Github link:- {user_info['html_url']}")
print(f" (~) Creation date: {user_info['created_at']}")
print(f" (~) Total followers: {user_info['followers']}")

for follower in followers:
    print(f" (~) Follower: {follower['login']}")
