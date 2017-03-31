import os
from Services.BuildServicesManager import BuildServiceManager

class CommandExecute:
	task = BuildServiceManager

	def __init__(self):
		self.task = BuildServiceManager()

	executeUnityCommand =  "%s -batchmode -nographics -quit  -projectPath %s  -executeMethod %s"

	def invoke(self):

		task = self.task.getTask()

		if task == None:
			return False

		os.system(self.executeUnityCommand % task)
		print("CREATE PROJECT SUCCESS ..")
		return True


	def buildProject(self):
		pass