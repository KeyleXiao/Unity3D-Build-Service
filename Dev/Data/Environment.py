from Data.ConfigBase import  ConfigBase
import json

class Environmnet(ConfigBase):

	ApplicationFolder = "" ; ProjectFolder = ""

	data = { "ApplicationFolder" : "","ProjectFolder":"" }

	def setJsonFileName(self):
		self.JsonFile = "EnvironmnetConfig.json"

	
	def analyseData(self):
		self.ApplicationFolder = self.data["ApplicationFolder"]
		self.ProjectFolder = self.data["ProjectFolder"]
		print(self.ApplicationFolder)


# test code
# e = Environmnet()
# content = e.loadConfig()
# e.analyseData()
# print(e.data)
# print(e.ApplicationFolder)