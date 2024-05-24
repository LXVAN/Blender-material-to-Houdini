my env:
blender 4.1
houdini 20.0.547
python intepreter : 3.12.3




不要用other文件夹中的代码
用vscode打开 GuiLearn
依次填写 blender软件安装路径,.blend 文件路径,blenderMatOnly.py的路径,后面的按钮可以让你检查路径是否有效

点击   使用blender执行py文件   后, 会生成一个json文件,用于houdini python读取

点击   生成代码   ,  在houdini 中的python source editor 粘贴代码,然后运行,blender 的材质就会转换到mantra 的vex build 材质   







files in "others" are origin version,which are not recommended to use


open GuiLearn with VS code:


type in your blender software path//path should not include space
type in your .blend file path
type in blenderMatOnly.py path 

click "使用blender执行py文件",it will create a json file for houdini to read

click "生成代码"  ,it will copy a python code running in houdini python source editor.

finally ,enjoy your blender material to mantra vex material!
