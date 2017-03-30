using UnityEditor;

public class CommandBuild
{
	public static void BuildAndroid()
	{
		string[] levels = { "Assets/1.unity" };
		BuildPipeline.BuildPlayer(levels, "Sample.apk", BuildTarget.Android, BuildOptions.None);
	}
}