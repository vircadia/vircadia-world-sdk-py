from typing import Any, Dict
from world_manager import WorldManager
from export_gltf import BlenderToGLTF

def sync_object_to_supabase(world_manager: WorldManager, blender_object: Any) -> Dict:
    blender_to_gltf = BlenderToGLTF()
    gltf_data = blender_to_gltf.convert_node(blender_object)
    return world_manager.supabase_ops.create_node(gltf_data)

def sync_scene_to_supabase(world_manager: WorldManager, scene: Any) -> Dict:
    blender_to_gltf = BlenderToGLTF()
    gltf_data = blender_to_gltf.convert_scene(scene)
    return world_manager.supabase_ops.create_scene(gltf_data)

# ... (other sync functions for different entity types)