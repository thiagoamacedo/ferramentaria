from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import askyesno
from tkcalendar import Calendar, DateEntry
from datetime import datetime,date,timedelta

def validacpf():
    cpf = [int(char) for char in telaTecnico.entCPF.get() if char.isdigit()]

    if len(cpf) != 11:
        return False

    if cpf == cpf[::-1]:
        return False

    for i in range(9, 11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


def isNaN(num):
    return num != num

window = Tk()
window.rowconfigure(0, weight=1)
window.title('Central de Ferramentaria')
window.columnconfigure(0, weight=1)
window.geometry("1920x1080")
window.state('zoomed')

telaLogin = Frame(window)
telaPrincipal = Frame(window)
telaFerramenta = Frame(window)
telaTecnico = Frame(window)
telaEmprestimo = Frame(window)
telaRelatorioEmprestimo = Frame(window)
telaSobre = Frame(window)

arquivoFerramentas = 'ferramentas.csv'
arquivoTecnicos = 'tecnicos.csv'
arquivoUsuarios = 'usuarios.csv'
arquivoReservas = 'reservas.csv'
usuarioLogado = ''

for frame in (telaLogin, telaPrincipal, telaFerramenta, telaTecnico, telaEmprestimo, telaRelatorioEmprestimo, telaSobre):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(telaLogin)

# ============= Inicio Tela de Login =========

telaLogin.Label1 = Label(telaLogin)
telaLogin.Label1.place(relx=0.0, rely=0.0, height=43, width=1920)
telaLogin.Label1.configure(background="#949494")
telaLogin.Label1.configure(anchor='center')
telaLogin.Label1.configure(compound='left')
telaLogin.Label1.configure(disabledforeground="#a3a3a3")
telaLogin.Label1.configure(font="-family {Segoe UI} -size 14 -weight bold")
telaLogin.Label1.configure(foreground="#000000")
telaLogin.Label1.configure(highlightcolor="#ffffff")
telaLogin.Label1.configure(text='''Central de Ferramentaria''')

telaLogin.Label2 = Label(telaLogin)
telaLogin.Label2.place(relx=0.0, rely=0.061, height=150, width=1920)
telaLogin.Label2.configure(background="#d9d9d9")
telaLogin.Label2.configure(compound='left')
telaLogin.Label2.configure(cursor="fleur")
telaLogin.Label2.configure(disabledforeground="#a3a3a3")
telaLogin.Label2.configure(foreground="#000000")
telaLogin.Label2.configure(text='''Digite o login e senha para acesso ao sistema''')

img = Image.open("logo.jpg")
photo = ImageTk.PhotoImage(img)
telaLogin.Imagem = Label(image=photo).place(relx=0.46, rely=0.213)

telaLogin.lblLogin = Label(telaLogin)
telaLogin.lblLogin.place(relx=0.328, rely=0.423, height=21, width=44)
telaLogin.lblLogin.configure(anchor='w')
telaLogin.lblLogin.configure(compound='left')
telaLogin.lblLogin.configure(disabledforeground="#a3a3a3")
telaLogin.lblLogin.configure(foreground="#000000")
telaLogin.lblLogin.configure(text='''Login:''')

telaLogin.lblSenha = Label(telaLogin)
telaLogin.lblSenha.place(relx=0.328, rely=0.463, height=21, width=44)
telaLogin.lblSenha.configure(anchor='w')
telaLogin.lblSenha.configure(compound='left')
telaLogin.lblSenha.configure(disabledforeground="#a3a3a3")
telaLogin.lblSenha.configure(foreground="#000000")
telaLogin.lblSenha.configure(text='''Senha:''')

telaLogin.entLogin = Entry(telaLogin)
telaLogin.entLogin.place(relx=0.382, rely=0.423, height=20, relwidth=0.263)
telaLogin.entLogin.configure(background="white")
telaLogin.entLogin.configure(disabledforeground="#a3a3a3")
telaLogin.entLogin.configure(font="TkFixedFont")
telaLogin.entLogin.configure(foreground="#000000")
telaLogin.entLogin.configure(insertbackground="black")
telaLogin.entLogin.insert(0, 'admin')

telaLogin.entSenha = Entry(telaLogin)
telaLogin.entSenha.place(relx=0.382, rely=0.463, height=20, relwidth=0.263)
telaLogin.entSenha.configure(show="*")
telaLogin.entSenha.configure(background="white")
telaLogin.entSenha.configure(disabledforeground="#a3a3a3")
telaLogin.entSenha.configure(font="TkFixedFont")
telaLogin.entSenha.configure(foreground="#000000")
telaLogin.entSenha.configure(insertbackground="black")
telaLogin.entSenha.insert(0, '1234')

telaLogin.btnAcessar = Button(telaLogin)
telaLogin.btnAcessar.place(relx=0.61, rely=0.492, height=24, width=47)
telaLogin.btnAcessar.configure(activebackground="beige")
telaLogin.btnAcessar.configure(activeforeground="black")
telaLogin.btnAcessar.configure(background="#d9d9d9")
telaLogin.btnAcessar.configure(command=lambda: logar())
telaLogin.btnAcessar.configure(compound='left')
telaLogin.btnAcessar.configure(disabledforeground="#a3a3a3")
telaLogin.btnAcessar.configure(foreground="#000000")
telaLogin.btnAcessar.configure(highlightbackground="#d9d9d9")
telaLogin.btnAcessar.configure(highlightcolor="black")
telaLogin.btnAcessar.configure(pady="0")
telaLogin.btnAcessar.configure(text='''Acessar''')
# ============= Fim Tela de Login =========

# ======== Inicio Tela Principal ==========
menuTelaPrincipalCadastro = Menubutton(telaPrincipal, text='Cadastro', activebackground='gray')
menuTelaPrincipalCadastro.grid(row=0, column=0)
menuTelaPrincipalCadastro.menu = Menu(menuTelaPrincipalCadastro, tearoff=0)
menuTelaPrincipalCadastro["menu"] = menuTelaPrincipalCadastro.menu
menuTelaPrincipalCadastro.menu.add_command(label='Principal', command=lambda: show_frame(telaPrincipal))
menuTelaPrincipalCadastro.menu.add_command(label='Ferramentas', command=lambda: show_frame(telaFerramenta))
menuTelaPrincipalCadastro.menu.add_command(label='Técnicos Responsáveis', command=lambda: show_frame(telaTecnico))

menuTelaPrincipalMovimentacao = Menubutton(telaPrincipal, text='Movimentação', activebackground='gray')
menuTelaPrincipalMovimentacao.grid(row=0, column=1)
menuTelaPrincipalMovimentacao.menu = Menu(menuTelaPrincipalMovimentacao, tearoff=0)
menuTelaPrincipalMovimentacao["menu"] = menuTelaPrincipalMovimentacao.menu
menuTelaPrincipalMovimentacao.menu.add_command(label='Empréstimo de Ferramentas', command=lambda: show_frame(telaEmprestimo))

menuTelaPrincipalRelatorios = Menubutton(telaPrincipal, text='Relatórios', activebackground='gray')
menuTelaPrincipalRelatorios.grid(row=0, column=2)
menuTelaPrincipalRelatorios.menu = Menu(menuTelaPrincipalRelatorios, tearoff=0)
menuTelaPrincipalRelatorios["menu"] = menuTelaPrincipalRelatorios.menu
menuTelaPrincipalRelatorios.menu.add_command(label='Empréstimo de Ferramentas', command=lambda: show_frame(telaRelatorioEmprestimo))

menuTelaPrincipalAjuda = Menubutton(telaPrincipal, text='Ajuda', activebackground='gray')
menuTelaPrincipalAjuda.grid(row=0, column=3)
menuTelaPrincipalAjuda.menu = Menu(menuTelaPrincipalAjuda, tearoff=0)
menuTelaPrincipalAjuda["menu"] = menuTelaPrincipalAjuda.menu
menuTelaPrincipalAjuda.menu.add_command(label='Sobre', command=lambda: show_frame(telaSobre))

telaPrincipal.Label1 = Label(telaPrincipal)
telaPrincipal.Label1.place(relx=0.0, rely=0.021, height=63, width=1920)
telaPrincipal.Label1.configure(background="#949494")
telaPrincipal.Label1.configure(anchor='center')
telaPrincipal.Label1.configure(compound='left')
telaPrincipal.Label1.configure(disabledforeground="#a3a3a3")
telaPrincipal.Label1.configure(font="-family {Segoe UI} -size 14 -weight bold")
telaPrincipal.Label1.configure(foreground="#000000")
telaPrincipal.Label1.configure(highlightcolor="#ffffff")
telaPrincipal.Label1.configure(text='''Tela Principal''')

# ======== Fim Tela Principal ==========

# ======== Inicio Cadastro de Ferramentas ===========
menuTelaFerramentaCadastro = Menubutton(telaFerramenta, text='Cadastro', activebackground='gray')
menuTelaFerramentaCadastro.grid(row=0, column=0)
menuTelaFerramentaCadastro.menu = Menu(menuTelaFerramentaCadastro, tearoff=0)
menuTelaFerramentaCadastro["menu"] = menuTelaFerramentaCadastro.menu
menuTelaFerramentaCadastro.menu.add_command(label='Principal', command=lambda: show_frame(telaPrincipal))
menuTelaFerramentaCadastro.menu.add_command(label='Ferramentas', command=lambda: show_frame(telaFerramenta))
menuTelaFerramentaCadastro.menu.add_command(label='Técnicos Responsáveis', command=lambda: show_frame(telaTecnico))

menuTelaFerramentaMovimentacao = Menubutton(telaFerramenta, text='Movimentação', activebackground='gray')
menuTelaFerramentaMovimentacao.grid(row=0, column=1)
menuTelaFerramentaMovimentacao.menu = Menu(menuTelaFerramentaMovimentacao, tearoff=0)
menuTelaFerramentaMovimentacao["menu"] = menuTelaFerramentaMovimentacao.menu
menuTelaFerramentaMovimentacao.menu.add_command(label='Empréstimo de Ferramentas', command=lambda: show_frame(telaEmprestimo))

menuTelaFerramentaRelatorios = Menubutton(telaFerramenta, text='Relatórios', activebackground='gray')
menuTelaFerramentaRelatorios.grid(row=0, column=2)
menuTelaFerramentaRelatorios.menu = Menu(menuTelaFerramentaRelatorios, tearoff=0)
menuTelaFerramentaRelatorios["menu"] = menuTelaFerramentaRelatorios.menu
menuTelaFerramentaRelatorios.menu.add_command(label='Empréstimo de Ferramentas', command=lambda: show_frame(telaRelatorioEmprestimo))

menuTelaFerramentaAjuda = Menubutton(telaFerramenta, text='Ajuda', activebackground='gray')
menuTelaFerramentaAjuda.grid(row=0, column=3)
menuTelaFerramentaAjuda.menu = Menu(menuTelaFerramentaAjuda, tearoff=0)
menuTelaFerramentaAjuda["menu"] = menuTelaFerramentaAjuda.menu
menuTelaFerramentaAjuda.menu.add_command(label='Sobre', command=lambda: show_frame(telaSobre))

telaFerramenta.Label1 = Label(telaFerramenta)
telaFerramenta.Label1.place(relx=0.0, rely=0.021, height=63, width=1920)
telaFerramenta.Label1.configure(background="#949494")
telaFerramenta.Label1.configure(anchor='center')
telaFerramenta.Label1.configure(compound='left')
telaFerramenta.Label1.configure(disabledforeground="#a3a3a3")
telaFerramenta.Label1.configure(font="-family {Segoe UI} -size 14 -weight bold")
telaFerramenta.Label1.configure(foreground="#000000")
telaFerramenta.Label1.configure(highlightcolor="#ffffff")
telaFerramenta.Label1.configure(text='''Cadastro de Ferramentas''')

colunasFerramenta = ('ID', 'Descricao', 'Fabricante', 'Voltagem', 'PartNumber', 'Tamanho', 'Unidade', 'Tipo', 'Material',
    'TempoMaximoReserva')
treeFerramenta = ttk.Treeview(telaFerramenta, columns=colunasFerramenta, show='headings')
scrollbar = ttk.Scrollbar(telaFerramenta,
                           orient="vertical",
                           command=treeFerramenta.yview)
scrollbar.place(relx=0.99, rely=0.091, height=280, width=20)
treeFerramenta.configure(xscrollcommand=scrollbar.set)

# define headings
treeFerramenta.heading("ID", text="ID", anchor=W)
treeFerramenta.heading("Descricao", text="Descrição", anchor=W)
treeFerramenta.heading("Fabricante", text="Fabricante", anchor=W)
treeFerramenta.heading("Voltagem", text="Voltagem", anchor=W)
treeFerramenta.heading("PartNumber", text="PartNumber", anchor=W)
treeFerramenta.heading("Tamanho", text="Tamanho", anchor=W)
treeFerramenta.heading("Unidade", text="Unidade", anchor=W)
treeFerramenta.heading("Tipo", text="Tipo", anchor=W)
treeFerramenta.heading("Material", text="Material", anchor=W)
treeFerramenta.heading("TempoMaximoReserva", text="Tempo Max. Reserva", anchor=W)

df = pd.read_csv(arquivoFerramentas, na_filter=False)
for row, series in df.iterrows():
    treeFerramenta.insert(parent='', index='end', iid=row, text='', values=(
        series['ID'], series['Descricao'], series['Fabricante'], series['Voltagem'], series['PartNumber'],
        series['Tamanho'], series['Unidade'], series['Tipo'], series['Material'], series['TempoMaximoReserva']))

def selecionaFerramenta(event):
    for selected_item in treeFerramenta.selection():
        item = treeFerramenta.item(selected_item)
        record = item['values']

treeFerramenta.bind('<<TreeviewSelect>>', selecionaFerramenta)
treeFerramenta.place(relx=0.0, rely=0.091, height=280, width=1920)

telaFerramenta.btnInserir = Button(telaFerramenta)
telaFerramenta.btnInserir.place(relx=0.37, rely=0.380, height=30, width=70)
telaFerramenta.btnInserir.configure(activebackground="beige")
telaFerramenta.btnInserir.configure(activeforeground="black")
telaFerramenta.btnInserir.configure(background="#d9d9d9")
telaFerramenta.btnInserir.configure(command=lambda: inserirFerramenta())
telaFerramenta.btnInserir.configure(compound='left')
telaFerramenta.btnInserir.configure(disabledforeground="#a3a3a3")
telaFerramenta.btnInserir.configure(foreground="#000000")
telaFerramenta.btnInserir.configure(highlightbackground="#d9d9d9")
telaFerramenta.btnInserir.configure(highlightcolor="black")
telaFerramenta.btnInserir.configure(pady="0")
telaFerramenta.btnInserir.configure(text='''Inserir''')

telaFerramenta.btnEditar = Button(telaFerramenta)
telaFerramenta.btnEditar.place(relx=0.42, rely=0.380, height=30, width=70)
telaFerramenta.btnEditar.configure(activebackground="beige")
telaFerramenta.btnEditar.configure(activeforeground="black")
telaFerramenta.btnEditar.configure(background="#d9d9d9")
telaFerramenta.btnEditar.configure(command=lambda: editarFerramenta())
telaFerramenta.btnEditar.configure(compound='left')
telaFerramenta.btnEditar.configure(disabledforeground="#a3a3a3")
telaFerramenta.btnEditar.configure(foreground="#000000")
telaFerramenta.btnEditar.configure(highlightbackground="#d9d9d9")
telaFerramenta.btnEditar.configure(highlightcolor="black")
telaFerramenta.btnEditar.configure(pady="0")
telaFerramenta.btnEditar.configure(text='''Editar''')

telaFerramenta.btnDeletar = Button(telaFerramenta)
telaFerramenta.btnDeletar.place(relx=0.47, rely=0.380, height=30, width=70)
telaFerramenta.btnDeletar.configure(activebackground="beige")
telaFerramenta.btnDeletar.configure(activeforeground="black")
telaFerramenta.btnDeletar.configure(background="#d9d9d9")
telaFerramenta.btnDeletar.configure(command=lambda: deletarFerramenta())
telaFerramenta.btnDeletar.configure(compound='left')
telaFerramenta.btnDeletar.configure(disabledforeground="#a3a3a3")
telaFerramenta.btnDeletar.configure(foreground="#000000")
telaFerramenta.btnDeletar.configure(highlightbackground="#d9d9d9")
telaFerramenta.btnDeletar.configure(highlightcolor="black")
telaFerramenta.btnDeletar.configure(pady="0")
telaFerramenta.btnDeletar.configure(text='''Deletar''')

telaFerramenta.btnGravar = Button(telaFerramenta)
telaFerramenta.btnGravar.place(relx=0.52, rely=0.380, height=30, width=70)
telaFerramenta.btnGravar.configure(activebackground="beige")
telaFerramenta.btnGravar.configure(activeforeground="black")
telaFerramenta.btnGravar.configure(background="#d9d9d9")
telaFerramenta.btnGravar.configure(command=lambda: gravarFerramenta())
telaFerramenta.btnGravar.configure(compound='left')
telaFerramenta.btnGravar.configure(disabledforeground="#a3a3a3")
telaFerramenta.btnGravar.configure(foreground="#000000")
telaFerramenta.btnGravar.configure(highlightbackground="#d9d9d9")
telaFerramenta.btnGravar.configure(highlightcolor="black")
telaFerramenta.btnGravar.configure(pady="0")
telaFerramenta.btnGravar.configure(text='''Gravar''')
telaFerramenta.btnGravar.configure(state="disabled")

telaFerramenta.btnCancelar = Button(telaFerramenta)
telaFerramenta.btnCancelar.place(relx=0.57, rely=0.380, height=30, width=70)
telaFerramenta.btnCancelar.configure(activebackground="beige")
telaFerramenta.btnCancelar.configure(activeforeground="black")
telaFerramenta.btnCancelar.configure(background="#d9d9d9")
telaFerramenta.btnCancelar.configure(command=lambda: cancelarFerramenta())
telaFerramenta.btnCancelar.configure(compound='left')
telaFerramenta.btnCancelar.configure(disabledforeground="#a3a3a3")
telaFerramenta.btnCancelar.configure(foreground="#000000")
telaFerramenta.btnCancelar.configure(highlightbackground="#d9d9d9")
telaFerramenta.btnCancelar.configure(highlightcolor="black")
telaFerramenta.btnCancelar.configure(pady="0")
telaFerramenta.btnCancelar.configure(text='''Cancelar''')
telaFerramenta.btnCancelar.configure(state="disabled")

telaFerramenta.lblID = Label(telaFerramenta)
telaFerramenta.lblID.place(relx=0.328, rely=0.435, height=21, width=60)
telaFerramenta.lblID.configure(anchor='w')
telaFerramenta.lblID.configure(compound='left')
telaFerramenta.lblID.configure(disabledforeground="#a3a3a3")
telaFerramenta.lblID.configure(foreground="#000000")
telaFerramenta.lblID.configure(text='''ID:''')
telaFerramenta.entID = Entry(telaFerramenta)
telaFerramenta.entID.place(relx=0.382, rely=0.435, height=20, relwidth=0.053)
telaFerramenta.entID.configure(background="white")
telaFerramenta.entID.configure(disabledforeground="#a3a3a3")
telaFerramenta.entID.configure(font="TkFixedFont")
telaFerramenta.entID.configure(foreground="#000000")
telaFerramenta.entID.configure(insertbackground="black")
telaFerramenta.entID.configure(state="disabled")

telaFerramenta.lblDescricao = Label(telaFerramenta)
telaFerramenta.lblDescricao.place(relx=0.328, rely=0.475, height=21, width=60)
telaFerramenta.lblDescricao.configure(anchor='w')
telaFerramenta.lblDescricao.configure(compound='left')
telaFerramenta.lblDescricao.configure(disabledforeground="#a3a3a3")
telaFerramenta.lblDescricao.configure(foreground="#000000")
telaFerramenta.lblDescricao.configure(text='''Descrição:''')
telaFerramenta.entDescricao = Entry(telaFerramenta)
telaFerramenta.entDescricao.place(relx=0.382, rely=0.475, height=20, relwidth=0.263)
telaFerramenta.entDescricao.configure(background="white")
telaFerramenta.entDescricao.configure(disabledforeground="#a3a3a3")
telaFerramenta.entDescricao.configure(font="TkFixedFont")
telaFerramenta.entDescricao.configure(foreground="#000000")
telaFerramenta.entDescricao.configure(insertbackground="black")
telaFerramenta.entDescricao.configure(state="disabled")

telaFerramenta.lblFabricante = Label(telaFerramenta)
telaFerramenta.lblFabricante.place(relx=0.328, rely=0.515, height=21, width=60)
telaFerramenta.lblFabricante.configure(anchor='w')
telaFerramenta.lblFabricante.configure(compound='left')
telaFerramenta.lblFabricante.configure(disabledforeground="#a3a3a3")
telaFerramenta.lblFabricante.configure(foreground="#000000")
telaFerramenta.lblFabricante.configure(text='''Fabricante:''')
telaFerramenta.entFabricante = Entry(telaFerramenta)
telaFerramenta.entFabricante.place(relx=0.382, rely=0.515, height=20, relwidth=0.163)
telaFerramenta.entFabricante.configure(background="white")
telaFerramenta.entFabricante.configure(disabledforeground="#a3a3a3")
telaFerramenta.entFabricante.configure(font="TkFixedFont")
telaFerramenta.entFabricante.configure(foreground="#000000")
telaFerramenta.entFabricante.configure(insertbackground="black")
telaFerramenta.entFabricante.configure(state="disabled")

telaFerramenta.lblVoltagem = Label(telaFerramenta)
telaFerramenta.lblVoltagem.place(relx=0.328, rely=0.555, height=21, width=60)
telaFerramenta.lblVoltagem.configure(anchor='w')
telaFerramenta.lblVoltagem.configure(compound='left')
telaFerramenta.lblVoltagem.configure(disabledforeground="#a3a3a3")
telaFerramenta.lblVoltagem.configure(foreground="#000000")
telaFerramenta.lblVoltagem.configure(text='''Voltagem:''')
telaFerramenta.entVoltagem = Entry(telaFerramenta)
telaFerramenta.entVoltagem.place(relx=0.382, rely=0.555, height=20, relwidth=0.100)
telaFerramenta.entVoltagem.configure(background="white")
telaFerramenta.entVoltagem.configure(disabledforeground="#a3a3a3")
telaFerramenta.entVoltagem.configure(font="TkFixedFont")
telaFerramenta.entVoltagem.configure(foreground="#000000")
telaFerramenta.entVoltagem.configure(insertbackground="black")
telaFerramenta.entVoltagem.configure(state="disabled")

telaFerramenta.lblPartNumber = Label(telaFerramenta)
telaFerramenta.lblPartNumber.place(relx=0.328, rely=0.595, height=21, width=80)
telaFerramenta.lblPartNumber.configure(anchor='w')
telaFerramenta.lblPartNumber.configure(compound='left')
telaFerramenta.lblPartNumber.configure(disabledforeground="#a3a3a3")
telaFerramenta.lblPartNumber.configure(foreground="#000000")
telaFerramenta.lblPartNumber.configure(text='''Part Number:''')
telaFerramenta.entPartNumber = Entry(telaFerramenta)
telaFerramenta.entPartNumber.place(relx=0.382, rely=0.595, height=20, relwidth=0.180)
telaFerramenta.entPartNumber.configure(background="white")
telaFerramenta.entPartNumber.configure(disabledforeground="#a3a3a3")
telaFerramenta.entPartNumber.configure(font="TkFixedFont")
telaFerramenta.entPartNumber.configure(foreground="#000000")
telaFerramenta.entPartNumber.configure(insertbackground="black")
telaFerramenta.entPartNumber.configure(state="disabled")

telaFerramenta.lblTamanho = Label(telaFerramenta)
telaFerramenta.lblTamanho.place(relx=0.328, rely=0.635, height=21, width=80)
telaFerramenta.lblTamanho.configure(anchor='w')
telaFerramenta.lblTamanho.configure(compound='left')
telaFerramenta.lblTamanho.configure(disabledforeground="#a3a3a3")
telaFerramenta.lblTamanho.configure(foreground="#000000")
telaFerramenta.lblTamanho.configure(text='''Tamanho:''')
telaFerramenta.entTamanho = Entry(telaFerramenta)
telaFerramenta.entTamanho.place(relx=0.382, rely=0.635, height=20, relwidth=0.150)
telaFerramenta.entTamanho.configure(background="white")
telaFerramenta.entTamanho.configure(disabledforeground="#a3a3a3")
telaFerramenta.entTamanho.configure(font="TkFixedFont")
telaFerramenta.entTamanho.configure(foreground="#000000")
telaFerramenta.entTamanho.configure(insertbackground="black")
telaFerramenta.entTamanho.configure(state="disabled")

unidadeMedida = ['centimetros', 'polegadas', 'metros']
telaFerramenta.lblUnidade = Label(telaFerramenta)
telaFerramenta.lblUnidade.place(relx=0.328, rely=0.675, height=21, width=80)
telaFerramenta.lblUnidade.configure(anchor='w')
telaFerramenta.lblUnidade.configure(compound='left')
telaFerramenta.lblUnidade.configure(disabledforeground="#a3a3a3")
telaFerramenta.lblUnidade.configure(foreground="#000000")
telaFerramenta.lblUnidade.configure(text='''Unidade:''')
telaFerramenta.comboUnidade = ttk.Combobox(telaFerramenta, width=15)
telaFerramenta.comboUnidade.place(relx=0.382, rely=0.675, height=20, relwidth=0.100)
telaFerramenta.comboUnidade.configure(background="white")
telaFerramenta.comboUnidade.configure(font="TkFixedFont")
telaFerramenta.comboUnidade.configure(foreground="#000000")
telaFerramenta.comboUnidade.configure(state="disabled")
telaFerramenta.comboUnidade['values'] = (unidadeMedida)

tipoFerramentas = ['elêtrica', 'mecânica', 'segurança']
telaFerramenta.lblTipoFerramenta = Label(telaFerramenta)
telaFerramenta.lblTipoFerramenta.place(relx=0.328, rely=0.715, height=21, width=100)
telaFerramenta.lblTipoFerramenta.configure(anchor='w')
telaFerramenta.lblTipoFerramenta.configure(compound='left')
telaFerramenta.lblTipoFerramenta.configure(disabledforeground="#a3a3a3")
telaFerramenta.lblTipoFerramenta.configure(foreground="#000000")
telaFerramenta.lblTipoFerramenta.configure(text='''Tipo:''')
telaFerramenta.comboTipoFerramenta = ttk.Combobox(telaFerramenta, width=15)
telaFerramenta.comboTipoFerramenta.place(relx=0.382, rely=0.715, height=20, relwidth=0.100)
telaFerramenta.comboTipoFerramenta.configure(background="white")
telaFerramenta.comboTipoFerramenta.configure(font="TkFixedFont")
telaFerramenta.comboTipoFerramenta.configure(foreground="#000000")
telaFerramenta.comboTipoFerramenta.configure(state="disabled")
telaFerramenta.comboTipoFerramenta['values'] = (tipoFerramentas)

materialFerramenta = ['ferro', 'madeira', 'borracha', 'plastico']
telaFerramenta.lblMaterialFerramenta = Label(telaFerramenta)
telaFerramenta.lblMaterialFerramenta.place(relx=0.328, rely=0.755, height=21, width=100)
telaFerramenta.lblMaterialFerramenta.configure(anchor='w')
telaFerramenta.lblMaterialFerramenta.configure(compound='left')
telaFerramenta.lblMaterialFerramenta.configure(disabledforeground="#a3a3a3")
telaFerramenta.lblMaterialFerramenta.configure(foreground="#000000")
telaFerramenta.lblMaterialFerramenta.configure(text='''Material:''')
telaFerramenta.comboMaterialFerramenta = ttk.Combobox(telaFerramenta, width=15)
telaFerramenta.comboMaterialFerramenta.place(relx=0.382, rely=0.755, height=20, relwidth=0.100)
telaFerramenta.comboMaterialFerramenta.configure(background="white")
telaFerramenta.comboMaterialFerramenta.configure(font="TkFixedFont")
telaFerramenta.comboMaterialFerramenta.configure(foreground="#000000")
telaFerramenta.comboMaterialFerramenta.configure(state="disabled")
telaFerramenta.comboMaterialFerramenta['values'] = (materialFerramenta)

telaFerramenta.lblTempoMaximo = Label(telaFerramenta)
telaFerramenta.lblTempoMaximo.place(relx=0.328, rely=0.795, height=21, width=100)
telaFerramenta.lblTempoMaximo.configure(anchor='w')
telaFerramenta.lblTempoMaximo.configure(compound='left')
telaFerramenta.lblTempoMaximo.configure(disabledforeground="#a3a3a3")
telaFerramenta.lblTempoMaximo.configure(foreground="#000000")
telaFerramenta.lblTempoMaximo.configure(text='''Tempo Máximo:''')
telaFerramenta.entTempoMaximo = Entry(telaFerramenta)
telaFerramenta.entTempoMaximo.place(relx=0.382, rely=0.795, height=20, relwidth=0.050)
telaFerramenta.entTempoMaximo.configure(background="white")
telaFerramenta.entTempoMaximo.configure(disabledforeground="#a3a3a3")
telaFerramenta.entTempoMaximo.configure(font="TkFixedFont")
telaFerramenta.entTempoMaximo.configure(foreground="#000000")
telaFerramenta.entTempoMaximo.configure(insertbackground="black")
telaFerramenta.entTempoMaximo.configure(state="disabled")

def inserirFerramenta():
    telaFerramenta.btnInserir.configure(state="disabled")
    telaFerramenta.btnEditar.configure(state="disabled")
    telaFerramenta.btnDeletar.configure(state="disabled")
    telaFerramenta.btnGravar.configure(state="normal")
    telaFerramenta.btnCancelar.configure(state="normal")

    telaFerramenta.entID.configure(state="normal")
    telaFerramenta.entDescricao.configure(state="normal")
    telaFerramenta.entFabricante.configure(state="normal")
    telaFerramenta.entVoltagem.configure(state="normal")
    telaFerramenta.entPartNumber.configure(state="normal")
    telaFerramenta.entTamanho.configure(state="normal")
    telaFerramenta.comboUnidade.configure(state="normal")
    telaFerramenta.comboTipoFerramenta.configure(state="normal")
    telaFerramenta.comboMaterialFerramenta.configure(state="normal")
    telaFerramenta.entTempoMaximo.configure(state="normal")

    telaFerramenta.entID.delete(0, END)
    telaFerramenta.entDescricao.delete(0, END)
    telaFerramenta.entFabricante.delete(0, END)
    telaFerramenta.entVoltagem.delete(0, END)
    telaFerramenta.entPartNumber.delete(0, END)
    telaFerramenta.entTamanho.delete(0, END)
    telaFerramenta.comboUnidade.delete(0, END)
    telaFerramenta.comboTipoFerramenta.delete(0, END)
    telaFerramenta.comboMaterialFerramenta.delete(0, END)
    telaFerramenta.entTempoMaximo.delete(0, END)

    df = pd.read_csv(arquivoFerramentas, na_filter=False)
    chaveNova = df["ID"].max()
    if isNaN(chaveNova):
        chaveNova = 0

    telaFerramenta.entID.insert(0, chaveNova+1)
    telaFerramenta.entID.configure(state="disabled")

    telaFerramenta.entDescricao.focus_set()

def editarFerramenta():
    selected = treeFerramenta.focus()
    values = treeFerramenta.item(selected, 'values')
    if values == '':
        messagebox.showwarning(title='Aviso', message='Selecione uma ferramenta antes de editar')
    else:
        telaFerramenta.btnInserir.configure(state="disabled")
        telaFerramenta.btnEditar.configure(state="disabled")
        telaFerramenta.btnDeletar.configure(state="disabled")
        telaFerramenta.btnGravar.configure(state="normal")
        telaFerramenta.btnCancelar.configure(state="normal")

        telaFerramenta.entID.configure(state="normal")
        telaFerramenta.entDescricao.configure(state="normal")
        telaFerramenta.entFabricante.configure(state="normal")
        telaFerramenta.entVoltagem.configure(state="normal")
        telaFerramenta.entPartNumber.configure(state="normal")
        telaFerramenta.entTamanho.configure(state="normal")
        telaFerramenta.comboUnidade.configure(state="normal")
        telaFerramenta.comboTipoFerramenta.configure(state="normal")
        telaFerramenta.comboMaterialFerramenta.configure(state="normal")
        telaFerramenta.entTempoMaximo.configure(state="normal")

        telaFerramenta.entID.delete(0, END)
        telaFerramenta.entDescricao.delete(0, END)
        telaFerramenta.entFabricante.delete(0, END)
        telaFerramenta.entVoltagem.delete(0, END)
        telaFerramenta.entPartNumber.delete(0, END)
        telaFerramenta.entTamanho.delete(0, END)
        telaFerramenta.comboUnidade.delete(0, END)
        telaFerramenta.comboTipoFerramenta.delete(0, END)
        telaFerramenta.comboMaterialFerramenta.delete(0, END)
        telaFerramenta.entTempoMaximo.delete(0, END)

        telaFerramenta.entID.insert(0, values[0])
        telaFerramenta.entID.configure(state="disabled")
        telaFerramenta.entDescricao.insert(0, values[1])
        telaFerramenta.entFabricante.insert(0, values[2])
        telaFerramenta.entVoltagem.insert(0, values[3])
        telaFerramenta.entPartNumber.insert(0, values[4])
        telaFerramenta.entTamanho.insert(0, values[5])
        telaFerramenta.comboUnidade.insert(0, values[6])
        telaFerramenta.comboTipoFerramenta.insert(0, values[7])
        telaFerramenta.comboMaterialFerramenta.insert(0, values[8])
        telaFerramenta.entTempoMaximo.insert(0, values[9])

        telaFerramenta.entDescricao.focus_set()

def gravarFerramenta():
    telaFerramenta.entID.configure(state="normal")

    df = pd.read_csv(arquivoFerramentas, na_filter=False)
    df['ID'] = df['ID'].astype(int)
    chave = telaFerramenta.entID.get()

    coluna = 'ID'
    valor = telaFerramenta.entID.get()
    df.loc[int(chave)-1, coluna] = valor

    coluna = 'Descricao'
    valor = telaFerramenta.entDescricao.get()
    tamanhoCampo = 60
    df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo]

    coluna = 'Fabricante'
    valor = telaFerramenta.entFabricante.get()
    tamanhoCampo = 30
    df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo]

    coluna = 'Voltagem'
    valor = telaFerramenta.entVoltagem.get()
    tamanhoCampo = 15
    df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo]

    coluna = 'PartNumber'
    valor = telaFerramenta.entPartNumber.get()
    tamanhoCampo = 25
    df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo]

    coluna = 'Tamanho'
    valor = telaFerramenta.entTamanho.get()
    tamanhoCampo = 20
    df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo]

    coluna = 'Unidade'
    valor = telaFerramenta.comboUnidade.get()
    tamanhoCampo = 15
    df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo]

    coluna = 'Tipo'
    valor = telaFerramenta.comboTipoFerramenta.get()
    tamanhoCampo = 15
    df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo]

    coluna = 'Material'
    valor = telaFerramenta.comboMaterialFerramenta.get()
    tamanhoCampo = 15
    df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo]

    coluna = 'TempoMaximoReserva'
    valor = telaFerramenta.entTempoMaximo.get()
    tamanhoCampo = 2
    df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo]


    df['ID'] = df['ID'].astype(int)
    df.to_csv(arquivoFerramentas, index=False)

    telaFerramenta.entID.delete(0, END)
    telaFerramenta.entDescricao.delete(0, END)
    telaFerramenta.entFabricante.delete(0, END)
    telaFerramenta.entVoltagem.delete(0, END)
    telaFerramenta.entPartNumber.delete(0, END)
    telaFerramenta.entTamanho.delete(0, END)
    telaFerramenta.comboUnidade.delete(0, END)
    telaFerramenta.comboTipoFerramenta.delete(0, END)
    telaFerramenta.comboMaterialFerramenta.delete(0, END)
    telaFerramenta.entTempoMaximo.delete(0, END)

    telaFerramenta.entID.configure(state="disabled")
    telaFerramenta.entDescricao.configure(state="disabled")
    telaFerramenta.entFabricante.configure(state="disabled")
    telaFerramenta.entVoltagem.configure(state="disabled")
    telaFerramenta.entPartNumber.configure(state="disabled")
    telaFerramenta.entTamanho.configure(state="disabled")
    telaFerramenta.comboUnidade.configure(state="disabled")
    telaFerramenta.comboTipoFerramenta.configure(state="disabled")
    telaFerramenta.comboMaterialFerramenta.configure(state="disabled")
    telaFerramenta.entTempoMaximo.configure(state="disabled")

    telaFerramenta.btnInserir.configure(state="normal")
    telaFerramenta.btnEditar.configure(state="normal")
    telaFerramenta.btnDeletar.configure(state="normal")
    telaFerramenta.btnGravar.configure(state="disabled")
    telaFerramenta.btnCancelar.configure(state="disabled")

    listaDadosFerramenta()

