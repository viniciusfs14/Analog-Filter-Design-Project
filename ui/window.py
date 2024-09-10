# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIGLqSqL.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFrame,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1353, 777)
        MainWindow.setMouseTracking(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"\n"
"QWidget{\n"
"background-color: white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(570, 0))
        self.widget.setMaximumSize(QSize(570, 16777215))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.content = QWidget(self.widget)
        self.content.setObjectName(u"content")
        self.gridLayout_5 = QGridLayout(self.content)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.amax_line = QLineEdit(self.content)
        self.amax_line.setObjectName(u"amax_line")

        self.gridLayout_5.addWidget(self.amax_line, 2, 5, 1, 1, Qt.AlignRight)

        self.label_9 = QLabel(self.content)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)

        self.gridLayout_5.addWidget(self.label_9, 9, 1, 1, 1)

        self.amin_line = QLineEdit(self.content)
        self.amin_line.setObjectName(u"amin_line")

        self.gridLayout_5.addWidget(self.amin_line, 3, 5, 1, 1, Qt.AlignRight)

        self.fs_line = QLineEdit(self.content)
        self.fs_line.setObjectName(u"fs_line")

        self.gridLayout_5.addWidget(self.fs_line, 5, 5, 1, 1, Qt.AlignRight)

        self.fp_line = QLineEdit(self.content)
        self.fp_line.setObjectName(u"fp_line")

        self.gridLayout_5.addWidget(self.fp_line, 4, 5, 1, 1, Qt.AlignRight)

        self.cheby_button = QCheckBox(self.content)
        self.filters = QButtonGroup(MainWindow)
        self.filters.setObjectName(u"filters")
        self.filters.addButton(self.cheby_button)
        self.cheby_button.setObjectName(u"cheby_button")
        self.cheby_button.setFont(font)

        self.gridLayout_5.addWidget(self.cheby_button, 7, 5, 1, 1, Qt.AlignRight)

        self.label_3 = QLabel(self.content)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_5.addWidget(self.label_3, 3, 1, 1, 1, Qt.AlignLeft)

        self.sallenkey_button = QCheckBox(self.content)
        self.topology = QButtonGroup(MainWindow)
        self.topology.setObjectName(u"topology")
        self.topology.addButton(self.sallenkey_button)
        self.sallenkey_button.setObjectName(u"sallenkey_button")
        self.sallenkey_button.setFont(font)
        self.sallenkey_button.setChecked(True)

        self.gridLayout_5.addWidget(self.sallenkey_button, 9, 2, 1, 1, Qt.AlignRight)

        self.mfb_button = QCheckBox(self.content)
        self.topology.addButton(self.mfb_button)
        self.mfb_button.setObjectName(u"mfb_button")
        self.mfb_button.setFont(font)

        self.gridLayout_5.addWidget(self.mfb_button, 9, 5, 1, 1, Qt.AlignRight)

        self.label_2 = QLabel(self.content)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_5.addWidget(self.label_2, 2, 1, 1, 1, Qt.AlignLeft)

        self.label_5 = QLabel(self.content)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_5.addWidget(self.label_5, 5, 1, 1, 1, Qt.AlignLeft)

        self.label_6 = QLabel(self.content)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_5.addWidget(self.label_6, 7, 1, 1, 1)

        self.buteerworth_button = QCheckBox(self.content)
        self.filters.addButton(self.buteerworth_button)
        self.buteerworth_button.setObjectName(u"buteerworth_button")
        self.buteerworth_button.setFont(font)
        self.buteerworth_button.setChecked(True)

        self.gridLayout_5.addWidget(self.buteerworth_button, 7, 2, 1, 1, Qt.AlignRight)

        self.label_4 = QLabel(self.content)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_5.addWidget(self.label_4, 4, 1, 1, 1, Qt.AlignLeft)

        self.label_13 = QLabel(self.content)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.gridLayout_5.addWidget(self.label_13, 6, 1, 1, 1)

        self.K_line = QLineEdit(self.content)
        self.K_line.setObjectName(u"K_line")

        self.gridLayout_5.addWidget(self.K_line, 6, 5, 1, 1, Qt.AlignRight)


        self.gridLayout_2.addWidget(self.content, 2, 0, 2, 1)

        self.bottom_2 = QWidget(self.widget)
        self.bottom_2.setObjectName(u"bottom_2")
        self.gridLayout_17 = QGridLayout(self.bottom_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.projetar_button = QPushButton(self.bottom_2)
        self.projetar_button.setObjectName(u"projetar_button")
        font1 = QFont()
        font1.setBold(True)
        self.projetar_button.setFont(font1)
        self.projetar_button.setStyleSheet(u"QPushButton{\n"
"    background-color: #000040; /* Cor de fundo */\n"
"    color: white; /* Cor do texto */\n"
"    border: none; /* Sem borda */\n"
"    padding: 10px 20px; /* Espa\u00e7amento interno */\n"
"    font-size: 16px; /* Tamanho da fonte */\n"
"    font-weight: bold; /* Texto em negrito */\n"
"    border-radius: 8px; /* Cantos arredondados */\n"
"    outline: none; /* Remover borda de foco */\n"
"    /* Infelizmente, `box-shadow` e `transform` n\u00e3o s\u00e3o suportados em QSS */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1a1aff; /* Cor de fundo ao passar o mouse */\n"
"    color: #fff; /* Cor do texto ao passar o mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0000a0; /* Cor de fundo ao clicar */\n"
"    padding: 11px 21px; /* Simula o movimento ao pressionar */\n"
"}")

        self.gridLayout_17.addWidget(self.projetar_button, 0, 0, 1, 1)

        self.clean_button = QPushButton(self.bottom_2)
        self.clean_button.setObjectName(u"clean_button")
        self.clean_button.setFont(font1)
        self.clean_button.setStyleSheet(u"QPushButton{\n"
"    background-color: #000040; /* Cor de fundo */\n"
"    color: white; /* Cor do texto */\n"
"    border: none; /* Sem borda */\n"
"    padding: 10px 20px; /* Espa\u00e7amento interno */\n"
"    font-size: 16px; /* Tamanho da fonte */\n"
"    font-weight: bold; /* Texto em negrito */\n"
"    border-radius: 8px; /* Cantos arredondados */\n"
"    outline: none; /* Remover borda de foco */\n"
"    /* Infelizmente, `box-shadow` e `transform` n\u00e3o s\u00e3o suportados em QSS */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1a1aff; /* Cor de fundo ao passar o mouse */\n"
"    color: #fff; /* Cor do texto ao passar o mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0000a0; /* Cor de fundo ao clicar */\n"
"    padding: 11px 21px; /* Simula o movimento ao pressionar */\n"
"}")

        self.gridLayout_17.addWidget(self.clean_button, 0, 1, 1, 1)

        self.label = QLabel(self.bottom_2)
        self.label.setObjectName(u"label")

        self.gridLayout_17.addWidget(self.label, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignBottom)


        self.gridLayout_2.addWidget(self.bottom_2, 4, 0, 1, 1)

        self.header = QWidget(self.widget)
        self.header.setObjectName(u"header")
        self.gridLayout_3 = QGridLayout(self.header)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.header)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_3.addWidget(self.label_7, 5, 0, 1, 1, Qt.AlignHCenter)

        self.line = QFrame(self.header)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 4, 0, 1, 1)

        self.label_8 = QLabel(self.header)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/newPrefix/logo.png"))

        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1, Qt.AlignHCenter)

        self.titulo = QLabel(self.header)
        self.titulo.setObjectName(u"titulo")
        font2 = QFont()
        font2.setPointSize(25)
        self.titulo.setFont(font2)

        self.gridLayout_3.addWidget(self.titulo, 2, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.header, 0, 0, 1, 1)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_6 = QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget = QTabWidget(self.widget_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Polos_page = QWidget()
        self.Polos_page.setObjectName(u"Polos_page")
        self.gridLayout_11 = QGridLayout(self.Polos_page)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.graf_polos = QWidget(self.Polos_page)
        self.graf_polos.setObjectName(u"graf_polos")
        self.gridLayout_12 = QGridLayout(self.graf_polos)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_polos = QLabel(self.graf_polos)
        self.label_polos.setObjectName(u"label_polos")

        self.gridLayout_12.addWidget(self.label_polos, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_11.addWidget(self.graf_polos, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Polos_page, "")
        self.T_s_page = QWidget()
        self.T_s_page.setObjectName(u"T_s_page")
        self.gridLayout_13 = QGridLayout(self.T_s_page)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.ts_widget = QWidget(self.T_s_page)
        self.ts_widget.setObjectName(u"ts_widget")
        self.gridLayout_14 = QGridLayout(self.ts_widget)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.ts_label = QLabel(self.ts_widget)
        self.ts_label.setObjectName(u"ts_label")

        self.gridLayout_14.addWidget(self.ts_label, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_13.addWidget(self.ts_widget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.T_s_page, "")
        self.Bode_page = QWidget()
        self.Bode_page.setObjectName(u"Bode_page")
        self.gridLayout_15 = QGridLayout(self.Bode_page)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.graf_bode = QWidget(self.Bode_page)
        self.graf_bode.setObjectName(u"graf_bode")
        self.gridLayout_16 = QGridLayout(self.graf_bode)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.bode_label = QLabel(self.graf_bode)
        self.bode_label.setObjectName(u"bode_label")

        self.gridLayout_16.addWidget(self.bode_label, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_15.addWidget(self.graf_bode, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Bode_page, "")
        self.SallenKey_page = QWidget()
        self.SallenKey_page.setObjectName(u"SallenKey_page")
        self.gridLayout_7 = QGridLayout(self.SallenKey_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_3 = QWidget(self.SallenKey_page)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_9 = QGridLayout(self.widget_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(u":/newPrefix/sallen2.png"))
        self.label_11.setScaledContents(False)

        self.gridLayout_9.addWidget(self.label_11, 1, 0, 1, 1, Qt.AlignHCenter)

        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_9.addWidget(self.label_10, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.table_components = QTableWidget(self.widget_3)
        if (self.table_components.columnCount() < 5):
            self.table_components.setColumnCount(5)
        font3 = QFont()
        font3.setPointSize(11)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.table_components.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_components.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_components.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_components.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_components.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.table_components.rowCount() < 1):
            self.table_components.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_components.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.table_components.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.table_components.setItem(0, 2, __qtablewidgetitem7)
        self.table_components.setObjectName(u"table_components")
        self.table_components.setMinimumSize(QSize(520, 0))
        self.table_components.setStyleSheet(u"QTableWidget, QTableView {\n"
"    background-color: white; /* Cor de fundo da tabela */\n"
"    gridline-color: black; /* Cor das linhas da grade */\n"
"    border: 1px solid #dcdcdc; /* Borda ao redor da tabela */\n"
"    font-size: 14px; /* Tamanho da fonte */\n"
"    color: #333; /* Cor do texto */\n"
"    selection-background-color: #1a73e8; /* Cor de fundo ao selecionar */\n"
"    selection-color: white; /* Cor do texto ao selecionar */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #000040; /* Cor de fundo do cabe\u00e7alho */\n"
"    color: white; /* Cor do texto do cabe\u00e7alho */\n"
"    padding: 5px; /* Espa\u00e7amento interno */\n"
"    border: 1px solid #dcdcdc; /* Borda ao redor das c\u00e9lulas do cabe\u00e7alho */\n"
"    font-weight: bold; /* Negrito para o texto do cabe\u00e7alho */\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #000040; /* Cor do canto superior esquerdo da tabela */\n"
"    border: 1px solid #dcdcdc; /* Borda ao redor do canto */\n"
""
                        "}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 8px; /* Espa\u00e7amento interno das c\u00e9lulas */\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_9.addWidget(self.table_components, 2, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_7.addWidget(self.widget_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.SallenKey_page, "")
        self.MFB_page = QWidget()
        self.MFB_page.setObjectName(u"MFB_page")
        self.gridLayout_8 = QGridLayout(self.MFB_page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_4 = QWidget(self.MFB_page)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_10 = QGridLayout(self.widget_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout_10.addWidget(self.label_12, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u":/newPrefix/mfb.png"))

        self.gridLayout_10.addWidget(self.label_14, 1, 0, 1, 1, Qt.AlignHCenter)

        self.table_components2 = QTableWidget(self.widget_4)
        if (self.table_components2.columnCount() < 6):
            self.table_components2.setColumnCount(6)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_components2.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_components2.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_components2.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_components2.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_components2.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_components2.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        if (self.table_components2.rowCount() < 1):
            self.table_components2.setRowCount(1)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_components2.setVerticalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.table_components2.setItem(0, 0, __qtablewidgetitem15)
        self.table_components2.setObjectName(u"table_components2")
        self.table_components2.setMinimumSize(QSize(610, 0))
        self.table_components2.setStyleSheet(u"QTableWidget, QTableView {\n"
"    background-color: white; /* Cor de fundo da tabela */\n"
"    gridline-color: black; /* Cor das linhas da grade */\n"
"    border: 1px solid #dcdcdc; /* Borda ao redor da tabela */\n"
"    font-size: 14px; /* Tamanho da fonte */\n"
"    color: #333; /* Cor do texto */\n"
"    selection-background-color: #1a73e8; /* Cor de fundo ao selecionar */\n"
"    selection-color: white; /* Cor do texto ao selecionar */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #000040; /* Cor de fundo do cabe\u00e7alho */\n"
"    color: white; /* Cor do texto do cabe\u00e7alho */\n"
"    padding: 5px; /* Espa\u00e7amento interno */\n"
"    border: 1px solid #dcdcdc; /* Borda ao redor das c\u00e9lulas do cabe\u00e7alho */\n"
"    font-weight: bold; /* Negrito para o texto do cabe\u00e7alho */\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #000040; /* Cor do canto superior esquerdo da tabela */\n"
"    border: 1px solid #dcdcdc; /* Borda ao redor do canto */\n"
""
                        "}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 8px; /* Espa\u00e7amento interno das c\u00e9lulas */\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_10.addWidget(self.table_components2, 2, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_8.addWidget(self.widget_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.MFB_page, "")

        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.amax_line.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Selecione a topol\u00f3gia do filtro:", None))
        self.amin_line.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.fs_line.setText(QCoreApplication.translate("MainWindow", u"10000", None))
        self.fp_line.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.cheby_button.setText(QCoreApplication.translate("MainWindow", u"Chebyshev", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Amin:", None))
        self.sallenkey_button.setText(QCoreApplication.translate("MainWindow", u"Sallen-Key", None))
        self.mfb_button.setText(QCoreApplication.translate("MainWindow", u"MFB", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Amax:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fs:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Selecione o tipo de filtro: ", None))
        self.buteerworth_button.setText(QCoreApplication.translate("MainWindow", u"Butterworth", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Fp:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Ganho:", None))
        self.K_line.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.projetar_button.setText(QCoreApplication.translate("MainWindow", u"Projetar", None))
        self.clean_button.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Desenvolvido por Vin\u00edcius Fernandes Silvestre", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Insira abaixo os par\u00e2metros para a proje\u00e7\u00e3o do filtro", None))
        self.label_8.setText("")
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"Projeto de Filtros Anal\u00f3gicos", None))
        self.label_polos.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Polos_page), QCoreApplication.translate("MainWindow", u"Polos", None))
        self.ts_label.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.T_s_page), QCoreApplication.translate("MainWindow", u"T(s)", None))
        self.bode_label.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Bode_page), QCoreApplication.translate("MainWindow", u"Bode", None))
        self.label_11.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Circuito Sallen-Key", None))
        ___qtablewidgetitem = self.table_components.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Bloco", None));
        ___qtablewidgetitem1 = self.table_components.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"R1", None));
        ___qtablewidgetitem2 = self.table_components.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"R2", None));
        ___qtablewidgetitem3 = self.table_components.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"C1", None));
        ___qtablewidgetitem4 = self.table_components.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"C2", None));

        __sortingEnabled = self.table_components.isSortingEnabled()
        self.table_components.setSortingEnabled(False)
        self.table_components.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SallenKey_page), QCoreApplication.translate("MainWindow", u"Sallen-Key", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Circuito MFB", None))
        self.label_14.setText("")
        ___qtablewidgetitem5 = self.table_components2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Bloco", None));
        ___qtablewidgetitem6 = self.table_components2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"R1", None));
        ___qtablewidgetitem7 = self.table_components2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"R2", None));
        ___qtablewidgetitem8 = self.table_components2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"R3", None));
        ___qtablewidgetitem9 = self.table_components2.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"C1", None));
        ___qtablewidgetitem10 = self.table_components2.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"C2", None));

        __sortingEnabled1 = self.table_components2.isSortingEnabled()
        self.table_components2.setSortingEnabled(False)
        self.table_components2.setSortingEnabled(__sortingEnabled1)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MFB_page), QCoreApplication.translate("MainWindow", u"MFB", None))
    # retranslateUi

