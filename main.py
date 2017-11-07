import sys
import time
import curses
from PyQt4 import QtCore, QtGui

from tela import tela
import tools
import math
import numbers

class Calculadora(QtGui.QMainWindow, tela.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        self.btnResult.setStyleSheet("background-color: rgb(52, 101, 164)")
    #    self.connect(self.btn0,QtCore.SIGNAL("clicked()"),self.testClick)
        self.btn0.clicked.connect(self.btn0Click)
        self.btn1.clicked.connect(self.btn1Click)
        self.btn2.clicked.connect(self.btn2Click)
        self.btn3.clicked.connect(self.btn3Click)
        self.btn4.clicked.connect(self.btn4Click)
        self.btn5.clicked.connect(self.btn5Click)
        self.btn6.clicked.connect(self.btn6Click)
        self.btn7.clicked.connect(self.btn7Click)
        self.btn8.clicked.connect(self.btn8Click)
        self.btn9.clicked.connect(self.btn9Click)
        self.btnSoma.clicked.connect(self.btnSomaClick)
        self.btnSub.clicked.connect(self.btnSubtClick)
        self.btnMult.clicked.connect(self.btnMultClick)
        self.btnDiv.clicked.connect(self.btnDivClick)
        self.undo.clicked.connect(self.btnZClick)
        self.btnBck.clicked.connect(self.btnBckClick)
        self.btnPaf.clicked.connect(self.btnPafClick)
        self.btnPai.clicked.connect(self.btnPaiClick)
        self.btnPot.clicked.connect(self.btnPotClick)
        self.btnSqrt.clicked.connect(self.btnSqrtClick)
        self.btnResult.clicked.connect(self.btnResultClick)
        #elf.inputCalc.keyPressEvent.connect(self.keyPressEvent)
    def btn0Click(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+self.btn0.text()
        self.inputCalc.setText(text)

    def btn1Click(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+self.btn1.text()
        self.inputCalc.setText(text)

    def btn2Click(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+self.btn2.text()
        self.inputCalc.setText(text)

    def btn3Click(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+self.btn3.text()
        self.inputCalc.setText(text)

    def btn4Click(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+self.btn4.text()
        self.inputCalc.setText(text)

    def btn5Click(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+self.btn5.text()
        self.inputCalc.setText(text)
    def btn6Click(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+self.btn6.text()
        self.inputCalc.setText(text)
    def btn7Click(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+self.btn7.text()
        self.inputCalc.setText(text)
    def btn8Click(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+self.btn8.text()
        self.inputCalc.setText(text)
    def btn9Click(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+self.btn9.text()
        self.inputCalc.setText(text)

    def btnSomaClick(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+" + "
        self.inputCalc.setText(text)


    def btnSubtClick(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+" "+self.btnSub.text()+ " "
        self.inputCalc.setText(text)
    def btnMultClick(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+" "+self.btnMult.text()+" "
        self.inputCalc.setText(text)
    def btnDivClick(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+" "+self.btnDiv.text()+" "
        self.inputCalc.setText(text)
    def btnRestoClick(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+" "+self.btnResto.text()+" "
        self.inputCalc.setText(text)
    def btnZClick(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+" "+self.undo.text()+" "

    def btnBckClick(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = self.inputCalc.text()
            if len(text) > 0:
                if text[len(text)-1] == " ":
                    text = text[:-2]
                else:
                    text = text[:-1]

        self.inputCalc.setText(text)

    def btnPotClick(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = self.inputCalc.text()
            v_text = text.split(" ")
            _pot = 0.0
            if len(v_text)==1:
                _pot = float(v_text[0])
                _pot = _pot*_pot
                text = str(_pot)
            else:
                error = QtGui.QErrorMessage(self)
                error.showMessage("Potencia so com uma variavel")
        self.inputCalc.setText(text)
    def btnSqrtClick(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = ""
            text = self.inputCalc.text()
            v_text = text.split(" ")
            _pot = 0.0
            if len(v_text)==1:
                _pot = float(v_text[0])
                _pot = math.sqrt(_pot)
                text = str(_pot)
            else:
                error = QtGui.QErrorMessage(self)
                error.showMessage("Potencia so com uma variavel")

            self.inputCalc.setText(text)

    def btnPaiClick(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+" "+self.btnPai.text()+" "
        self.inputCalc.setText(text)
    def btnPafClick(self):
        text = ""
        if self.inputCalc.text() !="" or self.inputCalc.text() != None:
            text = text + self.inputCalc.text()+" "+self.btnPaf.text()+" "
        self.inputCalc.setText(text)

    def soma(self,a,b):
        return a+b
    def subtracao(self,a,b):
        return a-b
    def divisao(self,a,b):
        return a/b
    def multiplicacao(self,a,b):
        return a*b

    def btnResultClick(self):
        print("result")
        result = self.resolveExp(self.inputCalc.text())
        self.inputCalc.setText(str(result))

    def resolveExp(self, expressao):
        expressao = str(expressao)
        if len(expressao.split(" "))>1:
            print("exp")
            v_ex = expressao.split(" ")
            if  "()" in expressao:
                self.alert(" Expressao mal formada!")
            else:
                if ")" in expressao:
                    arrayExp = str(expressao).split(")")
                    tools.imprimeLista(arrayExp)
                elif "*" in v_ex:
                    pos = tools.encontrarPosicao(v_ex,"*")
                    var1 = v_ex[pos-1]
                    var2 = v_ex[pos+1]
                    result = self.multiplicacao(float(var1),float(var2))
                    v_a = []
                    if v_ex[:pos-1] != []:
                        v_a = v_ex[:pos-1]
                    v_b = []
                    if v_ex[pos+2:] != []:
                        v_b =v_ex[pos+2:]
                    v_ex = v_a
                    v_ex += [result]
                    v_ex.extend(v_b)
                    text = str(result)
                    self.resultText.setText(text)
                    expressao = self.creaEx(v_ex)
                    self.resolveExp(expressao)
                elif "/" in v_ex:
                    pos = tools.encontrarPosicao(v_ex,"/")
                    var1 = v_ex[pos-1]
                    var2 = v_ex[pos+1]
                    result = self.divisao(float(var1),float(var2))
                    v_a = []
                    if v_ex[:pos-1] != []:
                        v_a = v_ex[:pos-1]
                    v_b = []
                    if v_ex[pos+2:] != []:
                        v_b =v_ex[pos+2:]
                    v_ex = v_a
                    v_ex += [result]
                    v_ex.extend(v_b)
                    text = str(result)
                    self.resultText.setText(text)
                    expressao = self.creaEx(v_ex)
                    self.resolveExp(expressao)
                elif "+" in v_ex:
                    pos = tools.encontrarPosicao(v_ex,"+")
                    var1 = v_ex[pos-1]
                    var2 = v_ex[pos+1]
                    result = self.soma(float(var1),float(var2))
                    v_a = []
                    if v_ex[:pos-1] != []:
                        v_a = v_ex[:pos-1]
                    v_b = []
                    if v_ex[pos+2:] != []:
                        v_b =v_ex[pos+2:]
                    v_ex = v_a
                    v_ex += [result]
                    v_ex.extend(v_b)
                    text = str(result)
                    self.resultText.setText(text)
                    expressao = self.creaEx(v_ex)
                    self.resolveExp(expressao)
                elif "-" in v_ex:
                    pos = tools.encontrarPosicao(v_ex,"-")
                    var1 = v_ex[pos-1]
                    var2 = v_ex[pos+1]
                    result = self.subtracao(float(var1),float(var2))
                    v_a = []
                    if v_ex[:pos-1] != []:
                        v_a = v_ex[:pos-1]
                    v_b = []
                    if v_ex[pos+2:] != []:
                        v_b =v_ex[pos+2:]
                    v_ex = v_a
                    v_ex += [result]
                    v_ex.extend(v_b)
                    text = str(result)
                    self.resultText.setText(text)
                    expressao = self.creaEx(v_ex)
                    self.resolveExp(expressao)
                else:
                    self.alert("END")
                    text = str(expressao)
                    self.inputCalc.setText(text)
        else:
            text = str(expressao)
            self.inputCalc.setText(text)


    def alert(self,msg, icon=QtGui.QMessageBox.Warning):
        d = QtGui.QMessageBox()
        d.setWindowTitle('ERRO:')
        d.setText(msg)
        d.setIcon(icon)
        d.setGeometry(50,50,100,50)
        d.exec_()

    def keyPressEvent(self, e):
        text = e.text()
        espaco = ""
        if text == "+" or text == "-" or text == "*" or text == "/":
            espaco = " "
        text = self.inputCalc.text() +espaco+text+espaco
        self.inputCalc.setText(text)



    def creaEx(self,v):
        r = ""
        if len(v) >0:
            for e in v:
                 r = r+" "+str(e)
        return r

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = Calculadora()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app



if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
