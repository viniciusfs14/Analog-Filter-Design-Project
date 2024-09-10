from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt, QRect
from PySide6.QtGui import QColor, QBrush, QPalette

class AnimatedTable(QTableWidget):
    def __init__(self):
        super().__init__(5, 3)
        self.setGeometry(100, 100, 400, 300)

        # Preencher tabela com valores de exemplo
        for row in range(5):
            for col in range(3):
                self.setItem(row, col, QTableWidgetItem(f'Item {row}, {col}'))
        
        # Conectar sinal de seleção de célula para iniciar animação
        self.cellClicked.connect(self.animate_selection)

    def animate_selection(self, row, col):
        item = self.item(row, col)
        if item:
            # Configura a animação
            anim = QPropertyAnimation(self, b'geometry')
            anim.setDuration(500)  # Duração da animação (500 milissegundos)
            anim.setStartValue(self.geometry())
            anim.setEndValue(QRect(self.x(), self.y(), self.width(), self.height() + 10))
            anim.setEasingCurve(QEasingCurve.InOutQuad)
            anim.start()
            
            # Altere o fundo da célula manualmente com uma cor
            self.setItem(row, col, QTableWidgetItem(f'Item {row}, {col}'))
            self.item(row, col).setBackground(QBrush(QColor(26, 115, 232)))

            # Após 500 milissegundos, restaure a cor original
            QTimer.singleShot(500, lambda: self.item(row, col).setBackground(QBrush(QColor(255, 255, 255))))

if __name__ == '__main__':
    app = QApplication([])
    table = AnimatedTable()
    table.show()
    app.exec()
