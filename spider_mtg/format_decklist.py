from os.path import dirname, join
from pprint import pprint
import os, glob
import re
import subprocess

# I got this cool multireplace function from here: https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string

def multireplace(string, replacements):
    """
    Given a string and a replacement map, it returns the replaced string.

    :param str string: string to execute replacements on
    :param dict replacements: replacement dictionary {value to find: value to replace}
    :rtype: str

    """
    # Place longer ones first to keep shorter substrings from matching
    # where the longer ones should take place
    # For instance given the replacements {'ab': 'AB', 'abc': 'ABC'} against 
    # the string 'hey abc', it should produce 'hey ABC' and not 'hey ABc'
    substrs = sorted(replacements, key=len, reverse=True)

    # Create a big OR regex that matches any of the substrings to replace
    regexp = re.compile('|'.join(map(re.escape, substrs)))

    # For each match, look up the new string in the replacements
    return regexp.sub(lambda match: replacements[match.group(0)], string)



# I was able to find these regex easily with this great website: https://regex101.com/

regex_qty = r">\d+\s"
regex_name =  r"class=\"L14.*?>(.*?)<*.span>"


output = subprocess.check_output("ls -1 decks_raw/ | wc -l", shell=True)
print('there are ',int(output),' files')

for i in range (1,int(output)+1,1):

	filename = 'decks_raw/deck_{}.html'.format(i)
	print('reading ', filename)

	with open(filename,'r') as f:
		event_txt = f.readlines()

	# Put all the lines into a single string
	whole_txt = "".join(event_txt)
	matches_name = re.finditer(regex_name, whole_txt, re.MULTILINE)
	match_list_name = []
	for matchNum, match in enumerate(matches_name, start=1):
		match_list_name.append(match.group())
	matches_qty = re.finditer(regex_qty, whole_txt, re.MULTILINE)
	match_list_qty = []
	for matchNum, match in enumerate(matches_qty, start=1):
		match_list_qty.append(match.group())

	with open('decks_formatted/deck_{}'.format(i), 'w') as file_handler:
		for (item,nb) in zip(match_list_name,match_list_qty):
			item = multireplace(item, {'</span>': '', 'class="L14">': ''})
			nb = nb.replace('>','')
			file_handler.write("{} {}\n".format(nb,item))




