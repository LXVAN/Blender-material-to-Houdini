import tkinter as tk
import subprocess  
import os
from tkinter import INSERT, messagebox
from datetime import datetime
import pyperclip

##############            创建主窗口         ######################
mainWindow = tk.Tk()#创建主窗口
mainWindow.resizable(1,1)
mainWindow.title("GeneriqueMaterial")#命名主窗口
mainWindow.geometry("1000x800")#宽乘高,中间只能用英文字母x,不能用星号"*"
mainWindow.iconbitmap("C:/Users/Administrator/Desktop/ICON/karmaBlue.ico")
#只能使用ico后缀的文件,png也可以直接更改ico但是不建议这么做
#mainWindow['background'] = 'grey'
#设置主窗口的背景颜色,颜色值可以是英文单词，
#或者颜色值的16进制数,除此之外还可以使用Tk内置的颜色常量
#################################################




'''
#test = tk.Label(mainWindow,text = "GeneriqueMaterial",bg='green',fg='black',font=('Times',20,'bold'))
#添加一个文本,设置字体的前景和后景色,字体类型与大小
#test.pack()#把文本放在窗口内
'''
###################          blender 软件路径          ########################
tk.Label(mainWindow,text="Blender软件路径:").grid(row=0)#row是行,column是列
#创建两个标签,放在第一行与第二行
blenderSoftwarePath = tk.Entry(mainWindow)#创建输入框控件,这个是软件路径的
blenderSoftwarePath.grid(row=0,column=1,ipadx=100)
blenderSoftwarePath.insert(0,"F:\\blender\\blender_otheredition\\Blender4.1\\blender.exe")
def BlenderSoftwareOpen():
    path = blenderSoftwarePath.get()#读取框中的文本
    #使用cmd启动blender
    if os.path.exists(path):
        try:
            DebugButton("Blender软件已开启")           
            subprocess.run([path])
        except:
            messagebox.showinfo('Error',f'No blender.exe exists in this path.当前输入路径不存在可执行的blender.exe文件')
    else:
         messagebox.showinfo('Error',f'address({path}) does not exist.输入的blender软件路径不存在请重新输入')
tk.Button(mainWindow,text="启动Blender",width = 10,
    command=lambda:BlenderSoftwareOpen()).grid(row=0,column=2,sticky='w')
#messagebox.showinfo("bottom clicked")
#sticky 是方位,东西南北的英文首字母
#注意 buttom()函数中,使用command运行含有参数的函数时,程序会自动跳过运行函数所需的条件,即自动运行
#使用匿名函数lambda来代理运行就可以解决这个问题
#################################################





##################           .blend 文件路径             #####################
tk.Label(mainWindow,text=".blend文件路径:").grid(row=1)
dotBlendPath = tk.Entry(mainWindow)#这个是.blend文件路径的输入控件
dotBlendPath.grid(row=1,column=1,ipadx=100)
dotBlendPath.insert(0,"F:\\standard_library\\RoundPacific\\running.blend")
def DotBlenderOpen():
    #使用cmd启动blender
    blenderPath = blenderSoftwarePath.get()
    dotPath = dotBlendPath.get()
    if os.path.exists(blenderPath) & os.path.exists(dotPath):
        try:
            DebugButton(f".blend文件({dotPath})已使用({blenderPath})开启")
            subprocess.run([blenderPath,dotPath])#使用cmd 打开.blend文件
        except:
            messagebox.showinfo('Error','blender软件路径或.blend文件路径有误')
    else:
        messagebox.showinfo('Error','blender软件路径或.blend文件路径有误')
tk.Button(mainWindow,text="打开.blend文件",width = 10,
    command=lambda:DotBlenderOpen()).grid(row=1,column=2,ipadx=10,sticky='w')
#################################################



