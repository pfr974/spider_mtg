from os.path import join
import json
import subprocess

output = subprocess.check_output("ls -1 decks_formatted/ | wc -l", shell=True)
print('there are ',int(output),' files')

with open("legacy.txt","w") as fh:

	for i in range (1,int(output)+1,1):

		filename = 'decks_formatted/deck_{}'.format(i)
		print('reading ', filename)
	
		with open(filename, "r") as f:
			whole_txt = f.readlines()
		single_string = "".join(whole_txt)
		without_line_breaks = single_string.replace("\n", " ")

		json.dump(without_line_breaks, fh)
		fh.write('\n')
