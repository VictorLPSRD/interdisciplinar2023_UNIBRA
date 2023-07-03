"""
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------

PROJETO DO INTERDISCIPLINAR DE 2023.1 DA TURMA DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - ADS2NAB (2022.2)
FACULDADE: UNIBRA (CENTRO UNIVERSITÁRIO BRASILEIRO)
GRUPO DE DESENVOLVIMENTO POO: JONATHAN, HENRIQUE, ELIAS, VICTOR
ORIENTADORA: ALINE FARIAS


>> PARA FUNCIONAMENTO DO CÓDIGO É NECESSÁRIO INSTALAR ALGUNS PACKAGES DO PYTHON

1 - Ter o Python da versão 3.10 ou superior: (https://www.python.org/)
2 - Instalar na máquina local, (não rodar no replit ou compilador online)

Recomendações: Recomendamos os compiladores:
* Pycharm (https://www.jetbrains.com/pt-br/pycharm/)
* VScode (https://code.visualstudio.com/)

-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------

>> RECURSOS PARA O SOFTWARE
>> instalando package
>> Verificação de pacotes e versões: pip freeze


1 - pip install tkinter | versão utilizada: nativo com python
2 - pip install customtkinter | versão utilizada: 5.1.2
3 - pip install webbrowser | versão utilizada: 6.0
4 - pip install sqlite3 | versão utilizada: 1.2.0
5 - pip install pandas | versão utilizada: 2.0.0
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------

>> RECURSOS PARA BANCO DE DADOS

1 - DB BROWSER : Download: https://sqlitebrowser.org/dl/

Obs.: Só use o comando CREATE TABLE se não houver o arquivo produto.db na pasta do arquivo.
-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------

>> É doce, mas não é mole não !!!

"""


import pandas as pd
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
import webbrowser
import customtkinter
from datetime import date

# --------------------------------------------- 1 - CRIAÇÃO E CONEXAO COM SQLITE -------------------------------------------------------------#
#  SE O CÓDIGO DA CRIAÇÃO RODAR E CRIAR O produto.db na máquina, se faz necessário tornar esse código COMENTÁRIO para não gerar um duplo banco
# PARA INICIAR E CRIAR UM .db EM MAQUINA NOVA SEM TER BANCO DE DADOS, DESCOMENTE O CÓDIGO E COMENTE O 2
#conexao = sqlite3.connect('produto.db')
#c = conexao.cursor()
#c.execute('''CREATE TABLE produto (
#    nome text,
#    quantidade interger,
#    genero text,
#    tipo text,
#    preco real,
#    validade text
#    )
#''')

#conexao.commit() 
#conexao.close()  


# --------------------------------------------- 2 - INSERIR DADOS NA TABELA -------------------------------------------------------------#
# UMA VEZ O BANCO CRIADO, COMENTAR O CÓDIGO DO PASSO 1 E USAR ESSE CÓDIGO SEM COMENTÁRIO
# PARA INICIAR E INSERIR DADOS JÁ TENDO UM .db EM MAQUINA DESCOMENTE ESSE CÓDIGO E COMENTE O 1
# OBS LINHA 291

#def cadastrar_produto():
#    conexao = sqlite3.connect('produto.db')
#    c = conexao.cursor()
#    c.execute(" INSERT INTO produto VALUES (:nome, :quantidade, :genero, :tipo, :preco, :validade)",
#              {
#                'nome':entry_produto.get(),
#                'quantidade':quantidadeEntrada.get(),
#                'genero':generoEntrada.get(),
#                'tipo':tipoEntrada.get(),
#                'preco':precoEntrada.get(),
#                'validade':validadeEntrada.get()
#              }
#              )
#    conexao.commit()
#    conexao.close()




dicionarioVenda = {}
dicionarioCompra = {}
dicionarioUsuario = {}
listaVenda = []
listaCompra = []
dicionarioEstoque = {}
dicAcesso = {}


def registroVenda():
    return dicionarioVenda


def registroCompra():
    return dicionarioCompra


def bancoDeUsuarios():
    return dicionarioUsuario


def estoqueTotal():
    return dicionarioEstoque


