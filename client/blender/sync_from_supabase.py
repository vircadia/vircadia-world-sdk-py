from world_manager import WorldManager
from import_gltf import GLTFToBlender

def sync_from_supabase(world_manager: WorldManager):
    gltf_to_blender = GLTFToBlender(world_manager)
    world = world_manager.get_current_world()
    if world:
        gltf_to_blender.convert_world(world)
    else:
        raise ValueError("No world selected or world not found")

# ... (other sync functions for different entity types)