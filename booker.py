import requests
from constants import *

#TODO:
# classes of find_holes + booker
#3. think of way to integrate both modules


def login(session):
	session.get('https://se.timeedit.net/web/liu/db1/timeedit/sso/?ssoserver=liu_stud_cas&entry=wr_stud&back=https%3A%2F%2Fcloud.timeedit.net%2Fliu%2Fweb%2Fwr_stud%2F')
	response = session.post(
		'https://login.it.liu.se/idp/profile/cas/login?execution=e1s1',
		data={
			'j_username': account,
			'j_password': password,
			'_eventId_proceed': '',
			'AuthMethod': 'FormsAuthentication'
		},
	)

def get_rooms(session):
	payload = {
		'max': '3',
		'fr': "f",
		'part': "t",
		'partajax': "t",
		'im': "f",
		'step': "1",
		'sid': "4",
		'l': "sv_SE",
		'types': "195",
		'subtypes': "230,231",
		'fe': "23.Valla",
		'dates': "20181222-20181222",
		'starttime': "14:0",
		'endtime': "15:0"
	}

	# bokade rum här
	response = session.get('https://cloud.timeedit.net/liu/web/wr_stud/objects.json',params=payload)

def book(session):
	payload = {
		'kind': 'reserve',
		'nocache': '4',
		'l': 'sv_SE',
		'o': ['263991.195', '435564.184'],
		'aos': '',
		'dates': '20181223',
		'starttime': '16:00',
		'endtime': '17:00',
		'url': 'https://cloud.timeedit.net/liu/web/wr_stud/ri1Q8.html#00263991',
		'fe7': '',
	}

	response = session.post(
		'https://cloud.timeedit.net/liu/web/wr_stud/ri1Q8.html',
		data=payload
	)
	print(response.text)

if __name__ == "__main__":
	session = requests.session()
	login(session)
	get_rooms(session)
	book(session)