def cancelarFerramenta():
    telaFerramenta.entID.configure(state="normal")

    telaFerramenta.entID.delete(0, END)
    telaFerramenta.entDescricao.delete(0, END)
    telaFerramenta.entFabricante.delete(0, END)
    telaFerramenta.entVoltagem.delete(0, END)
    telaFerramenta.entPartNumber.delete(0, END)
    telaFerramenta.entTamanho.delete(0, END)
    telaFerramenta.comboUnidade.delete(0, END)
    telaFerramenta.comboTipoFerramenta.delete(0, END)
    telaFerramenta.comboMaterialFerramenta.delete(0, END)
    telaFerramenta.entTempoMaximo.delete(0, END)

    telaFerramenta.entID.configure(state="disabled")
    telaFerramenta.entDescricao.configure(state="disabled")
    telaFerramenta.entFabricante.configure(state="disabled")
    telaFerramenta.entVoltagem.configure(state="disabled")
    telaFerramenta.entPartNumber.configure(state="disabled")
    telaFerramenta.entTamanho.configure(state="disabled")
    telaFerramenta.comboUnidade.configure(state="disabled")
    telaFerramenta.comboTipoFerramenta.configure(state="disabled")
    telaFerramenta.comboMaterialFerramenta.configure(state="disabled")
    telaFerramenta.entTempoMaximo.configure(state="disabled")

    telaFerramenta.btnInserir.configure(state="normal")
    telaFerramenta.btnEditar.configure(state="normal")
    telaFerramenta.btnDeletar.configure(state="normal")
    telaFerramenta.btnGravar.configure(state="disabled")
    telaFerramenta.btnCancelar.configure(state="disabled")

