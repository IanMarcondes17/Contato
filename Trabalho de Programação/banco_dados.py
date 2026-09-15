import sqlite3

# 1. Cria ou conecta ao arquivo de banco de dados 'clientes.db'
conexao = sqlite3.connect('clientes.db')
cursor = conexao.cursor()

# 2. Opercação C (Create Table): Cria a tabela de clientes se ela nao existir 
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    whatsapp TEXT NOT NULL,
    servico TEXT NOT NULL,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP )
''')

def cadastrar_cliente(nome, whatsapp, servico):
    #Opecação C (Create/Insert)
    cursor.execute('''
    INSERT INTO clientes (nome, whatsapp, servico) VALUES (?, ?, ?)
    ''', (nome, whatsapp, servico))
    conexao.commit()
    print(f"✅ Cliente {nome} cadastrado com sucesso!")

def listar_clientes():
    # Operação R (Read/Select): 
    print("\n--- 📋 LISTA DE CLIENTES CADASTRADOS ---")
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()

    for clientes in clientes:
        print(f"ID: {clientes[0]}, Nome: {clientes[1]}, WhatsApp: {clientes[2]}, Serviço: {clientes[3]}, Data de Cadastro: {clientes[4]}")

# --- TESTANDO AS OPERAÇÕES DE BANCO DE DADOS --- 
#Inserindo dados de teste 
cadastrar_cliente('Padaria do João', '1298887777', 'Lading Page Completa')
cadastrar_cliente('Clinica Estetica', '12977776666', 'Cartao de Links/ Bio')

#Lendo os dados salvos
listar_clientes()

#Fecha a conexão
conexao.close()