def criaJanelaTransacao():
    # ----------------------FUNCIONAMENTO DA JANELA TRANSAÇAO-----------------------------
    # -----------------------------------VENDAS--------------------------------------------
    def registraTransacaoVenda():
        chaveVenda = produtoEntrada.get()
        quantidadeVenda = quantidadeEntrada.get()
        precoVenda = precoEntrada.get()
        linVenda = precoLinha.get()
        genVenda = generoEntrada.get()
        tipoVenda = tipoEntrada.get()
        validadeVenda = validadeEntrada.get()

        tuplaVenda = (quantidadeVenda, precoVenda, linVenda,
                      genVenda, tipoVenda, validadeVenda)
        if chaveVenda in dicionarioVenda and chaveVenda in dicionarioEstoque:
            listaVenda = dicionarioVenda[chaveVenda]
            listaVenda.append(tuplaVenda)
            # ---------------------->>> ESCREVER NO ARQUIVO
            dicionarioVenda[chaveVenda] = listaVenda
        else:
            if chaveVenda in dicionarioEstoque:
                listaVenda = []
                listaVenda.append(tuplaVenda)
                dicionarioVenda[chaveVenda] = listaVenda
        if chaveVenda in dicionarioEstoque:
            dicionarioEstoque[chaveVenda] += -int(tuplaVenda[0])
            if dicionarioEstoque[chaveVenda] <= 0:
                dicionarioEstoque.pop(chaveVenda)

        else:
            dicionarioEstoque[chaveVenda] = -int(tuplaVenda[0])
            if dicionarioEstoque[chaveVenda] < 0:
                dicionarioEstoque.pop(chaveVenda)

        print(dicionarioVenda)
        print(dicionarioEstoque)

    # ------------------------------------COMPRAS-------------------------------------------
    def registraTransacaoCompra():
        chaveCompra = produtoEntrada.get()
        quantidadeCompra = quantidadeEntrada.get()
        precoCompra = precoEntrada.get()
        linCompra = precoLinha.get()
        genCompra = generoEntrada.get()
        tipoCompra = tipoEntrada.get()
        validadeCompra = validadeEntrada.get()

        tuplaCompra = (quantidadeCompra, precoCompra, linCompra,
                       genCompra, tipoCompra, validadeCompra)
        if chaveCompra in dicionarioCompra:
            listaCompra = dicionarioCompra[chaveCompra]
            listaCompra.append(tuplaCompra)
            # ---------------------->>> ESCREVER NO ARQUIVO
            dicionarioCompra[chaveCompra] = listaCompra
        else:
            listaCompra = []
            listaCompra.append(tuplaCompra)
            dicionarioCompra[chaveCompra] = listaCompra
        if chaveCompra in dicionarioEstoque:
            dicionarioEstoque[chaveCompra] += int(tuplaCompra[0])

        else:
            dicionarioEstoque[chaveCompra] = int(tuplaCompra[0])

        print(dicionarioCompra)
        print(dicionarioEstoque)

    # -----------------LAYOUT JANELA TRANSAÇAO--------------------
    janelaTransacao = customtkinter.CTk(fg_color='#efe1e1')

    largura = 400
    altura = 200

    largura_tela = janelaTransacao.winfo_screenwidth()
    altura_tela = janelaTransacao.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura / 2
    janelaTransacao.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY))

    janelaTransacao.title("Registrar Transação")
    janelaTransacao.geometry("680x370+350+200")
    janelaTransacao.resizable(width=False, height=False)

    # --------------------LAYOUT DOS BOTOES--------------------------
    produto = customtkinter.CTkLabel(janelaTransacao, fg_color='#efe1e1', text_color='black', text="Produto:")
    produto.place(x=60, y=20)

    produtoEntrada = customtkinter.CTkEntry(janelaTransacao, fg_color='white', text_color='black', placeholder_text='Nome do produto...', width=150)
    produtoEntrada.place(x=200, y=20)

    # teste bdd
    #produto = tk.Label(janelaTransacao, text='Produto:')
    #produto.grid(row=0, column=0, padx=10, pady=10)

    #entry_produto = tk.Entry(janelaTransacao, text='Produto', width=30)
    #entry_produto.grid(row=0, column=1, padx=10, pady=10)

    produtoQuantidade = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Quantidade:")
    produtoQuantidade.place(x=60, y=50)

    quantidadeEntrada = customtkinter.CTkEntry(
        janelaTransacao, fg_color='white', text_color='black', placeholder_text='Quantidade do produto...', width=150)
    quantidadeEntrada.place(x=200, y=50)

    produtoLinha = produto = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Linha:")
    produtoLinha = produtoLinha.place(x=60, y=80)

    precoLinha = customtkinter.CTkEntry(
        janelaTransacao, fg_color='white', text_color='black', placeholder_text='Linha do produto...', width=150)
    precoLinha.place(x=200, y=80)

    produtoGenero = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Genero:")
    produtoGenero.place(x=60, y=110)

    generoEntrada = customtkinter.CTkEntry(
        janelaTransacao, fg_color='white', text_color='black', placeholder_text='Genero do produto...', width=150)
    generoEntrada.place(x=200, y=110)

    tipoProduto = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Tipo:")
    tipoProduto.place(x=60, y=140)

    tipoEntrada = customtkinter.CTkEntry(
        janelaTransacao, fg_color='white', text_color='black', placeholder_text='Tipo do produto...', width=150)
    tipoEntrada.place(x=200, y=140)

    precoProduto = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Preço:")
    precoProduto.place(x=60, y=170)

    precoEntrada = customtkinter.CTkEntry(
        janelaTransacao, fg_color='white', text_color='black', placeholder_text='Preço do produto...', width=150)
    precoEntrada.place(x=200, y=170)

    validade = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Validade:")
    validade.place(x=60, y=200)

    validadeEntrada = customtkinter.CTkEntry(
        janelaTransacao, fg_color='white', text_color='black', placeholder_text='Validadedo produto...', width=150)
    validadeEntrada.place(x=200, y=200)

    descricao = customtkinter.CTkLabel(
        janelaTransacao, fg_color='#efe1e1', text_color='black', text="Descrição dos produto 🢃 :")
    descricao.place(x=450, y=20)

    descricaotexto = customtkinter.CTkTextbox(janelaTransacao, fg_color='white', text_color='black', width=250, height=180,
                                              border_color='black', border_width=2, corner_radius=15)
    descricaotexto.place(x=390, y=40)

    botaoVenda = customtkinter.CTkButton(janelaTransacao, fg_color='blue', text="Registrar Venda",
                                         command=registraTransacaoVenda)
    botaoVenda.place(x=180, y=270)
    # botaoVenda["bg"] = "red"

    botaoCompra = customtkinter.CTkButton(janelaTransacao, fg_color='green', text="Registrar Compra",
                                          command=registraTransacaoCompra)
    botaoCompra.place(x=340, y=270)
    # botaoCompra["bg"] = "green"

    botaoCancela = customtkinter.CTkButton(janelaTransacao, fg_color='red', text="Cancelar",
                                           command=janelaTransacao.destroy)
    botaoCancela.place(x=180, y=320)
    # botaoCancela["bg"] = "#FFE4B5"

    #For realizar o comando INSERT no banco de dados, deve primeiro ter o próprio CREATE TABLE
    #For utilizar o INSERT, por no command a função do INSERT definida na linha 79 = ficará assim: command=cadastrar_produto
    botaoCadastro = customtkinter.CTkButton(janelaTransacao, fg_color='orange',text="Cadastrar",
                                            command="") 
    botaoCadastro.place(x=340, y=320)

    janelaTransacao.mainloop()

    

