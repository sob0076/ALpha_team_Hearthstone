# راهنمای مشارکت در کد (Contributing Guidelines)

## قوانین معماری (Architecture Rules)
ما از معماری **Event-Driven** سخت‌گیرانه استفاده می‌کنیم.

### ⛔️ کارهای ممنوع (Don'ts):
1. **Magic Strings ممنوع:** هرگز از رشته‌های خام مثل `"DAMAGE"` یا `"CMD_BUY"` در کد استفاده نکنید.
2. **Logic در UI ممنوع:** هیچ منطق بازی (مثل کم کردن جان) نباید در فایل‌های UI (مثل `main.py` یا `views`) باشد.
3. **تغییر مستقیم Model ممنوع:** UI حق ندارد `minion.health -= 1` کند. فقط باید Event بفرستد.

### ✅ روش صحیح (Dos):
برای هر ایونت، حتماً از فایل `src/core/event_names.py` استفاده کنید.

**مثال غلط ❌:**
```python
# Code Review: REJECTED
event = {"type": "CMD_BUY_MINION"}

############################################
""" مثال صحیح و درست نمونه = 
import src.core.event_names as Events

# Code Review: APPROVED
event = {"type": Events.CMD_BUY_MINION}

"""
#############################################