import requests
from scrapy.selector import Selector
import argparse
import sys

def parse_url(url):
	try:

		resp = requests.get(url)
		sel = Selector(text=resp.content)

		final_img = sel.xpath('//meta[@property="og:image"]/@content').extract_first()
		print("Final image :: ",final_img)
	except Exception as e:
		raise e

try:
	parser = argparse.ArgumentParser(description="Download full size instagram by giving image URL")
	parser.add_argument('-u', '--url', type=str, help="Instagram image URL [ eg. : 'https://www.instagram.com/p/BcAkgR-FPav/' ]", required=True)
	args = parser.parse_args()

	insta_image_url = args.url
	parse_url(insta_image_url)
except KeyboardInterrupt:
	print("Bye!")
	sys.exit(0)		
except Exception as e:
	print('Oh No! => %s' %e)
	sys.exit(2)