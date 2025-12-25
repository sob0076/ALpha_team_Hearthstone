import queue

class EventBus:
    """
    سیستم مدیریت رویداد مرکزی (Generic Event Bus).
    این کلاس هیچ وابستگی به نام ایونت‌ها یا لاجیک بازی ندارد.
    فقط وظیفه انتقال بسته‌ها (Dictionaries) را دارد.
    """
    def __init__(self):
        # صف درخواست‌ها به سمت سرور (Commands)
        self.server_queue = queue.Queue()
        # صف نتایج به سمت رابط کاربری (State Events)
        self.ui_queue = queue.Queue()

    def send_to_server(self, event_payload: dict):
        """ارسال یک Command از UI به Logic"""
        self.server_queue.put(event_payload)

    def send_to_ui(self, event_payload: dict):
        """ارسال یک Event از Logic به UI"""
        self.ui_queue.put(event_payload)

    def process_server_events(self, handler_func, max_events=10):
        """
        پردازش صف سرور.
        handler_func: تابعی که باید روی ایونت اجرا شود (Logic Handler).
        """
        count = 0
        while not self.server_queue.empty() and count < max_events:
            event = self.server_queue.get()
            handler_func(event) # هندلر هر چه باشد اجرا می‌شود، باس دخالتی نمی‌کند
            count += 1

    def process_ui_events(self, handler_func):
        """پردازش تمام صف UI برای سینک شدن گرافیک"""
        while not self.ui_queue.empty():
            event = self.ui_queue.get()
            handler_func(event)