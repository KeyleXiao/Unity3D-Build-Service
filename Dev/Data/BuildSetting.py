from Data.ConfigBase import ConfigBase


class BuildSetting(ConfigBase):
	AndroidProjectFolder = ""
	XCodeProjectFolder = ""
	BuildTasks = {}
	data = {
		"BuildTasks": {
			"/Users/keyle/Unity3D-Build-Service/Target_Build_UnityProject/ProjectA": [
				"CommandBuild.EntryBuildTencentSDK_Android",
				"CommandBuild.EntryBuildTencentSDK_iOS"
			]
		},
		"AndroidProjectFolder": "/Users/keyle/Unity3D-Build-Service/Target_Build_UnityProject/ProjectA/Android_Template/ProjectA",
		"XCodeProjectFolder": "/Users/keyle/Unity3D-Build-Service/Target_Build_UnityProject/ProjectA/XCode_Template/ProjectA"
	}

	def setJsonFileName(self):
		self.JsonFile = "BuildSetting.json"

	def analyseData(self):
		self.AndroidProjectFolder = self.data["AndroidProjectFolder"]
		self.XCodeProjectFolder = self.data["XCodeProjectFolder"]
		self.BuildTasks = self.data["BuildTasks"]
