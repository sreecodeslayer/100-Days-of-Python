from notify2 import init, Notification
from time import sleep

import schedule


def notify():
	init('Notify')

	n = Notification("Drink Water", "Hey asshole, drink some water FFS")

	n.show()
	sleep(10)
	n.close()
	return True

schedule.every().hour.do(notify)

while True:
	schedule.run_pending()
	sleep(1)
	