# --------------------FUNÇÃO JANELA INFORMAÇÕES ESTOQUE (ESTOQUE/HISTÓRICO DE TRANSAÇÕES)----------------------------


def criaJanelaEstoque():
    # ------------------------------FUNÇÃO PESQUISA DE PRODUTOS----------------------------------------
    def auxiliar():
        def pesquisaProduto():
            pesquisaProdutoNome = entradaNomeProduto.get()
            if pesquisaProdutoNome in dicionarioEstoque:
                produtoResultadoNome["text"] = "Nome:", pesquisaProdutoNome
                produtoResultadoQuantidade["text"] = "Qtd em estoque:", dicionarioEstoque[pesquisaProdutoNome]
                # janelaPesquisaProduto.geometry("415x140+525+270")
            else:
                produtoResultadoNome["text"] = pesquisaProdutoNome, "em falta!"
                produtoResultadoQuantidade["text"] = ""

        # -------------------------LAYOUT DA JANELA PRODUTO PESQUISADO----------------------------------
        pesquisado = Toplevel(janelaDados)
        pesquisado.title('PRODUTO PESQUISADO')

        largura = 600
        altura = 500

        largura_tela = pesquisado.winfo_screenwidth()
        altura_tela = pesquisado.winfo_screenheight()
        posX = largura_tela / 2 - largura / 2
        posY = altura_tela / 2 - altura / 2
        pesquisado.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY))

        pesquisado.title("Produto Pesquisado")
        # janelaHistorico.geometry("400x400+525+0")
        pesquisado["bg"] = '#efe1e1'
        pesquisado.resizable(width=False, height=False)

        nomeProduto = tk.Label(pesquisado, text="Nome do produto:")
        nomeProduto.place(x=10, y=15)
        nomeProduto["bg"] = "#87CEFA"

        entradaNomeProduto = customtkinter.CTkEntry(
            pesquisado, fg_color="white", text_color='black')
        entradaNomeProduto.place(x=130, y=10.5)

        produtoResultadoNome = tk.Label(pesquisado, text="")
        produtoResultadoNome.place(x=10, y=50)
        produtoResultadoNome["bg"] = "#87CEFA"

        produtoResultadoQuantidade = tk.Label(pesquisado, text="")
        produtoResultadoQuantidade.place(x=10, y=70)
        produtoResultadoQuantidade["bg"] = "#87CEFA"

        botaoProcurar = customtkinter.CTkButton(
            pesquisado, fg_color='green', text="Pesquisar", command=pesquisaProduto)
        botaoProcurar.place(x=280, y=10.5)

    # --------------------CRIA JANELA INFORMAÇÕES DE ESTOQUE (ESTOQUE/HISTÓRICO DE TRANSAÇÕES)--------------------------
    janelaDados = tk.Tk()

    largura = 600
    altura = 500

    largura_tela = janelaDados.winfo_screenwidth()
    altura_tela = janelaDados.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura / 2
    janelaDados.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY))
    janelaDados.title("Informações de Estoque")
    # janelaHistorico.geometry("400x400+525+0")
    janelaDados["bg"] = '#efe1e1'
    janelaDados.resizable(width=False, height=False)

    # -----------------------------Criação de um Notebook(elemento ttk, para adição de abas)--------------------------------
    hist = ttk.Notebook(janelaDados)
    hist.place(x=0, y=0, width=600, height=500)

    # ---------------------------------------criando aba Compras-----------------------------------------
    tb1 = tk.Frame(hist)
    hist.add(tb1, text='Compras')
    tb1["bg"] = "#87CEFA"

    # ---------------------------------------criando aba Vendas------------------------------------------
    tb2 = tk.Frame(hist)
    hist.add(tb2, text='Vendas')
    tb2["bg"] = "#87CEFA"

    # ---------------------------------------criando aba Estoque-----------------------------------------
    tb3 = tk.Frame(hist)
    hist.add(tb3, text='Estoque')
    tb3["bg"] = "#87CEFA"

    ### ----------------------------------------FUNCIONAMENTO DO HISTÓRICO DE COMPRAS-------------------------------------------###
    # ------------------------------------LINHAS SUBSTITUIDAS PELA ADIÇÃO DO TREEVIEW--------------------------------------------
    # produto_label = customtkinter.CTkLabel(tb1,fg_color='#87CEFA', text_color='black' ,text="|    Produto    ", font=("Arial", 20))
    # produto_label.grid(row=0, column=1, padx=20, pady=10)
    # quantidade_label = customtkinter.CTkLabel(tb1,fg_color='#87CEFA', text_color='black', text="|    Qtd    ", font=("Arial", 20))
    # quantidade_label.grid(row=0, column=2, padx=20, pady=10)
    # preco_label = customtkinter.CTkLabel(tb1,fg_color='#87CEFA', text_color='black', text="|    Preço    |", font=("Arial", 20))
    # preco_label.grid(row=0, column=3, padx=20, pady=10)
    # ---------------------------------------------------------------------------------------------------------------------------
    tree = ttk.Treeview(tb1)
    tree.grid(row=1, column=0, padx=10, pady=10)
    tree['columns'] = ('Quantidade', 'Preço')
    tree.column('#0', width=120, minwidth=120, anchor='w')
    tree.column('Quantidade', width=120, minwidth=120, anchor='w')
    tree.column('Preço', width=120, minwidth=120, anchor='w')
    tree.heading('#0', text='Produto', anchor='w')  # PRODUTO
    tree.heading('Quantidade', text='Quantidade', anchor='w')  # QUANDIDADE
    tree.heading('Preço', text='Preço', anchor='w')  # PREÇO

    for produto, compras in dicionarioCompra.items():
        for dadosc in compras:
            tree.insert('', 'end', text=produto, values=(dadosc[0], dadosc[1]))

    # -------------TESTANDO A BARRA DE ROLAGEM------------------
    barra = ttk.Scrollbar(tb1, orient="vertical", command=tree.yview)
    barra.grid(row=1, column=1)
    tree.configure(yscrollcommand=barra.set)

