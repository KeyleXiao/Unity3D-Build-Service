import sys, os
import json

class ConfigBase:
	ConfigFolder = ""
	ConfigFullPath = ""
	JsonFile = ""
	data = {}

	def __init__(self):
		self.setJsonFileName()
		self.ConfigFolder = self.getCurrentConfigFolder()
		self.getFileFullPath()
		return

	def setJsonFileName(self):
		pass

	def loadConfig(self):
		if not os.path.exists(self.ConfigFullPath):
			return self.writeConfig()
		else:
			jsonFile = open(self.ConfigFullPath, 'r');
			content = jsonFile.read()
			jsonFile.close()
			self.data = json.loads(content)
			self.analyseData()
			return self.data

	def writeConfig(self):
		print(self.ConfigFullPath)
		w = open(self.ConfigFullPath,"w")
		w.write(json.dumps(self.data,sort_keys=True, indent=2))
		w.close()
		return None

	def getCurrentConfigFolder(self):
		path = sys.path[0]
		if os.path.isdir(path):
			return path
		elif os.path.isfile(path):
			return os.path.dirname(path)

	def getFileFullPath(self):
		self.ConfigFullPath = os.path.join(self.ConfigFolder, self.JsonFile)
		self.ConfigFullPath = self.ConfigFullPath.replace("/Dev", "") # Set Current Config Folder
		print("Set Json FileFull PATH : %s" % self.ConfigFullPath)

	def analyseData(self):
		pass