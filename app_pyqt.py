


import sys
from PyQt6.QtWidgets import QApplication, QWidget

# Es el "motor" invisible de Qt. Controla todo lo que pasa detrás (clics del mouse, eventos del sistema). 
# Siempre debe haber una sola instancia de esto al final de tu código.

class ventana(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Mi primera ventana")
        self.setGeometry(100, 100, 400, 300)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventanita = ventana()
    ventanita.show()
    
    sys.exit(app.exec())