# ------------Obtendo dados de Compra(Modelo Base)------------------
#    row = 1
#    for produto, compras in dicionarioCompra.items():
#        for dadosc in compras:
#            produto_label = tk.Label(tb1, text=produto)
#            produto_label.grid(row=row, column=1, padx=20, pady=10)
#
#            quantidade_label = tk.Label(tb1, text=dadosc[0])
#            quantidade_label.grid(row=row, column=2, padx=20, pady=10)
#
#            preco_label = tk.Label(tb1, text=dadosc[1])
#            preco_label.grid(row=row, column=3, padx=20, pady=10)
#
#            row += 1

    # ------------------------------------------FUNCIONAMENTO DO HISTÓRICO DE VENDAS--------------------------------------------###
    # ------------------------------------LINHAS SUBSTITUIDAS PELA ADIÇÃO DO TREEVIEW--------------------------------------------
    # produto_label = customtkinter.CTkLabel(tb2,fg_color='#87CEFA',text_color='black', text="|    Produto    ", font=("Arial", 20))
    # produto_label.grid(row=0, column=0, padx=10, pady=10)
    # quantidade_label = customtkinter.CTkLabel(tb2,fg_color='#87CEFA',text_color='black', text="|    Qtd    ", font=("Arial", 20))
    # quantidade_label.grid(row=0, column=1, padx=10, pady=10)
    # preco_label = customtkinter.CTkLabel(tb2,fg_color='#87CEFA',text_color='black', text="|    Preço    |", font=("Arial", 20))
    # preco_label.grid(row=0, column=2, padx=10, pady=10)
    # ---------------------------------------------------------------------------------------------------------------------------
    tree = ttk.Treeview(tb2)
    tree['columns'] = ('Quantidade', 'Preço')
    tree.column('#0', width=120, minwidth=120, anchor='w')
    tree.column('Quantidade', width=120, minwidth=120, anchor='w')
    tree.column('Preço', width=120, minwidth=120, anchor='w')
    tree.heading('#0', text='Produto', anchor='w')
    tree.heading('Quantidade', text='Quantidade', anchor='w')
    tree.heading('Preço', text='Preço', anchor='w')

    for produto, vendas in dicionarioVenda.items():
        for dadosv in vendas:
            tree.insert('', 'end', text=produto, values=(dadosv[0], dadosv[1]))

    tree.grid(row=1, column=0, padx=10, pady=10)

