from typing import List, Dict
from supabase import Client
from vircadia_world_meta.python.meta import *

class SupabaseOperations:
    def __init__(self, supabase: Client):
        self.supabase = supabase

    def create_node(self, node_data: World_Node) -> Dict:
        # Implementation details...
        pass

    def update_node(self, node_id: str, node_data: World_Node) -> Dict:
        # Implementation details...
        pass

    def delete_node(self, node_id: str) -> Dict:
        # Implementation details...
        pass

    def get_nodes(self) -> List[World_Node]:
        # Implementation details...
        pass

    # ... (CRUD operations for other entity types)

    def setup_realtime_subscriptions(self, callback):
        for table in World_Table:
            self.supabase.table(table.value).on('*', callback).subscribe()