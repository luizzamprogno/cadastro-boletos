import sqlite3
from datetime import datetime
from tkinter import messagebox

# Gerenciar a conexão com banco de dados
def conectar():
    return sqlite3.connect('boletos.db')

# Criar o banco de dados e a tabela
def criar_banco():
    with conectar() as conexao:
        cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS boletos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_boleto TEXT NOT NULL,
            valor REAL NOT NULL,
            data_vencimento TEXT NOT NULL,
            frequencia TEXT NOT NULL
        )
    ''')

# Função para cadastrar boletos no banco de dados
def cadastrar_boleto(nome_boleto, valor, data_vencimento, frequencia):
    with conectar() as conexao:
        cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO boletos (nome_boleto, valor, data_vencimento, frequencia)
        VALUES (?, ?, ?, ?)
    ''', (nome_boleto, valor, data_vencimento, frequencia))

    messagebox.showinfo("Sucesso", "Boleto cadastrado com sucesso!")