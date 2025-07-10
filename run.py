import subprocess
import webbrowser
import time

# Запускаем сервер uvicorn
process = subprocess.Popen([
    "poetry", "run", "uvicorn", "salaries_and_promotions.main:app", "--reload"
])

# Ждём немного, чтобы сервер успел запуститься
time.sleep(1.5)

# Открываем Swagger UI
webbrowser.open("http://127.0.0.1:8000/docs")

# Ждём завершения сервера
process.wait()