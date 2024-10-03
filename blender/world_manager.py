from supabase import Client
from supabase_operations import SupabaseOperations
from vircadia_world_meta.python.meta import World_WorldGLTF

class WorldManager:
    def __init__(self, supabase: Client):
        self.supabase = supabase
        self.supabase_ops = SupabaseOperations(supabase)
        self.current_world_id = None

    def select_world(self, world_id: str):
        result = self.supabase.table('world_gltf').select("*").eq("vircadia_uuid", world_id).execute()
        if result.data:
            self.current_world_id = world_id
        else:
            raise ValueError(f"World with id {world_id} not found")

    def get_current_world(self) -> World_WorldGLTF:
        if not self.current_world_id:
            raise ValueError("No world selected. Call select_world() first.")
        result = self.supabase.table('world_gltf').select("*").eq("vircadia_uuid", self.current_world_id).execute()
        return World_WorldGLTF(**result.data[0]) if result.data else None