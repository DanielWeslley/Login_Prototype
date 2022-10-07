import tkinter
from tkinter import *
import time
import os

def cadastrar():
    name = RegisterNomeEntrada.get()
    LastName= RegisterSobrenomeEntrada.get()
    User= RegisterUsuarioEntrada.get()
    password= RegisterSenhaEntrada.get()

    nome = str(name)
    sobrenome = str(LastName)
    usuario = str(User)
    senha = str(password)

    with open('./login/nomes/' + nome + '.txt', 'w') as infos:
        infos.write(f'{nome} {sobrenome}')

    with open('./login/senhas/' + usuario + ' user&pass.txt', 'w') as userpass:
        userpass.write(f'{usuario} {senha}')

    with open('./login/nomes/' + nome + '.txt', 'r') as arquivo:
        print(arquivo.read())

    if nome != None and sobrenome != None and usuario != None and senha != None :
        print('deu certo')


def logar():
    user = loginUsuario.get()
    password = loginSenha.get()
    usuario = str(user)
    senha = str(password)
    verifica = os.listdir('login/senhas')
    print(verifica)
    if usuario+' user&pass.txt' in verifica :
        with open(f'./login/senhas/{usuario} user&pass.txt', 'r') as usuariosenha:
            senha_certa = usuariosenha.read()
            senha2 = senha_certa.split()

            if usuario == senha2[0] and senha == senha2[1]:
                mensage['text'] = 'voce logou com sucesso!!'
                print('logado')
                programa()
            if usuario != senha2[0] or senha != senha2[1]:
                mensage['text'] = 'usuario ou senha incorreto!!'
    else:
        mensage['text'] = 'digite um usuario e senha valido!!'
def destruir(janela1,janela2):

    for widget in janela1.winfo_children():
        widget.destroy()
    for widget in janela2.winfo_children():
        widget.destroy()

# cores -----------------------------
preto = "#1c1b1b"
branco = "#feffff"
azul = '#283fd4'
verde = "#3fb5a3"
vermelho = "#FF0000"
co3 = "#38576b"  # cor para valores
co4 = "#403d3d"   # cor para letras

#criando janela de login
def logando():
    global janela, metade_cima,metade_baixo,loginUsuario,loginSenha, mensage
    janela = Tk()
    janela.title('login e cadastro testes')
    janela.geometry('310x310+100+100')
    janela.configure(background = branco)
    janela.resizable(width=False , height=False)

    #divisao de janela de login
    metade_cima = Frame(janela, width=410,height=70, bg=branco,relief='flat')
    metade_cima.grid(row=0, column=0, pady=1,padx=0,sticky= NSEW)

    metade_baixo = Frame(janela, width=410,height=230, bg=branco,relief='flat')
    metade_baixo.grid(row=1, column=0, pady =1,padx=0,sticky=NSEW)

    #config metade de cima/titulo da janela do login
    loginTitulo = Label(metade_cima, text = 'LOGIN', anchor=NE, font=('Ivy 25'), bg = branco, fg=co4)
    loginTitulo.place(x=5,y=5)

    loginLinha = Label(metade_cima, text = ' ',width=275, anchor=NW, font=('Ivy 1'), bg = azul, fg=co4)
    loginLinha.place(x=10,y=40)

    #config metade de baixo da janela de login

    loginUsuarioTitulo = Label(metade_baixo, text = 'usuario: ', anchor=NW, font=('Ivy 15'), bg = branco, fg=co4)
    loginUsuarioTitulo.place(x=5,y=5)

    loginUsuario = Entry(metade_baixo, font=('Ivy 17'), bg= branco, fg=co4,relief='solid')
    loginUsuario.place(x=5,y=45)

    loginSenhaTitulo = Label(metade_baixo, text = 'senha: ', anchor=NW, font=('Ivy 15'), bg = branco, fg=co4)
    loginSenhaTitulo.place(x=5,y=80)

    loginSenha = Entry(metade_baixo, font=('Ivy 17'), show='*',bg= branco, fg=co4,relief='solid')
    loginSenha.place(x=5,y=120)

    mensage = Label(metade_baixo, text = '', font=('Ivy 12'))
    mensage.place(x= 5 ,y=155)

    loginButton = Button(metade_baixo, text='Login',command=logar, font='Ivy 17', bg=azul, fg= preto, relief='raised')
    loginButton.place(x=5, y= 180)

    registerButton = Button(metade_baixo, text='Register', font='Ivy 17', bg=azul, fg= preto, relief='raised', command= register)
    registerButton.place(x=90, y= 180)
    janela.mainloop()


