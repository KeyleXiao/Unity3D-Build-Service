import os

# import Data.ConfigBase as config
from Data.ConfigBase import ConfigBase


# projectPath = input("Please input project folder path :")
#
# print("path : %s" % projectPath )
#
# projectPath = "/Applications/Unity/Unity.app/Contents/MacOS/Unity -batchmode -projectPath %s  -executeMethod CommandBuild.BuildAndroid"

# os.system(projectPath % projectPath)
#/Users/keyle/Unity3D-Build-Service/Target_Build_UnityProject/ProjectA/


# if __name__ == '__main__':
# 	C = ConfigBase()
# 	print(C.ConfigFolder)


os.system("defaults read /Applications/Unity/Unity.app/Contents/Info DVTPlugInCompatibilityUUID")
