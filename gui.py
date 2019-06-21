import  sys
import matplotlib
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import  QApplication,QMainWindow,QVBoxLayout, QSizePolicy, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np
from matplot import Ui_MainWindow
import pandas
from scipy.fftpack import fft,ifft
matplotlib.use('Qt5Agg')
m = pandas.read_csv(r'C:\Users\pc\Desktop\3.csv')

Y = m.values
y1 = Y[0]
y1 = 200/88.53*(y1*1000+3.03)
y1 = (y1 - sum(y1)/len(y1))*1000
x = np.arange(0,10,1/10000)

y2 = Y[1]
y2 = 200/78.7*(y2*1000+10.2)
y2 = (y2 - sum(y2)/len(y2))*1000

y3 = Y[2]
y3 = 200/77.62*(y3*1000+4.55)
y3 = (y3 - sum(y3)/len(y3))*1000

y4 = Y[3]
y4 = 200/75.59*(y4*1000+3.36)
y4 = (y4 - sum(y4)/len(y4))*1000

y5 = Y[4]
y5 = 200/78.41*(y5*1000+3.92)
y5 = (y5 - sum(y5)/len(y5))*1000

y6 = Y[5]
y6 = 200/75.46*(y6*1000+3.30)
y6 = (y6 - sum(y6)/len(y6))*1000

y7 = Y[6]
y7 = 200/74.26*(y7*1000+6.62)
y7 = (y7 - sum(y7)/len(y7))*1000

y8 = Y[7]
y8 = 200/77.04*(y8*1000+0.51)
y8 = (y8 - sum(y8)/len(y8))*1000

y9 = Y[8]
y9 = 200/68.24*(y9*1000+6.72)
y9 = (y9 - sum(y9)/len(y9))*1000

def FFT(y, x = x, Fs=10000):
    yy=fft(y)                     #快速傅里叶变换
    yf=abs(fft(y))                # 取模
    yf1=abs(fft(y))/((len(y)/2))           #归一化处理
    yf2 = yf1[range(int(len(y)/2))]   #由于对称性，只取一半区间

    xf = np.arange(len(y))# 频率
    T = len(y)/Fs
    xf1 = xf/T
    xf2 = xf1[range(int(len(y)/2))]  #取一半区间
    return xf2, yf2

class ShowFigure(FigureCanvas):
    def __init__(self,x,y,width=10,height=4,):
        self.fig = plt.figure(figsize=(width,height))
        self.x = x
        self.y = y
        super(ShowFigure, self).__init__(self.fig)

    def plot(self):
        #self.axes0 = self.fig.add_subplot(111)
        #self.axes0.plot(self.x[:2000],self.y[:2000])
        #self.axes0.locator_params('x', nbins=25)
        plt.plot(self.x[:2000],self.y[:2000])
        plt.locator_params('x', nbins=25)
        plt.title("Frequency")
class CallTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Show)
    def Show(self):
        line_dict = {'LINE1': FFT(y1),'LINE2': FFT(y2),'LINE3': FFT(y3),
                     'LINE4': FFT(y4),'LINE5': FFT(y5),'LINE6': FFT(y6),
                     'LINE7': FFT(y7),'LINE8': FFT(y8),'LINE9': FFT(y9)}
        m,n = line_dict.get(self.ui.comboBox.currentText())
        self.F = ShowFigure(m,n)
        self.F.plot()
        self.ui.verticalLayout.addWidget(self.F)
        self.ui.verticalLayout.removeWidget(self.F)
        content = self.ui.comboBox.currentText()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    demo = CallTest()
    demo.show()
    sys.exit(app.exec_())


