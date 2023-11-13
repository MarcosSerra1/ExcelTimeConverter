import sys

from cx_Freeze import Executable, setup

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter", "openpyxl"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Calculadora de Horas Decimais",
    version="2.0",
    description="Este é um aplicativo em Python que lê uma planilha Excel, converte horas e minutos em horas decimais e, em seguida, adiciona esses valores de volta à planilha em uma coluna chamada \"valor\". O script usa a biblioteca `openpyxl` para manipular a planilha.",
    options={"build_exe": build_exe_options},
    executables=[Executable("app1.0tk.py", base=base)]
)