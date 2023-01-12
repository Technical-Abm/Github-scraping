import requests
import time
import os
from bs4 import BeautifulSoup
import subprocess

github_scraping_link = "https://github.com/Technical-Abm/Github-scraping"
response_data = requests.get(github_scraping_link)
soup = BeautifulSoup(response_data.text, "html.parser")
modules_txt = soup.find(
    "a", {"class": "js-navigation-open Link--primary", "title": "modules.txt"})

if 'modules.txt' in modules_txt:
    subprocess.run(["pip", "install", "-r", "modules.txt"])
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
---------------------------------------------------
        project :- {}
---------------------------------------------------
""".format(author, github, page, website, project)


class github:
    def __init__(self):
        os.system("clear")
        self.option_1 = "[1] Scraping abm owner github-api"
        self.option_2 = "[2] Scraping abm owner github followers list"
        self.option_3 = "[3] Scraping own your github (token-required)"
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
            self.username = "Technical-Abm"
            self.token = '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'
            self.headers = {'Authorization': 'Token ' + self.token}
            self.response = f'https://api.github.com/users/{self.username}/repos'
            self.reverse = requests.get(self.response, headers=self.headers)
            self.repo = self.reverse.json()
            self.scraper = requests.get(self.githuburl)
            self.main = BeautifulSoup(self.scraper.content, "html.parser")
            self.urlscrapering = self.main.find(
                "span", {"class": "text-bold color-fg-default"}).get_text()
            self.urlscraperingdata = self.main.find(
                "span", {"class": "Counter"}).get_text()
            self.urlscraperingmain = self.main.find(
                "div", {"class": "p-note user-profile-bio mb-3 js-user-profile-bio f4"}).get_text()
            for self.connection in self.repo:
                self.name = self.connection['owner']['login']
                self.html = self.connection['owner']['html_url']
                self.owner = self.connection['owner']['url']
                self.id = self.connection['owner']['id']
                print("Abm Owner Github Scraping Details")
                print()
                time.sleep(2)
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
                pass
            else:
                print("Recorde not found or dir invalid")
                time.sleep(2)
                exit()
        elif "2" in self.ask:
            os.system("clear")
            self.username = "Technical-Abm"
            self.token = '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'
            self.headers = {'Authorization': 'Token ' + self.token}
            self.url = f'https://api.github.com/users/{self.username}'
            self.maincollect = requests.get(self.url, headers=self.headers)
            self.json = self.maincollect.json()
            self.list = self.json['followers_url']
            self.section = requests.get(self.list, headers=self.headers)
            self.nav = self.section.json()
            for self.navlist in self.nav:
                print(self.navlist['login'])
            else:
                exit()
                pass
        elif "3" in self.ask:
            self.container()
        elif "4" in self.ask:
            self.exiting()
        else:
            print("Please select an valid option")
            time.sleep(2)
            mycode.collect()

    def container(self):
        os.system("clear")
        print(wrapper)
        print("You can scraping own your github")
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
        self.urlscrapering = self.main.find(
            "span", {"class": "text-bold color-fg-default"}).get_text()
        self.urlscraperingdata = self.main.find(
            "span", {"class": "Counter"}).get_text()
        self.urlscraperingmain = self.main.find(
            "div", {"class": "p-note user-profile-bio mb-3 js-user-profile-bio f4"}).get_text()
        if self.response.status_code == 200:
            self.repos = self.response.json()
            for self.repo in self.repos:
                os.system("clear")
                print(wrapper)
                print("Scraping data output".center(50))
                time.sleep(2)
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
        os.system("clear")
        print(wrapper)
        self.close = input("Do you want to exit tool ")
        self.answer()

    def answer(self):
        if 'yes' or 'Yes' in self.close:
            exit()
        elif "no" or 'No' in self.close:
            mycode.collect()
        else:
            print("Please select an correct option".center(50))
            time.sleep(2)
            mycode.collect()


mycode = github()
mycode.collect()
