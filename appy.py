# Passos que devem ser seguidos para trabalhar com o tkinter
import customtkinter as ctk


# 1 - Configuração da Aparência
ctk.set_appearance_mode('dark')


# 2 - Criação das funções/funcionalidades
def validar_login():
    # Pegando os dados digitados no formulario de login
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    
    # Verificando se os dados informados estao correctos (poderia ser na bd, ficheiro, etc...). Nesse caso, vamos fazer uma verificacao fixa (user: moises; senha: 12345)
    if usuario == 'moises' and senha == '12345':
        resultado_login.configure(text='Login efetuado com sucesso!', text_color='green') # cofigure: permite alterar a propriedade de elemento
    else:
        resultado_login.configure(text='Login incorreto', text_color='red')


# 3 - Criação da janela principal
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')


# 4 - Criação dos campos necessários (Label, Entry e Button)
    # Criacao e adicao da label_usuario na tela
label_usuario = ctk.CTkLabel(app, text='Usuario') 
label_usuario.pack(pady = 10) #pady = 10 -> padding: propriedade para add um espaco em volta do elemento
#   Criacao e adicao do campo_usuario na tela
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuario')
campo_usuario.pack(pady = 10)
#   Criacao e adicao da label_senha na tela
label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady = 10)
#   Criacao e adicao do campo_senha na tela
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady = 10)
#   Criacao do botao
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady = 10)
#   Criacao de um campo de feedback sobre o login
resultado_login = ctk.CTkLabel(app, text='') # Inicialmente vai estar invisivel (pq nao tem valor no campo text). A acao do botao eh que vai definir o valor do text
resultado_login.pack(pady = 10)


# 5 - Iniciar a aplicação
app.mainloop()