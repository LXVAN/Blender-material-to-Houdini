
from operator import index
import hou
import json
import string
import difflib


jsonPath = "f:/Python_project/Generique_Material/GuiLearn.py/BlenderMaterial.json"



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

    NameAndIndex = {'baseColor': 1, 'BASECOLOR': 1, 'BaseColor': 1, 'base_color': 1, 'roughness': 7, 'rough': 7, 'Rough': 7, 'ROUGH': 7, 'metallic': 11, 'metalness': 11, 'METALLICE': 11, 'METALNESS': 11, 'reflect': 11, 'REFLECT': 11, 'coat': 13, 'COAT': 13, 'transparency': 15, 'TRANSPARENCY': 15, 'sss': 20, 'SSS': 20, 'emission': 27, 'EMISSION': 27, 'bump': 219, 'BUMP': 219, 'NORMAL': 219, 'normal': 219, 'DISPLACEMENT': 221, 'displacement': 221}
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
    