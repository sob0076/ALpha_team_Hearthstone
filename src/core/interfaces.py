from abc import ABC, abstractmethod

class Component(ABC):
    """
    قرارداد اجباری برای تمام اجزای رابط کاربری.
    هر کلاسی که این را ارث ببرد، مجبور است این ۳ متد را داشته باشد.
    """
    
    @abstractmethod
    def handle_event(self, event):
        """واکنش به ورودی‌ها (کلیک، کیبورد)"""
        pass

    @abstractmethod
    def update(self, dt):
        """آپدیت منطق در گذر زمان (انیمیشن‌ها)"""
        pass

    @abstractmethod
    def render(self, surface):
        """رسم روی صفحه"""
        pass