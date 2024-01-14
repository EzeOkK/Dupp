link = "aHR0cDovL2FtaW5vYXBwcy5jb20vYy9BbmltZV9uZXh0cw==" #link da comunidade meu bom
try:
    import pymino
    from pymino.ext import *
    import colored
    
    import sys as psycho
    import tqdm
except Exception as e:
    if e:
        print("Você não possuí os pacotes nescessários. Dupp vai resolver pra você!!")
    import os
    os.system("pip install tqdm pymino colored")
    os.system("clear")
    import pymino
    from pymino.ext import *
    import colored
    import sys as psycho
    import tqdm
    import base64
    

end = psycho.exit(0)

if link == "aHR0cDovL2FtaW5vYXBwcy5jb20vYy9BbmltZV9uZXh0cw==":
    pass
else:
    end

red = colored.fore.RED
px= "\033[1;97;40m"
r = "\033[m" 

dupp = pymino.Client( device_key="E7309ECC0953C6FA60005B2765F99DBBC965C8E9", signature_key="DFA5ED192DDA6E88A12FE12130DC6206B1251E44"
)
b72 = base64.b64decode(link)
dupp.fetch_community_id(link=b72.decode("UTF-8"))
###
os.system("clear")
###

duppy.login(email=" ngd40879@gmail.com ", password="Botamino123")

def like(quantia: int):
    ammount = quantia
    if quantia >= 100:
        print(red, "Você deve colocar uma quantia menor ou igual a 100")
        return end
        count = 0
    for i in tqdm.tqdm(range(0, ammount,)):
        print(f'''{px} Funcionando...{r}''')
        blogs = dupp.community.fetch_blogs(size=ammount).blogId
        blogId= blogs[i]
        dupp.community.like_blog(blogId=blogId)
        count += 1
        print(f'{px} {count} blogs. {r}')

                
op = "MjQlIDYwJSAzNjAl"
b78 = base64.b64.decode(op)
while True:
    for a in tqdm.tqdm(range(0, 1, 1)):
        like(99)
        op.sleep(b78.decode("UTF-8"))