def register():
    global janela2, RegisterNomeEntrada, RegisterSobrenomeEntrada,RegisterUsuarioEntrada,RegisterSenhaEntrada
    janela.destroy()
    janela2= Tk()
    janela2.title('cadastro teste')
    janela2.geometry('400x675+100+100')
    janela2.configure(background = branco)
    janela2.resizable(width=False , height=False)

    #divisao de janela
    metade1 = Frame(janela2, width=700, height=70, bg=branco, relief='flat')
    metade1.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    metade2 = Frame(janela2, width=410, height=630, bg=branco, relief='flat')
    metade2.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    #botoes da janela
    tituloRegister = Label(metade1, text='REGISTRO', anchor= NE,font=('Ivy 25'), bg=branco)
    tituloRegister.place(x=5,y=10)
    RegisterLinha = Label(metade1, text=' ', width=375, anchor=NW, font=('Ivy 1'), bg=azul, fg=co4)
    RegisterLinha.place(x=10, y=50)

    RegisterNome = Label(metade2, text='Nome:', anchor= NW,font=('Ivy 25'), bg=branco, fg=co4)
    RegisterNome.place(x=5,y=2)
    RegisterNomeEntrada = Entry(metade2,font='Ivy 17', bg= branco, fg=co4,relief='solid')
    RegisterNomeEntrada.place(x=10, y=50)

    RegisterSobrenome = Label(metade2, text='Sobrenome:', anchor=NW, font=('Ivy 25'), bg=branco, fg=co4)
    RegisterSobrenome.place(x=5, y=100)
    RegisterSobrenomeEntrada = Entry(metade2, font='Ivy 17', bg=branco, fg=co4, relief='solid')
    RegisterSobrenomeEntrada.place(x=10, y=150)

    RegisterUsuario = Label(metade2, text='Usuario:', anchor=NW, font=('Ivy 25'), bg=branco, fg=co4)
    RegisterUsuario.place(x=5, y=200)
    RegisterUsuarioEntrada = Entry(metade2, font='Ivy 17', bg=branco, fg=co4, relief='solid')
    RegisterUsuarioEntrada.place(x=10, y=250)

    RegisterSenha = Label(metade2, text='Senha:', anchor=NW, font=('Ivy 25'), bg=branco, fg=co4)
    RegisterSenha.place(x=5, y=300)
    RegisterSenhaEntrada = Entry(metade2, font='Ivy 17', show='*',bg=branco, fg=co4, relief='solid')
    RegisterSenhaEntrada.place(x=10, y=350)

    RegisterConfirmaçãoSenha = Label(metade2, text='Confirme a senha:', anchor=S, font=('Ivy 25'), bg=branco, fg=co4)
    RegisterConfirmaçãoSenha.place(x=5, y=400)
    RegisterConfirmaçãoSenhaEntrada = Entry(metade2, font='Ivy 17',show='*', bg=branco, fg=co4, relief='solid')
    RegisterConfirmaçãoSenhaEntrada.place(x=10, y=450)

    registerButton = Button(metade2,text='Registrar', width=10,height=1, font='Ivy 17', background=azul, foreground= preto, relief='raised', command=lambda:[cadastrar(),janela2.destroy(),logando()])
    registerButton.place(x=5,y=520)

    returnButton = Button(metade2, text='voltar ao login',width=15,height=1, font='Ivy 17', bg=azul, fg=preto, relief='raised',command=lambda: [janela2.destroy(), logando()])
    returnButton.pack()
    returnButton.place(x=150, y=520)

    janela2.mainloop()

def programa():
    janela.destroy()
    programa = Tk()
    programa.title('cadastro teste')
    programa.geometry('1400x800+0+0')
    programa.configure(background=branco)
    programa.resizable(width=False, height=False)
    programa.mainloop()

logando()