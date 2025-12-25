# this script just or check the correct form of sting uses for team 
# its not related to the project just for checking out the code 
import os

FORBIDDEN_STRINGS = [
    '"DAMAGE"', "'DAMAGE'", 
    '"CMD_', "'CMD_", 
    '"EVENT_', "'EVENT_"
]

def scan_files():
    print("--- Code Police: Scanning for Magic Strings ---")
    has_error = False
    for root, dirs, files in os.walk("src"):
        for file in files:
            if file.endswith(".py") and file != "event_names.py":
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        for bad in FORBIDDEN_STRINGS:
                            # اگر رشته خام پیدا شد ولی ایمپورت نبود
                            if bad in line and "import" not in line and "print" not in line:
                                print(f"❌ ERROR in {path}:{i+1}")
                                print(f"   Found magic string: {bad}")
                                print(f"   -> Please use Events.CONSTANT instead.\n")
                                has_error = True
    
    if not has_error:
        print("✅ Clean Code! Good job.")
    else:
        print("⚠️  Please fix the errors above before pushing.")

if __name__ == "__main__":
    scan_files()