import tkinter as tk
from utils.calcular_horas_decimais import calcular_horas_decimais

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Horas Decimais")
root.geometry("400x200")  # Definindo o tamanho da janela

# Botão para iniciar o cálculo
calcular_button = tk.Button(root, text="Calcular Horas Decimais", command=calcular_horas_decimais)
calcular_button.pack(pady=20)

# Botão para finalizar a aplicação
fechar_button = tk.Button(root, text="Fechar", command=root.destroy)
fechar_button.pack(pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()
