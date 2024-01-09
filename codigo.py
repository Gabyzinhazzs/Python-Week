#bibliotecas
import time 
import pyautogui
import pandas
#Passo a passo
#1-Entrar no navegador 

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.click (x=675, y=160)  
pyautogui.write("edge")
pyautogui.press("enter")

#2-Entrar no sistema da empresa 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")


time.sleep(1)
#Clicar na barra de email
pyautogui.click(x=1105, y=485)
#Digitar o email
pyautogui.write("gabrielyferreiradev@.gmail.com")
#Pular para a senha 
pyautogui.press("tab")
#Digitar minha senha 
pyautogui.write("minhasenha")
#Pular para login
pyautogui.press("tab")
pyautogui.press("enter")


tabela = pandas.read_csv("produtos.csv")


for linha in tabela.index:
#Cadastrar um produto
    pyautogui.click(x=650, y=336)
    codigo = tabela.loc[linha,"codigo"]
    time.sleep(1)
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")    
    pyautogui.scroll(5000)