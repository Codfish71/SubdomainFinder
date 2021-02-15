import requests

domain = 'xyz.com'

file = open('subdomnames.txt','r')
content = file.read()
subdomains = content.splitlines()

for subdomain in subdomains:
	url = f'http://{subdomain}.{domain}'
	try:
		requests.get(url)
	except requests.ConnectionError:
		pass
	else:
		print("Discovered subdmain : ",url)
