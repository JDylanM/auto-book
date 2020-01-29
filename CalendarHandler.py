from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

class CalendarHandler:
	def modify_time(self, time):
		return 1

	def book(self, date, starttime, endtime, location):
		"""Shows basic usage of the Google Calendar API.
		Prints the start and name of the next 10 events on the user's calendar.
		"""

		#Fix correct input for google API
		if ":" not in starttime:
			starttime = starttime + ':15:00'
		if ":" not in endtime:
			endtime = endtime + ':00:00'
		if len(date) == 8:
			date = date[:4] + "-" + date[4:6] + "-" + date[6:]

		datetime_start = date + "T" + starttime
		datetimes_end = date + "T" + endtime

		creds = None
		# The file token.pickle stores the user's access and refresh tokens, and is
		# created automatically when the authorization flow completes for the first
		# time.
		if os.path.exists('token.pickle'):
			with open('token.pickle', 'rb') as token:
				creds = pickle.load(token)
		# If there are no (valid) credentials available, let the user log in.
		if not creds or not creds.valid:
			if creds and creds.expired and creds.refresh_token:
				creds.refresh(Request())
			else:
				flow = InstalledAppFlow.from_client_secrets_file(
					'credentials.json', SCOPES)
				creds = flow.run_local_server(port=0)
			# Save the credentials for the next run
			with open('token.pickle', 'wb') as token:
				pickle.dump(creds, token)

		service = build('calendar', 'v3', credentials=creds)
		# jhgqt9obpt3i6cogiljuejvq0k@group.calendar.google.com THIS IS kandidat

		
		event = {
			'summary': 'Grupparbete Lokal',
			'location': location,
			'description': 'Grabana bot levererar ännu en gång',
			'start': {
				'dateTime': datetime_start,
				'timeZone': 'Europe/Stockholm',
			},
			'end': {
				'dateTime': datetimes_end,
				'timeZone': 'Europe/Stockholm',
			},
		}
		# Call the Calendar API
		event = service.events().insert(calendarId='primary', body=event).execute()
		print('Event created: %s' % (event.get('htmlLink')))
		page_token = None

if __name__ == '__main__':
	c = CalendarHandler()
	c.book("20200528", "19", "20", "Keyhuset")