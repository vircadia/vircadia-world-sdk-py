import bpy
import json
import os
import tempfile
import uuid
from datetime import datetime
from ...shared.modules.vircadia_world_meta.python.world import TableMesh, TableMaterial, TableTexture, TableImage

class BlenderToWorldGLTF:
    def __init__(self):
        self.world_uuid = str(uuid.uuid4())  # This should be set to the actual world UUID

    def convert_mesh(self, obj: bpy.types.Object) -> TableMesh:
        # Ensure the object is selected
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        # Create a temporary file to export to
        with tempfile.NamedTemporaryFile(suffix=".gltf", delete=False) as temp_file:
            temp_path = temp_file.name

        # Export to glTF
        bpy.ops.export_scene.gltf(
            filepath=temp_path,
            use_selection=True,
            export_format='GLTF_SEPARATE',
            export_texcoords=True,
            export_normals=True,
            export_materials='EXPORT'
        )

        # Read the exported JSON
        with open(temp_path, 'r') as f:
            gltf_data = json.load(f)

        # Clean up temporary files
        os.unlink(temp_path)
        os.unlink(temp_path.replace('.gltf', '.bin'))

        # Extract Vircadia-specific properties from the object
        vircadia_props = {
            prop: getattr(obj, prop)
            for prop in dir(obj)
            if prop.startswith('vircadia_')
        }

        # Create TableMesh object
        table_mesh = TableMesh(
            vircadia_uuid=str(uuid.uuid4()),
            vircadia_world_uuid=self.world_uuid,
            vircadia_version=vircadia_props.get('vircadia_version', "1.0"),
            vircadia_createdat=datetime.now(),
            vircadia_updatedat=datetime.now(),
            gltf_name=obj.name,
            gltf_primitives=gltf_data['meshes'][0]['primitives'],
            gltf_weights=gltf_data['meshes'][0].get('weights'),
            vircadia_babylonjs_lod_mode=vircadia_props.get('vircadia_babylonjs_lod_mode'),
            vircadia_babylonjs_lod_auto=vircadia_props.get('vircadia_babylonjs_lod_auto'),
            vircadia_babylonjs_lod_distance=vircadia_props.get('vircadia_babylonjs_lod_distance'),
            vircadia_babylonjs_lod_size=vircadia_props.get('vircadia_babylonjs_lod_size'),
            vircadia_babylonjs_lod_hide=vircadia_props.get('vircadia_babylonjs_lod_hide'),
            vircadia_babylonjs_billboard_mode=vircadia_props.get('vircadia_babylonjs_billboard_mode'),
            vircadia_babylonjs_light_lightmap=vircadia_props.get('vircadia_babylonjs_light_lightmap'),
            vircadia_babylonjs_light_level=vircadia_props.get('vircadia_babylonjs_light_level'),
            vircadia_babylonjs_light_color_space=vircadia_props.get('vircadia_babylonjs_light_color_space'),
            vircadia_babylonjs_light_texcoord=vircadia_props.get('vircadia_babylonjs_light_texcoord'),
            vircadia_babylonjs_light_use_as_shadowmap=vircadia_props.get('vircadia_babylonjs_light_use_as_shadowmap'),
            vircadia_babylonjs_light_mode=vircadia_props.get('vircadia_babylonjs_light_mode'),
            vircadia_babylonjs_script_agent_scripts=vircadia_props.get('vircadia_babylonjs_script_agent_scripts'),
            vircadia_babylonjs_script_persistent_scripts=vircadia_props.get('vircadia_babylonjs_script_persistent_scripts'),
        )

        return table_mesh

    def convert_material(self, material: bpy.types.Material) -> TableMaterial:
        # This method would convert a Blender material to a TableMaterial
        # Implementation depends on how materials are set up in your Blender scene
        pass

    def convert_texture(self, texture: bpy.types.Texture) -> TableTexture:
        # This method would convert a Blender texture to a TableTexture
        # Implementation depends on how textures are set up in your Blender scene
        pass

    def convert_image(self, image: bpy.types.Image) -> TableImage:
        # This method would convert a Blender image to a TableImage
        # Implementation depends on how images are set up in your Blender scene
        pass