from Entry.CommandExecute import CommandExecute


if __name__ == '__main__':

	c = CommandExecute()

	while c.task.getTask() is not None:

		print(         "CURRENT TASK   : " + c.task.getTask()[2])
		select = input("AutoMode       : 1\n"
		               "Create Project : 2\n"
		               "Build Project  : 3\n"
		               "Finish Task    : 4\n")

		if select == "1":
			while c.invoke():
				c.buildProject()
				c.task.finishTask()

		if select == "2":
			c.invoke()

		if select == "3":
			pass

		if select == "4":
			c.task.finishTask()

	print("COMPLETE !")