# ------------Obtendo dados de Venda(Modelo Base)------------------
#    row = 1
#    for produto, vendas in dicVenda.items():
#        for dadosv in vendas:
#            produto_label = tk.Label(tb2, text=produto)
#            produto_label.grid(row=row, column=0, padx=10, pady=10)
#
#            quantidade_label = tk.Label(tb2, text=dadosv[0])
#            quantidade_label.grid(row=row, column=1, padx=10, pady=10)
#
#            preco_label = tk.Label(tb2, text=dadosv[1])
#            preco_label.grid(row=row, column=2, padx=10, pady=10)
#
#            row += 1

    ### ----------------------------------------FUNCIONAMENTO DA ABA DE ESTOQUE---------------------------------------------------###
    # ---------------------------Linhas substituídas com a implementação do Treeview(linhas funcionais)----------------------------
    # produto_label = customtkinter.CTkLabel(tb3,fg_color='#87CEFA', text_color='black', text="|    Produto    |", font=("Arial", 20))
    # produto_label.grid(row=0, column=0, padx=10, pady=10)
    # quantidade_label = customtkinter.CTkLabel(tb3,fg_color='#87CEFA', text_color='black', text="   Qtd    |", font=("Arial", 20))
    # quantidade_label.grid(row=0, column=1, padx=10, pady=10)
    # validade_label = customtkinter.CTkLabel(tb3,fg_color='#87CEFA', text_color='black', text="   Validade   |", font=("Arial", 20))
    # validade_label.grid(row=0, column=3, padx=10, pady=10)
    # -----------------------------------------------------------------------------------------------------------------------------
    tree = ttk.Treeview(tb3)
    tree['columns'] = ('Quantidade',)
    # ----'#0' identificador padrão para a primeira coluna
    tree.column('#0', width=90, minwidth=0, anchor='w')
    tree.column('Quantidade', width=90, minwidth=0, anchor='w')
    tree.heading('#0', text='Produto', anchor='w')
    tree.heading('Quantidade', text='Quantidade', anchor='w')

    for produto, estocagem in dicionarioEstoque.items():
        tree.insert('', 'end', text=produto, values=(estocagem,))

    tree.grid(row=1, column=0, padx=10, pady=10)
# ---------------------TESTANDO TREEVIEW------------------------
#    tv = ttk.Treeview(tb3, columns=('Produto'), show='headings')
#    tv.column('Produto', width=100)
#    #tv.column('Quantidade', width=90)
#    tv.heading('Produto', text='Produto')
#    #tv.heading('Quantidade', text='QUANTIDADE')
#    tv.pack()
#
#    for (pro) in dicionarioEstoque:
#        tv.insert("", "end", values=(pro))
# --------------------DEU CERTO(modelo base)----------------------

# ------------Obtendo dados de Estoque(Modelo Base)------------------
#    row = 1
#    for produto, estocagem in dicionarioEstoque.items():
#        produto_label = tk.Label(tb3, text=produto)
#        produto_label.grid(row=row, column=0, padx=10, pady=10)
#
#        quantidade_label = tk.Label(tb3, text=estocagem)
#        quantidade_label.grid(row=row, column=1, padx=10, pady=10)
#
#        row += 1
# -------------------------------------------------------------------
    

    # ---------------------------------------------------Bloco de Botões--------------------------------------------------------
    # ---cancela procedimento
    botaoCancela = customtkinter.CTkButton(
        janelaDados, fg_color='red', text="Voltar", width=80, height=40, command=janelaDados.destroy)
    botaoCancela.place(x=500, y=80)
    # botaoCancela["bg"] = "#FFE4B5"

    # ---pesquisa especifica
    botaoProcurar = customtkinter.CTkButton(
        janelaDados, fg_color='green', text="Pesquisar Produto", command=auxiliar)
    botaoProcurar.place(x=450, y=30)

   # def exportar():
      #  marks_data = pd.DataFrame(dicionarioEstoque)
      #  file_name = 'MarksData.xlsx'
       # marks_data.to_excel(file_name)
   #exportar()

    #botaoexportacao = customtkinter.CTkButton(janelaDados, fg_color='blue', text="Exportar", width=80, height=40,command="")
    
    #botaoexportacao.place(x=500, y=130)

    janelaDados.mainloop()

# ------------------------------FUNÇAO JANELA GERENCIAMENTO DE USUARIO-------------------------------


