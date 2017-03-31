from Data.Config import Config as C


class BuildServiceManager:
	c = C

	def __init__(self):
		self.c = C()
		self.refreshTask()

	totalTask = {}
	currentTask = ""

	def refreshTask(self):
		for key in self.c.bs.BuildTasks:
			for item in self.c.bs.BuildTasks[key]:
				self.totalTask[item] = key
		return

	def getTask(self):
		if self.currentTask == "":
			for key in self.totalTask:
				self.currentTask = key
				return (self.c.en.ApplicationFolder, self.totalTask[key], key)
			return None
		else:
			return (self.c.en.ApplicationFolder, self.totalTask[self.currentTask], self.currentTask)

	def finishTask(self):
		if self.currentTask in self.totalTask:
			del self.totalTask[self.currentTask]
			print("Task Complete: " + self.currentTask)
		self.currentTask = ""

