import random, string
from tkinter import *

# metodo gerar senha
def gerador_senha():

    tamanho = int(entrada_valor.get())

    chars = string.ascii_letters + string.digits + 'ç!@#$%¨&*()-_=+;:' + '0123456789'

    rnd = random.SystemRandom()

    mostrar_senha["text"] = ''.join(rnd.choice(chars) for i in range(tamanho))

    # layout da tela

janela = Tk()
janela.wm_title("Gerador de Senha")
janela.configure(background="#feffff")
janela.wm_geometry("280x200")

frm = Label(janela, text="Digite o tamanho da senha desejada: ", relief="flat", anchor=CENTER, font=8, bg="#feffff", fg="#000000" )
frm.grid(row=0, column=0, padx=7, pady=10)

# Entrada de valor

entrada_valor = Entry(janela, justify="center", font=5)
entrada_valor.grid(row=1, column=0, sticky=NSEW, padx=7, pady=10)

# botão para gerar senha

botao = Button(janela, text="Gerar Senha", font=5, anchor=CENTER, command=gerador_senha, bg="#0074eb", fg="#feffff")
botao.grid(row=2, column=0, padx=7, pady=10)

# mostrar senha

mostrar_senha = Label(janela, text="", font=4, bg="#feffff")
mostrar_senha.grid(row=3, column= 0, padx=7, pady=10)




janela.mainloop()