def deletarFerramenta():

    df = pd.read_csv(arquivoFerramentas, na_filter=False)
    answer = askyesno(title='Confirmação',
                          message='Deseja excluir a ferramenta?')
    if answer == True:
        clicaritem = treeFerramenta.focus()
        valor = treeFerramenta.item(clicaritem)
        lista_valores = valor['values']
        valornormal = lista_valores[0] - 1
        df_s = df.drop(df.index[valornormal])
        df_s.to_csv(arquivoFerramentas, index=False)
        treeFerramenta.delete(*treeFerramenta.get_children())
        df = pd.read_csv(arquivoFerramentas, na_filter=False)
        for row, series in df.iterrows():
            treeFerramenta.insert(parent='', index='end', iid=row, text='', values=(
                series['ID'], series['Descricao'], series['Fabricante'], series['Voltagem'], series['PartNumber'],
                series['Tamanho'], series['Unidade'], series['Tipo'], series['Material'], series['TempoMaximoReserva']))

def listaDadosFerramenta():
    treeFerramenta.delete(*treeFerramenta.get_children())
    df = pd.read_csv(arquivoFerramentas, na_filter=False)
    for row, series in df.iterrows():
        treeFerramenta.insert(parent='', index='end', iid=row, text='', values=(
            series['ID'], series['Descricao'], series['Fabricante'], series['Voltagem'], series['PartNumber'],
            series['Tamanho'], series['Unidade'], series['Tipo'], series['Material'], series['TempoMaximoReserva']))


# ======== Fim Cadastro de Ferramentas ===========

# ======== Inicio Cadastro de Tecnicos ===========
menuTelaTecnicoCadastro = Menubutton(telaTecnico, text='Cadastro', activebackground='gray')
menuTelaTecnicoCadastro.grid(row=0, column=0)
menuTelaTecnicoCadastro.menu = Menu(menuTelaTecnicoCadastro, tearoff=0)
menuTelaTecnicoCadastro["menu"] = menuTelaTecnicoCadastro.menu
menuTelaTecnicoCadastro.menu.add_command(label='Principal', command=lambda: show_frame(telaPrincipal))
menuTelaTecnicoCadastro.menu.add_command(label='Ferramentas', command=lambda: show_frame(telaFerramenta))
menuTelaTecnicoCadastro.menu.add_command(label='Técnicos Responsáveis',command=lambda: show_frame(telaTecnico))

menuTelaTecnicoMovimentacao = Menubutton(telaTecnico, text='Movimentação', activebackground='gray')
menuTelaTecnicoMovimentacao.grid(row=0, column=1)
menuTelaTecnicoMovimentacao.menu = Menu(menuTelaTecnicoMovimentacao, tearoff=0)
menuTelaTecnicoMovimentacao["menu"] = menuTelaTecnicoMovimentacao.menu
menuTelaTecnicoMovimentacao.menu.add_command(label='Empréstimo de Ferramentas', command=lambda: show_frame(telaEmprestimo))

menuTelaTecnicoRelatorios = Menubutton(telaTecnico, text='Relatórios', activebackground='gray')
menuTelaTecnicoRelatorios.grid(row=0, column=2)
menuTelaTecnicoRelatorios.menu = Menu(menuTelaTecnicoRelatorios, tearoff=0)
menuTelaTecnicoRelatorios["menu"] = menuTelaTecnicoRelatorios.menu
menuTelaTecnicoRelatorios.menu.add_command(label='Empréstimo de Ferramentas', command=lambda: show_frame(telaRelatorioEmprestimo))

menuTelaTecnicoAjuda = Menubutton(telaTecnico, text='Ajuda', activebackground='gray')
menuTelaTecnicoAjuda.grid(row=0, column=3)
menuTelaTecnicoAjuda.menu = Menu(menuTelaTecnicoAjuda, tearoff=0)
menuTelaTecnicoAjuda["menu"] = menuTelaTecnicoAjuda.menu
menuTelaTecnicoAjuda.menu.add_command(label='Sobre', command=lambda: show_frame(telaSobre))

telaTecnico.Label1 = Label(telaTecnico)
telaTecnico.Label1.place(relx=0.0, rely=0.021, height=63, width=1920)
telaTecnico.Label1.configure(background="#949494")
telaTecnico.Label1.configure(anchor='center')
telaTecnico.Label1.configure(compound='left')
telaTecnico.Label1.configure(disabledforeground="#a3a3a3")
telaTecnico.Label1.configure(font="-family {Segoe UI} -size 14 -weight bold")
telaTecnico.Label1.configure(foreground="#000000")
telaTecnico.Label1.configure(highlightcolor="#ffffff")
telaTecnico.Label1.configure(text='''Cadastro de Tecnicos''')


colunasTecnico = ('ID', 'CPF', 'Nome', 'Telefone', 'Turno', 'NomeEquipe')
treeTecnico = ttk.Treeview(telaTecnico, columns=colunasTecnico, show='headings')
scrollbar = ttk.Scrollbar(telaTecnico,
                           orient="vertical",
                           command=treeTecnico.yview)
scrollbar.place(relx=0.99, rely=0.091, height=280, width=20)
treeTecnico.configure(xscrollcommand=scrollbar.set)

# define headings
treeTecnico.heading("ID", text="ID", anchor=W)
treeTecnico.heading("CPF", text="CPF", anchor=W)
treeTecnico.heading("Nome", text="Nome", anchor=W)
treeTecnico.heading("Telefone", text="Telefone/Radio", anchor=W)
treeTecnico.heading("Turno", text="Turno", anchor=W)
treeTecnico.heading("NomeEquipe", text="Equipe", anchor=W)

df = pd.read_csv(arquivoTecnicos, na_filter=False)
for row, series in df.iterrows():
    treeTecnico.insert(parent='', index='end', iid=row, text='', values=(
        series['ID'], series['CPF'], series['Nome'], series['Telefone'], series['Turno'], series['NomeEquipe']))

def selecionaTecnico(event):
    for selected_item in treeTecnico.selection():
        item = treeTecnico.item(selected_item)
        record = item['values']

treeTecnico.bind('<<TreeviewSelect>>', selecionaTecnico)
treeTecnico.place(relx=0.0, rely=0.091, height=280, width=1920)

telaTecnico.btnInserir = Button(telaTecnico)
telaTecnico.btnInserir.place(relx=0.37, rely=0.380, height=30, width=70)
telaTecnico.btnInserir.configure(activebackground="beige")
telaTecnico.btnInserir.configure(activeforeground="black")
telaTecnico.btnInserir.configure(background="#d9d9d9")
telaTecnico.btnInserir.configure(command=lambda: inserirTecnico())
telaTecnico.btnInserir.configure(compound='left')
telaTecnico.btnInserir.configure(disabledforeground="#a3a3a3")
telaTecnico.btnInserir.configure(foreground="#000000")
telaTecnico.btnInserir.configure(highlightbackground="#d9d9d9")
telaTecnico.btnInserir.configure(highlightcolor="black")
telaTecnico.btnInserir.configure(pady="0")
telaTecnico.btnInserir.configure(text='''Inserir''')

telaTecnico.btnEditar = Button(telaTecnico)
telaTecnico.btnEditar.place(relx=0.42, rely=0.380, height=30, width=70)
telaTecnico.btnEditar.configure(activebackground="beige")
telaTecnico.btnEditar.configure(activeforeground="black")
telaTecnico.btnEditar.configure(background="#d9d9d9")
telaTecnico.btnEditar.configure(command=lambda: editarTecnico())
telaTecnico.btnEditar.configure(compound='left')
telaTecnico.btnEditar.configure(disabledforeground="#a3a3a3")
telaTecnico.btnEditar.configure(foreground="#000000")
telaTecnico.btnEditar.configure(highlightbackground="#d9d9d9")
telaTecnico.btnEditar.configure(highlightcolor="black")
telaTecnico.btnEditar.configure(pady="0")
telaTecnico.btnEditar.configure(text='''Editar''')

telaTecnico.btnDeletar = Button(telaTecnico)
telaTecnico.btnDeletar.place(relx=0.47, rely=0.380, height=30, width=70)
telaTecnico.btnDeletar.configure(activebackground="beige")
telaTecnico.btnDeletar.configure(activeforeground="black")
telaTecnico.btnDeletar.configure(background="#d9d9d9")
telaTecnico.btnDeletar.configure(command=lambda: deletarTecnico())
telaTecnico.btnDeletar.configure(compound='left')
telaTecnico.btnDeletar.configure(disabledforeground="#a3a3a3")
telaTecnico.btnDeletar.configure(foreground="#000000")
telaTecnico.btnDeletar.configure(highlightbackground="#d9d9d9")
telaTecnico.btnDeletar.configure(highlightcolor="black")
telaTecnico.btnDeletar.configure(pady="0")
telaTecnico.btnDeletar.configure(text='''Deletar''')

telaTecnico.btnGravar = Button(telaTecnico)
telaTecnico.btnGravar.place(relx=0.52, rely=0.380, height=30, width=70)
telaTecnico.btnGravar.configure(activebackground="beige")
telaTecnico.btnGravar.configure(activeforeground="black")
telaTecnico.btnGravar.configure(background="#d9d9d9")
telaTecnico.btnGravar.configure(command=lambda: gravarTecnico())
telaTecnico.btnGravar.configure(compound='left')
telaTecnico.btnGravar.configure(disabledforeground="#a3a3a3")
telaTecnico.btnGravar.configure(foreground="#000000")
telaTecnico.btnGravar.configure(highlightbackground="#d9d9d9")
telaTecnico.btnGravar.configure(highlightcolor="black")
telaTecnico.btnGravar.configure(pady="0")
telaTecnico.btnGravar.configure(text='''Gravar''')
telaTecnico.btnGravar.configure(state="disabled")

telaTecnico.btnCancelar = Button(telaTecnico)
telaTecnico.btnCancelar.place(relx=0.57, rely=0.380, height=30, width=70)
telaTecnico.btnCancelar.configure(activebackground="beige")
telaTecnico.btnCancelar.configure(activeforeground="black")
telaTecnico.btnCancelar.configure(background="#d9d9d9")
telaTecnico.btnCancelar.configure(command=lambda: cancelarTecnico())
telaTecnico.btnCancelar.configure(compound='left')
telaTecnico.btnCancelar.configure(disabledforeground="#a3a3a3")
telaTecnico.btnCancelar.configure(foreground="#000000")
telaTecnico.btnCancelar.configure(highlightbackground="#d9d9d9")
telaTecnico.btnCancelar.configure(highlightcolor="black")
telaTecnico.btnCancelar.configure(pady="0")
telaTecnico.btnCancelar.configure(text='''Cancelar''')
telaTecnico.btnCancelar.configure(state="disabled")

telaTecnico.lblID = Label(telaTecnico)
telaTecnico.lblID.place(relx=0.328, rely=0.435, height=21, width=60)
telaTecnico.lblID.configure(anchor='w')
telaTecnico.lblID.configure(compound='left')
telaTecnico.lblID.configure(disabledforeground="#a3a3a3")
telaTecnico.lblID.configure(foreground="#000000")
telaTecnico.lblID.configure(text='''ID:''')
telaTecnico.entID = Entry(telaTecnico)
telaTecnico.entID.place(relx=0.382, rely=0.435, height=20, relwidth=0.053)
telaTecnico.entID.configure(background="white")
telaTecnico.entID.configure(disabledforeground="#a3a3a3")
telaTecnico.entID.configure(font="TkFixedFont")
telaTecnico.entID.configure(foreground="#000000")
telaTecnico.entID.configure(insertbackground="black")
telaTecnico.entID.configure(state="disabled")

def formatarCPF(event=None):
    text = telaTecnico.entCPF.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace":
        return

    for index in range(len(text)):

        if not text[index] in "0123456789":
            continue
        if index in [2, 5]:
            new_text += text[index] + "."
        elif index == 8:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    telaTecnico.entCPF.delete(0, "end")
    telaTecnico.entCPF.insert(0, new_text)

telaTecnico.lblCPF = Label(telaTecnico)
telaTecnico.lblCPF.place(relx=0.328, rely=0.475, height=21, width=60)
telaTecnico.lblCPF.configure(anchor='w')
telaTecnico.lblCPF.configure(compound='left')
telaTecnico.lblCPF.configure(disabledforeground="#a3a3a3")
telaTecnico.lblCPF.configure(foreground="#000000")
telaTecnico.lblCPF.configure(text='''CPF:''')
telaTecnico.entCPF = Entry(telaTecnico)
telaTecnico.entCPF.place(relx=0.382, rely=0.475, height=20, relwidth=0.100)
telaTecnico.entCPF.configure(background="white")
telaTecnico.entCPF.configure(disabledforeground="#a3a3a3")
telaTecnico.entCPF.configure(font="TkFixedFont")
telaTecnico.entCPF.configure(foreground="#000000")
telaTecnico.entCPF.configure(insertbackground="black")
telaTecnico.entCPF.configure(state="disabled")
telaTecnico.entCPF.bind("<KeyRelease>", formatarCPF)

telaTecnico.lblNome = Label(telaTecnico)
telaTecnico.lblNome.place(relx=0.328, rely=0.515, height=21, width=60)
telaTecnico.lblNome.configure(anchor='w')
telaTecnico.lblNome.configure(compound='left')
telaTecnico.lblNome.configure(disabledforeground="#a3a3a3")
telaTecnico.lblNome.configure(foreground="#000000")
telaTecnico.lblNome.configure(text='''Nome:''')
telaTecnico.entNome = Entry(telaTecnico)
telaTecnico.entNome.place(relx=0.382, rely=0.515, height=20, relwidth=0.263)
telaTecnico.entNome.configure(background="white")
telaTecnico.entNome.configure(disabledforeground="#a3a3a3")
telaTecnico.entNome.configure(font="TkFixedFont")
telaTecnico.entNome.configure(foreground="#000000")
telaTecnico.entNome.configure(insertbackground="black")
telaTecnico.entNome.configure(state="disabled")

telaTecnico.lblTelefone = Label(telaTecnico)
telaTecnico.lblTelefone.place(relx=0.328, rely=0.555, height=21, width=100)
telaTecnico.lblTelefone.configure(anchor='w')
telaTecnico.lblTelefone.configure(compound='left')
telaTecnico.lblTelefone.configure(disabledforeground="#a3a3a3")
telaTecnico.lblTelefone.configure(foreground="#000000")
telaTecnico.lblTelefone.configure(text='''Telefone/Radio:''')
telaTecnico.entTelefone = Entry(telaTecnico)
telaTecnico.entTelefone.place(relx=0.382, rely=0.555, height=20, relwidth=0.100)
telaTecnico.entTelefone.configure(background="white")
telaTecnico.entTelefone.configure(disabledforeground="#a3a3a3")
telaTecnico.entTelefone.configure(font="TkFixedFont")
telaTecnico.entTelefone.configure(foreground="#000000")
telaTecnico.entTelefone.configure(insertbackground="black")
telaTecnico.entTelefone.configure(state="disabled")

turno = ['manhã', 'tarde', 'noite']
telaTecnico.lblTurno = Label(telaTecnico)
telaTecnico.lblTurno.place(relx=0.328, rely=0.595, height=21, width=80)
telaTecnico.lblTurno.configure(anchor='w')
telaTecnico.lblTurno.configure(compound='left')
telaTecnico.lblTurno.configure(disabledforeground="#a3a3a3")
telaTecnico.lblTurno.configure(foreground="#000000")
telaTecnico.lblTurno.configure(text='''Turno:''')
telaTecnico.comboTurno = ttk.Combobox(telaTecnico, width=15)
telaTecnico.comboTurno.place(relx=0.382, rely=0.595, height=20, relwidth=0.100)
telaTecnico.comboTurno.configure(background="white")
telaTecnico.comboTurno.configure(font="TkFixedFont")
telaTecnico.comboTurno.configure(foreground="#000000")
telaTecnico.comboTurno.configure(state="disabled")
telaTecnico.comboTurno['values'] = (turno)

telaTecnico.lblNomeEquipe = Label(telaTecnico)
telaTecnico.lblNomeEquipe.place(relx=0.328, rely=0.635, height=21, width=60)
telaTecnico.lblNomeEquipe.configure(anchor='w')
telaTecnico.lblNomeEquipe.configure(compound='left')
telaTecnico.lblNomeEquipe.configure(disabledforeground="#a3a3a3")
telaTecnico.lblNomeEquipe.configure(foreground="#000000")
telaTecnico.lblNomeEquipe.configure(text='''Equipe:''')
telaTecnico.entNomeEquipe = Entry(telaTecnico)
telaTecnico.entNomeEquipe.place(relx=0.382, rely=0.635, height=20, relwidth=0.200)
telaTecnico.entNomeEquipe.configure(background="white")
telaTecnico.entNomeEquipe.configure(disabledforeground="#a3a3a3")
telaTecnico.entNomeEquipe.configure(font="TkFixedFont")
telaTecnico.entNomeEquipe.configure(foreground="#000000")
telaTecnico.entNomeEquipe.configure(insertbackground="black")
telaTecnico.entNomeEquipe.configure(state="disabled")


