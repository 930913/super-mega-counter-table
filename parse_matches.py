#!/usr/bin/python
import json, os
from collections import defaultdict
from config import dir

def main():
	winmap=defaultdict(int)
	for file in (dir+file for file in os.listdir(dir) if file.endswith(".json")):
		for id in process_match(file):
			winmap[id]+=1
	json.dump(winmap,open(dir+"winmap","w"))

def process_match(file):
	wonteam,lostteam,ret,data=[],[],[],json.load(open(file,"r"))
	for champ in data["participants"]:
		(wonteam if champ["stats"]["winner"] else lostteam).append(champ["championId"])
	return ["{}-{}".format(wonner,loster) for wonner in wonteam for loster in lostteam]

if __name__=="__main__":
	main()
