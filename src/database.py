import sqlite3
from datetime import datetime
from tkinter import messagebox


# Função para criar o banco de dados e a tabela
def criar_banco():
    conexao = sqlite3.connect('boletos.db')
    cursor = conexao.cursor()

    # Criação da tabela de boletos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS boletos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_boleto TEXT NOT NULL,
            valor REAL NOT NULL,
            data_vencimento TEXT NOT NULL,
            frequencia TEXT NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()

# Função para cadastrar boletos no banco de dados
def cadastrar_boleto(nome_boleto, valor, data_vencimento, frequencia):
    conexao = sqlite3.connect('boletos.db')
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO boletos (nome_boleto, valor, data_vencimento, frequencia)
        VALUES (?, ?, ?, ?)
    ''', (nome_boleto, valor, data_vencimento, frequencia))

    conexao.commit()
    conexao.close()

    messagebox.showinfo("Sucesso", "Boleto cadastrado com sucesso!")