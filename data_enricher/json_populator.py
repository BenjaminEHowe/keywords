#!/usr/bin/python3
import requests
import json
import argparse
import sys
import re

def main():
	if not len(sys.argv) == 3 :
		print("Incorrect argument count. Usage: json_populator [input file] [output file]")
		sys.exit()
	
	input_file_name = sys.argv[1]
	output_file_name = sys.argv[2]
	input = open(input_file_name,"r")
	parsed_input = json.loads(input.read())
	for key, value in parsed_input.items():
		parsed_input[key]["title"] = getTitle(value)
	output = open(output_file_name,"w")
	output.write(json.dumps(parsed_input, indent=4, sort_keys=True))

def getTitle(entry):
	url = entry["url"]
	result = requests.get(url)
	title_search = re.search(r'<title.*?>(.*?)</title>',result.text)
	if not title_search == None :
		title = title_search.group(1)
		return title
	else :
		return url

if __name__ == "__main__":
    main()
