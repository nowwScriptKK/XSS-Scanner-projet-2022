## XSS-Scanner

# Update 15/01/2025

Detector :
403 Forbidden
503 Service Unavailable
520 à 527 Cloudflare specific errors.

    URL ERROR: HTTPSConnectionPool(host='www.exghjghjgample.com', port=443): Max retries exceeded with url: /?q=';alert('XSS');//%0A (Caused by     NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x0000025DE0F9A540>: Failed to resolve 'www.exghjghjgample.com' ([Errno 11001] getaddrinfo failed)"))

# Update du 14/01/2024
Added support for single proxy or proxy file management

Added "-p" for unique proxy and "-s" for list proxy add "-s -f /files/wordlist/proxylist.txt"

Added new payload list : "xssBigPayloadList.txt"

Added the Firefox Gecko for windows

Adaptation of the code for use under Windows

Add multiparam

### Exemple 1 : Basic Usage with a GET URL
    python ./main.py -l https://www.example.com/?q={{inject}}

### Exemple 2 : Basic Usage with a POST URL
    python ./main.py -l https://www.example.com/ -d data1={{inject}}#data2={{inject}}

### Exemple 3 : Use with a custom wordlist
    python ./main.py -l https://www.example.com/?q={{inject}} -w files/wordlist/xssBigPayloadList.txt

### Exemple 4 : Use with a single proxy
    python ./main.py -l https://www.example.com/?q={{inject}} -p http://user:pass@proxy.example.com:8080

### Exemple 5 : Using with a proxy list
    python ./main.py -l https://www.example.com/?q={{inject}} -s -f files/proxylist.txt

### Exemple 6 : Use with a custom wordlist and proxy list
    python ./main.py -l https://www.example.com/?q={{inject}} -s -f files/proxylist.txt -w files/wordlist/xssBigPayloadList.txt

### Exemple 7 : Use post data, proxy list, wordlist 
    python ./main.py -l https://www.example.com/ -d data1={{inject}}#data2={{inject}}  -s -f files/proxylist.txt  -w files/wordlist/xssBigPayloadList.txt


A future update will certainly be made to detect the presence of a cloudflare, or potential blockage


# The project dates back to 2022; XSS is a static vulnerability over time, but improvements can be added to the detection files.

Thanks to the use of gecko, this script can be made almost completely invisible.

If you need help with installation or configuration, contact me on Discord : actheglitch

Simple XSS HTTP/S scanner, it can scan dom or any other script. <br>I used Selenium to develop this software, it launches a browser in the background and returns the result to you, the script is waiting to receive an alert(). <br>So you can use any wordlist for AngularJS, Electron etc.<br><br>

<br>
## Setting: 
If you are using Windows you need to change the webdriver : <br>
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/<br>
You must change the direction of the file in xss.py<br>
      
    self.driver = webdriver.Firefox(executable_path="files/driver/geckodriver", options=sets)
    
For use get method<br>
      
    python3 main.py -l http://yoururl.com/?data={{inject}}\&data2={{inject}}\&data3=NoInject
    Note: for get data use \& to change data.

For use post method

    python3 main.py -l http://yoururl.com/ -d data={{inject}}#data1={{inject}}#data2=NoInject
    Note: use # to change data.


If you use custom wordlist

    python3 main.py -l http://yoururl.com/{{inject}}\&data={{inject}} -w files/wordlist/youcustomwordlist.txt


Script use # for change data scope
The post method generates the HTML code of the web page before running it in brute on Selenium, 
I have a small bug in the result, it detects alerts well but the target data is not recovered.


<br>
<br><br>
Simple XSS Scanner HTTP/HTTPS with Selenium, use -d to add data.<br><br>

## Xss Simple Detected
<a href='https://postimg.cc/PPSTvjzg' target='_blank'><img src='https://i.postimg.cc/6pX3S67p/Capture-d-cran-2022-01-17-17-30-15.png' border='0' alt=''/></a><br><br>

## Xss Dom Detected
<a href='https://postimg.cc/wtq61jSY' target='_blank'><img src='https://i.postimg.cc/bvbdFGgr/xssssssss.png' border='0' alt='xssssssss'/></a>

<br>
