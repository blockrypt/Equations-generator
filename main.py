import sys
from PyQt5.QtWidgets import QApplication
from ui_components import MathSolverApp

def main():
    app = QApplication(sys.argv)
    ex = MathSolverApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
