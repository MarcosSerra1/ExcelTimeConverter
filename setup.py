import sys

from cx_Freeze import Executable, setup

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"],
                     "includes": ["tkinter", "openpyxl", "utils"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="ExcelTimeConverter",
    version="3.0",
    description="Conversor de horas para decimal",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)