def inserirTecnico():
    telaTecnico.btnInserir.configure(state="disabled")
    telaTecnico.btnEditar.configure(state="disabled")
    telaTecnico.btnDeletar.configure(state="disabled")
    telaTecnico.btnGravar.configure(state="normal")
    telaTecnico.btnCancelar.configure(state="normal")

    telaTecnico.entID.configure(state="normal")
    telaTecnico.entCPF.configure(state="normal")
    telaTecnico.entNome.configure(state="normal")
    telaTecnico.entTelefone.configure(state="normal")
    telaTecnico.comboTurno.configure(state="normal")
    telaTecnico.entNomeEquipe.configure(state="normal")

    telaTecnico.entID.delete(0, END)
    telaTecnico.entCPF.delete(0, END)
    telaTecnico.entNome.delete(0, END)
    telaTecnico.entTelefone.delete(0, END)
    telaTecnico.comboTurno.delete(0, END)
    telaTecnico.entNomeEquipe.delete(0, END)

    df = pd.read_csv(arquivoTecnicos, na_filter=False)
    chaveNova = df["ID"].max()
    if isNaN(chaveNova):
        chaveNova = 0

    telaTecnico.entID.insert(0, chaveNova+1)
    telaTecnico.entID.configure(state="disabled")

    telaTecnico.entCPF.focus_set()

def editarTecnico():
    selected = treeTecnico.focus()
    values = treeTecnico.item(selected, 'values')
    if values == '':
        messagebox.showwarning(title='Aviso', message='Selecione um técnico antes de editar')
    else:
        telaTecnico.btnInserir.configure(state="disabled")
        telaTecnico.btnEditar.configure(state="disabled")
        telaTecnico.btnDeletar.configure(state="disabled")
        telaTecnico.btnGravar.configure(state="normal")
        telaTecnico.btnCancelar.configure(state="normal")

        telaTecnico.entID.configure(state="normal")
        telaTecnico.entCPF.configure(state="normal")
        telaTecnico.entNome.configure(state="normal")
        telaTecnico.entTelefone.configure(state="normal")
        telaTecnico.comboTurno.configure(state="normal")
        telaTecnico.entNomeEquipe.configure(state="normal")

        telaTecnico.entID.delete(0, END)
        telaTecnico.entCPF.delete(0, END)
        telaTecnico.entNome.delete(0, END)
        telaTecnico.entTelefone.delete(0, END)
        telaTecnico.comboTurno.delete(0, END)
        telaTecnico.entNomeEquipe.delete(0, END)
        
        telaTecnico.entID.insert(0, values[0])
        telaTecnico.entID.configure(state="disabled")
        telaTecnico.entCPF.insert(0, values[1])
        telaTecnico.entNome.insert(0, values[2])
        telaTecnico.entTelefone.insert(0, values[3])
        telaTecnico.comboTurno.insert(0, values[4])
        telaTecnico.entNomeEquipe.insert(0, values[5])

        telaTecnico.entCPF.focus_set()

def gravarTecnico():
    df = pd.read_csv('tecnicos.csv', na_filter=False)
    lista_cpfs = []

    df.iterrows()
    for row, series in df.iterrows():
        lista_cpfs.append(series['CPF'])

    if validacpf() and telaTecnico.entTelefone.get().isnumeric() and telaTecnico.entCPF.get() not in lista_cpfs:
        telaTecnico.entID.configure(state="normal")

        df = pd.read_csv(arquivoTecnicos, na_filter=False)
        df['ID'] = df['ID'].astype(int)
        chave = telaTecnico.entID.get()

        coluna = 'ID'
        valor = telaTecnico.entID.get()
        df.loc[int(chave)-1, coluna] = valor

        coluna = 'CPF'
        valor = telaTecnico.entCPF.get()
        tamanhoCampo = 14
        df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo]

        coluna = 'Nome'
        valor = telaTecnico.entNome.get()
        tamanhoCampo = 40
        df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo]

        coluna = 'Telefone'
        valor = telaTecnico.entTelefone.get()
        tamanhoCampo = 9
        df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo]

        coluna = 'Turno'
        valor = telaTecnico.comboTurno.get()
        tamanhoCampo = 10
        df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo]

        coluna = 'NomeEquipe'
        valor = telaTecnico.entNomeEquipe.get()
        tamanhoCampo = 30
        df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo]

        df['ID'] = df['ID'].astype(int)
        df['Telefone'] = df['Telefone'].astype(int)
        df.to_csv(arquivoTecnicos, index=False)

        telaTecnico.entID.delete(0, END)
        telaTecnico.entCPF.delete(0, END)
        telaTecnico.entNome.delete(0, END)
        telaTecnico.entTelefone.delete(0, END)
        telaTecnico.comboTurno.delete(0, END)
        telaTecnico.entNomeEquipe.delete(0, END)

        telaTecnico.entID.configure(state="disabled")
        telaTecnico.entCPF.configure(state="disabled")
        telaTecnico.entNome.configure(state="disabled")
        telaTecnico.entTelefone.configure(state="disabled")
        telaTecnico.comboTurno.configure(state="disabled")
        telaTecnico.entNomeEquipe.configure(state="disabled")

        telaTecnico.btnInserir.configure(state="normal")
        telaTecnico.btnEditar.configure(state="normal")
        telaTecnico.btnDeletar.configure(state="normal")
        telaTecnico.btnGravar.configure(state="disabled")
        telaTecnico.btnCancelar.configure(state="disabled")

        listaDadosTecnico()

    else:
        messagebox.showerror('','CADASTRO INVÁLIDO')

def cancelarTecnico():
    telaTecnico.entID.configure(state="normal")

    telaTecnico.entID.delete(0, END)
    telaTecnico.entCPF.delete(0, END)
    telaTecnico.entNome.delete(0, END)
    telaTecnico.entTelefone.delete(0, END)
    telaTecnico.comboTurno.delete(0, END)
    telaTecnico.entNomeEquipe.delete(0, END)

    telaTecnico.entID.configure(state="disabled")
    telaTecnico.entCPF.configure(state="disabled")
    telaTecnico.entNome.configure(state="disabled")
    telaTecnico.entTelefone.configure(state="disabled")
    telaTecnico.comboTurno.configure(state="disabled")
    telaTecnico.entNomeEquipe.configure(state="disabled")

    telaTecnico.btnInserir.configure(state="normal")
    telaTecnico.btnEditar.configure(state="normal")
    telaTecnico.btnDeletar.configure(state="normal")
    telaTecnico.btnGravar.configure(state="disabled")
    telaTecnico.btnCancelar.configure(state="disabled")

def deletarTecnico():
    df = pd.read_csv(arquivoTecnicos, na_filter=False)
    answer = askyesno(title='Confirmação',
                      message='Deseja excluir o técnico?')
    if answer == True:
        clicaritem = treeTecnico.focus()
        valor = treeTecnico.item(clicaritem)
        lista_valores = valor['values']
        valornormal = lista_valores[0]-1
        df_s = df.drop(df.index[valornormal])
        df_s.to_csv(arquivoTecnicos, index=False)
        treeTecnico.delete(*treeTecnico.get_children())
        df = pd.read_csv(arquivoTecnicos, na_filter=False)
        for row, series in df.iterrows():
            treeTecnico.insert(parent='', index='end', iid=row, text='', values=(
                series['ID'], series['CPF'], series['Nome'], series['Telefone'], series['Turno'], series['NomeEquipe']))

def listaDadosTecnico():
    treeTecnico.delete(*treeTecnico.get_children())
    df = pd.read_csv(arquivoTecnicos, na_filter=False)
    for row, series in df.iterrows():
        treeTecnico.insert(parent='', index='end', iid=row, text='', values=(
            series['ID'], series['CPF'], series['Nome'], series['Telefone'], series['Turno'], series['NomeEquipe']))

# ======== Fim  Cadastro de Tecnicos ===========

# ======== Inicio Tela Emprestimo Backup ==========

