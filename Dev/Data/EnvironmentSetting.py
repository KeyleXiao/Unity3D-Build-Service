from Data.ConfigBase import  ConfigBase

class EnvironmnetSetting(ConfigBase):

	ApplicationFolder = ""

	data = { "ApplicationFolder" : "" }

	def setJsonFileName(self):
		self.JsonFile = "EnvironmnetConfig.json"

	def analyseData(self):
		self.ApplicationFolder = self.data["ApplicationFolder"]
