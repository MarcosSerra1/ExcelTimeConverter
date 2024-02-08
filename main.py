import tkinter as tk
from utils.calcular_horas_decimais import calcular_horas_decimais

# Configuração da janela principal
ROOT = tk.Tk()
ROOT.title("Calculadora de Horas Decimais")
ROOT.geometry("400x200")  # Definindo o tamanho da janela

# Botão para iniciar o cálculo
BUTAO_CALCULAR = tk.Button(ROOT, text="Calcular Horas Decimais", command=calcular_horas_decimais)
BUTAO_CALCULAR.pack(pady=20)

# Botão para finalizar a aplicação
BOTAO_FECHAR = tk.Button(ROOT, text="Fechar", command=ROOT.destroy)
BOTAO_FECHAR.pack(pady=10)

# Iniciar o loop principal da interface gráfica
ROOT.mainloop()
