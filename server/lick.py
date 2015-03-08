import urllib
import ConfigParser
import json

class lick:
	
	def __init__(self):
		
		self.conf = ConfigParser.ConfigParser()
		self.conf.read("config.ini")
		self.levels = [0,0,0,0,0,0]
		for i in range(0,6):
			self.levels[i] = self.sendQuery(i)
			print "{index}: {num}".format(index=i, num=self.levels[i])	
	
	def sendBuy(self, slotnum):
		try:
			slot = self.conf.get("SLOTS", "M"+str(slotnum+1))
			prefix = self.conf.get("LICK", "prefix")
			urlFactory = self.conf.get("LICK", "buy")
			apikey = self.conf.get("LICK", "apikey")
			url = prefix + urlFactory.format(APIKEY=apikey, SCHACHTID=str(slot))
			print url	
			f = urllib.urlopen(url)
			
			data = json.load(f);
			self.levels[slotnum] = data["fuellstand"]
		except:
			print "lick error"
		return self.levels[slotnum]
		
	def sendEmpty(self, slotnum):
		try:
			slot = self.conf.get("SLOTS", "M"+str(slotnum+1))
			
			prefix = self.conf.get("LICK", "prefix")
			urlFactory = self.conf.get("LICK", "empty")
			apikey = self.conf.get("LICK", "apikey")
			url = prefix + urlFactory.format(APIKEY=apikey, SCHACHTID=str(slot))
			print url	
			urllib.urlopen(url)
			
			self.levels[slotnum] = 0
		except:
			print "lick error"
		return 0
		
		
	def sendQuery(self, slotnum):
		try:
			slot = self.conf.get("SLOTS", "M"+str(slotnum+1))
			
			prefix = self.conf.get("LICK", "prefix")
			urlFactory = self.conf.get("LICK", "query")
			url = prefix + urlFactory.format(SCHACHTID=str(slot))
			print url	
			f = urllib.urlopen(url)
			
			data = json.load(f);
			self.levels[slotnum] = data["fuellstand"]
		except:
			print "lick error"
		return self.levels[slotnum]


	def getLevel(self, slotnum):
		return self.levels[slotnum]

		
