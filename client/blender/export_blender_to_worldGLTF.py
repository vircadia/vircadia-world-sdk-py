import bpy
import bmesh
import uuid
try:
    import bpy
    from io_scene_gltf2.io.exp import gltf2_io_export
    from io_scene_gltf2.blender.exp import gltf2_blender_export
except ImportError:
    # We're not in Blender, use fake-bpy-module
    import fake_bpy_module_latest as bpy
    from fake_bpy_module_latest.io_scene_gltf2.io.exp import gltf2_io_export
    from fake_bpy_module_latest.io_scene_gltf2.blender.exp import gltf2_blender_export
from ...shared.modules.vircadia_world_meta.python.world import *

class BlenderToWorldGLTF:
    def __init__(self):
        self.export_settings = gltf2_blender_export.create_default_export_settings()
        self.export_settings['gltf_format'] = 'JSON'
        self.export_settings['use_selection'] = True

    def convert_mesh(self, obj: bpy.types.Object) -> TableMesh:
        mesh = obj.data
        
        # Create a new bmesh to triangulate
        bm = bmesh.new()
        bm.from_mesh(mesh)
        bmesh.ops.triangulate(bm, faces=bm.faces[:])
        
        # Create primitives
        primitives = []
        for material_index in range(len(obj.material_slots)):
            primitive = self._create_primitive(bm, material_index)
            if primitive:
                primitives.append(primitive)
        
        bm.free()

        # Create TableMesh object
        table_mesh = TableMesh(
            vircadia_uuid=str(uuid.uuid4()),
            vircadia_world_uuid=str(uuid.uuid4()),  # This should be set to the actual world UUID
            name=obj.name,
            primitives=primitives,
            vircadia_version="1.0",  # Set appropriate version
            vircadia_createdat=datetime.now(),
            vircadia_updatedat=datetime.now(),
            vircadia_babylonjs_lod_mode=None,  # Set if applicable
            vircadia_babylonjs_lod_auto=None,  # Set if applicable
            vircadia_babylonjs_lod_distance=None,  # Set if applicable
            vircadia_babylonjs_lod_size=None,  # Set if applicable
            vircadia_babylonjs_lod_hide=None,  # Set if applicable
            vircadia_babylonjs_billboard_mode=None,  # Set if applicable
            vircadia_babylonjs_light_lightmap=None,  # Set if applicable
            vircadia_babylonjs_light_level=None,  # Set if applicable
            vircadia_babylonjs_light_color_space=None,  # Set if applicable
            vircadia_babylonjs_light_texcoord=None,  # Set if applicable
            vircadia_babylonjs_light_use_as_shadowmap=None,  # Set if applicable
            vircadia_babylonjs_light_mode=None,  # Set if applicable
            vircadia_babylonjs_script_agent_scripts=None,  # Set if applicable
            vircadia_babylonjs_script_persistent_scripts=None,  # Set if applicable
        )

        return table_mesh

    def _create_primitive(self, bm: bmesh.types.BMesh, material_index: int) -> dict:
        # Filter faces by material index
        faces = [f for f in bm.faces if f.material_index == material_index]
        if not faces:
            return None

        # Collect vertex data
        positions = []
        normals = []
        uvs = []
        indices = []

        uv_layer = bm.loops.layers.uv.active

        for face in faces:
            for loop in face.loops:
                positions.extend(loop.vert.co)
                normals.extend(loop.vert.normal)
                if uv_layer:
                    uvs.extend(loop[uv_layer].uv)
                indices.append(len(indices))

        # Create primitive dictionary
        primitive = {
            "attributes": {
                "POSITION": positions,
                "NORMAL": normals,
            },
            "indices": indices,
            "mode": 4,  # TRIANGLES
            "material": material_index
        }

        if uvs:
            primitive["attributes"]["TEXCOORD_0"] = uvs

        return primitive