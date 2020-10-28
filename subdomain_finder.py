from bs4 import BeautifulSoup
import tldextract
import requests
import sys
import re

banner = """\n

-------------------------------------------------------
 ____        _         _                       _       
/ ___| _   _| |__   __| | ___  _ __ ___   __ _(_)_ __  
\___ \| | | | '_ \ / _` |/ _ \| '_ ` _ \ / _` | | '_ \ 
 ___) | |_| | |_) | (_| | (_) | | | | | | (_| | | | | |
|____/ \__,_|_.__/ \__,_|\___/|_| |_| |_|\__,_|_|_| |_|
                                                       
 _____ _           _           
|  ___(_)_ __   __| | ___ _ __ 
| |_  | | '_ \ / _` |/ _ \ '__|
|  _| | | | | | (_| |  __/ |   
|_|   |_|_| |_|\__,_|\___|_|   
                               

-------------------------------------------------------
@author1 - @abhijitastlar

"""


certsh_url = r"https://crt.sh/?q="
enumerated_subdomains = []
def enumerate_domain(domain_name):
	try:
		certsh_response = requests.get(certsh_url+domain_name)
		parse_content = BeautifulSoup(certsh_response.content, 'html.parser')

		for each_item in parse_content.find_all('td'):
			parsed_subdomain = each_item.get_text()
			tld_domain =  tldextract.extract(parsed_subdomain)
			if(tld_domain.suffix != "" and parsed_subdomain.endswith(tld_domain.suffix)) and parsed_subdomain not in enumerated_subdomains:
				enumerated_subdomains.append(parsed_subdomain)
		for subdomain in enumerated_subdomains:
			print(subdomain)
	except Exception as e:
		print("Exception raised : {}".format(e))

if __name__ =="__main__":
	
	print(banner)
	if( len(sys.argv)!=2):
		print("Usage : python3 subdomain_finder.py domain\n")
		sys.exit(0)
	enumerate_domain(sys.argv[1])
