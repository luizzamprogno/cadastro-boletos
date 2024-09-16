import sqlite3
from datetime import datetime, timedelta
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
            frequencia TEXT NOT NULL,
            lembrete_enviado INTEGER DEFAULT 0
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

    conexao.commit()

# Verifica boletos que vencem em 3 dias ou menos e não enviou lembrete
def verificar_boletos_proximos_vencimento():
    hoje = datetime.now().date()
    data_limite = hoje + timedelta(days=3)

    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT id, nome_boleto, data_vencimento FROM boletos
            WHERE lembrete_enviado = 0
        ''')
        boletos = cursor.fetchall()

        for boleto in boletos:
            id_boleto, nome_boleto, data_vencimento_str = boleto

            data_vencimento = datetime.strptime(data_vencimento_str, '%d-%m-%Y').date()
            
            if data_vencimento <= data_limite:
                messagebox.showwarning('Lembrete de Boleto', f'O Boleto {nome_boleto}, vence em {data_vencimento.strftime("%d-%m-%Y")}')

                # Atualizar o campo 'lembrete_enviado' para 1
                cursor.execute('''
                    UPDATE boletos
                    SET lembrete_enviado = 1
                    WHERE id = ?
                ''', (id_boleto,))
        conexao.commit()