import customtkinter as ctk
from database import *

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

        # Verifica se todos os campos estão preenchidos
        if not nome_boleto or not valor or not data_vencimento or not frequencia:
            message.configure(text="Preencha todos os campos")

        try:
            valor = float(valor)  # Converte o valor para float
        except ValueError:
            message.configure(text="O valor do boleto deve ser numérico")
            
        cadastrar_boleto(nome_boleto, valor, data_vencimento, frequencia)

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
    frequencia_label = ctk.CTkLabel(app, text="Frequência (mensal, anual, etc.):")
    frequencia_label.pack(pady=10)
    frequencia_entry = ctk.CTkEntry(app, width=250)
    frequencia_entry.pack()

    # Botão para submeter o formulário
    submit_button = ctk.CTkButton(app, text="Cadastrar Boleto", command=submit)
    submit_button.pack(pady=20)

    message = ctk.CTkLabel(app, text='')
    message.pack(pady=10)

    app.mainloop()