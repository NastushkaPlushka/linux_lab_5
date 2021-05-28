import os
import socket
import shutil


def process(req):
    
    req = req.split(' ')


    if req == 'pwd':
        return os.getcwd()

    
    elif req == 'ls':
        return '; '.join(os.listdir(MY_DIRECT))

                         
    elif req[0] == 'mkdir':
        try:
            os.mkdir(MY_DIRECT + "/" + req[1])
            return "Папка успешно создана."
        except Exception:
            return "Папки не существует."

    
    elif req[0] == 'touch':
        try:
            with open(MY_DIRECT + "/" + req[1], "w") as file:
                file.write(name)
                text = file.read()
            if text:
                return "Файл успешно создан."
        except Exception:
            return "Папки не существует."

    
    elif req[0] == 'rm':
        try:
            if "." in req[1]:
                os.remove(MY_DIRECT + "/" + req[1])
                return "Удаление файла прошло успешно."
            else:
                shutil.rmtree(MY_DIRECT + "/" + req[1])
                return "Удаление папки прошло успешно."
        except Exception:
            return "Файл или директория не найдены"

    
    elif req[0] == 'rename':
        try:
            os.rename(MY_DIRECT + "/" + req[1], MY_DIRECT + "/" + req[2])
            print("Файл переименован")
        except Exception:
            print("Файла не существует.")

    
    elif req[0] == 'cps':
        try:
            text = conn.recv(int(length)).decode()
            with open(req[1], 'w') as file:
                file.write(text)
                text = file.read()
                if text:
                    return "Файл скопирован на сервер "
        except Exception:
            return "Файла не существует"
                         
        
    elif req[0] == 'cpc':
        try:
            with open(req[1], 'r') as file:
                text = file.read()
            if text:
                conn.send(str(len(text)).encode())
                return "Файл скопирован на клиент "
        except Exception:
            return "Файла не существует"
                         
                         
    elif req == 'exit':
        return "Выход"
    
    else:
        return ('Введите одну из следующих команд','pwd - название директории\n','ls - содержимое директории\n','mkdir - создает новую папку\n','touch - создает файл\n','rm - удаление папки или файла\n','rename  - переименовывет файл\n','cps  - копирует файл на сервер\n','cpc  - копирует файл с сервера\n','exit - выход')

PORT = 8080
MY_DIRECT = os.path.join(os.getcwd(), 'Моя папка')
                         
sock = socket.socket()
sock.bind(('', PORT))
sock.listen()

while True:
    print("Слушаем порт", PORT)
    conn, addr = sock.accept()
    print(addr)
    
    request = conn.recv(1024).decode()
    print(request)
    
    response = process(request)
    if response == 'exit':
        conn.close()
    conn.send(response.encode())
 
conn.close()

