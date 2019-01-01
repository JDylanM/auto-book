import schedule
import time
from datetime import date, timedelta, datetime
import sys
from Booker import *
from constants import *

def job(date, start_time, end_time, email):
	booker = Booker()
	print("Signing in...")
	booker.login(account, password)
	#booker.get_rooms("20181222-20181222", "14:00", "15:00")
	print("Booking...")
	book_id = booker.book(date, start_time, end_time)
	print("Sending verification email...")
	booker.send_email(book_id, email)
	print("Booking done! Hopefully without errors heheheuhue")	


if __name__ == "__main__":
	print(type(sys.argv))
	if(len(sys.argv) != 5):
		raise ValueError("Need 5 arguments, example: python3 executer.py 20190102 14 15 dylma900@student.liu.se")
		sys.exit(0)

	today = str(date.today()).replace("-", "")

	print(today)
	in_date = sys.argv[1]
	start_time = sys.argv[2]
	end_time = sys.argv[3]
	email = sys.argv[4]

	if(today == in_date):
		print("tja")
		job(in_date, start_time, end_time, email)
	else:
		in_date = datetime.strptime(in_date, '%Y%m%d').date()
		day_before = str(in_date - timedelta(days=1))
		print(day_before)
		#TODO schedule at correct in_date
			#while True:
			#	schedule.every().day.at("23:26").do(job,'It is 01:00')
			#	schedule.run_pending()
			#	time.sleep(60) # wait one minute


