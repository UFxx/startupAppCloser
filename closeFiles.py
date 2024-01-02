import os
import time
# Время, которое требуется на запуск всех приложений из автозагрузки
time.sleep(7)
# Приложения, которые нужно закрыть
process_names = ["notepad.exe", "Everything.exe"]

for process_name in process_names:
    os.system(f"taskkill /im {process_name}")
    print(f"Процесс {process_name} успешно закрыт.")
