from Data.ConfigBase import ConfigBase

class BuildSetting(ConfigBase):

	data = {"C:/folder/":["EneryBuild360SDK", "EneryBuildTencentSDK"], "D:/folder":["EneryBuild360SDK", "EneryBuildTencentSDK"]}

	def setJsonFileName(self):
		self.JsonFile = "BuildSetting.json"
