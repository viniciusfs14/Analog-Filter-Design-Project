import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as fc
import control as c 
from ui.window import Ui_MainWindow
from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QTabWidget, QMainWindow, QApplication
from PySide6.QtGui import QPixmap, QImage
import sys, os
from ui.images.fonte_rc import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Filtros Analógicos')
        self.projetar_button.clicked.connect(self.start_function)
        self.clean_button.clicked.connect(self.clear_var)
        
    def start_function(self):
        self.widget_2.show()
        self.Amax = float(self.amax_line.text())
        self.Amin = float(self.amin_line.text())
        self.Fp = float(self.fp_line.text())
        self.Fs = float(self.fs_line.text())
        self.K = float(self.K_line.text())
        self.Wp = (2 * np.pi * self.Fp)
        self.Ws = (2 * np.pi * self.Fs)
        
        if self.buteerworth_button.isChecked() and self.sallenkey_button.isChecked():  
            self.butterkey()
        if self.buteerworth_button.isChecked() and self.mfb_button.isChecked():
            self.buttermfb()
        if self.cheby_button.isChecked() and self.sallenkey_button.isChecked():
            self.chebykey()
        if self.cheby_button.isChecked() and self.mfb_button.isChecked():
            self.chebymfb()
 
    def varbutter(self):
        self.e = np.sqrt(10**(self.Amax/10) - 1)
        self.n = (np.log10((10**(self.Amin/10) - 1) / (self.e**2))) / (2 * np.log10(self.Ws/self.Wp))
        self.N = np.ceil(self.n)
        self.W0 = self.Wp * ((1/self.e)**(1/self.N))

    def varcheby(self):
        self.e = np.sqrt(10**(self.Amax/10)-1)
        self.N = int(np.ceil((np.arccosh(np.sqrt((10**(self.Amin/10)-1)/self.e**2)))/np.arccosh(self.Ws/self.Wp)))   
                        
    def transfer_butter(self):
        self.Tnum = self.K * (self.W0**self.N)
        self.Tden = np.poly(self.polos)
        self.T = c.TransferFunction(self.Tnum, self.Tden)
        print(self.T)
        
        # Extraindo a parte real dos coeficientes
        real_Tnum = np.real(self.Tnum)
        real_Tden = np.real(self.Tden)
        
        fig, ax = plt.subplots(figsize=(6.4, 4.8))

        transfer_function_latex = r"$H(s) = \frac{" + f"{real_Tnum:.2e}" + r"}{" + r" + ".join([f"{c:.2e}s^{len(real_Tden)-i-1}" for i, c in enumerate(real_Tden)]) + r"}$"
        ax.text(0.5, 0.5, transfer_function_latex, fontsize=15, ha='center', va='center')
        ax.axis('off')
        ax.set_title('Função de Transferência', fontsize=20)

        canvas = fc(fig)
        canvas.draw()

        buf = canvas.buffer_rgba()
        qimage = QImage(buf, canvas.width(), canvas.height(), canvas.width() * 4, QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qimage)

        self.ts_label.setPixmap(pixmap)
        
    def bode(self):
        # Cálculo manual do diagrama de Bode
        x = np.logspace(np.log10(self.Wp/100), np.log10(100*self.Wp), 1000)
        H = np.abs(np.polyval([self.Tnum], 1j*x)/np.polyval(self.Tden, 1j*x))
        
        # Diagrama de Bode (Magnitude)
        Hdb = 20 * np.log10(H)
        
        # Diagrama de Bode (Fase)
        fase = np.zeros_like(x)
        for polo in self.polos:
            wp = np.abs(polo)
            if wp != 0:
                fase -= np.arctan(x/wp)
            
        fase_deg = np.degrees(fase)
        
        # Criação das figuras com Matplotlib
        fig, axs = plt.subplots(1, 2, figsize=(8, 4.8))
        
        # Magnitude
        axs[0].semilogx(x, Hdb)
        axs[0].set_xlabel('Frequência [rad/s]')
        axs[0].set_ylabel('Magnitude [dB]')
        axs[0].set_title('Magnitude')
        axs[0].grid(which='both', linestyle='--', linewidth=0.5)
        
        # Fase
        axs[1].semilogx(x, fase_deg)
        axs[1].set_xlabel('Frequência [rad/s]')
        axs[1].set_ylabel('Fase [°]')
        axs[1].set_title('Fase')
        axs[1].grid(which='both', linestyle='--', linewidth=0.5)
        
        plt.tight_layout()

        # Converter a figura para QPixmap
        canvas = fc(fig)
        canvas.draw()

        buf = canvas.buffer_rgba()
        qimage = QImage(buf, canvas.width(), canvas.height(), canvas.width() * 4, QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qimage)

        # Exibir na interface
        self.bode_label.setPixmap(pixmap)
        
    def comp_sallenkey(self):
        # Cálculo dos componentes R e C
        self.R1 = []
        self.R2 = []
        self.C1 = []
        self.C2 = []
        
        k = len(self.polos)
        
        for i in range(0, k//2):
            polo1 = self.polos[i].real
            polo2 = self.polos[i].imag
            W0 = np.abs(self.polos[i])
            ksi = abs(polo2)/abs(polo1)
            Q = 1/(2*ksi)
            n = 1.1 * 4*(Q**2)
            m = (-(2 - (n / (Q**2))) + np.sqrt(((2 - (n / (Q**2)))**2) - 4)) / 2
            
            C1v = 10e-9
            C2v = n * C1v
            R2v = 1/(W0 * C1v * np.sqrt(m * n))
            R1v = m * R2v
            
            self.C1.append(C1v)
            self.R1.append(R1v)
            self.R2.append(R2v)
            self.C2.append(C2v)
        
        self.R1 = [f"{r:.2e}" for r in self.R1]
        self.R2 = [f"{r:.2e}" for r in self.R2]
        self.C1 = [f"{r:.2e}" for r in self.C1]
        self.C2 = [f"{r:.2e}" for r in self.C2]
        
        # Looping se o vetor dos componentes tiverem mais de 1 componente, se tiver ele vai adicionando mais linhas
        for i in range(len(self.R1)):
            if i >= self.table_components.rowCount():  
                self.table_components.insertRow(i)
                
            bloco_item = QtWidgets.QTableWidgetItem(f'{i+1}')
            self.table_components.setItem(i, 0, bloco_item)       
               
            self.table_components.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.R1[i])))
            self.table_components.setItem(i, 2, QtWidgets.QTableWidgetItem(str(self.R2[i])))
            self.table_components.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.C1[i])))
            self.table_components.setItem(i, 4, QtWidgets.QTableWidgetItem(str(self.C2[i])))
      
    def polosbutter(self):
        i = 1
        self.tetac = []  # Valores em graus
        teta = []  # Valores em radianos
        self.polos = []  # Polos calculados
            
        while i <= self.N:
            if i == 1:
                tetac_i = (180/(2*self.N))
                teta_i = np.deg2rad(tetac_i)
                polo = self.W0 * (-np.sin(teta_i) + 1j * np.cos(teta_i))
            else:
                tetac_i = (180 * (2 * i - 1) / (2 * self.N))
                teta_i = np.deg2rad(tetac_i)
                polo = self.W0 * (-np.sin(teta_i) + 1j * np.cos(teta_i))
                
            teta.append(teta_i)
            self.tetac.append(tetac_i)
            self.polos.append(polo)
            i += 1
        
        self.polos = np.array(self.polos)
       

        fig, ax = plt.subplots()
        ax.scatter(np.real(self.polos), np.imag(self.polos), color='red', marker='x')
        
        for polo in self.polos:
            ax.plot([0, np.real(polo)], [0, np.imag(polo)], color='blue', linestyle='--', linewidth=0.5)
        
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.set_xlabel('Parte Real')
        ax.set_ylabel('Parte Imaginária')
        ax.set_title('Polos do Filtro Butterworth')
        ax.grid()
        
        # Converter o gráfico para QPixmap
        canvas = fc(fig)
        canvas.draw()
        
        buf = canvas.buffer_rgba()
        qimage = QImage(buf, canvas.width(), canvas.height(), canvas.width() * 4, QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qimage)
        
        self.label_polos.setPixmap(pixmap)
        
    def butterkey(self): # Função para chamar todas as funções para o butterworth e sallen-key
       self.varbutter()
       self.polosbutter()
       self.transfer_butter()
       self.bode()
       self.comp_sallenkey()
       
    def buttermfb(self): # Função para chamar todas as funções para o butterworth e MFB
       self.varbutter() 
       self.polosbutter()
       self.transfer_butter()
       self.bode()
       self.comp_mfb()
            
    def poloscheby(self):
        self.polos = []  # Variável que armazena os valores dos polos
    
        for i in range(1, self.N+1):
            polo = -self.Wp*np.sin(((2*i - 1)/self.N)*(np.pi/2))*np.sinh(1/self.N * np.arcsinh(1/self.e)) + 1j*self.Wp*np.cos(((2*i - 1)/self.N)*(np.pi/2))*np.cosh(1/self.N * np.arcsinh(1/self.e))
            self.polos.append(polo)
        
        print('-'*50)
        print('Polos:')
        
        for polo in self.polos:
            print(f'    {polo.real:.2e} + {polo.imag:.2e}j')
        print('-'*50)

        fig, ax = plt.subplots()
        ax.scatter(np.real(self.polos), np.imag(self.polos), color='red', marker='x')
        
        for polo in self.polos:
            ax.plot([0, np.real(polo)], [0, np.imag(polo)], color='blue', linestyle='--', linewidth=0.5)
        
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.set_xlabel('Parte Real')
        ax.set_ylabel('Parte Imaginária')
        ax.set_title('Polos do Filtro Chebyshev')
        ax.grid()
        
        # Converter o gráfico para QPixmap
        canvas = fc(fig)
        canvas.draw()
        
        buf = canvas.buffer_rgba()
        qimage = QImage(buf, canvas.width(), canvas.height(), canvas.width() * 4, QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qimage)
        
        self.label_polos.setPixmap(pixmap)
        
    def comp_mfb(self):
        # Cálculo dos componentes R e C
        self.R1 = []
        self.R2 = []
        self.R3 = []
        self.C1 = []
        self.C2 = []
        self.K_n = self.K**(1/np.floor(self.N/2))
        self.k = len(self.polos)
        
        for i in range(0, self.k//2):  
            self.polo1 = self.polos[i].real
            self.polo2 = self.polos[i].imag
            g = 1 + self.K_n
            ksi = self.polo2/abs(self.polos[i])
            W0 = np.abs(self.polos[i])
            Q = 1/(2*ksi)
            #print('Valor de Q: ', Q)
            n = 1.1*g*4*(Q**2)
            #print('valor de n: ', n)
            a = (2/g) - (n/((g**2)*Q**2))
            m = (- a + np.sqrt((a**2)-(4/(g**2)))/2)
            C1v = 1.0e-9
            C2v = (n * C1v)
            R2v = (1/(W0 * C1v * np.sqrt(m * n)))
            R3v = (m * R2v)
            R1v = (R3v/self.K)
            
            self.C1.append(C1v)
            self.R1.append(R1v)
            self.R2.append(R2v)
            self.R3.append(R3v)
            self.C2.append(C2v)
            
        self.R1 = [f"{r:.2e}" for r in self.R1]
        self.R2 = [f"{r:.2e}" for r in self.R2]
        self.R3 = [f"{r:.2e}" for r in self.R3]
        self.C1 = [f"{r:.2e}" for r in self.C1]
        self.C2 = [f"{r:.2e}" for r in self.C2]
        
        # Looping se o vetor dos componentes tiverem mais de 1 componente, se tiver ele vai adicionando mais linhas
        for i in range(len(self.R1)):
            if i >= self.table_components2.rowCount():  
                self.table_components2.insertRow(i)
                
            bloco_item = QtWidgets.QTableWidgetItem(f'{i+1}')
            self.table_components2.setItem(i, 0, bloco_item)       
               
            self.table_components2.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.R1[i])))
            self.table_components2.setItem(i, 2, QtWidgets.QTableWidgetItem(str(self.R2[i])))
            self.table_components2.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.R3[i])))
            self.table_components2.setItem(i, 4, QtWidgets.QTableWidgetItem(str(self.C1[i])))
            self.table_components2.setItem(i, 5, QtWidgets.QTableWidgetItem(str(self.C2[i])))
                
    def transfer_cheby(self):
        self.Tnum = np.array([self.K*self.Wp**self.N])
        self.Tden = np.poly(self.polos)*(self.e*2**(self.N-1))
        self.T = c.TransferFunction(self.Tnum, self.Tden)
        
        # Extraindo a parte real dos coeficientes
        real_Tnum = np.real(self.Tnum)[0]
        real_Tden = np.real(self.Tden)
        
        fig, ax = plt.subplots(figsize=(10, 5))

        transfer_function_latex = r"$H(s) = \frac{" + f"{real_Tnum:.2e}" + r"}{" + r" + ".join([f"{c:.2e}s^{len(real_Tden)-i-1}" for i, c in enumerate(real_Tden)]) + r"}$"
        ax.text(0.5, 0.5, transfer_function_latex, fontsize=15, ha='center', va='center')
        ax.axis('off')
        ax.set_title('Função de Transferência', fontsize=20)

        canvas = fc(fig)
        canvas.draw()

        buf = canvas.buffer_rgba()
        qimage = QImage(buf, canvas.width(), canvas.height(), canvas.width() * 4, QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qimage)

        self.ts_label.setPixmap(pixmap)   
    
    def chebykey(self):
        self.varcheby()
        self.poloscheby()
        self.transfer_cheby()
        self.bode()  
        self.comp_sallenkey()  
        
    def chebymfb(self):
        self.varcheby()
        self.poloscheby()
        self.transfer_cheby()
        self.bode()  
        self.comp_mfb()

    def clear_var(self):
        self.R1 = []
        self.R2 = []
        self.R3 = []
        self.C1 = []
        self.C2 = []
        self.polos = []
        
        self.table_components.setRowCount(0)
        self.table_components2.setRowCount(0)
        
        self.label_polos.clear()
        self.ts_label.clear()
        self.bode_label.clear()
        
        self.T = None
        self.Tnum = None
        self.Tden = None
    
    
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show() 
sys.exit(app.exec())
