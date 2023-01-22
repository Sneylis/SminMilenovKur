import subprocess


cmd = "python manage.py runserver"
returned_cmd = subprocess.check_output(cmd)
print("СОСТОЯНИЕ СЕРВЕРА: ", returned_cmd.decode("utf-8"))
