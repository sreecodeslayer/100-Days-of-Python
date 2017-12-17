import re

def validate_number(phn_num):
	regex = re.compile(r"\+91\d{10}")
	searched = regex.search(phn_num)
	if searched:
		print("Found: ", searched.group())
		return True
	else:
		print("Not Found :(")
		return False


phn_num = input("Enter phone number: ")

validate_number(phn_num)