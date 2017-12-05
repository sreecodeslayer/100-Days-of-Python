import requests, base64

DELUGE_URL = "http://192.168.10.109:5656/json"
DELUGE_PASS = 'deluge'

class Deluge(object):
	cookies = None
	headers = {'Accept':'application/json', 'Content-Type':'application/json'}

	AUTH_LOGIN = 'auth.login'
	GET_TORRENTS = 'webapi.get_torrents'
	ADD_TORRENT = 'webapi.add_torrent'


	def __init__(self):
		data = {
			'id':1,
			'method':self.AUTH_LOGIN,
			'params':[DELUGE_PASS]
		}
		resp = requests.post(DELUGE_URL, json = data, headers=self.headers)
		if resp.status_code == 200:
			self.cookies = resp.cookies
		else:
			self.cookies = None

	def add_torrent(self,magnet_url ,download_location='/home/sreenadh/Videos'):
		if self.cookies:
			if not magnet_url:
				return False, "magnet_url required"
			if not download_location:
				return False, "download_location required"
			download_location = {'download_location': download_location}
			data = {
				'id':1,
				'method':self.ADD_TORRENT,
				'params':[magnet_url, download_location]
			}
			resp = requests.post(DELUGE_URL, json = data, headers=self.headers, cookies=self.cookies)
			if resp.status_code == 200:
				data = resp.json()
				if not data.get('error') and data.get('result'):
					return True, data.get('result')
				else:
					return False, data.get('error')
		else:
			return False, "Not authorized"
