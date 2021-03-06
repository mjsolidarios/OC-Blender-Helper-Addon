import bpy 
import os

osl_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'osl')

def load_objects(name, category):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), category, name + '.blend')
    with bpy.data.libraries.load(path) as (data_from, data_to):
        data_to.objects = data_from.objects
        bpy.ops.wm.append(directory=os.path.join(path, 'Object'), files=[{'name': name} for name in data_to.objects])
        return bpy.context.selected_objects

def save_objects(name, objects, category):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), category, name + '.blend')
    data_blocks = {
        *objects
    }
    bpy.data.libraries.write(path, data_blocks, compress=True)