def criaJanelaGerenciamento():
    # ---------------------------FUNCIONAMENTO GERENCIAMENTO DE USUARIO -----------------------------
    def gerenciaUsuario():
        chaveNome = entradaNomeUsuario.get()
        cpf = entradaCpf.get()
        telefone = entradaTelefone.get()
        senha = entradaSenha.get()
        nivel = entradaNivel.get()
        # (chaveNome,cpf,telefone,senha,nivel)
        tuplaUsuario = (chaveNome, senha, cpf, telefone, nivel)

        if chaveNome in dicionarioUsuario:
            # ---------------------->>> ESCREVER NO ARQUIVO
            dicionarioUsuario[chaveNome] = tuplaUsuario
        else:
            listaUsuario = []
            listaUsuario.append(tuplaUsuario)
            dicionarioUsuario[chaveNome] = listaUsuario
        print(dicionarioUsuario)

    # ---------------------------------FUNCIONAMENTO PESQUISA DE USUARIO----------------------------

    def pesquisaUsuario():
        pesquisaNome = pesquisaEntrada.get()
        if pesquisaNome in dicionarioUsuario:
            resultadoNome["text"] = "Nome:", pesquisaNome
            resultadoCpf["text"] = "CPF:", dicionarioUsuario[pesquisaNome][0][3]
            resultadoTelefone["text"] = "Telefone:", dicionarioUsuario[pesquisaNome][0][2]
            resultadoNivel["text"] = "Nível:", dicionarioUsuario[pesquisaNome][0][1]
        else:
            resultadoNome["text"] = ""
            resultadoCpf["text"] = "ERRO: Usuário não cadastrado no sistema"
            resultadoTelefone["text"] = ""
            resultadoNivel["text"] = ""

    # ------------------------------FUNCIONAMENTO BOTAO EXCLUIR----------------------------------------
    def excluirUsuario():
        excluiNome = pesquisaEntrada.get()
        if excluiNome in dicionarioUsuario:
            dicionarioUsuario.pop(excluiNome)
            print(dicionarioUsuario)
            resultadoNome["text"] = ""
            resultadoCpf["text"] = ""
            resultadoTelefone["text"] = ""
            resultadoNivel["text"] = ""
            resultadoExclusao["text"] = "USUÁRIO EXCLUÍDO COM SUCESSO!"
        else:
            resultadoNome["text"] = ""
            resultadoCpf["text"] = ""
            resultadoTelefone["text"] = ""
            resultadoNivel["text"] = ""
            resultadoExclusao["text"] = "IMPOSSÍVEL EXCLUIR"

    # ------------------------------------LAYOUT JANELA GERENCIAMENTO---------------------------------
    janelaGerenciamento = tk.Tk()

    largura = 530
    altura = 420

    largura_tela = janelaGerenciamento.winfo_screenwidth()
    altura_tela = janelaGerenciamento.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura / 2
    janelaGerenciamento.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY))
    janelaGerenciamento["bg"] = "#efe1e1"
    # janelaGerenciamento.geometry("530x420+525+0")
    janelaGerenciamento.title("Gerenciamento de Usuário")
    janelaGerenciamento.resizable(width=False, height=False)

    # ---------------------------------------BOTÕES ADICIONAR USUARIO--------------------------------------------------------
    nomeUsuario = customtkinter.CTkLabel(
        janelaGerenciamento, fg_color='#efe1e1', text_color='black', text="Nome do usuário:")
    nomeUsuario.place(x=20, y=20)
    # nomeUsuario["bg"] = "#87CEFA"

    entradaNomeUsuario = customtkinter.CTkEntry(
        janelaGerenciamento, fg_color='white', text_color='black', width=280, height=20)
    entradaNomeUsuario.place(x=150, y=20)

    cpfUsuario = customtkinter.CTkLabel(
        janelaGerenciamento, fg_color='#efe1e1', text_color='black', text="CPF do usuário:")
    cpfUsuario.place(x=20, y=50)
    # cpfUsuario["bg"] = "#87CEFA"

    entradaCpf = customtkinter.CTkEntry(
        janelaGerenciamento, fg_color='white', text_color='black', width=280, height=20)
    entradaCpf.place(x=150, y=50)

    telefoneUsuario = customtkinter.CTkLabel(
        janelaGerenciamento, fg_color='#efe1e1', text_color='black', text="Telefone do usuário:")
    telefoneUsuario.place(x=20, y=80)
    # telefoneUsuario["bg"] = "#87CEFA"

    entradaTelefone = customtkinter.CTkEntry(
        janelaGerenciamento, fg_color='white', text_color='black', width=280, height=20)
    entradaTelefone.place(x=150, y=80)

    senhaUsuario = customtkinter.CTkLabel(
        janelaGerenciamento, fg_color='#efe1e1', text_color='black', text="Senha do usuário:")
    senhaUsuario.place(x=20, y=110)
    # senhaUsuario["bg"] = "#87CEFA"

    entradaSenha = customtkinter.CTkEntry(
        janelaGerenciamento, fg_color='white', text_color='black', width=280, height=20)
    entradaSenha.place(x=150, y=110)

    nivelUsuario = customtkinter.CTkLabel(janelaGerenciamento, fg_color='#efe1e1', text_color='black',
                                          text="Digite o nível de acesso:\n\nNível 1:Acesso mínimo | Nível 2:Acesso intermediário | Nível 3: Acesso máximo")
    nivelUsuario.place(x=20, y=145)
    # nivelUsuario["bg"] = "#87CEFA"

    entradaNivel = customtkinter.CTkEntry(
        janelaGerenciamento, fg_color='white', text_color='black', width=50, height=20)
    entradaNivel.place(x=340, y=140)

    botaoAddUsuario = customtkinter.CTkButton(
        janelaGerenciamento, fg_color='orange', text="Atualizar usuário", command=gerenciaUsuario)
    botaoAddUsuario.place(x=200, y=200)

    # -----------------------------------BOTÕES PESQUISAR USUARIO-----------------------------------
    nomePesquisa = customtkinter.CTkLabel(
        janelaGerenciamento, fg_color='#efe1e1', text_color='black', text="Nome:")
    nomePesquisa.place(x=20, y=270)
    # nomePesquisa["bg"] = "#87CEFA"

    pesquisaEntrada = customtkinter.CTkEntry(
        janelaGerenciamento, fg_color='white', text_color='black', width=280, height=20)
    pesquisaEntrada.place(x=70, y=270)
    # pesquisaEntrada["bg"] = "#87CEFA"

    botaoPesquisar = customtkinter.CTkButton(
        janelaGerenciamento, fg_color='green', text="Pesquisar", command=pesquisaUsuario)
    botaoPesquisar.place(x=370, y=267)

    # ----------------------------------RESULTADO DA PESQUISA---------------------------------------
    resultadoNome = tk.Label(janelaGerenciamento, text="")
    resultadoNome.place(x=70, y=300)
    resultadoNome["bg"] = "#efe1e1"

    resultadoCpf = tk.Label(janelaGerenciamento, text="")
    resultadoCpf.place(x=70, y=320)
    resultadoCpf["bg"] = "#efe1e1"

    resultadoTelefone = tk.Label(janelaGerenciamento, text="")
    resultadoTelefone.place(x=70, y=340)
    resultadoTelefone["bg"] = "#efe1e1"

    resultadoNivel = tk.Label(janelaGerenciamento, text="")
    resultadoNivel.place(x=70, y=360)
    resultadoNivel["bg"] = "#efe1e1"

    # ------------------------------BOTAO PARA EXCLUIR USUARIO---------------------------------------
    botaoExcluir = customtkinter.CTkButton(
        janelaGerenciamento, fg_color="red", text="Excluir\nUsuário", command=excluirUsuario)
    botaoExcluir.place(x=370, y=320)
    botaoVoltar = customtkinter.CTkButton(
        janelaGerenciamento, fg_color='blue', text="Voltar", command=janelaGerenciamento.destroy)
    botaoVoltar.place(x=370, y=370)

    # -----------------------------RESULTADO DA AÇAO EXCLUIR---------------------------------------
    resultadoExclusao = tk.Label(janelaGerenciamento, text="")
    resultadoExclusao.place(x=160, y=400)
    resultadoExclusao["bg"] = "#efe1e1"

