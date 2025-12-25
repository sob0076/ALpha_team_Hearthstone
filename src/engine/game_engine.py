import src.core.event_names as Events

class GameEngine:
    """
    مغز متفکر بازی.
    مسئولیت‌ها:
    1. نگه داشتن وضعیت تمام موجودیت‌ها (Minions, Players)
    2. پردازش Commandها طبق قوانین بازی
    """
    def __init__(self):
        # این دیکشنری نقش "Database" مینیون‌های زنده را دارد
        # Key: Minion ID, Value: Minion Object
        self.minions = {}

    def register_minion(self, minion):
        """مینیون را به سیستم معرفی می‌کند تا قابل تارگت شدن باشد"""
        self.minions[minion.id] = minion
        print(f"[Engine] Minion registered: {minion.id}")

    def process_event(self, event):
        """
        این متد جایگزین handle_game_logic در main می‌شود.
        استاندارد A2 را رعایت می‌کند.
        """
        event_type = event.get("type")
        source = event.get("source", "unknown")
        target_id = event.get("target")
        payload = event.get("payload", {})

        # --- مسیریابی (Routing) بر اساس نوع ایونت ---
        
        if event_type == Events.CMD_DEBUG_DAMAGE:
            self._handle_debug_damage(target_id, payload, source)
            
        # اینجا بعداً elif CMD_BUY_MINION اضافه می‌شود...

    def _handle_debug_damage(self, target_id, payload, source):
        """منطق اختصاصی دمیج خوردن"""
        amount = payload.get("amount", 0)
        
        # جستجو در دیتابیس مینیون‌ها
        target_minion = self.minions.get(target_id)

        if target_minion:
            print(f"[Engine] Processing Logic: {source} -> Damage {amount} -> {target_id}")
            target_minion.take_damage(amount)
        else:
            print(f"[Engine] Error: Target {target_id} not found!")