from typing import Any, Dict
from world_manager import WorldManager
from sync_to_supabase import sync_object_to_supabase
from sync_from_supabase import sync_from_supabase
import logging

logger = logging.getLogger(__name__)

class BlenderSupabaseSync:
    def __init__(self, world_manager: WorldManager):
        self.world_manager = world_manager

    def sync_object(self, blender_object: Any) -> Dict:
        return sync_object_to_supabase(self.world_manager, blender_object)

    def sync_from_supabase(self):
        sync_from_supabase(self.world_manager)

    def handle_realtime_update(self, payload):
        logger.info(f'Realtime update received: {payload}')
        # TODO: Implement Blender update logic here

    def setup_realtime_subscriptions(self):
        self.world_manager.supabase_ops.setup_realtime_subscriptions(self.handle_realtime_update)