using UnityEditor;
using UnityEngine;
using System;
using System.IO;
public class CommandBuild : Editor
{
	public static void EntryBuildTencentSDK_Android()
	{
		string[] levels = { "Assets/1.unity" };
		EditorUserBuildSettings.androidBuildSystem = AndroidBuildSystem.Gradle;
		BuildPipeline.BuildPlayer(levels, "Android_Template", BuildTarget.Android, BuildOptions.AcceptExternalModificationsToPlayer);
	}

	public static void EntryBuildTencentSDK_iOS()
	{
		string[] levels = { "Assets/1.unity" };

		BuildPipeline.BuildPlayer(levels, "XCode_Template", BuildTarget.iOS, BuildOptions.AcceptExternalModificationsToPlayer);
	}
}