# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poresizerwidget.ui'
#
# Created: Wed Oct 07 16:36:34 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PoreSizerWidget(object):
    def setupUi(self, PoreSizerWidget):
        PoreSizerWidget.setObjectName(_fromUtf8("PoreSizerWidget"))
        PoreSizerWidget.resize(800, 400)
        PoreSizerWidget.setWindowTitle(_fromUtf8(""))
        PoreSizerWidget.setAutoFillBackground(False)
        self.gridLayout = QtGui.QGridLayout(PoreSizerWidget)
        self.gridLayout.setContentsMargins(10, 100, 10, 10)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_10 = QtGui.QLabel(PoreSizerWidget)
        self.label_10.setGeometry(QtCore.QRect(340, 190, 151, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 4, 4, 1, 2)
        self.current_blockade = QtGui.QLineEdit(PoreSizerWidget)
        self.current_blockade.setGeometry(QtCore.QRect(220, 190, 51, 21))
        self.current_blockade.setObjectName(_fromUtf8("current_blockade"))
        self.gridLayout.addWidget(self.current_blockade, 4, 2, 1, 1)
        self.analyte_diameter = QtGui.QLineEdit(PoreSizerWidget)
        self.analyte_diameter.setGeometry(QtCore.QRect(220, 270, 51, 21))
        self.analyte_diameter.setObjectName(_fromUtf8("analyte_diameter"))
        self.gridLayout.addWidget(self.analyte_diameter, 6, 2, 1, 1)
        self.label_3 = QtGui.QLabel(PoreSizerWidget)
        self.label_3.setGeometry(QtCore.QRect(300, 10, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
#        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 3)
        self.open_pore_current = QtGui.QLineEdit(PoreSizerWidget)
        self.open_pore_current.setGeometry(QtCore.QRect(220, 150, 51, 21))
        self.open_pore_current.setObjectName(_fromUtf8("open_pore_current"))
        self.gridLayout.addWidget(self.open_pore_current, 3, 2, 1, 1)
        self.label_2 = QtGui.QLabel(PoreSizerWidget)
        self.label_2.setGeometry(QtCore.QRect(410, 60, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 5, 1, 1)
        self.pore_diameter = QtGui.QTextBrowser(PoreSizerWidget)
        self.pore_diameter.setGeometry(QtCore.QRect(530, 190, 51, 21))
        self.pore_diameter.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pore_diameter.setAcceptDrops(True)
        self.pore_diameter.setFrameShape(QtGui.QFrame.Box)
        self.pore_diameter.setFrameShadow(QtGui.QFrame.Plain)
        self.pore_diameter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pore_diameter.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pore_diameter.setObjectName(_fromUtf8("pore_diameter"))
        self.pore_diameter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.gridLayout.addWidget(self.pore_diameter, 4, 6, 1, 1)
        self.label_7 = QtGui.QLabel(PoreSizerWidget)
        self.label_7.setGeometry(QtCore.QRect(10, 230, 181, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 2)
        self.label_8 = QtGui.QLabel(PoreSizerWidget)
        self.label_8.setGeometry(QtCore.QRect(10, 270, 151, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 2)
        self.voltage = QtGui.QLineEdit(PoreSizerWidget)
        self.voltage.setGeometry(QtCore.QRect(220, 110, 51, 21))
        self.voltage.setObjectName(_fromUtf8("voltage"))
        self.gridLayout.addWidget(self.voltage, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(PoreSizerWidget)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 81, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_9 = QtGui.QLabel(PoreSizerWidget)
        self.label_9.setGeometry(QtCore.QRect(10, 310, 151, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 2)
        self.pore_eff_thickness = QtGui.QTextBrowser(PoreSizerWidget)
        self.pore_eff_thickness.setGeometry(QtCore.QRect(530, 230, 51, 21))
        self.pore_eff_thickness.setFrameShape(QtGui.QFrame.Box)
        self.pore_eff_thickness.setFrameShadow(QtGui.QFrame.Plain)
        self.pore_eff_thickness.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pore_eff_thickness.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pore_eff_thickness.setObjectName(_fromUtf8("pore_eff_thickness"))
        self.pore_eff_thickness.setMaximumSize(QtCore.QSize(16777215, 30))
        self.gridLayout.addWidget(self.pore_eff_thickness, 5, 6, 1, 1)
        self.buffer_conductance = QtGui.QLineEdit(PoreSizerWidget)
        self.buffer_conductance.setGeometry(QtCore.QRect(220, 230, 51, 21))
        self.buffer_conductance.setObjectName(_fromUtf8("buffer_conductance"))
        self.gridLayout.addWidget(self.buffer_conductance, 5, 2, 1, 1)
        self.label_11 = QtGui.QLabel(PoreSizerWidget)
        self.label_11.setGeometry(QtCore.QRect(320, 230, 191, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 5, 4, 1, 2)
        self.label_6 = QtGui.QLabel(PoreSizerWidget)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 151, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 2)
        self.compute_button = QtGui.QPushButton(PoreSizerWidget)
        self.compute_button.setGeometry(QtCore.QRect(190, 360, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.compute_button.setFont(font)
        self.compute_button.setObjectName(_fromUtf8("compute_button"))
        self.gridLayout.addWidget(self.compute_button, 8, 2, 1, 1)
        self.label_5 = QtGui.QLabel(PoreSizerWidget)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 151, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 2)
        self.label = QtGui.QLabel(PoreSizerWidget)
        self.label.setGeometry(QtCore.QRect(100, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.precision = QtGui.QLineEdit(PoreSizerWidget)
        self.precision.setGeometry(QtCore.QRect(220, 310, 51, 21))
        self.precision.setObjectName(_fromUtf8("precision"))
        self.gridLayout.addWidget(self.precision, 7, 2, 1, 1)
        self.line = QtGui.QFrame(PoreSizerWidget)
        self.line.setGeometry(QtCore.QRect(290, 70, 16, 331))
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 3, 7, 1)

        self.retranslateUi(PoreSizerWidget)
        QtCore.QMetaObject.connectSlotsByName(PoreSizerWidget)

    def retranslateUi(self, PoreSizerWidget):
        self.label_10.setText(_translate("PoreSizerWidget", "<html><head/><body><p><span style=\" color:#cc0033;\">Pore Diameter (nm)</span></p></body></html>", None))
        self.current_blockade.setText(_translate("PoreSizerWidget", "0.5", None))
        self.analyte_diameter.setText(_translate("PoreSizerWidget", "2.2", None))
        self.label_3.setText(_translate("PoreSizerWidget", "Pore Sizer", None))
        self.open_pore_current.setText(_translate("PoreSizerWidget", "0.7", None))
        self.label_2.setText(_translate("PoreSizerWidget", "<html><head/><body><p><span style=\" text-decoration: underline; color:#cc0033;\">Outputs</span></p></body></html>", None))
        self.label_7.setText(_translate("PoreSizerWidget", "<html><head/><body><p><span style=\" color:#0000ff;\">Buffer Conductance (mS/cm)</span></p></body></html>", None))
        self.label_8.setText(_translate("PoreSizerWidget", "<html><head/><body><p><span style=\" color:#0000ff;\">Analyte Diameter (nm)</span></p></body></html>", None))
        self.voltage.setText(_translate("PoreSizerWidget", "200", None))
        self.label_4.setText(_translate("PoreSizerWidget", "<html><head/><body><p><span style=\" color:#0000ff;\">Voltage (mV)</span></p></body></html>", None))
        self.label_9.setText(_translate("PoreSizerWidget", "<html><head/><body><p><span style=\" color:#0000ff;\">Precision (nm)</span></p></body></html>", None))
        self.buffer_conductance.setText(_translate("PoreSizerWidget", "50", None))
        self.label_11.setText(_translate("PoreSizerWidget", "<html><head/><body><p><span style=\" color:#cc0033;\">Eff. Membrane Thickness (nm)</span></p></body></html>", None))
        self.label_6.setText(_translate("PoreSizerWidget", "<html><head/><body><p><span style=\" color:#0000ff;\">Current Blockade (nA)</span></p></body></html>", None))
        self.compute_button.setText(_translate("PoreSizerWidget", "Compute", None))
        self.label_5.setText(_translate("PoreSizerWidget", "<html><head/><body><p><span style=\" color:#0000ff;\">Open Pore Current (nA)</span></p></body></html>", None))
        self.label.setText(_translate("PoreSizerWidget", "<html><head/><body><p><span style=\" text-decoration: underline; color:#0000ff;\">Inputs</span></p></body></html>", None))
        self.precision.setText(_translate("PoreSizerWidget", "0.1", None))

