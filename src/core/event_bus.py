import queue

class EventBus:
    """
    سیستم مدیریت رویدادها برای جدا کردن سرور از UI.
    """
    def __init__(self):
        # طبق خواسته TA: دو صف جداگانه
        self.server_queue = queue.Queue()
        self.ui_queue = queue.Queue()

    def send_to_server(self, event):
        """ارسال درخواست به لاجیک یا سرور"""
        self.server_queue.put(event)

    def send_to_ui(self, event):
        """ارسال نتیجه به رابط کاربری"""
        self.ui_queue.put(event)

    def process_server_events(self, handler_func, max_events=5):
        """
        پردازش صف سرور با محدودیت تعداد در هر فریم.
        handler_func: تابعی که ایونت را پردازش می‌کند.
        """
        count = 0
        while not self.server_queue.empty() and count < max_events:
            event = self.server_queue.get()
            handler_func(event)
            count += 1

    def process_ui_events(self, handler_func):
        """
        پردازش صف UI (معمولاً همه را پردازش می‌کنیم تا لگ نزند)
        """
        while not self.ui_queue.empty():
            event = self.ui_queue.get()
            handler_func(event)