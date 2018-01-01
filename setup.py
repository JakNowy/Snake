import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\test\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\test\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'



cx_Freeze.setup(
    name="Kobas Games: Snake",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ['snakehead3.bmp','apple sound.wav',
                                             'freefall.mp3','jablko.bmp']}},
    description = 'Snake Game',
    executables = [cx_Freeze.Executable(script="snake.py", base = "Win32GUI")]

    )