# def btnreservarFerramenta():
#     telaEmprestimo.btnReservar.configure(state="disabled")
#     telaEmprestimo.btnConfirmar.configure(state="normal")
#     telaEmprestimo.btnCancelar.configure(state="normal")
# 
#     telaEmprestimo.entIDferramenta.configure(state="normal")
#     telaEmprestimo.entCPFemprestimo.configure(state="normal")
#     telaEmprestimo.btnDataDevolucao.configure(state="normal")
#     telaEmprestimo.btnDataRetirada.configure(state="normal")
#     telaEmprestimo.entNomeEmprestimo.configure(state="normal")
#     
#     telaEmprestimo.entIDferramenta.delete(0, END)
#     telaEmprestimo.entCPFemprestimo.delete(0, END)
#     telaEmprestimo.entNomeEmprestimo.delete(0, END)
#     telaEmprestimo.entDataRetirada.delete(0, END)
#     telaEmprestimo.entDataDevolucao.delete(0, END)
#     
# def cancelarReserva():
#     telaEmprestimo.btnReservar.configure(state="normal")
#     telaEmprestimo.btnConfirmar.configure(state="disabled")
#     telaEmprestimo.btnCancelar.configure(state="disabled")
# 
#     telaEmprestimo.entIDferramenta.configure(state="disabled")
#     telaEmprestimo.entCPFemprestimo.configure(state="disabled")
#     telaEmprestimo.btnDataDevolucao.configure(state="disabled")
#     telaEmprestimo.btnDataRetirada.configure(state="disabled")
#     telaEmprestimo.entNomeEmprestimo.configure(state="disabled")
#     
#     telaEmprestimo.entIDferramenta.delete(0, END)
#     telaEmprestimo.entCPFemprestimo.delete(0, END)
#     telaEmprestimo.entNomeEmprestimo.delete(0, END)
#     telaEmprestimo.entDataRetirada.delete(0, END)
#     telaEmprestimo.entDataDevolucao.delete(0, END)
#     
#     telaEmprestimo.btnInserirRetirada.place(relx=1.800, rely=1.900, height=30, width=70)
#     calendarioRetirada.place(relx=1.800, rely=1.800)
#     telaEmprestimo.lblHorarioRetirada.place(relx=1.800, rely=1.800)
#     telaEmprestimo.entHorarioRetirada.place(relx=1.800, rely=1.800, height=25, width=78)
#     telaEmprestimo.entDataRetirada.configure(state="disabled")
#     
#     calendarioDevolucao.place(relx=1.800, rely=1.800)
#     telaEmprestimo.btnInserirDevolucao.place(relx=1.800, rely=1.800, height=30, width=70)
#     telaEmprestimo.lblHorarioDevolucao.place(relx=1.800, rely=1.800)
#     telaEmprestimo.entHorarioDevolucao.place(relx=1.800, rely=1.800, height=25, width=78)
#     telaEmprestimo.entDataDevolucao.configure(state="disabled")
#     
# def inserirnomeTecnico(event):
#     global nome
#     df = pd.read_csv("tecnicos.csv")
#     cpfpegar = str(telaEmprestimo.entCPFemprestimo.get())
#     cpf = df[df.CPF==cpfpegar]
#     nome1 = cpf['Nome'].astype(str)
#     nome2 = list(nome1)
#     nome = nome2[0]
#     print(nome)
#     
#     telaEmprestimo.entNomeEmprestimo.configure(state="normal")
#     telaEmprestimo.entNomeEmprestimo.delete(0,'end')
#     telaEmprestimo.entNomeEmprestimo.insert(0,nome)
#     telaEmprestimo.entNomeEmprestimo.configure(state="disabled")
#     
# def calendarioabrirRetirada():
#     global calendarioRetirada, btnInserirRetirada
#     calendarioRetirada = Calendar(telaEmprestimo,fg='gray75',bg='blue',font='Bahnschrift',locate='pt_br')
#     calendarioRetirada.place(relx=0.408, rely=0.475)
#     
#     telaEmprestimo.btnInserirRetirada = Button(telaEmprestimo)
#     telaEmprestimo.btnInserirRetirada.place(relx=0.5335, rely=0.699, height=30, width=70)
#     telaEmprestimo.btnInserirRetirada.configure(activebackground="beige")
#     telaEmprestimo.btnInserirRetirada.configure(activeforeground="black")
#     telaEmprestimo.btnInserirRetirada.configure(background="#d9d9d9")
#     telaEmprestimo.btnInserirRetirada.configure(command=lambda: FecharcalendarioRetirada())
#     telaEmprestimo.btnInserirRetirada.configure(compound='left')
#     telaEmprestimo.btnInserirRetirada.configure(disabledforeground="#a3a3a3")
#     telaEmprestimo.btnInserirRetirada.configure(foreground="#000000")
#     telaEmprestimo.btnInserirRetirada.configure(highlightbackground="#d9d9d9")
#     telaEmprestimo.btnInserirRetirada.configure(highlightcolor="black")
#     telaEmprestimo.btnInserirRetirada.configure(pady="0")
#     telaEmprestimo.btnInserirRetirada.configure(text='''Inserir''')
#     
#     telaEmprestimo.lblHorarioRetirada = Label(telaEmprestimo)
#     telaEmprestimo.lblHorarioRetirada.place(relx=0.408, rely=0.700)
#     telaEmprestimo.lblHorarioRetirada.configure(anchor='w')
#     telaEmprestimo.lblHorarioRetirada.configure(compound='left')
#     telaEmprestimo.lblHorarioRetirada.configure(disabledforeground="#a3a3a3")
#     telaEmprestimo.lblHorarioRetirada.configure(foreground="#000000")
#     telaEmprestimo.lblHorarioRetirada.configure(text='''HORÁRIO:''')
#     telaEmprestimo.lblHorarioRetirada.configure(font=("Bahnschrift",'13'))
#     
#     telaEmprestimo.entHorarioRetirada = Entry(telaEmprestimo)
#     telaEmprestimo.entHorarioRetirada.place(relx=0.455, rely=0.702, height=25, width=78)
#     telaEmprestimo.entHorarioRetirada.configure(background="white")
#     telaEmprestimo.entHorarioRetirada.configure(disabledforeground="#a3a3a3")
#     telaEmprestimo.entHorarioRetirada.configure(font=("Bahnschrift",'11'))
#     telaEmprestimo.entHorarioRetirada.configure(foreground="#000000")
#     telaEmprestimo.entHorarioRetirada.configure(insertbackground="black")
#     telaEmprestimo.entHorarioRetirada.bind('<KeyRelease>',FormatarHoraRetirada)
#     
# def FecharcalendarioRetirada():
#     horario_formatar = telaEmprestimo.entHorarioRetirada.get().split(':')
#     
#     if telaEmprestimo.entHorarioRetirada.get()=='' or len(telaEmprestimo.entHorarioRetirada.get())!=5 or int(horario_formatar[0])>=24 or int(horario_formatar[1])>=60:
#         messagebox.showerror('','Horário inválido')
#     else:
#         telaEmprestimo.entDataRetirada.configure(state="normal")
#         data_da_retirada = calendarioRetirada.get_date()
#         hora_retirada = telaEmprestimo.entHorarioRetirada.get()
#         telaEmprestimo.entDataRetirada.delete(0,'end')
#         telaEmprestimo.entDataRetirada.insert(0,data_da_retirada)
#         telaEmprestimo.entDataRetirada.insert(11,' ')
#         telaEmprestimo.entDataRetirada.insert(12,hora_retirada)
#         
#         telaEmprestimo.btnInserirRetirada.place(relx=1.800, rely=1.900, height=30, width=70)
#         calendarioRetirada.place(relx=1.800, rely=1.800)
#         telaEmprestimo.lblHorarioRetirada.place(relx=1.800, rely=1.800)
#         telaEmprestimo.entHorarioRetirada.place(relx=1.800, rely=1.800, height=25, width=78)
#         telaEmprestimo.entDataRetirada.configure(state="disabled")
#     
# def calendarioabrirDevolucao():
#     global calendarioDevolucao
#     calendarioDevolucao = Calendar(telaEmprestimo,fg='gray75',bg='blue',font='Bahnschrift',locate='pt_br')
#     calendarioDevolucao.place(relx=0.505, rely=0.475)
# 
# 
#     telaEmprestimo.btnInserirDevolucao = Button(telaEmprestimo)
#     telaEmprestimo.btnInserirDevolucao.place(relx=0.6305, rely=0.700, height=30, width=70)
#     telaEmprestimo.btnInserirDevolucao.configure(activebackground="beige")
#     telaEmprestimo.btnInserirDevolucao.configure(activeforeground="black")
#     telaEmprestimo.btnInserirDevolucao.configure(background="#d9d9d9")
#     telaEmprestimo.btnInserirDevolucao.configure(command=lambda: FecharcalendarioDevolucao())
#     telaEmprestimo.btnInserirDevolucao.configure(compound='left')
#     telaEmprestimo.btnInserirDevolucao.configure(disabledforeground="#a3a3a3")
#     telaEmprestimo.btnInserirDevolucao.configure(foreground="#000000")
#     telaEmprestimo.btnInserirDevolucao.configure(highlightbackground="#d9d9d9")
#     telaEmprestimo.btnInserirDevolucao.configure(highlightcolor="black")
#     telaEmprestimo.btnInserirDevolucao.configure(pady="0")
#     telaEmprestimo.btnInserirDevolucao.configure(text='''Inserir''')
#     
#     telaEmprestimo.lblHorarioDevolucao = Label(telaEmprestimo)
#     telaEmprestimo.lblHorarioDevolucao.place(relx=0.505, rely=0.700)
#     telaEmprestimo.lblHorarioDevolucao.configure(anchor='w')
#     telaEmprestimo.lblHorarioDevolucao.configure(compound='left')
#     telaEmprestimo.lblHorarioDevolucao.configure(disabledforeground="#a3a3a3")
#     telaEmprestimo.lblHorarioDevolucao.configure(foreground="#000000")
#     telaEmprestimo.lblHorarioDevolucao.configure(text='''HORÁRIO:''')
#     telaEmprestimo.lblHorarioDevolucao.configure(font=("Bahnschrift",'13'))
#     
#     telaEmprestimo.entHorarioDevolucao = Entry(telaEmprestimo)
#     telaEmprestimo.entHorarioDevolucao.place(relx=0.552, rely=0.702, height=25, width=78)
#     telaEmprestimo.entHorarioDevolucao.configure(background="white")
#     telaEmprestimo.entHorarioDevolucao.configure(disabledforeground="#a3a3a3")
#     telaEmprestimo.entHorarioDevolucao.configure(font=("Bahnschrift",'11'))
#     telaEmprestimo.entHorarioDevolucao.configure(foreground="#000000")
#     telaEmprestimo.entHorarioDevolucao.configure(insertbackground="black")
#     telaEmprestimo.entHorarioDevolucao.bind('<KeyRelease>',FormatarHoraDevolucao)
# 
# def FecharcalendarioDevolucao():
#     horario_formatar = telaEmprestimo.entHorarioDevolucao.get().split(':')
#     print(horario_formatar)
#     
#     if telaEmprestimo.entHorarioDevolucao.get()=='' or len(telaEmprestimo.entHorarioDevolucao.get())!=5 or int(horario_formatar[0])>=24 or int(horario_formatar[1])>=60:
#         messagebox.showerror('','Horário inválido')
#     else:
#         telaEmprestimo.entDataDevolucao.configure(state="normal")
#         data_da_devolucao = calendarioDevolucao.get_date()
#         hora_devolucao = telaEmprestimo.entHorarioDevolucao.get()
#         telaEmprestimo.entDataDevolucao.delete(0,'end')
#         telaEmprestimo.entDataDevolucao.insert(0,data_da_devolucao)
#         telaEmprestimo.entDataDevolucao.insert(11,' ')
#         telaEmprestimo.entDataDevolucao.insert(12,hora_devolucao)
#         
#         calendarioDevolucao.place(relx=1.800, rely=1.800)
#         telaEmprestimo.btnInserirDevolucao.place(relx=1.800, rely=1.800, height=30, width=70)
#         telaEmprestimo.lblHorarioDevolucao.place(relx=1.800, rely=1.800)
#         telaEmprestimo.entHorarioDevolucao.place(relx=1.800, rely=1.800, height=25, width=78)
#         telaEmprestimo.entDataDevolucao.configure(state="disabled")
# 
# def FormatarHoraRetirada(event=None):
#     if len(telaEmprestimo.entHorarioRetirada.get())==2:
#         telaEmprestimo.entHorarioRetirada.insert(2,':')
#         
#     if len(telaEmprestimo.entHorarioRetirada.get())==6:
#         telaEmprestimo.entHorarioRetirada.delete(5,'end')
# 
# def FormatarHoraDevolucao(event=None):
#     if len(telaEmprestimo.entHorarioDevolucao.get())==2:
#         telaEmprestimo.entHorarioDevolucao.insert(2,':')
#     if len(telaEmprestimo.entHorarioDevolucao.get())==6:
#         telaEmprestimo.entHorarioDevolucao.delete(5,'end')
# 
# def reservarFerramenta():
#     data_retirada = telaEmprestimo.entDataRetirada.get()
#     data_e_hora_retirada = datetime.strptime(data_retirada, "%d/%m/%Y %H:%M")
#     
#     data_devolucao = telaEmprestimo.entDataDevolucao.get()
#     data_e_hora_devolucao = datetime.strptime(data_devolucao, "%d/%m/%Y %H:%M")
#     
#     df = pd.read_csv("ferramentas.csv")
#     id_ferramenta = df[df.ID==int(telaEmprestimo.entIDferramenta.get())]
#     numero1 = id_ferramenta['TempoMaximoReserva']
#     numero2 = list(numero1)
#     numero3= str(numero2).replace(']','')
#     numero4 = numero3.replace('[','')
# 
#     tempo_max_reserva = float(numero4)
#     
#     time_1 = timedelta(days=0, hours=0)
#     time_2 = timedelta(hours=tempo_max_reserva)
#     print(time_2)
#     data_devolucao_max = time_1+time_2
#     print(data_devolucao_max)
#     data_max = data_devolucao_max + data_e_hora_retirada
#     print(data_max)
#     
#     if data_e_hora_devolucao>data_max:
#         messagebox.showerror('','Data de devolução inválida')
#     # elif data_e_hora_devolucao<=data_max:
#     #     ################ COLOCAR AQUI O CÓDIGO PARA RESERVAR NO CSV ################
# 
# def gravarReserva():
#     telaEmprestimo.entIDferramenta.configure(state="normal")
# 
#     df = pd.read_csv(arquivoReservas, na_filter=False)
#     df['ID'] = df['ID'].astype(int)
#     chave = telaEmprestimo.entID.get()
# 
#     coluna = 'ID do Emprestimo'
#     valor = telaEmprestimo.entID.get()
#     df.loc[int(chave)-1, coluna] = valor
# 
#     coluna = 'Id Ferramenta'
#     valor = telaEmprestimo.entIDferramenta.get()
#     tamanhoCampo_1 = 30
#     df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo_1]
# 
#     coluna = 'CPF Técnico'
#     valor = telaEmprestimo.entCPFemprestimo.get()
#     tamanhoCampo_1 = 30
#     df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo_1]
# 
#     coluna = 'Nome'
#     valor = telaEmprestimo.entNomeEmprestimo.get()
#     tamanhoCampo_1 = 15
#     df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo_1]
# 
#     coluna = 'Data Retirada'
#     valor= telaEmprestimo.entDataRetirada.get()
#     tamanhoCampo_1 = 25
#     df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo_1]
# 
#     coluna = 'Data Devolução'
#     valor = telaEmprestimo.entDataDevolucao.get()
#     tamanhoCampo_1 = 25
#     df.loc[int(chave)-1, coluna] = valor[0:tamanhoCampo_1]
# 
#     df['ID'] = df['ID'].astype(int)
#     df.to_csv(arquivoReservas, index=False)
# 
# def formatarCPFReserva(event=None):
#     text = telaEmprestimo.entCPFemprestimo.get().replace(".", "").replace("-", "")[:11]
#     new_text = ""
# 
#     if event.keysym.lower() == "backspace":
#         return
# 
#     for index in range(len(text)):
# 
#         if not text[index] in "0123456789":
#             continue
#         if index in [2, 5]:
#             new_text += text[index] + "."
#         elif index == 8:
#             new_text += text[index] + "-"
#         else:
#             new_text += text[index]
# 
#     telaEmprestimo.entCPFemprestimo.delete(0, "end")
#     telaEmprestimo.entCPFemprestimo.insert(0, new_text)
# 
# menuTelaEmprestimoCadastro = Menubutton(telaEmprestimo, text='Cadastro', activebackground='gray')
# menuTelaEmprestimoCadastro.grid(row=0, column=0)
# menuTelaEmprestimoCadastro.menu = Menu(menuTelaEmprestimoCadastro, tearoff=0)
# menuTelaEmprestimoCadastro["menu"] = menuTelaEmprestimoCadastro.menu
# menuTelaEmprestimoCadastro.menu.add_command(label='Principal', command=lambda: show_frame(telaPrincipal))
# menuTelaEmprestimoCadastro.menu.add_command(label='Ferramentas', command=lambda: show_frame(telaFerramenta))
# menuTelaEmprestimoCadastro.menu.add_command(label='Técnicos Responsáveis', command=lambda: show_frame(telaTecnico))
# 
# menuTelaEmprestimoMovimentacao = Menubutton(telaEmprestimo, text='Movimentação', activebackground='gray')
# menuTelaEmprestimoMovimentacao.grid(row=0, column=1)
# menuTelaEmprestimoMovimentacao.menu = Menu(menuTelaEmprestimoMovimentacao, tearoff=0)
# menuTelaEmprestimoMovimentacao["menu"] = menuTelaEmprestimoMovimentacao.menu
# menuTelaEmprestimoMovimentacao.menu.add_command(label='Empréstimo de Ferramentas', command=lambda: show_frame(telaEmprestimo))
# 
# menuTelaEmprestimoRelatorios = Menubutton(telaEmprestimo, text='Relatórios', activebackground='gray')
# menuTelaEmprestimoRelatorios.grid(row=0, column=2)
# menuTelaEmprestimoRelatorios.menu = Menu(menuTelaEmprestimoRelatorios, tearoff=0)
# menuTelaEmprestimoRelatorios["menu"] = menuTelaEmprestimoRelatorios.menu
# menuTelaEmprestimoRelatorios.menu.add_command(label='Empréstimo de Ferramentas', command=lambda: show_frame(telaRelatorioEmprestimo))
# 
# menuTelaPrincipalAjuda = Menubutton(telaEmprestimo, text='Ajuda', activebackground='gray')
# menuTelaPrincipalAjuda.grid(row=0, column=3)
# menuTelaPrincipalAjuda.menu = Menu(menuTelaPrincipalAjuda, tearoff=0)
# menuTelaPrincipalAjuda["menu"] = menuTelaPrincipalAjuda.menu
# menuTelaPrincipalAjuda.menu.add_command(label='Sobre', command=lambda: show_frame(telaSobre))
# 
# 
# telaEmprestimo.btnReservar = Button(telaEmprestimo)
# telaEmprestimo.btnReservar.place(relx=0.420, rely=0.280, height=30, width=70)
# telaEmprestimo.btnReservar.configure(activebackground="beige")
# telaEmprestimo.btnReservar.configure(activeforeground="black")
# telaEmprestimo.btnReservar.configure(background="#d9d9d9")
# telaEmprestimo.btnReservar.configure(command=lambda: btnreservarFerramenta())
# telaEmprestimo.btnReservar.configure(compound='left')
# telaEmprestimo.btnReservar.configure(disabledforeground="#a3a3a3")
# telaEmprestimo.btnReservar.configure(foreground="#000000")
# telaEmprestimo.btnReservar.configure(highlightbackground="#d9d9d9")
# telaEmprestimo.btnReservar.configure(highlightcolor="black")
# telaEmprestimo.btnReservar.configure(pady="0")
# telaEmprestimo.btnReservar.configure(text='''Reservar''')
# 
# 
# telaEmprestimo.btnConfirmar = Button(telaEmprestimo)
# telaEmprestimo.btnConfirmar.place(relx=0.47, rely=0.280, height=30, width=70)
# telaEmprestimo.btnConfirmar.configure(activebackground="beige")
# telaEmprestimo.btnConfirmar.configure(activeforeground="black")
# telaEmprestimo.btnConfirmar.configure(background="#d9d9d9")
# telaEmprestimo.btnConfirmar.configure(command=lambda: gravarReserva())
# telaEmprestimo.btnConfirmar.configure(compound='left')
# telaEmprestimo.btnConfirmar.configure(disabledforeground="#a3a3a3")
# telaEmprestimo.btnConfirmar.configure(foreground="#000000")
# telaEmprestimo.btnConfirmar.configure(highlightbackground="#d9d9d9")
# telaEmprestimo.btnConfirmar.configure(highlightcolor="black")
# telaEmprestimo.btnConfirmar.configure(pady="0")
# telaEmprestimo.btnConfirmar.configure(text='''Confirmar''')
# telaEmprestimo.btnConfirmar.configure(state="disabled")
# 
# telaEmprestimo.btnCancelar = Button(telaEmprestimo)
# telaEmprestimo.btnCancelar.place(relx=0.52, rely=0.280, height=30, width=70)
# telaEmprestimo.btnCancelar.configure(activebackground="beige")
# telaEmprestimo.btnCancelar.configure(activeforeground="black")
# telaEmprestimo.btnCancelar.configure(background="#d9d9d9")
# telaEmprestimo.btnCancelar.configure(command=lambda: cancelarReserva())
# telaEmprestimo.btnCancelar.configure(compound='left')
# telaEmprestimo.btnCancelar.configure(disabledforeground="#a3a3a3")
# telaEmprestimo.btnCancelar.configure(foreground="#000000")
# telaEmprestimo.btnCancelar.configure(highlightbackground="#d9d9d9")
# telaEmprestimo.btnCancelar.configure(highlightcolor="black")
# telaEmprestimo.btnCancelar.configure(pady="0")
# telaEmprestimo.btnCancelar.configure(text='''Cancelar''')
# telaEmprestimo.btnCancelar.configure(state="disabled")
# 
# 
# telaEmprestimo.Label1 = Label(telaEmprestimo)
# telaEmprestimo.Label1.place(relx=0.0, rely=0.021, height=63, width=1920)
# telaEmprestimo.Label1.configure(background="#949494")
# telaEmprestimo.Label1.configure(anchor='center')
# telaEmprestimo.Label1.configure(compound='left')
# telaEmprestimo.Label1.configure(disabledforeground="#a3a3a3")
# telaEmprestimo.Label1.configure(font="-family {Segoe UI} -size 14 -weight bold")
# telaEmprestimo.Label1.configure(foreground="#000000")
# telaEmprestimo.Label1.configure(highlightcolor="#ffffff")
# telaEmprestimo.Label1.configure(text='''Tela de Emprestimo de Ferramenta''')
# 
# telaEmprestimo.lblIDferramenta = Label(telaEmprestimo)
# telaEmprestimo.lblIDferramenta.place(relx=0.354, rely=0.355)
# telaEmprestimo.lblIDferramenta.configure(anchor='w')
# telaEmprestimo.lblIDferramenta.configure(compound='left')
# telaEmprestimo.lblIDferramenta.configure(disabledforeground="#a3a3a3")
# telaEmprestimo.lblIDferramenta.configure(foreground="#000000")
# telaEmprestimo.lblIDferramenta.configure(text='''ID da ferramenta:''')
# telaEmprestimo.entIDferramenta = Entry(telaEmprestimo)
# telaEmprestimo.entIDferramenta.place(relx=0.408, rely=0.355, height=20, relwidth=0.163)
# telaEmprestimo.entIDferramenta.configure(background="white")
# telaEmprestimo.entIDferramenta.configure(disabledforeground="#a3a3a3")
# telaEmprestimo.entIDferramenta.configure(font="TkFixedFont")
# telaEmprestimo.entIDferramenta.configure(foreground="#000000")
# telaEmprestimo.entIDferramenta.configure(insertbackground="black")
# telaEmprestimo.entIDferramenta.configure(state="disabled")
# 
# telaEmprestimo.lblCPFemprestimo = Label(telaEmprestimo)
# telaEmprestimo.lblCPFemprestimo.place(relx=0.354, rely=0.395)
# telaEmprestimo.lblCPFemprestimo.configure(anchor='w')
# telaEmprestimo.lblCPFemprestimo.configure(compound='left')
# telaEmprestimo.lblCPFemprestimo.configure(disabledforeground="#a3a3a3")
# telaEmprestimo.lblCPFemprestimo.configure(foreground="#000000")
# telaEmprestimo.lblCPFemprestimo.configure(text='''CPF do Técnico:''')
# telaEmprestimo.entCPFemprestimo = Entry(telaEmprestimo)
# telaEmprestimo.entCPFemprestimo.place(relx=0.408, rely=0.395, height=20, relwidth=0.163)
# telaEmprestimo.entCPFemprestimo.configure(background="white")
# telaEmprestimo.entCPFemprestimo.configure(disabledforeground="#a3a3a3")
# telaEmprestimo.entCPFemprestimo.configure(font="TkFixedFont")
# telaEmprestimo.entCPFemprestimo.configure(foreground="#000000")
# telaEmprestimo.entCPFemprestimo.configure(insertbackground="black")
# telaEmprestimo.entCPFemprestimo.configure(state="disabled")
# telaEmprestimo.entCPFemprestimo.bind("<FocusOut>",inserirnomeTecnico)
# telaEmprestimo.entCPFemprestimo.bind("<KeyRelease>", formatarCPFReserva)
# 
# 
# telaEmprestimo.lblNomeEmprestimo = Label(telaEmprestimo)
# telaEmprestimo.lblNomeEmprestimo.place(relx=0.354, rely=0.435, height=21, width=60)
# telaEmprestimo.lblNomeEmprestimo.configure(anchor='w')
# telaEmprestimo.lblNomeEmprestimo.configure(compound='left')
# telaEmprestimo.lblNomeEmprestimo.configure(disabledforeground="#a3a3a3")
# telaEmprestimo.lblNomeEmprestimo.configure(foreground="#000000")
# telaEmprestimo.lblNomeEmprestimo.configure(text='''Nome:''')
# telaEmprestimo.entNomeEmprestimo = Entry(telaEmprestimo)
# telaEmprestimo.entNomeEmprestimo.place(relx=0.408, rely=0.435, height=20, relwidth=0.163)
# telaEmprestimo.entNomeEmprestimo.configure(background="white")
# telaEmprestimo.entNomeEmprestimo.configure(disabledforeground="#a3a3a3")
# telaEmprestimo.entNomeEmprestimo.configure(font="TkFixedFont")
# telaEmprestimo.entNomeEmprestimo.configure(foreground="#000000")
# telaEmprestimo.entNomeEmprestimo.configure(insertbackground="black")
# telaEmprestimo.entNomeEmprestimo.configure(state="disabled")
# 
# 
# 
# telaEmprestimo.btnDataRetirada = Button(telaEmprestimo)
# telaEmprestimo.btnDataRetirada.place(relx=0.421, rely=0.475, height=30, width=70)
# telaEmprestimo.btnDataRetirada.configure(activebackground="beige")
# telaEmprestimo.btnDataRetirada.configure(activeforeground="black")
# telaEmprestimo.btnDataRetirada.configure(background="#d9d9d9")
# telaEmprestimo.btnDataRetirada.configure(command=lambda: calendarioabrirRetirada())
# telaEmprestimo.btnDataRetirada.configure(compound='left')
# telaEmprestimo.btnDataRetirada.configure(disabledforeground="#a3a3a3")
# telaEmprestimo.btnDataRetirada.configure(foreground="#000000")
# telaEmprestimo.btnDataRetirada.configure(highlightbackground="#d9d9d9")
# telaEmprestimo.btnDataRetirada.configure(highlightcolor="black")
# telaEmprestimo.btnDataRetirada.configure(pady="0")
# telaEmprestimo.btnDataRetirada.configure(text='''Retirada''')
# telaEmprestimo.btnDataRetirada.configure(state="disabled")
# 
# telaEmprestimo.entDataRetirada = Entry(telaEmprestimo)
# telaEmprestimo.entDataRetirada.place(relx=0.408, rely=0.515, height=25, width=120)
# telaEmprestimo.entDataRetirada.configure(background="white")
# telaEmprestimo.entDataRetirada.configure(disabledforeground="#a3a3a3")
# telaEmprestimo.entDataRetirada.configure(font=("Bahnschrift",'11'))
# telaEmprestimo.entDataRetirada.configure(foreground="#000000")
# telaEmprestimo.entDataRetirada.configure(insertbackground="black")
# telaEmprestimo.entDataRetirada.configure(state="disabled")
# 
# 
# telaEmprestimo.btnDataDevolucao = Button(telaEmprestimo)
# telaEmprestimo.btnDataDevolucao.place(relx=0.520, rely=0.475, height=30, width=70)
# telaEmprestimo.btnDataDevolucao.configure(activebackground="beige")
# telaEmprestimo.btnDataDevolucao.configure(activeforeground="black")
# telaEmprestimo.btnDataDevolucao.configure(background="#d9d9d9")
# telaEmprestimo.btnDataDevolucao.configure(command=lambda: calendarioabrirDevolucao())
# telaEmprestimo.btnDataDevolucao.configure(compound='left')
# telaEmprestimo.btnDataDevolucao.configure(disabledforeground="#a3a3a3")
# telaEmprestimo.btnDataDevolucao.configure(foreground="#000000")
# telaEmprestimo.btnDataDevolucao.configure(highlightbackground="#d9d9d9")
# telaEmprestimo.btnDataDevolucao.configure(highlightcolor="black")
# telaEmprestimo.btnDataDevolucao.configure(pady="0")
# telaEmprestimo.btnDataDevolucao.configure(text='''Devolução''')
# telaEmprestimo.btnDataDevolucao.configure(state="disabled")
# 
# telaEmprestimo.entDataDevolucao = Entry(telaEmprestimo)
# telaEmprestimo.entDataDevolucao.place(relx=0.507, rely=0.515, height=25, width=120)
# telaEmprestimo.entDataDevolucao.configure(background="white")
# telaEmprestimo.entDataDevolucao.configure(disabledforeground="#a3a3a3")
# telaEmprestimo.entDataDevolucao.configure(font=("Bahnschrift",'11'))
# telaEmprestimo.entDataDevolucao.configure(foreground="#000000")
# telaEmprestimo.entDataDevolucao.configure(insertbackground="black")
# telaEmprestimo.entDataDevolucao.configure(state="disabled")
# 
# 
# ======== Fim Tela Emprestimo Backup ==========

