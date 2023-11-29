#Задание 1.
#Условие:
#Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования
# с путями (x).

import subprocess
out = "/home/user/out"
folder1 = "/home/user/folder1"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if (text in result.stdout or text in result.stderr) and result.returncode != 0:
        return True
    else:
        return False