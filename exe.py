
import subprocess
import sys
import os

# Lanza Jupyter Notebook automáticamente
notebook_dir = os.getcwd()  # Carpeta actual (puedes cambiarla si lo necesitas)
subprocess.run([sys.executable, "-m", "notebook", notebook_dir])