# ======== Inicio Tela Emprestimo ==========

menuTelaEmprestimoCadastro = Menubutton(telaEmprestimo, text='Cadastro', activebackground='gray')
menuTelaEmprestimoCadastro.grid(row=0, column=0)
menuTelaEmprestimoCadastro.menu = Menu(menuTelaEmprestimoCadastro, tearoff=0)
menuTelaEmprestimoCadastro["menu"] = menuTelaEmprestimoCadastro.menu
menuTelaEmprestimoCadastro.menu.add_command(label='Principal', command=lambda: show_frame(telaPrincipal))
menuTelaEmprestimoCadastro.menu.add_command(label='Ferramentas', command=lambda: show_frame(telaFerramenta))
menuTelaEmprestimoCadastro.menu.add_command(label='Técnicos Responsáveis', command=lambda: show_frame(telaTecnico))

menuTelaEmprestimoMovimentacao = Menubutton(telaEmprestimo, text='Movimentação', activebackground='gray')
menuTelaEmprestimoMovimentacao.grid(row=0, column=1)
menuTelaEmprestimoMovimentacao.menu = Menu(menuTelaEmprestimoMovimentacao, tearoff=0)
menuTelaEmprestimoMovimentacao["menu"] = menuTelaEmprestimoMovimentacao.menu
menuTelaEmprestimoMovimentacao.menu.add_command(label='Empréstimo de Ferramentas', command=lambda: show_frame(telaEmprestimo))

menuTelaEmprestimoRelatorios = Menubutton(telaEmprestimo, text='Relatórios', activebackground='gray')
menuTelaEmprestimoRelatorios.grid(row=0, column=2)
menuTelaEmprestimoRelatorios.menu = Menu(menuTelaEmprestimoRelatorios, tearoff=0)
menuTelaEmprestimoRelatorios["menu"] = menuTelaEmprestimoRelatorios.menu
menuTelaEmprestimoRelatorios.menu.add_command(label='Empréstimo de Ferramentas', command=lambda: show_frame(telaRelatorioEmprestimo))

menuTelaEmprestimoAjuda = Menubutton(telaEmprestimo, text='Ajuda', activebackground='gray')
menuTelaEmprestimoAjuda.grid(row=0, column=3)
menuTelaEmprestimoAjuda.menu = Menu(menuTelaEmprestimoAjuda, tearoff=0)
menuTelaEmprestimoAjuda["menu"] = menuTelaEmprestimoAjuda.menu
menuTelaEmprestimoAjuda.menu.add_command(label='Sobre', command=lambda: show_frame(telaSobre))

telaEmprestimo.Label1 = Label(telaEmprestimo)
telaEmprestimo.Label1.place(relx=0.0, rely=0.021, height=63, width=1920)
telaEmprestimo.Label1.configure(background="#949494")
telaEmprestimo.Label1.configure(anchor='center')
telaEmprestimo.Label1.configure(compound='left')
telaEmprestimo.Label1.configure(disabledforeground="#a3a3a3")
telaEmprestimo.Label1.configure(font="-family {Segoe UI} -size 14 -weight bold")
telaEmprestimo.Label1.configure(foreground="#000000")
telaEmprestimo.Label1.configure(highlightcolor="#ffffff")
telaEmprestimo.Label1.configure(text='''Empréstimo de Ferramentas''')

colunasEmprestimo = ('ID', 'Ferramenta', 'Tecnico', 'DataRetirada', 'DataPrevisaoDevolucao','DataDevolucao')
treeEmprestimo = ttk.Treeview(telaEmprestimo, columns=colunasEmprestimo, show='headings')
scrollbar = ttk.Scrollbar(telaEmprestimo,
                          orient="vertical",
                          command=treeEmprestimo.yview)
scrollbar.place(relx=0.99, rely=0.091, height=280, width=20)
treeEmprestimo.configure(xscrollcommand=scrollbar.set)

# define headings
treeEmprestimo.heading("ID", text="ID", anchor=W)
treeEmprestimo.heading("Ferramenta", text="Ferramenta", anchor=W)
treeEmprestimo.heading("Tecnico", text="Tecnico", anchor=W)
treeEmprestimo.heading("DataRetirada", text="Data Retirada", anchor=W)
treeEmprestimo.heading("DataPrevisaoDevolucao", text="Data Previsão Devolução", anchor=W)
treeEmprestimo.heading("DataDevolucao", text="Data Devolução", anchor=W)

df = pd.read_csv(arquivoReservas, na_filter=False)
for row, series in df.iterrows():
    treeEmprestimo.insert(parent='', index='end', iid=row, text='', values=(
        series['ID'], series['Ferramenta'], series['Tecnico'], series['DataRetirada'], series['DataPrevisaoDevolucao'], series['DataDevolucao']))

def selecionaEmprestimo(event):
    for selected_item in treeEmprestimo.selection():
        item = treeEmprestimo.item(selected_item)
        record = item['values']


treeEmprestimo.bind('<<TreeviewSelect>>', selecionaEmprestimo)
treeEmprestimo.place(relx=0.0, rely=0.091, height=280, width=1920)

telaEmprestimo.btnReservar = Button(telaEmprestimo)
telaEmprestimo.btnReservar.place(relx=0.37, rely=0.380, height=30, width=70)
telaEmprestimo.btnReservar.configure(activebackground="beige")
telaEmprestimo.btnReservar.configure(activeforeground="black")
telaEmprestimo.btnReservar.configure(background="#d9d9d9")
telaEmprestimo.btnReservar.configure(command=lambda: inserirEmprestimo())
telaEmprestimo.btnReservar.configure(compound='left')
telaEmprestimo.btnReservar.configure(disabledforeground="#a3a3a3")
telaEmprestimo.btnReservar.configure(foreground="#000000")
telaEmprestimo.btnReservar.configure(highlightbackground="#d9d9d9")
telaEmprestimo.btnReservar.configure(highlightcolor="black")
telaEmprestimo.btnReservar.configure(pady="0")
telaEmprestimo.btnReservar.configure(text='''Reservar''')

telaEmprestimo.btnDevolver = Button(telaEmprestimo)
telaEmprestimo.btnDevolver.place(relx=0.42, rely=0.380, height=30, width=70)
telaEmprestimo.btnDevolver.configure(activebackground="beige")
telaEmprestimo.btnDevolver.configure(activeforeground="black")
telaEmprestimo.btnDevolver.configure(background="#d9d9d9")
telaEmprestimo.btnDevolver.configure(command=lambda: editarEmprestimo())
telaEmprestimo.btnDevolver.configure(compound='left')
telaEmprestimo.btnDevolver.configure(disabledforeground="#a3a3a3")
telaEmprestimo.btnDevolver.configure(foreground="#000000")
telaEmprestimo.btnDevolver.configure(highlightbackground="#d9d9d9")
telaEmprestimo.btnDevolver.configure(highlightcolor="black")
telaEmprestimo.btnDevolver.configure(pady="0")
telaEmprestimo.btnDevolver.configure(text='''Devolver''')

telaEmprestimo.btnDeletar = Button(telaEmprestimo)
telaEmprestimo.btnDeletar.place(relx=0.47, rely=0.380, height=30, width=70)
telaEmprestimo.btnDeletar.configure(activebackground="beige")
telaEmprestimo.btnDeletar.configure(activeforeground="black")
telaEmprestimo.btnDeletar.configure(background="#d9d9d9")
telaEmprestimo.btnDeletar.configure(command=lambda: deletarEmprestimo())
telaEmprestimo.btnDeletar.configure(compound='left')
telaEmprestimo.btnDeletar.configure(disabledforeground="#a3a3a3")
telaEmprestimo.btnDeletar.configure(foreground="#000000")
telaEmprestimo.btnDeletar.configure(highlightbackground="#d9d9d9")
telaEmprestimo.btnDeletar.configure(highlightcolor="black")
telaEmprestimo.btnDeletar.configure(pady="0")
telaEmprestimo.btnDeletar.configure(text='''Deletar''')

telaEmprestimo.btnGravar = Button(telaEmprestimo)
telaEmprestimo.btnGravar.place(relx=0.52, rely=0.380, height=30, width=70)
telaEmprestimo.btnGravar.configure(activebackground="beige")
telaEmprestimo.btnGravar.configure(activeforeground="black")
telaEmprestimo.btnGravar.configure(background="#d9d9d9")
telaEmprestimo.btnGravar.configure(command=lambda: gravarEmprestimo())
telaEmprestimo.btnGravar.configure(compound='left')
telaEmprestimo.btnGravar.configure(disabledforeground="#a3a3a3")
telaEmprestimo.btnGravar.configure(foreground="#000000")
telaEmprestimo.btnGravar.configure(highlightbackground="#d9d9d9")
telaEmprestimo.btnGravar.configure(highlightcolor="black")
telaEmprestimo.btnGravar.configure(pady="0")
telaEmprestimo.btnGravar.configure(text='''Gravar''')
telaEmprestimo.btnGravar.configure(state="disabled")

telaEmprestimo.btnCancelar = Button(telaEmprestimo)
telaEmprestimo.btnCancelar.place(relx=0.57, rely=0.380, height=30, width=70)
telaEmprestimo.btnCancelar.configure(activebackground="beige")
telaEmprestimo.btnCancelar.configure(activeforeground="black")
telaEmprestimo.btnCancelar.configure(background="#d9d9d9")
telaEmprestimo.btnCancelar.configure(command=lambda: cancelarEmprestimo())
telaEmprestimo.btnCancelar.configure(compound='left')
telaEmprestimo.btnCancelar.configure(disabledforeground="#a3a3a3")
telaEmprestimo.btnCancelar.configure(foreground="#000000")
telaEmprestimo.btnCancelar.configure(highlightbackground="#d9d9d9")
telaEmprestimo.btnCancelar.configure(highlightcolor="black")
telaEmprestimo.btnCancelar.configure(pady="0")
telaEmprestimo.btnCancelar.configure(text='''Cancelar''')
telaEmprestimo.btnCancelar.configure(state="disabled")

telaEmprestimo.lblID = Label(telaEmprestimo)
telaEmprestimo.lblID.place(relx=0.328, rely=0.435, height=21, width=60)
telaEmprestimo.lblID.configure(anchor='w')
telaEmprestimo.lblID.configure(compound='left')
telaEmprestimo.lblID.configure(disabledforeground="#a3a3a3")
telaEmprestimo.lblID.configure(foreground="#000000")
telaEmprestimo.lblID.configure(text='''ID:''')
telaEmprestimo.entID = Entry(telaEmprestimo)
telaEmprestimo.entID.place(relx=0.382, rely=0.435, height=20, relwidth=0.053)
telaEmprestimo.entID.configure(background="white")
telaEmprestimo.entID.configure(disabledforeground="#a3a3a3")
telaEmprestimo.entID.configure(font="TkFixedFont")
telaEmprestimo.entID.configure(foreground="#000000")
telaEmprestimo.entID.configure(insertbackground="black")
telaEmprestimo.entID.configure(state="disabled")

df = pd.read_csv('tecnicos.csv', na_filter=False)
tecnicos = []
for row, series in df.iterrows():
    tecnicos.append(series['Nome'])

telaEmprestimo.lblTecnico = Label(telaEmprestimo)
telaEmprestimo.lblTecnico.place(relx=0.328, rely=0.475, height=21, width=60)
telaEmprestimo.lblTecnico.configure(anchor='w')
telaEmprestimo.lblTecnico.configure(compound='left')
telaEmprestimo.lblTecnico.configure(disabledforeground="#a3a3a3")
telaEmprestimo.lblTecnico.configure(foreground="#000000")
telaEmprestimo.lblTecnico.configure(text='''Técnico:''')
telaEmprestimo.comboTecnico = ttk.Combobox(telaEmprestimo, width=15)
telaEmprestimo.comboTecnico.place(relx=0.382, rely=0.475, height=20, relwidth=0.180)
telaEmprestimo.comboTecnico.configure(background="white")
telaEmprestimo.comboTecnico.configure(font="TkFixedFont")
telaEmprestimo.comboTecnico.configure(foreground="#000000")
telaEmprestimo.comboTecnico.configure(state="disabled")
telaEmprestimo.comboTecnico['values'] = (tecnicos)

df = pd.read_csv('ferramentas.csv', na_filter=False)
ferramentas = []
for row, series in df.iterrows():
    ferramentas.append(series['Descricao'])

telaEmprestimo.lblcomboFerramenta = Label(telaEmprestimo)
telaEmprestimo.lblcomboFerramenta.place(relx=0.328, rely=0.515, height=21, width=80)
telaEmprestimo.lblcomboFerramenta.configure(anchor='w')
telaEmprestimo.lblcomboFerramenta.configure(compound='left')
telaEmprestimo.lblcomboFerramenta.configure(disabledforeground="#a3a3a3")
telaEmprestimo.lblcomboFerramenta.configure(foreground="#000000")
telaEmprestimo.lblcomboFerramenta.configure(text='''Ferramenta:''')
telaEmprestimo.comboFerramenta = ttk.Combobox(telaEmprestimo, width=15)
telaEmprestimo.comboFerramenta.place(relx=0.382, rely=0.515, height=20, relwidth=0.180)
telaEmprestimo.comboFerramenta.configure(background="white")
telaEmprestimo.comboFerramenta.configure(font="TkFixedFont")
telaEmprestimo.comboFerramenta.configure(foreground="#000000")
telaEmprestimo.comboFerramenta.configure(state="disabled")
telaEmprestimo.comboFerramenta['values'] = (ferramentas)
def calendarioabrirRetirada():
    global calendarioRetirada, btnInserirRetirada
    calendarioRetirada = Calendar(telaEmprestimo,fg='gray75',bg='blue',font='Bahnschrift',locate='pt_br', date_pattern='dd/MM/yyyy')
    calendarioRetirada.place(relx=0.408, rely=0.475)

    telaEmprestimo.btnInserirRetirada = Button(telaEmprestimo)
    telaEmprestimo.btnInserirRetirada.place(relx=0.5335, rely=0.699, height=30, width=70)
    telaEmprestimo.btnInserirRetirada.configure(activebackground="beige")
    telaEmprestimo.btnInserirRetirada.configure(activeforeground="black")
    telaEmprestimo.btnInserirRetirada.configure(background="#d9d9d9")
    telaEmprestimo.btnInserirRetirada.configure(command=lambda: FecharcalendarioRetirada())
    telaEmprestimo.btnInserirRetirada.configure(compound='left')
    telaEmprestimo.btnInserirRetirada.configure(disabledforeground="#a3a3a3")
    telaEmprestimo.btnInserirRetirada.configure(foreground="#000000")
    telaEmprestimo.btnInserirRetirada.configure(highlightbackground="#d9d9d9")
    telaEmprestimo.btnInserirRetirada.configure(highlightcolor="black")
    telaEmprestimo.btnInserirRetirada.configure(pady="0")
    telaEmprestimo.btnInserirRetirada.configure(text='''Inserir''')

    telaEmprestimo.lblHorarioRetirada = Label(telaEmprestimo)
    telaEmprestimo.lblHorarioRetirada.place(relx=0.408, rely=0.700)
    telaEmprestimo.lblHorarioRetirada.configure(anchor='w')
    telaEmprestimo.lblHorarioRetirada.configure(compound='left')
    telaEmprestimo.lblHorarioRetirada.configure(disabledforeground="#a3a3a3")
    telaEmprestimo.lblHorarioRetirada.configure(foreground="#000000")
    telaEmprestimo.lblHorarioRetirada.configure(text='''HORÁRIO:''')
    telaEmprestimo.lblHorarioRetirada.configure(font=("Bahnschrift",'13'))

    telaEmprestimo.entHorarioRetirada = Entry(telaEmprestimo)
    telaEmprestimo.entHorarioRetirada.place(relx=0.455, rely=0.702, height=25, width=78)
    telaEmprestimo.entHorarioRetirada.configure(background="white")
    telaEmprestimo.entHorarioRetirada.configure(disabledforeground="#a3a3a3")
    telaEmprestimo.entHorarioRetirada.configure(font=("Bahnschrift",'11'))
    telaEmprestimo.entHorarioRetirada.configure(foreground="#000000")
    telaEmprestimo.entHorarioRetirada.configure(insertbackground="black")
    telaEmprestimo.entHorarioRetirada.bind('<KeyRelease>',FormatarHoraRetirada)

