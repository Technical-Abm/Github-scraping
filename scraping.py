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
        self.websiteabm = "https://abmportfolioweb.000webhostapp.com/"
        pass

logo_object = logo()

author = logo_object.author
github = logo_object.github
page = logo_object.page
websiteabm = logo_object.websiteabm

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
""".format(author, github, page, websiteabm, forks)

class github:
    def __init__(self):
        os.system("clear")
        self.option_1 = "[01] Scraping abm owner github lookup"
        self.option_2 = "[02] Scraping own your github (token-required)"
        self.option_3 = "[03] Scraping Someone user complete public access"
        self.option_4 = "[04] Get unlimited useragents (latest and old mix)"
        self.option_5 = "[05] Get own your iplookup"
        self.option_6 = "[06] Get someone ipaddress (lookup)"
        self.option_7 = "[07] Install Cython and compile on python3"
        self.option_8 = "[08] Find github username and scraping"
        self.option_9 = "[09] Exit"
        pass

    def collect(self):
        os.system("clear")
        print(wrapper)
        print(self.option_1)
        print(self.option_2)
        print(self.option_3)
        print(self.option_4)
        print(self.option_5)
        print(self.option_6)
        print(self.option_7)
        print(self.option_8)
        print(self.option_9)
        print("---------------------------------------------------")
        print()
        self.ask = input("Enter an option:- ")
        if '1' or '01' in self.ask:
            os.system("clear")
            print(wrapper)
            self.githuburl = "https://github.com/Technical-Abm"
            self.scraper = requests.get(self.githuburl)
            self.main = BeautifulSoup(self.scraper.content, "html.parser")
            self.ownername = self.main.find(
                "span", {"class": "p-name vcard-fullname d-block overflow-hidden"}).get_text()
            self.ownerusername = self.main.find(
                "span", {"class": "p-nickname vcard-username d-block"}).get_text()
            self.joingithub = self.main.find("a", {"id": "year-link-2019"})
            self.urlscrapering = self.main.find(
                "span", {"class": "text-bold color-fg-default"}).get_text()
            self.urlscraperingdata = self.main.find(
                "span", {"class": "Counter"}).get_text()
            self.urlscraperingmain = self.main.find(
                "div", {"class": "p-note user-profile-bio mb-3 js-user-profile-bio f4"}).get_text()
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
        elif "2" or "02" in self.ask:
            self.container()
        elif "3" or "03" in self.ask:
            self.someoneaccess()
        elif "4" or "04" in self.ask:
            self.useragents()
        elif "5" or "05" in self.ask:
            self.ipaddress()
        elif "6" or "06" in self.ask:
            self.get()
        elif "7" or "07" in self.ask:
            self.compile()
        elif "8" or "08" in self.ask:
            self.jslink()
        elif "9" or "09" in self.ask:
            sys.exit()
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
        self.expirydate = self.find.find(
            "span", {"class": "text-semibold text-italic"}).get_text()
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
            self.useragent = int(
                input("(~) How many user-agents do you want to generate? "))
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

    def ipaddress(self):
        os.system("clear")
        print(wrapper)
        print("Your ipaddress lookup....".center(50))
        print()
        self.ip = requests.get("http://ip-api.com/json/")
        self.details = self.ip.json()
        print("status :- "+self.details["status"])
        print("country :- "+self.details["country"])
        print("countryCode :- "+self.details["countryCode"])
        print("regionName :- "+self.details["regionName"])
        print("city :- "+self.details["city"])
        print("isp:- "+self.details["isp"])
        print()
        input("Press enter to back.. ")
        mycode.collect()

    def get(self):
        os.system("clear")
        print(wrapper)
        try:
            self.get = int(input("(~) Enter ipaddress :- "))
            self.clean = requests.get("http://ip-api.com/json/"+self.get)
            self.go = self.clean.json()
            print("Your ipaddress lookup....".center(50))
            print("status :- "+self.go["status"])
            print("country :- "+self.go["country"])
            print("countryCode :- "+self.go["countryCode"])
            print("regionName :- "+self.go["regionName"])
            print("city :- "+self.go["city"])
            print("isp:- "+self.go["isp"])
            print()
            input("Press enter to back.. ")
            mycode.collect()
        except (KeyError, AttributeError, KeyboardInterrupt):
            print("something wrong....".center(50))
            mycode.collect()

    def compile(self):
        os.system("clear")
        print(wrapper)
        print("Compile cython on your python3".center(50))
        print()
        try:
            self.compile = input("(~) Enter filename :- ")
            if self.compile.endswith(".py"):
                print(
                    "error; .pyx files require - please change filename extension".center(50))
                time.sleep(3)
                input("Press enter to back....")
                mycode.collect()
            else:
                os.system("cythonize --3str -i "+self.compile)
        except (FileNotFoundError, IOError, FileExistsError):
            print("Invalid filename or something error".center(50))
            time.sleep(2)
            input("Press enter to back...")
            mycode.collect()

    def jslink(self):
        try:
            os.system("cd username-finder && python find.py")
        except KeyError:
            print("something wrong...".center(50))
    
    def someoneaccess(self):
        os.system("clear")
        print(wrapper)
        print("Enter correct username to find Github all access data".center(50))
        print()
        self.username = input("(~) Enter Username :- ")
        print("---------------------------------------------------")
        print()
        self.urllink = f"https://api.github.com/users/{self.username}"
        self.paramas = {
            "Accept": "application/vnd.github+json"
            }
        self.response = requests.get(self.urllink, headers=self.paramas)
        if self.response.status_code == 200:
            self.reverse = self.response.json()
            try:
                if "login" in self.reverse:
                    print("(~) Owner Username : %s" % self.reverse["login"])
                elif "login" not in self.reverse:
                    print(" (~) Username not found : %s" % self.reverse["login"])
                if "html_url" in self.reverse:
                    print("(~) User Link : %s" % self.reverse["html_url"])
                elif "html_url" not in self.reverse:
                    print("(~) Link not found : %s" % self.reverse["html_url"])
                if "type" in self.reverse:
                    print("(~) User Type : %s" % self.reverse["type"])
                elif "type" not in self.reverse:
                    print("(~) User not found : %s" % self.reverse["type"])
                if "location" in self.reverse:
                    print("(~) User Location : %s" % self.reverse["location"])
                elif "location" not in self.reverse:
                    print("(~) Location not found : %s" % self.reverse["location"])
                if "bio" in self.reverse:
                    print("(~) User Bio : %s" % self.reverse["bio"])
                elif "bio" not in self.reverse:
                    print("(~) Bio not found : %s" % self.reverse["bio"])
                if "public_repos" in self.reverse:
                    print("(~) User Public Repo : %s" % self.reverse["public_repos"])
                elif "public_repos" not in self.reverse:
                    print("(~) Public Repo not found : %s" % self.reverse["public_repos"])
                if "followers" in self.reverse:
                    print("(~) User Followers : %s" % self.reverse["followers"])
                elif "followers" not in self.reverse:
                    print("(~) Followers not found : %s" % self.reverse["followers"])
                if "following" in self.reverse:
                    print("(~) User Following : %s" % self.reverse["following"])
                elif "following" not in self.reverse:
                    print("(~) Following not found : %s" % self.reverse["following"])
                if "created_at" in self.reverse:
                    print("(~) User Joined/Created : %s" % self.reverse["created_at"])
                elif "created_at" not in self.reverse:
                    print("(~) Joined/Created not found : %s" % self.reverse["created_at"])
                if "updated_at" in self.reverse:
                    print("(~) User Last Updated : %s" % self.reverse["updated_at"])
                elif "updated_at" not in self.reverse:
                    print("(~) Last Updated not found : %s" % self.reverse["updated_at"])
                print()
                input(" Press enter to back < ")
                mycode.collect()
            except KeyError:
                print("Something wrong".center(50))
                time.sleep(2)
                mycode.collect()
        elif self.response.status_code == 404:
            print("Error 404, You entered {} username not found ".center(50)).format(self.username)
            time.sleep(2)
            mycode.collect()
        else:
            print("Invalid response file".center(50))
            time.sleep(2)
            mycode.collect()
            
mycode = github()
mycode.collect()