# ----------------------FUNÇÃO REALOCADA PARA JANELA INFORMAÇÕES DE ESTOQUE---------------------------
# -----------------------------FUNÇAO CRIA JANELA PESQUISAR PRODUTO----------------------------------
# def criaJanelaPesquisaProduto():
#    # ---------------------------FUNCIONAMENTO BOTOES PESQUISA PRODUTO-------------------------------
#    def pesquisaProduto():
#        pesquisaProdutoNome = entradaNomeProduto.get()
#        if pesquisaProdutoNome in dicionarioEstoque:
#            produtoResultadoNome["text"] = "Nome:", pesquisaProdutoNome
#            produtoResultadoQuantidade["text"] = "Qtd em estoque:", dicionarioEstoque[pesquisaProdutoNome]
#            janelaPesquisaProduto.geometry("415x140+525+270")
#        else:
#            produtoResultadoNome["text"] = pesquisaProdutoNome, "em falta!"
#            produtoResultadoQuantidade["text"] = ""
#
#    # -------------------------------LAYOUT JANELA PESQUISA PRODUTO---------------------------------
#    janelaPesquisaProduto = tk.Tk()
#
#    largura = 415
#    altura = 100
#
#    largura_tela = janelaPesquisaProduto.winfo_screenwidth()
#    altura_tela = janelaPesquisaProduto.winfo_screenheight()
#    posX = largura_tela / 2 - largura / 2
#    posY = altura_tela / 2 - altura  / 2
#    janelaPesquisaProduto.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))
#
#    #janelaPesquisaProduto.geometry("415x100+525+270")
#    janelaPesquisaProduto.title("Pesquisa Produto")
#    janelaPesquisaProduto["bg"] = "#87CEFA"
#    janelaPesquisaProduto.resizable(width=False, height=False)
#
#    # -----------------------------LAYOUT BOTOES PESQUISA PRODUTO-----------------------------------
#    nomeProduto = tk.Label(janelaPesquisaProduto, text="Nome do produto:")
#    nomeProduto.place(x=20, y=20)
#    nomeProduto["bg"] = "#87CEFA"
#
#    entradaNomeProduto = customtkinter.CTkEntry(janelaPesquisaProduto,fg_color="white", text_color='black')
#    entradaNomeProduto.place(x=140, y=20)
#
#    botaoProcurar = customtkinter.CTkButton(janelaPesquisaProduto,fg_color='green' ,text="Pesquisar", command=pesquisaProduto)
#    botaoProcurar.place(x=60, y=52)
#
#
#
#    botaoVoltar =customtkinter.CTkButton(janelaPesquisaProduto,text="Voltar", command=janelaPesquisaProduto.destroy)
#    botaoVoltar.place(x=220, y=52)
#
#
#    produtoResultadoNome = tk.Label(janelaPesquisaProduto, text="")
#    produtoResultadoNome.place(x=140, y=80)
#    produtoResultadoNome["bg"] = "#87CEFA"
#
#    produtoResultadoQuantidade = tk.Label(janelaPesquisaProduto, text="")
#    produtoResultadoQuantidade.place(x=125, y=100)
#    produtoResultadoQuantidade["bg"] = "#87CEFA"
# -------------------------------------------------------------------------------------------

