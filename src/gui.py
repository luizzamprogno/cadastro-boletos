import customtkinter as ctk
from database import *
from tkinter import messagebox
from datetime import datetime

def validar_entrada(nome_boleto, valor, data_vencimento, frequencia):
    
    if not nome_boleto or not valor or not data_vencimento or not frequencia:
        return 'Preencha todos os campos'
    
    # Verifica se o valor do boleto é numético
    try:
        valor = float(valor)
    except ValueError:
        return 'O valor do boleto deve ser numérico'

    # Verificar formato da data de vencimento
    try:
        datetime.strptime(data_vencimento, '%d-%m-%Y')
    except ValueError:
        return 'A data de vencimento deve estar no formato DD-MM-YYYY'

    # Verificar a frequencia
    if frequencia.lower() not in ['mensal', 'anual', 'semanal']:
        return 'A frequência deve ser mensal, anual ou semanal'

    return None

def init_gui():
    app = ctk.CTk()
    app.title("Cadastro de Boletos")
    app.geometry("400x500")

    # Função para submeter o formulário
    def submit():
        nome_boleto = nome_entry.get()
        valor = valor_entry.get()
        data_vencimento = data_entry.get()
        frequencia = frequencia_entry.get()

        erro = validar_entrada(nome_boleto, valor, data_vencimento, frequencia)
        if erro:
            message.configure(text=erro)
            return
            
        cadastrar_boleto(nome_boleto, valor, data_vencimento, frequencia)
        message.configure(text='Boleto cadastrado com sucesso')

    # Label e campo para nome do boleto
    nome_label = ctk.CTkLabel(app, text="Nome do Boleto:")
    nome_label.pack(pady=10)
    nome_entry = ctk.CTkEntry(app, width=250)
    nome_entry.pack()

    # Label e campo para valor do boleto
    valor_label = ctk.CTkLabel(app, text="Valor:")
    valor_label.pack(pady=10)
    valor_entry = ctk.CTkEntry(app, width=250)
    valor_entry.pack()

    # Label e campo para data de vencimento
    data_label = ctk.CTkLabel(app, text="Data de Vencimento (YYYY-MM-DD):")
    data_label.pack(pady=10)
    data_entry = ctk.CTkEntry(app, width=250)
    data_entry.pack()

    # Label e campo para frequência
    frequencia_label = ctk.CTkLabel(app, text="Frequência (mensal, anual, semanal.):")
    frequencia_label.pack(pady=10)
    frequencia_entry = ctk.CTkEntry(app, width=250)
    frequencia_entry.pack()

    # Botão para submeter o formulário
    submit_button = ctk.CTkButton(app, text="Cadastrar Boleto", command=submit)
    submit_button.pack(pady=20)

    message = ctk.CTkLabel(app, text='')
    message.pack(pady=10)

    app.mainloop()