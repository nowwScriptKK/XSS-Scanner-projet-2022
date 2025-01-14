# Main
from xss import XssScanner
from time import sleep
import argparse

def _run(url, data, proxy, wordlist, use_proxy_list, proxy_list_file):
    if data:
        print('Set send POST')
        methode = 'post'
        print(data)
    else:
        methode = 'get'

    try:
        print('URL SET : ' + url)
    except:
        pass

    lunch = XssScanner(url, wordlist, methode, proxy, data, use_proxy_list, proxy_list_file)
    lunch.run()

def __main():
    parser = argparse.ArgumentParser(prefix_chars='-')
    parser.add_argument('-l', type=str, help='URL type is https://link.com/?data1={{inject}}&?data2={{inject}}\nPayload injected in "inject"')
    parser.add_argument("-d", required=False, help='Use data POST send data1={{inject}}#data2={{inject}}\nPayload injected in "inject"')
    parser.add_argument("-w", required=False, help='Specify the wordlist file (default is : files/wordlist/low.txt)')
    parser.add_argument("-p", required=False, help='Use a single proxy (format: http://user:pass@host:port or http://host:port)')
    parser.add_argument("-s", action='store_true', help='Use a proxy from the specified file for each request')
    parser.add_argument("-f", required=False, help='Specify the proxy list file (default is : files/proxylist.txt)')

    args = parser.parse_args()

    if not args.w:
        args.w = "files/wordlist/low.txt"

    if not args.d:
        sleep(0.5)
        args.d = False
        print('Send GET data')

    if not args.l:
        args.l = 'http://localhost/xsstest.php?q='
    print('default url :'+args.l)

    if not args.f:
        args.f = "files/proxylist.txt"

    return args

print(" _   _     _       _       _   _                  _ _       _     \n| |_| |__ (_)___  (_)___  | |_| |__   ___    __ _(_| |_ ___| |__  \n| __| '_ \| / __| | / __| | __| '_ \ / _ \  / _` | | __/ __| '_ \ \n| |_| | | | \__ \ | \__ \ | |_| | | |  __/ | (_| | | || (__| | | |\n \__|_| |_|_|___/ |_|___/  \__|_| |_|\___|  \__, |_|\__\___|_| |_|\n                                            |___/                 \n")
if __name__ == '__main__':
    print('With run use\npython3 ./main.py -l https://link.com/?data1={{inject}}&?data2={{inject}}\n\nIf you use post data\npython3 ./main.py -l https://link.com/ -d data1={{inject}}#data2={{inject}}&data3=text \n\n')

    parse = __main()
    _run(parse.l, parse.d, parse.p, parse.w, parse.s, parse.f)
