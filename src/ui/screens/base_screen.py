from abc import ABC, abstractmethod

class Screen(ABC):
    """
    کلاس والد تمام صفحات بازی.
    تضمین می‌کند که هر صفحه متدهای اصلی را دارد.
    """
    def __init__(self, name, event_bus):
        self.name = name
        self.event_bus = event_bus

    @abstractmethod
    def handle_event(self, event):
        """پردازش ورودی‌های خام (ماوس/کیبورد)"""
        pass

    @abstractmethod
    def update(self, dt):
        """آپدیت انیمیشن‌ها و وضعیت داخلی صفحه"""
        pass

    @abstractmethod
    def render(self, surface):
        """رسم گرافیک روی صفحه"""
        pass