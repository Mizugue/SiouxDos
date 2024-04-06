import requests
import queue
import threading


q = queue.Queue()
valid_proxies = []

with open('proxies', "r") as f:
    f.seek(0)
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)

def checar():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("http://google.com", proxies={"http": proxy, "https": proxy}, timeout=3)
        except:
            print(f"{proxy} / Sem conexão")
            continue
        if res.status_code == 200:
            print(f"{proxy} / Sucesso ")
            with open('proxiesvalidos.txt', 'a') as f:
                f.writelines(proxy + '\n')
        elif res.status_code == 500:
            print(f"{proxy} / Erro no servidor alvo")
        elif res.status_code == 404:
            print(f"{proxy} / Página nao encontrada")



for _ in range(1000):
    threading.Thread(target=checar()).start()

