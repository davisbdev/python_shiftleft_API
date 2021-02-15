import requests
import csv
import pandas
import json
from pprint import pprint as pp
from config import baseurl, orgid, version, token, appid


def main ():
	get_apps()
	list_app_findings()


def get_apps():
	with requests.Session() as s:
		url = 'https://www.shiftleft.io/api/v4/orgs/{}/apps'.format(orgid)
		headers = {'Authorization':'Bearer {}'.format(token)}
		r = requests.get(url, headers=headers)
		#print(r.status_code)
		#print(r.content)
		apps = r.json()['response']
		#print(apps)
		#appids = []
		#for x in apps:
		#	if x['id'] != None:
		#		print('added app id')
		#		appids.append(x['id'])
		#	else:
		#		print('no app ids to add')
		#print(appids)
	

def list_app_findings():
	with requests.Session() as s:
		url = 'https://www.shiftleft.io/api/v4/orgs/{}/apps/{}/findings'.format(orgid, appid)
		headers = {'Authorization':'Bearer {}'.format(token)}
		payload = {'severity':'critical','finding_tags':'category=XSS'}
		r = requests.get(url, params=payload, headers=headers)
		findings = r.json()['response']
		pp(r.text)
		with open('output.csv', 'w+') as f:
			f.write(r.text)



#def read_app_finding():
	#with requests.Session() as s:
	#	url = 'https://www.shiftleft.io/api/v4/orgs/{}/apps/{}/findings/{findingID}'


#def get_app_scans():
		#appscans = []
		#for x in appids:
			#	scansurl = url + '/{}/scans'.format(x)
			#	appscans.append(scansurl)
			#print(appscans)
			#r = requests.get(scansurl, headers=headers)
			#print(r.status_code)
			#scansresponse = r.json()['response']
			#pp(r.content)


if __name__ == "__main__":
	main()