############             blender Python 运行文件路径            ######################
tk.Label(mainWindow,text="BlenderPython运行文件路径:").grid(row=2)
blenderPythonMaterialJson = tk.Entry(mainWindow)#在blenderpython中运行的.py文件
blenderPythonMaterialJson.grid(row=2,column=1,ipadx=100)
blenderPythonMaterialJson.insert(0,"F:\\Python_project\\Generique_Material\\blenderMatOnly.py")
def BlenderPythonOpen():
    blenderPath = blenderSoftwarePath.get()
    dotPath = dotBlendPath.get()
    pyPath = blenderPythonMaterialJson.get()
    jsonFile = __file__ + "\\BlenderMaterial.json"
    if(os.path.exists(pyPath)):
        try:
            DebugButton(f"已使用py文件({pyPath})在blender中运行,并输出json文件至{jsonFile}")
            command = f"\"{blenderPath}\" -b \"{dotPath}\" -P \"{pyPath}\""
            #使用 subprocess 运行命令  
            subprocess.Popen(command, shell=True)
            messagebox.showinfo('',f'已成功使用({blenderPath})打开{dotPath}并且使用{pyPath}输出json文件至{jsonFile}')
        except:
            messagebox.showinfo('Error',f'({pyPath})当前路径不存在可执行的py文件')
    else:
        messagebox.showinfo('Error',f'py文件路径有误({pyPath})')
tk.Button(mainWindow,text="使用blender执行py文件",width=15,command=lambda:BlenderPythonOpen()).grid(row=2,column=2,ipadx=10,sticky='w')

#####################################################




###############              houdini软件启动            ##########################
tk.Label(mainWindow,text="Houdini软件路径:").grid(row=3)#row是行,column是列
#创建两个标签,放在第一行与第二行
houdiniSoftwarePath = tk.Entry(mainWindow)#创建输入框控件,这个是软件路径的
houdiniSoftwarePath.grid(row=3,column=1,ipadx=100)
houdiniSoftwarePath.insert(0,"E:\\Program Files\\Side Effects Software\\Houdini 20.0.547\\bin\\houdini.exe")

def HoudiniSoftwareOpen():
    path = houdiniSoftwarePath.get()#读取框中的文本
    #使用cmd启动blender
    if os.path.exists(path):
        try:
            DebugButton("Houdini软件已开启")           
            subprocess.run([path])
        except:
            messagebox.showinfo('Error','当前输入路径不存在可执行的houdini.exe文件')
    else:
         messagebox.showinfo('Error',f'address({path}) does not exist.输入的houdini软件路径不存在请重新输入')
tk.Button(mainWindow,text="启动Houdini",width = 10,
    command=lambda:HoudiniSoftwareOpen()).grid(row=3,column=2,sticky='w')

###############################################

#################        生成在houdini python source editor 中运行的代码至 debug窗口  ###############
tk.Button(mainWindow,text="生成代码",width=10,
          command=lambda:CopyCodes()).grid(row=3,column=3,sticky="w")
NameAndIndex = {
    "baseColor" : 1,
    "BASECOLOR" : 1,
    "BaseColor" : 1,
    "base_color" :1,
    
    "roughness" : 7,
    "rough" : 7,
    "Rough" :7,
    "ROUGH" : 7,

    "metallic" : 11,
    "metalness" : 11,
    "METALLICE" : 11,
    "METALNESS" : 11,

    "reflect" : 11,
    "REFLECT" : 11,

    "coat" : 13,
    "COAT" : 13,

    "transparency" : 15,
    "TRANSPARENCY" : 15,

    "sss" : 20,
    "SSS" : 20,

    "emission" : 27 ,
    "EMISSION" :27,

    "bump" : 219,
    "BUMP" : 219,

    "NORMAL" : 219,
    "normal" : 219,

    "DISPLACEMENT" : 221,
    "displacement" : 221
}


absoluteJsonFilePath = os.path.abspath(os.getcwd()+ "\\BlenderMaterial.json").replace("\\",'/')