# ----------FUNÇÃO REALOCADA NA JANELA INFORMAÇÕES DE ESTOQUE (ESTOQUE/HISTÓRICOS)-----------
# ----------------------------------CHECAR ESTOQUE -----------------------------------------
# def criaJanelaEstoque():
#    janelaEstoque = tk.Tk()
#
#    largura = 400
#    altura = 200
#
#    largura_tela = janelaEstoque.winfo_screenwidth()
#    altura_tela = janelaEstoque.winfo_screenheight()
#    posX = largura_tela / 2 - largura / 2
#    posY = altura_tela / 2 - altura  / 2
#    janelaEstoque.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))
#
#    #janelaEstoque.title("Total de Estoque")
#    #janelaEstoque.geometry("400x200")
#    janelaEstoque.resizable(width=False, height=False)
#    janelaEstoque.mainloop()
# -------------------------------------------------------------------------------------------

# ------------------------------------FUNÇAO TELA ADMIN--------------------------------------


def telaMenu(x):
    # --------------------LAYOUT JANELA ADMIN----------------------
    x.destroy()
    janela = customtkinter.CTk(fg_color='#efe1e1')

    largura = 1000 #400
    altura = 700 #350

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura / 2
    janela.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY))
    # janela.geometry("400x350") #400x350
    janela.title("Controle de Estoque - Unibra (Administrador)")
    janela.resizable(width=False, height=False)

    # ----------------------LAYOUT DOS BOTOES--------------------------
    botaoTransacao = customtkinter.CTkButton(
        janela, width=360, fg_color='#CD5C5C', height=50, text="Registrar Transação", command=criaJanelaTransacao)
    botaoTransacao.place(x=20, y=20)
    # botaoTransacao["bg"] = "#B0E0E6"

    botaoCadastro = customtkinter.CTkButton(
        janela, text="Gerenciamento de Usuário", fg_color='#CD5C5C', width=360, height=50, command=criaJanelaGerenciamento)
    botaoCadastro.place(x=20, y=80)
    # botaoCadastro["bg"] = "#B0E0E6"

    # -------------------------------botão inoperante desde a versão 1.2.2, informações mantidas para fins de estudo----------------------------------------
    # botaoPesquisa = customtkinter.CTkButton(janela, text="Pesquisar Produto",fg_color='#CD5C5C' , width=360, height=50, command=criaJanelaPesquisaProduto)
    # botaoPesquisa.place(x=20, y=140)
    # botaoPesquisa["bg"] = "#B0E0E6"
    # ------------------------------------------------------------------------------------------------------------------------------------------------------

    # RAZAO DO Y = 60
    botaoHistorico = customtkinter.CTkButton(
        janela, text="Informações de Estoque", fg_color='#CD5C5C', width=360, height=50, command=criaJanelaEstoque)
    botaoHistorico.place(x=20, y=140)
    # botaoHistorico["bg"] = "#B0E0E6"

    botaoHistoria = customtkinter.CTkButton(janela, text="Conheça nossos Produtos",
                                            fg_color='#CD5C5C', width=360, height=50, command=lambda: webbrowser.open('index.html'))
    botaoHistoria.place(x=20, y=200)
    # botaoHistoria["bg"] = "#FFC0CB"

    # DATA DE ACESSO
    data_acesso = date.today()
    data_str = data_acesso.strftime('%d/%m/%Y')

    logAcesso = customtkinter.CTkLabel(
        janela, text_color='white', text=f'\n Acessado em: \n{data_str} ', fg_color='#CD5C5C', width=360, height=50)
    logAcesso.place(x=20, y=260)

    janela.mainloop()

# ----------------------------------FUNÇAO DE LOGIN---------------------------------

# ------------------- REGISTRO DE USUÁRIO ------------------------------------------#
"""
OBSERVAR QUE NA FUNÇÃO INICIAL DE REGISTRO DE USUÁRIO O {nomeChave} e {senha} será atribuidos a (tulplaUsuario}, 
e consequentemente direcionado ao {dicionarioUsuario}.
A função que traz o valor das duas funções não está rodando no código principal do login.

Obs1.: Relizar o percorrimento da tulpla/dicionário e trazer o valor de nomeChave e senha
Obs2.: Finalizar o projeto com usuario e password != "" e dar entrada com qualquer comando digitado.

Pontos a analisar com calma, evitar raiva e estresse.
"""
def acesso(key1, key2, erro, inicio):

    usuario = key1.get()
    password = key2.get()
    aviso = erro

    if usuario != "" and password != "":
        telaMenu(inicio)
    elif usuario == "cadastro" and password == "cadastro":
        criaJanelaGerenciamento()
    else:
        aviso["text"] = "Usuário ou senha incorretos"

