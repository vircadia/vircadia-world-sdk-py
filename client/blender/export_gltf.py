import bpy
from io_scene_gltf2.io.exp import gltf2_io_export
from io_scene_gltf2.blender.exp import gltf2_blender_export
from vircadia_world_meta.python.meta import *

class BlenderToGLTF:
    def __init__(self):
        self.export_settings = gltf2_blender_export.create_default_export_settings()
        self.export_settings['gltf_format'] = 'JSON'
        self.export_settings['use_selection'] = True

    def convert_world(self) -> World_WorldGLTF:
        # Implementation details...
        pass

    def convert_scene(self, scene: bpy.types.Scene) -> World_Scene:
        # Implementation details...
        pass

    def convert_node(self, obj: bpy.types.Object) -> World_Node:
        # Implementation details...
        pass

    def convert_mesh(self, obj: bpy.types.Object) -> World_Mesh:
        # Implementation details...
        pass

    def convert_material(self, material: bpy.types.Material) -> World_Material:
        # Implementation details...
        pass

    # ... (other conversion methods)