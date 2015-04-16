#!/usr/bin/python
import json, urllib2, io
from datetime import datetime
from config import api_key, dir

def main():
	d=datetime.now()
	for id in json.loads(urllib2.urlopen("https://euw.api.pvp.net/api/lol/euw/v4.1/game/ids?beginDate={}&api_key={}".format(int((datetime(d.year,d.month,d.day,d.hour,int(d.minute/5)*5) - datetime(1970,1,1)).total_seconds())-(36000),api_key)).read()):
	        with io.open(dir+"{}.json".format(id),"w",encoding="utf-8") as f:
	                f.write(unicode(urllib2.urlopen("https://euw.api.pvp.net/api/lol/euw/v2.2/match/{}?api_key={}".format(id,api_key)).read()))

if __name__=="__main__":
	main()