def FecharcalendarioRetirada():
    horario_formatar = telaEmprestimo.entHorarioRetirada.get().split(':')

    if telaEmprestimo.entHorarioRetirada.get()=='' or len(telaEmprestimo.entHorarioRetirada.get())!=5 or int(horario_formatar[0])>=24 or int(horario_formatar[1])>=60:
        messagebox.showerror('','Horário inválido')
    else:
        telaEmprestimo.entDataRetirada.configure(state="normal")
        data_da_retirada = calendarioRetirada.get_date()
        hora_retirada = telaEmprestimo.entHorarioRetirada.get()
        telaEmprestimo.entDataRetirada.delete(0,'end')
        telaEmprestimo.entDataRetirada.insert(0,data_da_retirada)
        telaEmprestimo.entDataRetirada.insert(11,' ')
        telaEmprestimo.entDataRetirada.insert(12,hora_retirada)

        telaEmprestimo.btnInserirRetirada.place(relx=1.800, rely=1.900, height=30, width=70)
        calendarioRetirada.place(relx=1.800, rely=1.800)
        telaEmprestimo.lblHorarioRetirada.place(relx=1.800, rely=1.800)
        telaEmprestimo.entHorarioRetirada.place(relx=1.800, rely=1.800, height=25, width=78)
        telaEmprestimo.entDataRetirada.configure(state="disabled")

def calendarioabrirDevolucao():
    global calendarioDevolucao
    calendarioDevolucao = Calendar(telaEmprestimo,fg='gray75',bg='blue',font='Bahnschrift',locate='pt_br', date_pattern='dd/MM/yyyy')
    calendarioDevolucao.place(relx=0.505, rely=0.475)


    telaEmprestimo.btnInserirDevolucao = Button(telaEmprestimo)
    telaEmprestimo.btnInserirDevolucao.place(relx=0.6305, rely=0.700, height=30, width=70)
    telaEmprestimo.btnInserirDevolucao.configure(activebackground="beige")
    telaEmprestimo.btnInserirDevolucao.configure(activeforeground="black")
    telaEmprestimo.btnInserirDevolucao.configure(background="#d9d9d9")
    telaEmprestimo.btnInserirDevolucao.configure(command=lambda: FecharcalendarioDevolucao())
    telaEmprestimo.btnInserirDevolucao.configure(compound='left')
    telaEmprestimo.btnInserirDevolucao.configure(disabledforeground="#a3a3a3")
    telaEmprestimo.btnInserirDevolucao.configure(foreground="#000000")
    telaEmprestimo.btnInserirDevolucao.configure(highlightbackground="#d9d9d9")
    telaEmprestimo.btnInserirDevolucao.configure(highlightcolor="black")
    telaEmprestimo.btnInserirDevolucao.configure(pady="0")
    telaEmprestimo.btnInserirDevolucao.configure(text='''Inserir''')

    telaEmprestimo.lblHorarioDevolucao = Label(telaEmprestimo)
    telaEmprestimo.lblHorarioDevolucao.place(relx=0.505, rely=0.700)
    telaEmprestimo.lblHorarioDevolucao.configure(anchor='w')
    telaEmprestimo.lblHorarioDevolucao.configure(compound='left')
    telaEmprestimo.lblHorarioDevolucao.configure(disabledforeground="#a3a3a3")
    telaEmprestimo.lblHorarioDevolucao.configure(foreground="#000000")
    telaEmprestimo.lblHorarioDevolucao.configure(text='''HORÁRIO:''')
    telaEmprestimo.lblHorarioDevolucao.configure(font=("Bahnschrift",'13'))

    telaEmprestimo.entHorarioDevolucao = Entry(telaEmprestimo)
    telaEmprestimo.entHorarioDevolucao.place(relx=0.552, rely=0.702, height=25, width=78)
    telaEmprestimo.entHorarioDevolucao.configure(background="white")
    telaEmprestimo.entHorarioDevolucao.configure(disabledforeground="#a3a3a3")
    telaEmprestimo.entHorarioDevolucao.configure(font=("Bahnschrift",'11'))
    telaEmprestimo.entHorarioDevolucao.configure(foreground="#000000")
    telaEmprestimo.entHorarioDevolucao.configure(insertbackground="black")
    telaEmprestimo.entHorarioDevolucao.bind('<KeyRelease>',FormatarHoraDevolucao)

def FecharcalendarioDevolucao():
    horario_formatar = telaEmprestimo.entHorarioDevolucao.get().split(':')

    if telaEmprestimo.entHorarioDevolucao.get()=='' or len(telaEmprestimo.entHorarioDevolucao.get())!=5 or int(horario_formatar[0])>=24 or int(horario_formatar[1])>=60:
        messagebox.showerror('','Horário inválido')
    else:
        telaEmprestimo.entDataDevolucao.configure(state="normal")
        data_da_devolucao = calendarioDevolucao.get_date()
        hora_devolucao = telaEmprestimo.entHorarioDevolucao.get()
        telaEmprestimo.entDataDevolucao.delete(0,'end')
        telaEmprestimo.entDataDevolucao.insert(0,data_da_devolucao)
        telaEmprestimo.entDataDevolucao.insert(11,' ')
        telaEmprestimo.entDataDevolucao.insert(12,hora_devolucao)

        calendarioDevolucao.place(relx=1.800, rely=1.800)
        telaEmprestimo.btnInserirDevolucao.place(relx=1.800, rely=1.800, height=30, width=70)
        telaEmprestimo.lblHorarioDevolucao.place(relx=1.800, rely=1.800)
        telaEmprestimo.entHorarioDevolucao.place(relx=1.800, rely=1.800, height=25, width=78)
        telaEmprestimo.entDataDevolucao.configure(state="disabled")


def calendarioabrirPrevisaoDevolucao():
    global calendarioPrevisaoDevolucao
    calendarioPrevisaoDevolucao = Calendar(telaEmprestimo,fg='gray75',bg='blue',font='Bahnschrift',locate='pt_br', date_pattern='dd/MM/yyyy')
    calendarioPrevisaoDevolucao.place(relx=0.505, rely=0.475)


    telaEmprestimo.btnInserirPrevisaoDevolucao = Button(telaEmprestimo)
    telaEmprestimo.btnInserirPrevisaoDevolucao.place(relx=0.6305, rely=0.700, height=30, width=70)
    telaEmprestimo.btnInserirPrevisaoDevolucao.configure(activebackground="beige")
    telaEmprestimo.btnInserirPrevisaoDevolucao.configure(activeforeground="black")
    telaEmprestimo.btnInserirPrevisaoDevolucao.configure(background="#d9d9d9")
    telaEmprestimo.btnInserirPrevisaoDevolucao.configure(command=lambda: FecharcalendarioPrevisaoDevolucao())
    telaEmprestimo.btnInserirPrevisaoDevolucao.configure(compound='left')
    telaEmprestimo.btnInserirPrevisaoDevolucao.configure(disabledforeground="#a3a3a3")
    telaEmprestimo.btnInserirPrevisaoDevolucao.configure(foreground="#000000")
    telaEmprestimo.btnInserirPrevisaoDevolucao.configure(highlightbackground="#d9d9d9")
    telaEmprestimo.btnInserirPrevisaoDevolucao.configure(highlightcolor="black")
    telaEmprestimo.btnInserirPrevisaoDevolucao.configure(pady="0")
    telaEmprestimo.btnInserirPrevisaoDevolucao.configure(text='''Inserir''')

    telaEmprestimo.lblHorarioPrevisaoDevolucao = Label(telaEmprestimo)
    telaEmprestimo.lblHorarioPrevisaoDevolucao.place(relx=0.505, rely=0.700)
    telaEmprestimo.lblHorarioPrevisaoDevolucao.configure(anchor='w')
    telaEmprestimo.lblHorarioPrevisaoDevolucao.configure(compound='left')
    telaEmprestimo.lblHorarioPrevisaoDevolucao.configure(disabledforeground="#a3a3a3")
    telaEmprestimo.lblHorarioPrevisaoDevolucao.configure(foreground="#000000")
    telaEmprestimo.lblHorarioPrevisaoDevolucao.configure(text='''HORÁRIO:''')
    telaEmprestimo.lblHorarioPrevisaoDevolucao.configure(font=("Bahnschrift",'13'))

    telaEmprestimo.entHorarioPrevisaoDevolucao = Entry(telaEmprestimo)
    telaEmprestimo.entHorarioPrevisaoDevolucao.place(relx=0.552, rely=0.702, height=25, width=78)
    telaEmprestimo.entHorarioPrevisaoDevolucao.configure(background="white")
    telaEmprestimo.entHorarioPrevisaoDevolucao.configure(disabledforeground="#a3a3a3")
    telaEmprestimo.entHorarioPrevisaoDevolucao.configure(font=("Bahnschrift",'11'))
    telaEmprestimo.entHorarioPrevisaoDevolucao.configure(foreground="#000000")
    telaEmprestimo.entHorarioPrevisaoDevolucao.configure(insertbackground="black")
    telaEmprestimo.entHorarioPrevisaoDevolucao.bind('<KeyRelease>',FormatarHoraPrevisaoDevolucao)

def FecharcalendarioPrevisaoDevolucao():
    horario_formatar = telaEmprestimo.entHorarioPrevisaoDevolucao.get().split(':')

    if telaEmprestimo.entHorarioPrevisaoDevolucao.get()=='' or len(telaEmprestimo.entHorarioPrevisaoDevolucao.get())!=5 or int(horario_formatar[0])>=24 or int(horario_formatar[1])>=60:
        messagebox.showerror('','Horário inválido')
    else:
        telaEmprestimo.entDataPrevisaoDevolucao.configure(state="normal")
        data_da_devolucao = calendarioPrevisaoDevolucao.get_date()
        hora_devolucao = telaEmprestimo.entHorarioPrevisaoDevolucao.get()
        telaEmprestimo.entDataPrevisaoDevolucao.delete(0,'end')
        telaEmprestimo.entDataPrevisaoDevolucao.insert(0,data_da_devolucao)
        telaEmprestimo.entDataPrevisaoDevolucao.insert(11,' ')
        telaEmprestimo.entDataPrevisaoDevolucao.insert(12,hora_devolucao)

        calendarioPrevisaoDevolucao.place(relx=1.800, rely=1.800)
        telaEmprestimo.btnInserirPrevisaoDevolucao.place(relx=1.800, rely=1.800, height=30, width=70)
        telaEmprestimo.lblHorarioPrevisaoDevolucao.place(relx=1.800, rely=1.800)
        telaEmprestimo.entHorarioPrevisaoDevolucao.place(relx=1.800, rely=1.800, height=25, width=78)
        telaEmprestimo.entDataPrevisaoDevolucao.configure(state="disabled")

def FormatarHoraRetirada(event=None):
    if len(telaEmprestimo.entHorarioRetirada.get())==2:
        telaEmprestimo.entHorarioRetirada.insert(2,':')

    if len(telaEmprestimo.entHorarioRetirada.get())==6:
        telaEmprestimo.entHorarioRetirada.delete(5,'end')

def FormatarHoraDevolucao(event=None):
    if len(telaEmprestimo.entHorarioDevolucao.get())==2:
        telaEmprestimo.entHorarioDevolucao.insert(2,':')
    if len(telaEmprestimo.entHorarioDevolucao.get())==6:
        telaEmprestimo.entHorarioDevolucao.delete(5,'end')

def FormatarHoraPrevisaoDevolucao(event=None):
    if len(telaEmprestimo.entHorarioPrevisaoDevolucao.get())==2:
        telaEmprestimo.entHorarioPrevisaoDevolucao.insert(2,':')
    if len(telaEmprestimo.entHorarioPrevisaoDevolucao.get())==6:
        telaEmprestimo.entHorarioPrevisaoDevolucao.delete(5,'end')


telaEmprestimo.btnDataRetirada = Button(telaEmprestimo)
telaEmprestimo.btnDataRetirada.place(relx=0.401, rely=0.555, height=30, width=70)
telaEmprestimo.btnDataRetirada.configure(activebackground="beige")
telaEmprestimo.btnDataRetirada.configure(activeforeground="black")
telaEmprestimo.btnDataRetirada.configure(background="#d9d9d9")
telaEmprestimo.btnDataRetirada.configure(command=lambda: calendarioabrirRetirada())
telaEmprestimo.btnDataRetirada.configure(compound='left')
telaEmprestimo.btnDataRetirada.configure(disabledforeground="#a3a3a3")
telaEmprestimo.btnDataRetirada.configure(foreground="#000000")
telaEmprestimo.btnDataRetirada.configure(highlightbackground="#d9d9d9")
telaEmprestimo.btnDataRetirada.configure(highlightcolor="black")
telaEmprestimo.btnDataRetirada.configure(pady="0")
telaEmprestimo.btnDataRetirada.configure(text='''Retirada''')
telaEmprestimo.btnDataRetirada.configure(state="disabled")

telaEmprestimo.entDataRetirada = Entry(telaEmprestimo)
telaEmprestimo.entDataRetirada.place(relx=0.388, rely=0.595, height=25, width=120)
telaEmprestimo.entDataRetirada.configure(background="white")
telaEmprestimo.entDataRetirada.configure(disabledforeground="#a3a3a3")
telaEmprestimo.entDataRetirada.configure(font=("Bahnschrift",'11'))
telaEmprestimo.entDataRetirada.configure(foreground="#000000")
telaEmprestimo.entDataRetirada.configure(insertbackground="black")
telaEmprestimo.entDataRetirada.configure(state="disabled")

telaEmprestimo.btnDataPrevisaoDevolucao = Button(telaEmprestimo)
telaEmprestimo.btnDataPrevisaoDevolucao.place(relx=0.486, rely=0.555, height=30, width=120)
telaEmprestimo.btnDataPrevisaoDevolucao.configure(activebackground="beige")
telaEmprestimo.btnDataPrevisaoDevolucao.configure(activeforeground="black")
telaEmprestimo.btnDataPrevisaoDevolucao.configure(background="#d9d9d9")
telaEmprestimo.btnDataPrevisaoDevolucao.configure(command=lambda: calendarioabrirPrevisaoDevolucao())
telaEmprestimo.btnDataPrevisaoDevolucao.configure(compound='left')
telaEmprestimo.btnDataPrevisaoDevolucao.configure(disabledforeground="#a3a3a3")
telaEmprestimo.btnDataPrevisaoDevolucao.configure(foreground="#000000")
telaEmprestimo.btnDataPrevisaoDevolucao.configure(highlightbackground="#d9d9d9")
telaEmprestimo.btnDataPrevisaoDevolucao.configure(highlightcolor="black")
telaEmprestimo.btnDataPrevisaoDevolucao.configure(pady="0")
telaEmprestimo.btnDataPrevisaoDevolucao.configure(text='''Previsão Devolução''')
telaEmprestimo.btnDataPrevisaoDevolucao.configure(state="disabled")

telaEmprestimo.entDataPrevisaoDevolucao = Entry(telaEmprestimo)
telaEmprestimo.entDataPrevisaoDevolucao.place(relx=0.486, rely=0.595, height=25, width=120)
telaEmprestimo.entDataPrevisaoDevolucao.configure(background="white")
telaEmprestimo.entDataPrevisaoDevolucao.configure(disabledforeground="#a3a3a3")
telaEmprestimo.entDataPrevisaoDevolucao.configure(font=("Bahnschrift",'11'))
telaEmprestimo.entDataPrevisaoDevolucao.configure(foreground="#000000")
telaEmprestimo.entDataPrevisaoDevolucao.configure(insertbackground="black")
telaEmprestimo.entDataPrevisaoDevolucao.configure(state="disabled")

telaEmprestimo.btnDataDevolucao = Button(telaEmprestimo)
telaEmprestimo.btnDataDevolucao.place(relx=0.599, rely=0.555, height=30, width=70)
telaEmprestimo.btnDataDevolucao.configure(activebackground="beige")
telaEmprestimo.btnDataDevolucao.configure(activeforeground="black")
telaEmprestimo.btnDataDevolucao.configure(background="#d9d9d9")
telaEmprestimo.btnDataDevolucao.configure(command=lambda: calendarioabrirDevolucao())
telaEmprestimo.btnDataDevolucao.configure(compound='left')
telaEmprestimo.btnDataDevolucao.configure(disabledforeground="#a3a3a3")
telaEmprestimo.btnDataDevolucao.configure(foreground="#000000")
telaEmprestimo.btnDataDevolucao.configure(highlightbackground="#d9d9d9")
telaEmprestimo.btnDataDevolucao.configure(highlightcolor="black")
telaEmprestimo.btnDataDevolucao.configure(pady="0")
telaEmprestimo.btnDataDevolucao.configure(text='''Devolução''')
telaEmprestimo.btnDataDevolucao.configure(state="disabled")

telaEmprestimo.entDataDevolucao = Entry(telaEmprestimo)
telaEmprestimo.entDataDevolucao.place(relx=0.586, rely=0.595, height=25, width=120)
telaEmprestimo.entDataDevolucao.configure(background="white")
telaEmprestimo.entDataDevolucao.configure(disabledforeground="#a3a3a3")
telaEmprestimo.entDataDevolucao.configure(font=("Bahnschrift",'11'))
telaEmprestimo.entDataDevolucao.configure(foreground="#000000")
telaEmprestimo.entDataDevolucao.configure(insertbackground="black")
telaEmprestimo.entDataDevolucao.configure(state="disabled")

def inserirEmprestimo():
    telaEmprestimo.btnReservar.configure(state="disabled")
    telaEmprestimo.btnDevolver.configure(state="disabled")
    telaEmprestimo.btnDeletar.configure(state="disabled")
    telaEmprestimo.btnGravar.configure(state="normal")
    telaEmprestimo.btnCancelar.configure(state="normal")

    telaEmprestimo.entID.configure(state="normal")
    telaEmprestimo.comboTecnico.configure(state="normal")
    telaEmprestimo.comboFerramenta.configure(state="normal")
    telaEmprestimo.btnDataRetirada.configure(state="normal")
    telaEmprestimo.btnDataPrevisaoDevolucao.configure(state="normal")
    telaEmprestimo.btnDataDevolucao.configure(state="disabled")
    telaEmprestimo.entDataDevolucao.configure(state="normal")

    telaEmprestimo.entID.delete(0, END)
    telaEmprestimo.comboTecnico.delete(0, END)
    telaEmprestimo.comboFerramenta.delete(0, END)
    telaEmprestimo.entDataRetirada.delete(0, END)
    telaEmprestimo.entDataPrevisaoDevolucao.delete(0, END)
    telaEmprestimo.entDataDevolucao.delete(0, END)

    df = pd.read_csv(arquivoReservas, na_filter=False)
    chaveNova = df["ID"].max()
    if isNaN(chaveNova):
        chaveNova = 0

    telaEmprestimo.entID.insert(0, chaveNova + 1)
    telaEmprestimo.entID.configure(state="disabled")
    telaEmprestimo.entDataDevolucao.configure(state="disabled")

    telaEmprestimo.comboTecnico.focus_set()


