import os
import bpy
from world_manager import WorldManager
from blender_supabase_sync import BlenderSupabaseSync
from supabase import create_client, Client
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_supabase() -> Client:
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_ANON_KEY")
    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_ANON_KEY must be set in environment variables")
    return create_client(url, key)

def main():
    try:
        supabase = setup_supabase()
        world_manager = WorldManager(supabase)
        world_manager.select_world("example_world_id")

        sync_manager = BlenderSupabaseSync(world_manager)
        sync_manager.setup_realtime_subscriptions()

        # Example: Sync all Blender objects
        for obj in bpy.data.objects:
            result = sync_manager.sync_object(obj)
            logger.info(f"Sync result for {obj.name}: {result}")

        # Example: Sync from Supabase to Blender
        sync_manager.sync_from_supabase()

    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)

if __name__ == "__main__":
    main()