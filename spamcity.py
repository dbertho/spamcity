import requests
from bs4 import BeautifulSoup
import urllib
from random import choice
from random import randint

def proxy_generator():
	proxy = choice(list(lines))
	proxy = {"https": proxy}
	print(proxy)
	return proxy

def pretty_print_POST(req):
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------REQUEST-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

def spam():
	while True:
		proxy = proxy_generator()
		try:
			sleep(1)
			response = requests.get('https://api.myip.com/', proxies=proxy, timeout=5)
			print(response.json())
			if response.status_code == 200:	
				break
			else:
				pass
		except:
			print("Proxy is not responding, trying another one")
			pass
	
	session = requests.Session()
	url = 'https://www.numbeo.com/crime/form.jsp?country=France&city=Brest&returnUrl=https%3A%2F%2Fwww.numbeo.com%2Fcrime%2Fin%2FBrest'
	jsessionid = "0"
	try:
		response = session.get(url, proxies=proxy, timeout=10)
		soup = BeautifulSoup(response.text, "html.parser")
		checking = soup.find('input', {'name': 'checking'}).get('value')
		print(checking)
		session_cookies = session.cookies
		cookies_dictionary = session_cookies.get_dict()
		jsessionid = cookies_dictionary['JSESSIONID']
		print(jsessionid)
	except:
		print("connection failed")

	ua=["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15"]

	level_of_crime = ["2.0", "2.0","2.0","2.0","2.0","1.0"]
	crime_increasing = ["2.0","2.0","2.0","2.0"]
	safe_alone_daylight = ["-2.0","-2.0","-2.0","-1.0","-1.0"]
	safe_alone_night = ["-2.0","-2.0","-2.0","-2.0","-2.0"]
	worried_home_broken = ["2.0","2.0","2.0","2.0","2.0","1.0"]
	worried_mugged_robbed = ["2.0","2.0","2.0","2.0","2.0","1.0","2.0","1.0"]
	worried_car_stolen = ["2.0","2.0","2.0","2.0","2.0","2.0","1.0"]
	worried_things_car_stolen = ["2.0","2.0","2.0","2.0","2.0","1.0"]
	worried_attacked = ["2.0","2.0","2.0","2.0","2.0","2.0"]
	worried_insulted = ["2.0","2.0","2.0","2.0","2.0","2.0","1.0"]
	worried_skin_ethnic_religion = ["2.0","2.0","2.0","2.0","2.0","1.0"]
	problem_drugs = ["2.0","2.0","2.0","2.0","2.0","2.0","1.0"]
	problem_property_crimes = ["2.0","2.0","2.0","2.0","1.0"]
	problem_violent_crimes = ["2.0","2.0","2.0","2.0","2.0","1.0"]
	problem_corruption_bribery = ["2.0","2.0","2.0","2.0","2.0","2.0","1.0"]
		
	headers = {
		"Host": "fr.numbeo.com",
		"User-Agent": choice(ua),
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" ,
		"Accept-Language": "en-US,en;q=0.5" ,
		"Accept-Encoding": "gzip, deflate, br" ,
		"Content-Type": "application/x-www-form-urlencoded" ,
		"Origin": "https://www.numbeo.com" ,
		"DNT": "1" ,
		"Connection": "keep-alive" ,
		"Referer": 'https://fr.numbeo.com/criminalit%C3%A9/modifier?returnUrl=https%3A%2F%2Ffr.numbeo.com%2Fcriminalit%25C3%25A9%2Fville%2FBrest&tracking=getEnterDataHtml2ForExtendedModuos&locCity=Brest&locCountry=France' ,
		"Cookie": "JSESSIONID="+jsessionid ,
		"Upgrade-Insecure-Requests": "1" ,
		"Sec-Fetch-Dest": "document" ,
		"Sec-Fetch-Mode": "navigate" ,
		"Sec-Fetch-Site": "same-origin" ,
		"Sec-Fetch-User": "?1" ,
		"Sec-GPC": "1",
	}
	data = {
		"locCountry":"France",
		"locCity":"Brest",
		"level_of_crime":choice(level_of_crime),
		"crime_increasing":choice(crime_increasing),
		"safe_alone_daylight":choice(safe_alone_daylight),
		"safe_alone_night":choice(safe_alone_night),
		"worried_home_broken":choice(worried_home_broken),
		"worried_mugged_robbed":choice(worried_mugged_robbed),
		"worried_car_stolen":choice(worried_car_stolen),
		"worried_things_car_stolen":choice(worried_things_car_stolen),
		"worried_attacked":choice(worried_attacked),
		"worried_insulted":choice(worried_insulted),
		"worried_skin_ethnic_religion":choice(worried_skin_ethnic_religion),
		"problem_drugs":choice(problem_drugs),
		"problem_property_crimes":choice(problem_property_crimes),
		"problem_violent_crimes":choice(problem_violent_crimes),
		"problem_corruption_bribery":choice(problem_corruption_bribery),
		"checking":jsessionid,
		"returnUrl":'https://fr.numbeo.com/criminalit%C3%A9/ville/Brest'
	}

	url = "https://fr.numbeo.com/crime/i18n-save"

	req = requests.Request('POST',url, headers=headers, data=data)
	prepared = req.prepare()
	pretty_print_POST(prepared)
	try:
		response = session.send(prepared, proxies=proxy, timeout=10)
		print(response.status_code)
	except:
		print("connection failed")


response1 = requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt")
response2 = requests.get("https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/ultrafast.txt")
response3 = requests.get("https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt")
response4 = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt")
response5 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt")
response6 = requests.get("https://raw.githubusercontent.com/rx443/proxy-list/main/online/https.txt")
response7 = requests.get("https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt")
lines = response1.text.splitlines()
lines.extend(response2.text.splitlines())
lines.extend(response3.text.splitlines())
lines.extend(response4.text.splitlines())
lines.extend(response5.text.splitlines())
lines.extend(response6.text.splitlines())
lines.extend(response7.text.splitlines())

while True:
	spam()
