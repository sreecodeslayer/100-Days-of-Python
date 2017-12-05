 #!/usr/bin/python3

import sys
import argparse
from deluge import Deluge


deluge = Deluge()
def getMagnetUrl():
	try:
		parser = argparse.ArgumentParser(description="Download torrent by giving Magnet URL")
		parser.add_argument('-m', '--magnet', type=str, help="Torrent Magnet URL", required=True)
		parser.add_argument('-p', '--downloadLocation', type=str, help="Torrent download location", required=True)
		args = parser.parse_args()

		magnetUrl = args.magnet
		download_location = args.downloadLocation
		
		return magnetUrl, download_location
	except KeyboardInterrupt:
		print("Bye!")
		sys.exit(0)		
	except Exception as e:
		print('Oh No! => %s' %e)
		sys.exit(2)

magnetUrl, download_location = getMagnetUrl()

status, msg = deluge.add_torrent(magnetUrl, download_location)

if not status:
	print("Adding torrent failed: ", msg)
	sys.exit(2)
else:
	print("Torrent added, Download started!!")
	sys.exit(0)

