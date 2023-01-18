import requests
import time
import os
from bs4 import BeautifulSoup
import sys
import fake_useragent
import subprocess

if sys.version_info < (3, 11):
    print("This script requires Python 3.11 or higher. Please upgrade your Python version.".center(50))
    sys.exit()
else:
    os.system("clear")
    print()
    print()
    print("python3.11 has already installed.".center(50))

github_scraping_link = "https://github.com/Technical-Abm/Github-scraping"
response_data = requests.get(github_scraping_link)
soup = BeautifulSoup(response_data.text, "html.parser")
forks = soup.find("span", {"id": "repo-network-counter"}).get_text()
modules_txt = soup.find("a", {"class": "js-navigation-open Link--primary", "title": "modules.txt"})

if 'modules.txt' in modules_txt:
    with open("modules.txt", 'r') as main:
        modules = main.readlines()
        pass
    for pipnes in modules:
        subprocess.run(['pip', 'install', pipnes])
else:
    print("modules.txt not found or filename has changed".center(50))
    time.sleep(2)
    exit()


class logo:
    def __init__(self):
        self.author = "Technical Abm"
        self.github = "https://github.com/Technical-Abm"
        self.page = "https://www.facebook.com/techabm"
        self.website = "https://abmportfolioweb.000webhostapp.com/"
        self.project = "Github scraping tool"
        pass


logo_object = logo()

author = logo_object.author
github = logo_object.github
page = logo_object.page
website = logo_object.website
project = logo_object.project

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
        project :- {}
---------------------------------------------------
""".format(author, github, page, website, forks, project)


class github:
    def __init__(self):
        os.system("clear")
        self.option_1 = "[1] Scraping abm owner github-api"
        self.option_2 = "[2] Scraping own your github (token-required)"
        self.option_3 = "[3] Get unlimited useragents (latest and old mix)"
        self.option_4 = "[4] Exit"
        pass

    def collect(self):
        os.system("clear")
        print(wrapper)
        print(self.option_1)
        print(self.option_2)
        print(self.option_3)
        print(self.option_4)
        print("---------------------------------------------------")
        print()
        self.ask = input("Enter an option:- ")
        if '1' in self.ask:
            os.system("clear")
            print(wrapper)
            self.githuburl = "https://github.com/Technical-Abm"
            self.scraper = requests.get(self.githuburl)
            self.main = BeautifulSoup(self.scraper.content, "html.parser")
            self.ownername = self.main.find("span", {"class": "p-name vcard-fullname d-block overflow-hidden"}).get_text()
            self.ownerusername = self.main.find("span", {"class": "p-nickname vcard-username d-block"}).get_text()
            self.joingithub = self.main.find("a", {"id": "year-link-2019"})
            self.urlscrapering = self.main.find("span", {"class": "text-bold color-fg-default"}).get_text()
            self.urlscraperingdata = self.main.find("span", {"class": "Counter"}).get_text()
            self.urlscraperingmain = self.main.find("div", {"class": "p-note user-profile-bio mb-3 js-user-profile-bio f4"}).get_text()
            for self.connection in self.main:
                print("Abm Owner Github Scraping Details".center(50))
                print()
                print("(~) Github Ower name: "+self.ownername)
                time.sleep(1)
                print("(~) Github Username"+self.ownerusername)
                time.sleep(1)
                print("(~) Github Joined Date: "+self.joingithub.text)
                time.sleep(1)
                print("(~) Github Followers: "+self.urlscrapering)
                time.sleep(1)
                print("(~) Github Projects Count: "+self.urlscraperingdata)
                time.sleep(1)
                print("(~) Github Owner Bio: "+self.urlscraperingmain)
                time.sleep(1)
                print()
                input("Process has completed, Go to back <")
                mycode.collect()
                pass
            else:
                print("Recorde not found or dir invalid".center(50))
                time.sleep(2)
                exit()
        elif "2" in self.ask:
            self.container()
        elif "3" in self.ask:
            self.useragents()
        elif "4" in self.ask:
            self.exiting()
        else:
            print("Please select an valid option".center(50))
            time.sleep(2)
            mycode.collect()

    def container(self):
        os.system("clear")
        print(wrapper)
        print("You can scraping own your github".center(50))
        print()
        time.sleep(2)
        self.complete = input("(~) Enter complete github-link:- ")
        self.username = input("(~) Enter your Github username:- ")
        self.token = input("(~) Enter your Github token:- ")
        self.headers = {'Authorization': 'Token ' + self.token}
        self.repos_url = f'https://api.github.com/users/{self.username}/repos'
        self.response = requests.get(self.repos_url, headers=self.headers)
        self.scraper = requests.get(self.complete)
        self.main = BeautifulSoup(self.scraper.content, "html.parser")
        self.htmlexpired = "<span class='text-semibold text-italic'>on Sun, Feb 12 2023</span>"
        self.find = BeautifulSoup(self.htmlexpired, "html.parser")
        self.expirydate = self.find.find("span", {"class": "text-semibold text-italic"}).get_text()
        self.urlscrapering = self.main.find("span", {"class": "text-bold color-fg-default"}).get_text()
        self.urlscraperingdata = self.main.find("span", {"class": "Counter"}).get_text()
        self.urlscraperingmain = self.main.find("div", {"class": "p-note user-profile-bio mb-3 js-user-profile-bio f4"}).get_text()
        if self.response.status_code == 200:
            self.repos = self.response.json()
            for self.repo in self.repos:
                os.system("clear")
                print(wrapper)
                print("Scraping data output".center(50))
                time.sleep(2)
                print()
                print("(~) Your Token: "+self.token)
                print("(~) Token Expires Date: "+self.expirydate)
                print()
                self.name = self.repo['owner']['login']
                self.html = self.repo['owner']['html_url']
                self.owner = self.repo['owner']['url']
                self.id = self.repo['owner']['id']
                print("(~) Github name: "+self.name)
                time.sleep(1)
                print("(~) Github link: "+self.html)
                time.sleep(1)
                print("(~) Github api: "+self.owner)
                time.sleep(1)
                print("(~) Github ID: "+str(self.id))
                time.sleep(1)
                print("(~) Github followers: "+self.urlscrapering)
                time.sleep(1)
                print("(~) Github repos: "+self.urlscraperingdata)
                time.sleep(1)
                print("(~) Github Bio: "+self.urlscraperingmain)
                time.sleep(1)
                print()
                input("Process has completed, Go to back <")
                mycode.collect()
        else:
            print(f'Error {self.response.status_code}: {self.response.reason}')

    def exiting(self):
        self.alert = input("Do you want to exit this tool: ")
        self.me()

    def me(self):
        if 'yes' or 'Yes' or 'y' in self.alert:
            exit()
        elif 'No' or 'no' or 'n' in self.alert:
            mycode.collect()
    
    def useragents(self):
        os.system("clear")
        print(wrapper)
        self.ua = fake_useragent.UserAgent()
        try:
            self.useragent = int(input("(~) How many user-agents do you want to generate? "))
            user_agents_main = []
            for x in range(self.useragent):
                user_agents_main.append(self.ua.random)
            with open("useragent.txt", "w") as f:
                for user in user_agents_main:
                    f.write(user + "\n")
                    pass
                pass
            print(user_agents_main)
            self.saved()
        except ValueError:
            print("Useragent not found or invalid number for  generate.".center(50))
            time.sleep(2)
            mycode.collect()

    def saved(self):
        print()
        print()
        print("File saved as useragent.txt".center(50))
        time.sleep(3)
        mycode.collect()

mycode = github()
mycode.collect()
