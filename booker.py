import requests

#TODO:
#1. import and gitignore file with credentials
#2. make functions
#3. think of way to integrate both modules

session = requests.session()

session.get('https://se.timeedit.net/web/liu/db1/timeedit/sso/?ssoserver=liu_stud_cas&entry=wr_stud&back=https%3A%2F%2Fcloud.timeedit.net%2Fliu%2Fweb%2Fwr_stud%2F')
response = session.post('https://login.it.liu.se/idp/profile/cas/login?execution=e1s1', 
data={
	'j_username': 'din mammma',
	'j_password': '',
	'_eventId_proceed': '',
	'AuthMethod': 'FormsAuthentication'
}, 
)

response = session.get("https://cloud.timeedit.net/liu/web/wr_stud/objects.json?max=50&fr=f&part=t&partajax=t&im=f&step=1&sid=4&l=sv_SE&types=195&subtypes=230,231&dates=20181219-20181219&starttime=7:0&endtime=14:0")

print(response.headers)
print(response.text)