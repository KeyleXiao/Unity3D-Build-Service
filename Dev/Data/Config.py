from Data.BuildSetting import BuildSetting
from Data.EnvironmentSetting import EnvironmnetSetting

class Config:
	bs = BuildSetting
	en = EnvironmnetSetting

	def __init__(self):
		self.bs = BuildSetting()
		self.en = EnvironmnetSetting()
		self.bs.loadConfig()
		self.en.loadConfig()

	def getBuildSetting(self):
		return self.bs

	def getEnvironmnetSetting(self):
		return self.en
