import bpy
import json
import os
#测试在blender中操控材质节点的各个功能

#材质由其他渲染器导入时,需要创建一些图像纹理,可能需要再py中创建一些class
#不打算从其他软件导入材质进来
def CreateTextureNode(nodes,label):
    #创建一个textureNode,
    #nodes填入material.node_tree.nodes
    #label填入这个textureNode在blender中的命名
    textureNode = nodes.new('ShaderNodeTexImage')
    textureNode.label = label
    return textureNode
def ImportImage(imagePath):
    #输入要导入的图片路径,可以自动判断图片是否已经被导入,没有则导入,反之控制台会提示已导入过
    #输入的图片路径不要出现'\',必须全部更换为'/'
    imageToLoad = None
    if not bpy.data.images.get(imagePath.split("/")[-1]):  
        #加载图片至blender之前判断一下这个图片是否被导入
        imageToLoad = bpy.data.images.load(imagePath)  
    else:  
        print(f'Texture({imagePath}) has already been imported')
        imageToLoad = bpy.data.images[imagePath.split("/")[-1]]
    return imageToLoad
def NodeLink(links,outputNode,outputName,inputNode,inputName):
    #从outputNode节点 的outputName 一栏连接到 inputNode节点的inputName一栏
    link = links.new(outputNode.outputs[outputName],inputNode.inputs[inputName])
    return link


materialInformation1 = {}
materialInformation2 = {}
objects = bpy.context.scene.objects#获取场景中的所有物体

# 遍历场景中的所有物体 
for obj in bpy.context.scene.objects:  
    # 跳过相机和灯光（如果你不想打印它们）  
    #if obj.type not in {'CAMERA', 'LIGHT'}: 
    #print(obj.type) 可以查看场景中物体的种类
    if obj.type in {'MESH'}:

        #material = bpy.data.materials.new("myMaterials") 
        #material.use_nodes = True  # 确保使用节点编辑器
        #material = obj.data.materials[0]#找到物体的第一个材质
        
        for material in obj.data.materials:                    
            nodes = material.node_tree.nodes#获得这个材质中的所有节点,类似一个空间
            links = material.node_tree.links


            '''
            nodes.clear()#先清除,方便后面创建principled shader 来连接各个texture

            principledShaderNode = nodes.new('ShaderNodeBsdfPrincipled')#创建一个principled shader
            outputNode = nodes.new('ShaderNodeOutputMaterial')#创建output节点

            ######创建两个textureNode 节点############
            baseColorTextureNode = CreateTextureNode(nodes,'baseColor')
            baseColorTextureNode.image = ImportImage('C:/Users/Administrator/Desktop/ICON/karma_blue.png')
            metallicTextureNode = CreateTextureNode(nodes,'metallic')
            metallicTextureNode.image = ImportImage('C:/Users/Administrator/Desktop/ICON/leave.png')
            ########################################

            ########把创建的节点连接起来################
            outputLink = NodeLink(links,principledShaderNode,'BSDF',outputNode,'Surface')
            baseColorLink = NodeLink(links,baseColorTextureNode,'Color',principledShaderNode,'Base Color')
            metallicLink = NodeLink(links,metallicTextureNode,'Color',principledShaderNode,'Metallic')       
            ##########################################
            '''
            for node in nodes:
                type = node.type#节点的类型
                #print(type,'\n') 快速获得一个材质中所有节点的类型
                    
                if type == 'TEX_IMAGE':
                    #检查有无空的textureNode,如果没有路径就把这个节点删除
                    if node.image == None:
                        nodes.remove(node)
            
            pbrList = []
            for link in links:
                #print(link.from_socket.name,'\n')# 从...连接 的接口的名字
                #print(link.to_socket.name)#连接到 接口 的名字
                fromNodeName = link.from_node.name
                fromNode = link.from_node
                fromSocketName = link.from_socket.name
                toNodeName = link.to_node.name
                toNode = link.to_node
                toSocketName = link.to_socket.name
                if fromNode.type == 'TEX_IMAGE':
                    imagePath = fromNode.image.filepath                 
                    #print(f'{toSocketName}:{imagePath}') 
                    pbrList.append(f'{toSocketName}:{imagePath}')
                    #pbrList.append(obj.name +':'+material.name + ':' + f'{toSocketName}:{imagePath}'+'\n')                    
                    materialInformation0 ={idx + 1: name for idx, name in enumerate(pbrList)}
                    materialInformation1[material.name] = materialInformation0#输出所有材质的路径
                    #materialInformation2[obj.name] = materialInformation1#输出所有物品的材质,及其路径
                    
                        
   
        

        
jsonFile = os.path.dirname(os.path.abspath(__file__)) + "\\test_info.json"

jsonData = json.dumps(materialInformation1,ensure_ascii=False,indent=4,sort_keys=True)
with open(jsonFile,'w',encoding= 'utf-8') as f:
    f.write(jsonData)
#ensure_ascii=False,加上这一个才能让中文正常输出


            
           
# 删除所有载入的图像
#for img in list(bpy.data.images):  
#     bpy.data.images.remove(img)  


# 清除控制台中的内容            
# import os
#   os.system("cls")  
'''
现阶段的问题
1.判断principled shader 是否连接,然后输出base color ,metallic 等的值,输出到字典上,替换路径
2.对于一些特殊的link.to_socket.name,比如置换会再连接bump,displacement等,不仅不连接至principled shader
  而且还会直接连接到 material output上
3.把字典中,每个材质下面的各个参数(baseColor,metallic等)前的数字替换成 各个参数的名字(baseColor,metallice)
4.在窗口中输出导出的物体及材质名称,还有数量
'''

'''
在houdini中的问题
1.通过python启动houdini,使用houdini运行python
2.读取由blender python运行产生的json文件
3.将json 文件中的信息转换成mantra材质
4.将mantra材质转换为houdini 中的arnold , materialX 
5.在solaris 中,把转换好的materialX 赋予给各个primitive


'''

'''
未来与展望:
1.在这个窗口直接看到材质如何连接
2.一键生成文件

'''