class Card:
    """
    کلاس والد برای تمام کارت‌های بازی
    """
    def __init__(self, name: str, image_path: str):
        self.name = name
        self.image_path = image_path

    def get_info(self):
        return f"Card: {self.name}"


class Minion(Card):
    """
    کلاس مینیون با قابلیت شناسایی (ID) و مدیریت وضعیت مرگ/زندگی
    """
    def __init__(self, id: str, name: str, image_path: str, attack: int, health: int, tier: int, minion_type: str):
        # فراخوانی کلاس پدر
        super().__init__(name, image_path)
        
        # شناسه منحصر به فرد برای سیستم ایونت
        self.id = id           
        
        # ویژگی‌های گیم‌پلی
        self.attack = attack
        self.health = health
        self.max_health = health  
        self.tier = tier
        self.minion_type = minion_type 
        self.keywords = []  
        
        # وضعیت حیاتی (State Machine)
        self.is_alive = True 

    def take_damage(self, amount: int):
        """اعمال دمیج فقط در صورتی که مینیون زنده باشد"""
        
        # 1. گارد: اگر مرده است، دمیج نزن
        if not self.is_alive:
            return 

        # 2. اعمال دمیج
        self.health -= amount
        
        # 3. بررسی مرگ و کلمپ کردن (Logic & State Update)
        if self.health <= 0:
            self.health = 0          # جان منفی نداریم
            self.is_alive = False    # تغییر وضعیت به مرده
            print(f"XX {self.name} (ID: {self.id}) has died! XX")
        else:
            print(f"-> {self.name} took {amount} damage! Health is now {self.health}.")

    def __str__(self):
        status = "Alive" if self.is_alive else "Dead"
        return f"[{self.name} | {self.attack}/{self.health} | {status}]"