def CopyCodes():
    text_to_copy =   f'''
from operator import index
import hou
import json
import string
import difflib


jsonPath = "{absoluteJsonFilePath}"



def replace_spaces_and_punctuation_with_underscore(s):
    # 创建一个转换表，将空格和标点映射为下划线
    trans = str.maketrans(string.whitespace + string.punctuation, '_' * len(string.whitespace + string.punctuation))
    # 使用转换表替换字符串中的空格和标点
    return s.translate(trans)

def fuzzy_match(s1, s2):
    
    matcher = difflib.SequenceMatcher(None, s1, s2)
    ratio = matcher.ratio()
    return ratio



def MaterialFromJson():

    NameAndIndex = {
    NameAndIndex
}
#后面的数字不是数出来的,要对所有输入名称在python中进行排序输出,才能获得序号来进行连接




    
    objPath = hou.node("/obj")#obj层级
    matNode = objPath.createNode("matnet","blenderMaterial")#在obj层级下创建的节点自动载入python成为一个对象,可以在这个对象下面直接创建节点
    
    #ps = matNode.createNode('principledshader::2.0','myshader')

    with open(jsonPath,"r") as jsonFile:
        materialData = json.load(jsonFile)
        #print(materialData)

    for materialName, texturePathDictionary in materialData.items():    
        materialName = replace_spaces_and_punctuation_with_underscore(materialName)
        vexBuild = matNode.createNode("materialbuilder",materialName)
        principledShader = vexBuild.createNode("principledshader::2.0","principledshader")
        #principledShader.setInputGroupExpanded("Surface","expanded")#把刚刚创建的principled shader 中的surface 输入组全部展开
        #principledShader.setInputGroupExpanded("Other","collapse")
        principledShader.parm("baseBumpAndNormal_enable").set(True)
        computeLighting = vexBuild.createNode("computelighting::2.0","computelighting")
        computeLighting.setInput(0,principledShader,2)
        

        # surfaceOutput.setInput(0,computeLighting,0)
        # surfaceOutput.setInput(1,computeLighting,1)
        # surfaceOutput.setInput(4,computeLighting,2)

        #print(materialName)
        for textureName,texturePath in texturePathDictionary.items():
            textureNameReplaced = replace_spaces_and_punctuation_with_underscore(textureName)
            texture = vexBuild.createNode("texture::2.0",textureNameReplaced)
            texture.parm("map").set(texturePath)

            for key in NameAndIndex:
                matchRatio = fuzzy_match(key,textureNameReplaced)
                #print (key,textureName,matchRatio)
                if matchRatio>0.55:
                    index = int(NameAndIndex[key])#principled shader 的输入接口序号                    
                    principledShader.setInput(index,texture,0)
                    
    vexBuilds = matNode.children()
    for build in vexBuilds:
        #连接 computelight 和 output
        clighting = build.node("computelighting")
        sOutput = build.node("surface_output")
        sOutput.setInput(0,clighting,0)
        sOutput.setInput(1,clighting,1)
        sOutput.setInput(4,clighting,2)
    '''
    pyperclip.copy(text_to_copy)    
    DebugButton("代码已复制进粘贴板,请在houdini中的python source editor中运行")























################             debug 输出窗口           #####################
debugText = tk.Text(mainWindow,width=120,height=30,state='normal')
debugText.grid(row=10,column=0,columnspan=10,sticky='ws')
def DebugButton(string):
    #在string处输入你想要输出的文字即可,这个text会自动输出时间加刚才的指令
    time = datetime.now().strftime("%H:%M:%S")
    debugText.config(state='normal')
    debugText.insert(INSERT,f"{time}"+" "+string+"\n")
    debugText.config(state='disabled')
#################################################






# button = tk.Button(mainWindow,text=("close"),command=mainWindow.quit)# 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
# button.pack(side="bottom")# 将按钮放置在主窗口内,grid函数不能和pack函数混合使用!
















mainWindow.mainloop()#主循环,让窗口一直显示