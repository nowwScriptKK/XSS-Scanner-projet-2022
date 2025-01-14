from time import sleep
from colorama import Fore, init
from os import path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import randint
import requests

# Initialiser colorama pour Windows
init(autoreset=True)

class XssScanner:
    def __init__(self, url, wordlist, methode, proxy, data, use_proxy_list):
        self.proxy = proxy
        self.use_proxy_list = use_proxy_list
        self.proxy_list = []
        if self.use_proxy_list:
            self.load_proxy_list()

        if proxy:
            print('API PROXY SELECTED')
        else:
            print('No proxy')

        self.payload = False
        self.methode = methode
        self.wordlist = wordlist
        self.url = url
        self.payloads = ''
        self.datasets = ''
        if self.methode == 'post':
            self.data = tuple(data.split('#'))

        print(Fore.GREEN + "Selenium start...")

    def load_proxy_list(self):
        with open('files/proxylist.txt', 'r') as f:
            self.proxy_list = [line.strip() for line in f]

    def close_browser(self):
        print('Close Browser...')
        try:
            self.driver.quit()
        except:
            pass
        quit()

    def save_result(self):
        filename = randint(1, 1000000)
        files = open(f'files/save/{filename}_result.txt', "a")
        if self.payloads:
            files.write('\nPayload ->' + self.payloads + '\nData ->' + self.datasets + '\n')

        files.write(self.result)
        if self.methode == 'get':
            files.write(str(self.data_result))
        else:
            files.write(str(self.data_result))
        print(f'File save in files/save/{filename}_result.txt')
        files.close()
        self.close_browser()

    def scan(self):
        try:
            WebDriverWait(self.driver, 0).until(EC.alert_is_present())
            self.detect += 1
            alert = self.driver.switch_to.alert
            alert.accept()
            if self.methode == 'post':
                print(Fore.GREEN + 'FAILLIBLE  ->' + self.url + '\n')
            else:
                print(Fore.GREEN + 'FAILLIBLE  ->' + self.links)
            if self.methode == 'post':
                if self.payload:
                    self.payloads = str(self.payloads) + str(self.payload) + '\n'
                    self.datasets = str(self.datasets) + str(self.dataset) + '\n'
                    self.data_result.extend([self.url])
            else:
                self.data_result.extend([self.links])
        except TimeoutException:
            if self.methode == 'post':
                print(Fore.WHITE + 'TESTE ->' + self.url + '\n')
            else:
                print(Fore.WHITE + 'TEST ->' + self.links)

    def lunchWebDriver(self):
        try:
            sets = webdriver.FirefoxOptions()
            sets.add_argument('--headless')
            self.driver = webdriver.Firefox(options=sets)
            self.driver.get(self.url)
        except Exception as e:
            print(f"Error launching WebDriver: {e}")

    def run(self):
        self.data_result = []
        print(Fore.GREEN + 'URL attack : ' + self.url)
        if path.exists(self.wordlist):
            print(Fore.GREEN + 'Wordlist : ' + self.wordlist)
        else:
            print(Fore.RED + 'Wordlist does not exist : ' + self.wordlist)
            self.close_browser()
        self.count = 0
        self.detect = 0
        result = []
        self.lunchWebDriver()

        with open(self.wordlist, 'r') as f:
            for i, line in enumerate(f):
                if self.methode in ['get', 'GET']:
                    self.links = self.url.replace('{{inject}}', str(line))
                    try:
                        self.driver.get(self.links)
                        sleep(1)
                    except Exception as e:
                        print(Fore.RED + f'URL ERROR: {e}')
                        self.count -= 1
                    sleep(2)
                    self.scan()
                    self.count += 1
                elif self.methode in ['post', 'POST']:
                    injected = ''
                    c = 0
                    for o in self.data:
                        rq = tuple(o.split('='))
                        lst = list(rq)
                        self.dataset = lst[0]
                        lst[1] = lst[1].replace('{{inject}}', str(line))
                        self.payload = lst[1]
                        result.append(tuple(lst))

                    if self.use_proxy_list and self.proxy_list:
                        current_proxy = self.proxy_list[i % len(self.proxy_list)]
                        proxies = {
                            "http": current_proxy,
                            "https": current_proxy,
                        }
                    elif self.proxy:
                        proxies = {
                            "http": self.proxy,
                            "https": self.proxy,
                        }
                    else:
                        proxies = None

                    x = requests.post(self.url, data=result, proxies=proxies)
                    html_content = x.text
                    self.driver.get(f"data:text/html;charset=utf-8,{html_content}")
                    sleep(2)
                    self.scan()
                    result = []
                    self.payload = False
        print("######SCAN_END####")
        if self.detect >= 1:
            print(Fore.GREEN + 'DETECTED\n(' + str(self.detect) + '/' + str(self.count) + ')')
            self.result = 'URL DETECTED (' + str(self.detect) + '/' + str(self.count) + ')\n'

            for item in self.data_result:
                print(str(item))
            save = input('Save scan result ?(y/yes)')
            if save in ["yes", "y"]:
                self.save_result()
            else:
                self.close_browser()
        else:
            print(Fore.RED + 'No XSS detected.')
            self.close_browser()