def editarEmprestimo():
    selected = treeEmprestimo.focus()
    values = treeEmprestimo.item(selected, 'values')
    if values == '':
        messagebox.showwarning(title='Aviso', message='Selecione uma reserva antes de devolver')
    else:
        if len(values[5]) < 2:
            telaEmprestimo.btnReservar.configure(state="disabled")
            telaEmprestimo.btnDevolver.configure(state="disabled")
            telaEmprestimo.btnDeletar.configure(state="disabled")
            telaEmprestimo.btnGravar.configure(state="normal")
            telaEmprestimo.btnCancelar.configure(state="normal")

            telaEmprestimo.entID.configure(state="normal")
            telaEmprestimo.comboTecnico.configure(state="normal")
            telaEmprestimo.comboFerramenta.configure(state="normal")
            telaEmprestimo.btnDataRetirada.configure(state="disabled")
            telaEmprestimo.btnDataPrevisaoDevolucao.configure(state="disabled")
            telaEmprestimo.btnDataDevolucao.configure(state="normal")
            telaEmprestimo.entDataRetirada.configure(state="normal")
            telaEmprestimo.entDataPrevisaoDevolucao.configure(state="normal")
            telaEmprestimo.entDataDevolucao.configure(state="normal")

            telaEmprestimo.entID.delete(0, END)
            telaEmprestimo.comboTecnico.delete(0, END)
            telaEmprestimo.comboFerramenta.delete(0, END)
            telaEmprestimo.entDataRetirada.delete(0, END)
            telaEmprestimo.entDataPrevisaoDevolucao.delete(0, END)
            telaEmprestimo.entDataDevolucao.delete(0, END)

            telaEmprestimo.entID.insert(0, values[0])
            telaEmprestimo.entID.configure(state="disabled")
            telaEmprestimo.comboTecnico.insert(1, values[2])
            telaEmprestimo.comboFerramenta.insert(1, values[1])
            telaEmprestimo.entDataRetirada.insert(0, values[3])
            telaEmprestimo.entDataPrevisaoDevolucao.insert(0, values[4])
            telaEmprestimo.entDataDevolucao.insert(0, values[5])

            telaEmprestimo.entDataRetirada.configure(state="disabled")
            telaEmprestimo.entDataPrevisaoDevolucao.configure(state="disabled")

            telaEmprestimo.comboTecnico.focus_set()
        else:
            messagebox.showwarning(title='Aviso', message='Essa reserva já foi devolvida')

def gravarEmprestimo():

    telaEmprestimo.entID.configure(state="normal")
    telaEmprestimo.entDataRetirada.configure(state="normal")
    telaEmprestimo.entDataPrevisaoDevolucao.configure(state="normal")
    telaEmprestimo.entDataDevolucao.configure(state="normal")

    df = pd.read_csv(arquivoReservas, na_filter=False)
    df['ID'] = df['ID'].astype(int)
    chave = telaEmprestimo.entID.get()

    coluna = 'ID'
    valor = telaEmprestimo.entID.get()
    df.loc[int(chave) - 1, coluna] = valor

    coluna = 'Tecnico'
    valor = telaEmprestimo.comboTecnico.get()
    tamanhoCampo = 40
    df.loc[int(chave) - 1, coluna] = valor[0:tamanhoCampo]

    coluna = 'Ferramenta'
    valor = telaEmprestimo.comboFerramenta.get()
    tamanhoCampo = 60
    df.loc[int(chave) - 1, coluna] = valor[0:tamanhoCampo]

    coluna = 'DataRetirada'
    valor = telaEmprestimo.entDataRetirada.get()
    tamanhoCampo = 17
    df.loc[int(chave) - 1, coluna] = valor[0:tamanhoCampo]

    coluna = 'DataPrevisaoDevolucao'
    valor = telaEmprestimo.entDataPrevisaoDevolucao.get()
    tamanhoCampo = 17
    df.loc[int(chave) - 1, coluna] = valor[0:tamanhoCampo]

    coluna = 'DataDevolucao'
    valor = telaEmprestimo.entDataDevolucao.get()
    tamanhoCampo = 17
    df.loc[int(chave) - 1, coluna] = valor[0:tamanhoCampo]

    df['ID'] = df['ID'].astype(int)
    df.to_csv(arquivoReservas, index=False)

    telaEmprestimo.entID.delete(0, END)
    telaEmprestimo.comboTecnico.delete(0, END)
    telaEmprestimo.comboFerramenta.delete(0, END)
    telaEmprestimo.entDataRetirada.delete(0, END)
    telaEmprestimo.entDataPrevisaoDevolucao.delete(0, END)
    telaEmprestimo.entDataDevolucao.delete(0, END)

    telaEmprestimo.entID.configure(state="disabled")
    telaEmprestimo.comboTecnico.configure(state="disabled")
    telaEmprestimo.comboFerramenta.configure(state="disabled")
    telaEmprestimo.btnDataRetirada.configure(state="disabled")
    telaEmprestimo.btnDataPrevisaoDevolucao.configure(state="disabled")
    telaEmprestimo.btnDataDevolucao.configure(state="disabled")
    telaEmprestimo.entDataRetirada.configure(state="disabled")
    telaEmprestimo.entDataPrevisaoDevolucao.configure(state="disabled")
    telaEmprestimo.entDataDevolucao.configure(state="disabled")

    telaEmprestimo.btnReservar.configure(state="normal")
    telaEmprestimo.btnDevolver.configure(state="normal")
    telaEmprestimo.btnDeletar.configure(state="normal")
    telaEmprestimo.btnGravar.configure(state="disabled")
    telaEmprestimo.btnCancelar.configure(state="disabled")

    listaDadosEmprestimo()

def cancelarEmprestimo():
    telaEmprestimo.entID.configure(state="normal")

    telaEmprestimo.entID.configure(state="normal")
    telaEmprestimo.comboTecnico.configure(state="normal")
    telaEmprestimo.comboFerramenta.configure(state="normal")
    telaEmprestimo.btnDataRetirada.configure(state="disabled")
    telaEmprestimo.btnDataPrevisaoDevolucao.configure(state="disabled")
    telaEmprestimo.btnDataDevolucao.configure(state="disabled")
    telaEmprestimo.entDataRetirada.configure(state="normal")
    telaEmprestimo.entDataPrevisaoDevolucao.configure(state="normal")
    telaEmprestimo.entDataDevolucao.configure(state="normal")

    telaEmprestimo.entID.delete(0, END)
    telaEmprestimo.comboTecnico.delete(0, END)
    telaEmprestimo.comboFerramenta.delete(0, END)
    telaEmprestimo.entDataRetirada.delete(0, END)
    telaEmprestimo.entDataPrevisaoDevolucao.delete(0, END)
    telaEmprestimo.entDataDevolucao.delete(0, END)

    telaEmprestimo.entID.configure(state="disabled")
    telaEmprestimo.comboTecnico.configure(state="disabled")
    telaEmprestimo.comboFerramenta.configure(state="disabled")
    telaEmprestimo.btnDataRetirada.configure(state="disabled")
    telaEmprestimo.btnDataPrevisaoDevolucao.configure(state="disabled")
    telaEmprestimo.btnDataDevolucao.configure(state="disabled")
    telaEmprestimo.entDataRetirada.configure(state="disabled")
    telaEmprestimo.entDataPrevisaoDevolucao.configure(state="disabled")
    telaEmprestimo.entDataDevolucao.configure(state="disabled")

    telaEmprestimo.btnReservar.configure(state="normal")
    telaEmprestimo.btnDevolver.configure(state="normal")
    telaEmprestimo.btnDeletar.configure(state="normal")
    telaEmprestimo.btnGravar.configure(state="disabled")
    telaEmprestimo.btnCancelar.configure(state="disabled")

def deletarEmprestimo():
    df = pd.read_csv(arquivoReservas, na_filter=False)
    answer = askyesno(title='Confirmação',
                      message='Deseja excluir a reserva?')
    if answer == True:
        clicaritem = treeEmprestimo.focus()
        valor = treeEmprestimo.item(clicaritem)
        lista_valores = valor['values']
        valornormal = lista_valores[-0] - 1
        df_s = df.drop(df.index[valornormal])
        df_s.to_csv(arquivoReservas, index=False)
        treeEmprestimo.delete(*treeEmprestimo.get_children())
        df = pd.read_csv(arquivoReservas, na_filter=False)
        for row, series in df.iterrows():
            treeEmprestimo.insert(parent='', index='end', iid=row, text='', values=(
                series['ID'], series['Ferramenta'], series['Tecnico'], series['DataRetirada'],
                series['DataPrevisaoDevolucao'], series['DataDevolucao']))
def listaDadosEmprestimo():
    treeEmprestimo.delete(*treeEmprestimo.get_children())
    df = pd.read_csv(arquivoReservas, na_filter=False)
    for row, series in df.iterrows():
        treeEmprestimo.insert(parent='', index='end', iid=row, text='', values=(
            series['ID'], series['Ferramenta'], series['Tecnico'], series['DataRetirada'],
            series['DataPrevisaoDevolucao'], series['DataDevolucao']))

# ======== Fim Tela Emprestimo ==========

# ======== Inicio Relatorio Emprestimo ==========
menuTelaRelatorioEmprestimoCadastro = Menubutton(telaRelatorioEmprestimo, text='Cadastro', activebackground='gray')
menuTelaRelatorioEmprestimoCadastro.grid(row=0, column=0)
menuTelaRelatorioEmprestimoCadastro.menu = Menu(menuTelaRelatorioEmprestimoCadastro, tearoff=0)
menuTelaRelatorioEmprestimoCadastro["menu"] = menuTelaRelatorioEmprestimoCadastro.menu
menuTelaRelatorioEmprestimoCadastro.menu.add_command(label='Principal', command=lambda: show_frame(telaPrincipal))
menuTelaRelatorioEmprestimoCadastro.menu.add_command(label='Ferramentas', command=lambda: show_frame(telaFerramenta))
menuTelaRelatorioEmprestimoCadastro.menu.add_command(label='Técnicos Responsáveis', command=lambda: show_frame(telaTecnico))

menuTelaRelatorioEmprestimoMovimentacao = Menubutton(telaRelatorioEmprestimo, text='Movimentação', activebackground='gray')
menuTelaRelatorioEmprestimoMovimentacao.grid(row=0, column=1)
menuTelaRelatorioEmprestimoMovimentacao.menu = Menu(menuTelaRelatorioEmprestimoMovimentacao, tearoff=0)
menuTelaRelatorioEmprestimoMovimentacao["menu"] = menuTelaRelatorioEmprestimoMovimentacao.menu
menuTelaRelatorioEmprestimoMovimentacao.menu.add_command(label='Empréstimo de Ferramentas', command=lambda: show_frame(telaEmprestimo))

menuTelaEmprestimoRelatorios = Menubutton(telaRelatorioEmprestimo, text='Relatórios', activebackground='gray')
menuTelaEmprestimoRelatorios.grid(row=0, column=2)
menuTelaEmprestimoRelatorios.menu = Menu(menuTelaEmprestimoRelatorios, tearoff=0)
menuTelaEmprestimoRelatorios["menu"] = menuTelaEmprestimoRelatorios.menu
menuTelaEmprestimoRelatorios.menu.add_command(label='Empréstimo de Ferramentas', command=lambda: show_frame(telaRelatorioEmprestimo))

menuTelaRelatorioEmprestimoAjuda = Menubutton(telaRelatorioEmprestimo, text='Ajuda', activebackground='gray')
menuTelaRelatorioEmprestimoAjuda.grid(row=0, column=3)
menuTelaRelatorioEmprestimoAjuda.menu = Menu(menuTelaRelatorioEmprestimoAjuda, tearoff=0)
menuTelaRelatorioEmprestimoAjuda["menu"] = menuTelaRelatorioEmprestimoAjuda.menu
menuTelaRelatorioEmprestimoAjuda.menu.add_command(label='Sobre', command=lambda: show_frame(telaSobre))

telaRelatorioEmprestimo.Label1 = Label(telaRelatorioEmprestimo)
telaRelatorioEmprestimo.Label1.place(relx=0.0, rely=0.021, height=63, width=1920)
telaRelatorioEmprestimo.Label1.configure(background="#949494")
telaRelatorioEmprestimo.Label1.configure(anchor='center')
telaRelatorioEmprestimo.Label1.configure(compound='left')
telaRelatorioEmprestimo.Label1.configure(disabledforeground="#a3a3a3")
telaRelatorioEmprestimo.Label1.configure(font="-family {Segoe UI} -size 14 -weight bold")
telaRelatorioEmprestimo.Label1.configure(foreground="#000000")
telaRelatorioEmprestimo.Label1.configure(highlightcolor="#ffffff")
telaRelatorioEmprestimo.Label1.configure(text='''Tela de Relatório de Emprestimo de Ferramenta''')

### treeview

#telaRelatorioEmprestimo


colunasRelatorioEmprestimo = ( 'Ferramenta', 'Tecnico', 'DataRetirada', 'DataPrevisaoDevolucao', 'DataDevolucao')
treetelaRelatorioEmprestimo = ttk.Treeview(telaRelatorioEmprestimo, columns=colunasRelatorioEmprestimo, show='headings')
scrollbar = ttk.Scrollbar(telaRelatorioEmprestimo,
                          orient="vertical",
                          command=treetelaRelatorioEmprestimo.yview)
scrollbar.place(relx=0.99, rely=0.091, height=280, width=20)
treetelaRelatorioEmprestimo.configure(xscrollcommand=scrollbar.set)

# define headings
#treetelaRelatorioEmprestimo.heading("ID", text="ID", anchor=W)
treetelaRelatorioEmprestimo.heading("Ferramenta", text="Ferramenta", anchor=W)
treetelaRelatorioEmprestimo.heading("Tecnico", text="Tecnico", anchor=W)
treetelaRelatorioEmprestimo.heading("DataRetirada", text="Data Retirada", anchor=W)
treetelaRelatorioEmprestimo.heading("DataPrevisaoDevolucao", text="Data Previsão Devolução", anchor=W)
treetelaRelatorioEmprestimo.heading("DataDevolucao", text="Data Devolução", anchor=W)

df = pd.read_csv(arquivoReservas, na_filter=False)
for row, series in df.iterrows():
    treetelaRelatorioEmprestimo.insert(parent='', index='end', iid=row, text='', values=(
        series['Ferramenta'], series['Tecnico'], series['DataRetirada'], series['DataPrevisaoDevolucao'],
        series['DataDevolucao']))


def selecionaEmprestimo(event):
    for selected_item in treetelaRelatorioEmprestimo.selection():
        item = treetelaRelatorioEmprestimo.item(selected_item)
        record = item['values']


treetelaRelatorioEmprestimo.bind('<<TreeviewSelect>>', selecionaEmprestimo)
treetelaRelatorioEmprestimo.place(relx=0.0, rely=0.091, height=280, width=1920)

# ======== Fim Relatorio Emprestimo ==========

# ======== Inicio Tela Sobre ==========
menuTelaSobreCadastro = Menubutton(telaSobre, text='Cadastro', activebackground='gray')
menuTelaSobreCadastro.grid(row=0, column=0)
menuTelaSobreCadastro.menu = Menu(menuTelaSobreCadastro, tearoff=0)
menuTelaSobreCadastro["menu"] = menuTelaSobreCadastro.menu
menuTelaSobreCadastro.menu.add_command(label='Principal', command=lambda: show_frame(telaPrincipal))
menuTelaSobreCadastro.menu.add_command(label='Ferramentas', command=lambda: show_frame(telaFerramenta))
menuTelaSobreCadastro.menu.add_command(label='Técnicos Responsáveis', command=lambda: show_frame(telaTecnico))

menuTelaSobreMovimentacao = Menubutton(telaSobre, text='Movimentação', activebackground='gray')
menuTelaSobreMovimentacao.grid(row=0, column=1)
menuTelaSobreMovimentacao.menu = Menu(menuTelaSobreMovimentacao, tearoff=0)
menuTelaSobreMovimentacao["menu"] = menuTelaSobreMovimentacao.menu
menuTelaSobreMovimentacao.menu.add_command(label='Empréstimo de Ferramentas', command=lambda: show_frame(telaEmprestimo))

menuTelaSobreRelatorios = Menubutton(telaSobre, text='Relatórios', activebackground='gray')
menuTelaSobreRelatorios.grid(row=0, column=2)
menuTelaSobreRelatorios.menu = Menu(menuTelaSobreRelatorios, tearoff=0)
menuTelaSobreRelatorios["menu"] = menuTelaSobreRelatorios.menu
menuTelaSobreRelatorios.menu.add_command(label='Empréstimo de Ferramentas', command=lambda: show_frame(telaRelatorioEmprestimo))

menuTelaSobreAjuda = Menubutton(telaSobre, text='Ajuda', activebackground='gray')
menuTelaSobreAjuda.grid(row=0, column=3)
menuTelaSobreAjuda.menu = Menu(menuTelaSobreAjuda, tearoff=0)
menuTelaSobreAjuda["menu"] = menuTelaSobreAjuda.menu
menuTelaSobreAjuda.menu.add_command(label='Sobre', command=lambda: show_frame(telaSobre))

telaSobre.Label1 = Label(telaSobre)
telaSobre.Label1.place(relx=0.0, rely=0.021, height=63, width=1920)
telaSobre.Label1.configure(background="#949494")
telaSobre.Label1.configure(anchor='center')
telaSobre.Label1.configure(compound='left')
telaSobre.Label1.configure(disabledforeground="#a3a3a3")
telaSobre.Label1.configure(font="-family {Segoe UI} -size 14 -weight bold")
telaSobre.Label1.configure(foreground="#000000")
telaSobre.Label1.configure(highlightcolor="#ffffff")
telaSobre.Label1.configure(text='''Tela Sobre o Sistema''')

# ======== Fim Tela Sobre ==========


# logar
def logar():
    df = pd.read_csv(arquivoUsuarios, na_filter=False)
    for row, series in df.iterrows():
        if str(series['User']) == str(telaLogin.entLogin.get()):
            #usuario encontrado
            if str(series['Password']) == str(telaLogin.entSenha.get()):
                #senha correta
                usuarioLogado = telaLogin.entLogin.get()
                telaPrincipal.Label1.configure(text='Seja bem vindo(a): '+str(usuarioLogado))
                show_frame(telaPrincipal)
                break
            else:
                # senha incorreta
                usuarioLogado = ''
        else:
            # usuario incorreto
            usuarioLogado = ''
    if usuarioLogado == '':
        messagebox.showerror(title='Erro', message='Usuário ou senha não encontrados, tente novamente')
        telaLogin.entLogin.delete(0, END)
        telaLogin.entSenha.delete(0, END)
        telaLogin.entLogin.focus_set()

window.mainloop()


