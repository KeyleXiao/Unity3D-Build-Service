import sys, os
import json


class ConfigBase:
	ConfigFolder = ""
	ConfigFullPath = ""
	JsonFile = ""
	data = {}

	def __init__(self):
		self.setJsonFileName()
		self.ConfigFolder = self.getCurrentConfigFolder().replace("/Dev/Data", "")  # Set Current Config Folder
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
			return self.data

	def writeConfig(self):
		print(self.ConfigFullPath)
		w = open(self.ConfigFullPath,"w")
		w.write(json.dumps(self.data))
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
		print("Set Json FileFull PATH : %s" % self.JsonFile)

	def analyseData(self):
		pass