# importações das bibliotecas

import os

import customtkinter

from tkinter import *

from PIL import Image

from tkinter import messagebox

# caracteristicas da janela inicial

janela_inicial = customtkinter.CTk()

janela_inicial.iconbitmap("ctk/imagensctk/icon app.ico")

janela_inicial.title("Login")

janela_inicial.geometry("817x500+460+200")

janela_inicial.resizable(width=False, height=False)

customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("dark-blue")

# função de registrar conta no app

def registar_conta():
    ler_usuario = input_usuario.get()
    ler_senha = input_senha.get()
    ler_senha_confirmada = input_senha_confirmar.get()

    if(ler_usuario == ""):
        messagebox.showwarning("Erro", "Insira um usuário valido")
   
    elif(ler_senha == ""):
        messagebox.showwarning("Erro", "Insira uma senha valida")

    elif(ler_senha != ler_senha_confirmada):
        messagebox.showerror("Erro", "Usuário ou senha incorreta")

    else:
        arquivo = open("dados.txt", "w")

        arquivo.write(ler_usuario + "\n")

        arquivo.write(ler_senha + "\n")

        arquivo.close()

        messagebox.showinfo("Parabéns", "Registro completo")


def entar_conta():
    ler_usuario = input_usuario.get()
    ler_senha = input_senha.get()
    ler_senha_confirmada = input_senha_confirmar.get()

    if(ler_usuario == ""):
        messagebox.showwarning("Erro", "Insira um usuário valido")
   
    elif(ler_senha == ""):
        messagebox.showwarning("Erro", "Insira uma senha valida")

    elif(ler_senha != ler_senha_confirmada):
        messagebox.showerror("Erro", "Usuário ou senha incorreta")

    else:
        arquivo = open("dados.txt", "r")

        dados = arquivo.readlines()

        usuario_registrado = dados[0].strip()

        senha_registrada = dados[1].strip()

        arquivo.close()

        if(ler_usuario == usuario_registrado) and (ler_senha == senha_registrada):
            messagebox.showinfo("Parabéns", "Entrando na conta...")

        else:
            messagebox.showerror("Erro de cadastro", "Usuário ou senha incorreta")

# imagem na tela de login / entrada

image_path = os.path.join(os.path.dirname(__file__), 'ctk/imagensctk/tela login.png')

image_entrada = customtkinter.CTkImage(light_image= Image.open(image_path), 
                                       size=(320, 320)) # tamanho da imagem

# imagem na tela de login / saida

image_saida = customtkinter.CTkLabel(master=janela_inicial,
                                     image= image_entrada,
                                     text="")

image_saida.place(x=50, y=90)


# frame da tela de login 

frame_login = customtkinter.CTkFrame(master=janela_inicial,
                                     width=250,
                                     height=450,
                                     bg_color= janela_inicial["bg"],
                                     fg_color= janela_inicial["bg"])

frame_login.place(x=450, y=40)

# titulo de login / frame

escrita_login = customtkinter.CTkLabel(master=frame_login,
                                       text="Login",
                                       text_color="#ac0dd4", # roxo
                                       font=("Microsoft YaHei UI Light", 42, "bold"))

escrita_login.place(x=70, y=8)

# input usuário / frame 

input_usuario = customtkinter.CTkEntry(master=frame_login,
                                       width=250,
                                       placeholder_text="Usuário",
                                       placeholder_text_color="#ac0dd4",
                                       font=("Microsoft YaHei UI Light", 13),
                                       border_width=0,
                                       border_color= janela_inicial["bg"],
                                       bg_color= janela_inicial["bg"],
                                       fg_color= janela_inicial["bg"])

input_usuario.place(x=0, y=120)


# linha branca e baixo de input usuário / frame

Frame(frame_login,
      width=400,
      height=2).place(x=0, y=181)


# input senha / frame 

input_senha = customtkinter.CTkEntry(master=frame_login,
                                       width=250,
                                       show="*",
                                       placeholder_text="Senha",
                                       placeholder_text_color="#ac0dd4",
                                       font=("Microsoft YaHei UI Light", 13),
                                       border_width=0,
                                       border_color= janela_inicial["bg"],
                                       bg_color= janela_inicial["bg"],
                                       fg_color= janela_inicial["bg"])

input_senha.place(x=0, y=190)


# linha branca e baixo de input senha / frame

Frame(frame_login,
      width=400,
      height=2).place(x=0, y=269)

# input confrimar senha / frame 

input_senha_confirmar = customtkinter.CTkEntry(master=frame_login,
                                       width=250,
                                       show="*",
                                       placeholder_text="Confirme sua senha",
                                       placeholder_text_color="#ac0dd4",
                                       font=("Microsoft YaHei UI Light", 13),
                                       border_width=0,
                                       border_color= janela_inicial["bg"],
                                       bg_color= janela_inicial["bg"],
                                       fg_color= janela_inicial["bg"])

input_senha_confirmar.place(x=0, y=259)


# linha branca e baixo de input senha / frame

Frame(frame_login,
      width=400,
      height=2).place(x=0, y=355)

# botão de entrar / frame

butao_login = customtkinter.CTkButton(master=frame_login,
                                      command=entar_conta,
                                      width=252,
                                      text="Entrar",
                                      text_color="white",
                                      font=("Microsoft YaHei UI Light", 12, "bold"),
                                      fg_color="#07aaeb",
                                      bg_color="#07aaeb")

butao_login.place(x=0, y=342)


# escrita em baixo do botão de entrar / frame

escrita_login_secundario = customtkinter.CTkLabel(master=frame_login,
                                                  text="Não tem uma conta?",
                                                  text_color="white",
                                                  fg_color= janela_inicial["bg"],
                                                  font=("Microsoft YaHei UI Light", 11))

escrita_login_secundario.place(x=62, y=390)


# butão seuncundario de login

butao_login_secundario = customtkinter.CTkButton(master=frame_login,
                                                 command=registar_conta,
                                                 text="Registrar-se",
                                                 text_color="#07aaeb",
                                                 fg_color= janela_inicial["bg"],
                                                 bg_color= janela_inicial["bg"],
                                                 border_spacing=0,
                                                 border_width=0,
                                                 width=8,
                                                 cursor= "hand2"
                                                 )

butao_login_secundario.place(x=168, y=390)


janela_inicial.mainloop()
