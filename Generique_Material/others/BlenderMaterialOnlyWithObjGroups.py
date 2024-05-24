import json  
import bpy  
import os

#这一版有物体分组

materials_info = {}  

currentFile = __file__
currentFile = os.path.dirname(os.path.abspath(currentFile))

jsonFile = currentFile + "\\bl_mat_output.json"




 # 遍历场景中的所有材质  
for mat in bpy.data.materials:  
    # 创建一个字典来存储当前材质的信息  
    material_dict = {  
        "name": mat.name,  
        #"type": mat,  
        "diffuse_color": list(mat.diffuse_color[:]),  
        # 你可以根据需要添加更多材质属性，比如:  
        # "specular_intensity": mat.specular_intensity,  
        # "specular_hardness": mat.specular_hardness,  
        # ...等等  
    }  
    # 将当前材质的信息添加到 materials_info 字典中，以材质名称作为键  
    materials_info[mat.name] = material_dict  
  
# 将材质信息字典转换为 JSON 格式的字符串  
json_data = json.dumps(materials_info, indent=4, sort_keys=True) 


# 将 JSON 数据写入文件  
file_path = jsonFile  # 替换为你的输出文件路径  
with open(file_path, 'w', encoding='utf-8') as f:  
    f.write(json_data) 









    