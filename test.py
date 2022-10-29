from unicodedata import name
import psutil
for proc in psutil.process_iter():
    print(proc.name().lower())
