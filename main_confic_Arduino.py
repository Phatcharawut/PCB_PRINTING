


from ast import Break
from doctest import master
from operator import setitem
from tkinter.font import names
from turtle import Screen, delay
from unicodedata import name
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from pyGUI import Ui_MainWindow
import sys
import serial
# from time import sleep
from msilib.schema import Class
from gerber_renderer import Gerber
from tkinter import *
from tkinter.filedialog import *
import tkinter as tk
from tkPDFViewer import tkPDFViewer as pdf
import os
from PIL import Image
from pdf2image import convert_from_path
from ezdxf import recover
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
import ezdxf
import matplotlib.pyplot as plt
import time
# import test_timer as count_D
from threading import Timer
from pdf2image import convert_from_path
from tkinter import *
from PIL import ImageTk,Image
from gerber_renderer.Gerber import Board
from Gerber import *
from dxf import *
import math
import matplotlib.pyplot as plt
import glob
import re
from ezdxf import bbox
import glob
import re


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

class Myclass(Ui_MainWindow):
    def __init__(self): 
        super().setupUi(MainWindow)
        self.ser = serial.Serial("COM6",9600,timeout=1)
        self.start.clicked.connect(self.sta)
        self.reset.clicked.connect(self.re)
        self.stop.clicked.connect(self.ST)
        self.Auto.clicked.connect(self.modeA)
        self.Man.clicked.connect(self.modeM)
        self.home.clicked.connect(self.HOME)
        self.open.clicked.connect(self.OPEN)
        self.open_2.clicked.connect(self.OPEN)
        self.pull.clicked.connect(self.PULL)
        self.rele.clicked.connect(self.RELE)
        self.PBnameF.clicked.connect(self.setnamefolder)
        self.startman.clicked.connect(self.modemanStart)
        self.stopman.clicked.connect(self.modemanstop)
        self.logo = r"C:\Users\Phatcharawut\Desktop\FINAL PROJECT\NEW_PROJECT\Used folder\logo-elec (1).png"
        self.label_4.setPixmap(QPixmap(self.logo))
        


        self.z1.clicked.connect(self.Z1)        
        self.z2.clicked.connect(self.Z2)

        self.y1.clicked.connect(self.Y1)
        self.y2.clicked.connect(self.Y2)

        self.x1.clicked.connect(self.X1)
        self.x2.clicked.connect(self.X2)
        

        self.x1.setEnabled(False)
        self.x2.setEnabled(False)
        self.y1.setEnabled(False)
        self.y2.setEnabled(False)
        self.z1.setEnabled(False)
        self.z2.setEnabled(False)
        self.pull.setEnabled(False)
        self.rele.setEnabled(False)
        self.time2.setEnabled(False)
        self.start.setEnabled(False)
        self.stop.setEnabled(False)
        self.open.setEnabled(False)
        self.reset.setEnabled(False)
        self.home.setEnabled(False)
        self.Auto.setEnabled(False)
        self.Man.setEnabled(False)
        self.PBnameF.setEnabled(True)
        self.linenameF.setEnabled(True)
        
    def setnamefolder(self):
        self.Auto.setEnabled(True)
        self.Man.setEnabled(True)
        self.label_slectmode.setText("Please select mode tab!!!")
        self.label_slectmode.setStyleSheet("color: rgb(0, 255, 0);")
        self.label_6.setText("When selecting a PDF or PNG file,")
        self.label_7.setText("enter the desired width and length.")
        self.label_6.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_7.setStyleSheet("color: rgb(255, 0, 0);")
        
    def modeA(self):
        self.ser.write("O".encode())
        self.x1.setEnabled(False)
        self.x2.setEnabled(False)
        self.y1.setEnabled(False)
        self.y2.setEnabled(False)
        self.z1.setEnabled(False)
        self.z2.setEnabled(False)
        self.pull.setEnabled(False)
        self.rele.setEnabled(False)
        self.time2.setEnabled(False)
        self.open.setEnabled(True)
        self.start.setEnabled(True)
        self.stop.setEnabled(True)
        self.home.setEnabled(True)
        self.reset.setEnabled(True)
    def modeM(self):
        # self.valuetime = int(self.time2.value())
        self.ser.write("L".encode())
        self.x1.setEnabled(True)
        self.x2.setEnabled(True)
        self.y1.setEnabled(True)
        self.y2.setEnabled(True)
        self.z1.setEnabled(True)
        self.z2.setEnabled(True)
        self.pull.setEnabled(True)
        self.rele.setEnabled(True)
        self.time2.setEnabled(True)
        self.open.setEnabled(True)
        self.home.setEnabled(True)
        self.start.setEnabled(False)
        self.stop.setEnabled(False)
        self.reset.setEnabled(False)
        
    def modemanStart(self):
        
        self.valuetime = self.time2.value()
        if int(self.valuetime) == 0:
            self.ser.write("c".encode())
        if int(self.valuetime) == 1:
            self.ser.write("z".encode())
        if int(self.valuetime) == 2:
            self.ser.write("x".encode())
        if int(self.valuetime) == 3:
            self.ser.write("X".encode())
        if int(self.valuetime) == 4:
            self.ser.write("Z".encode())    
             
    def modemanstop(self):
        self.ser.write('v'.encode())
        
        
    def sta(self):
        self.ser.write("A".encode())
    def re(self):
        self.ser.write("I".encode()) 


    def Z1(self):                                   ## Z switch setting
        if self.z1.isChecked()==True:
            self.ser.write("W".encode())     
        elif self.z1.isDown()==False:
            self.ser.write("S".encode())
    def Z2(self):
        if self.z2.isChecked()==True:
            self.ser.write("F".encode())
        elif self.z2.isDown()==False:
            self.ser.write("S".encode())


    def X1(self):                                           ## X switch setting
        if self.x1.isChecked()==True:
            self.ser.write("R".encode())
        elif self.x1.isDown()==False:
            self.ser.write("T".encode())
    def X2(self):
        if self.x2.isChecked()==True:
            self.ser.write("r".encode())
        elif self.x2.isDown()==False:
            self.ser.write("T".encode())





    def Y1(self):                                           ## Y switch setting
        if self.y1.isChecked()==True:
            self.ser.write("U".encode())
            print('x')
        elif self.y1.isDown()==False:
            self.ser.write("T".encode())
            print('y')
    def Y2(self):
        if self.y2.isChecked()==True:
            print('x')
            self.ser.write("D".encode())
        elif self.y2.isDown()==False:
            print('y')
            self.ser.write("T".encode())
    
    def ST(self):
        self.ser.write("H".encode())
    
    def HOME(self):
        self.ser.write("E".encode())

    def PULL(self):
        self.ser.write("Q".encode())
           
    def RELE(self):
        self.ser.write("M".encode()) 

    def OPEN(self):
        try:
            self.fileopen = askopenfile()
            self.dir_folder_cre = "C:/Users/Phatcharawut/Desktop/FINAL PROJECT/NEW_PROJECT/Used folder"
            self.namefile = self.fileopen.name
        except:
            pass

        
        if '.zip' in self.namefile:

            os.makedirs("C:/Users/Phatcharawut/Desktop/FINAL PROJECT/NEW_PROJECT/Used folder/gerber_pdf",exist_ok=True)
            self.namefolder = self.linenameF.text()     #รับค่า name จาก ui
            self.path_gerber = "C:/Users/Phatcharawut/Desktop/FINAL PROJECT/NEW_PROJECT/Used folder/gerber_pdf"
            board = Gerber.Board(self.namefile, verbose=True)
            self.suc_file = board.render_pdf(output=self.path_gerber, layer='top_copper', color='white', scale_compensation=(2,2), full_page=False, mirrored=True, offset=(0, 0))
            h = board.h()
            w = board.w()
            print(h)
            print(w)
            high =math.ceil(h)

            wigth = math.ceil(w)
            print(h)
            print(w)
            print(high)
            print(wigth)
            self.images = convert_from_path(r"C:\Users\Phatcharawut\Desktop\FINAL PROJECT\NEW_PROJECT\Used folder\gerber_pdf\top_copper.pdf",poppler_path=r"C:\poppler-0.68.0\bin")
            for i in range(len(self.images)):
                self.images[i].save("C:/Users/Phatcharawut/Desktop/FINAL PROJECT/NEW_PROJECT/Used folder/gerber_pdf/top_copper.jpg")
            self.pixmapgerber = QPixmap("C:/Users/Phatcharawut/Desktop/FINAL PROJECT/NEW_PROJECT/Used folder/gerber_pdf/top_copper.jpg")
            self.screen.setScaledContents(True)
            self.screen_2.setScaledContents(True)
            self.screen.setPixmap(self.pixmapgerber)
            self.screen_2.setPixmap(self.pixmapgerber)
            tk.Tk()
            label = tk.Label(text='Click exis for to close the projection page!!')
            c=tk.Toplevel()
            c.geometry('%dx%d+1980+%d'%(2500,472,0))
            self.load=Image.open(r"C:/Users/Phatcharawut/Desktop/FINAL PROJECT/NEW_PROJECT/Used folder/gerber_pdf/top_copper.jpg").resize(((wigth+2)*19,(high+2)*6))
            
            self.render=ImageTk.PhotoImage(self.load)
            self.img=tk.Label(c,image=self.render)
            self.img.pack()
            c.mainloop()
            


        if '.jpg' in self.namefile:
            lineH=self.lineEdit_2.text()
            lineW=self.lineWimage.text()
            self.pixmapgerber = QPixmap(self.namefile)
            self.screen.setScaledContents(True)
            self.screen_2.setScaledContents(True)
            self.screen.setPixmap(self.pixmapgerber)
            self.screen_2.setPixmap(self.pixmapgerber)
            root=Tk()
            c=tk.Toplevel()
            c.geometry('%dx%d+1980+%d'%(2500,472,0))
            self.load=Image.open(self.namefile).resize(((int(lineW)+3)*20,(int(lineH)+7)*6))
            # self.load=Image.open(self.namefile).resize((52,32))
            self.render=ImageTk.PhotoImage(self.load)
            self.img=tk.Label(c,image=self.render)
            self.img.pack()
            c.mainloop()

        if '.png' in self.namefile:
            lineH=self.lineEdit_2.text()
            lineW=self.lineWimage.text()
            self.pixmapgerber = QPixmap(self.namefile)
            self.screen.setScaledContents(True)
            self.screen_2.setScaledContents(True)
            self.screen.setPixmap(self.pixmapgerber)
            self.screen_2.setPixmap(self.pixmapgerber)
            root=Tk()
            c=tk.Toplevel()
            c.geometry('%dx%d+1980+%d'%(2500,472,0))
            self.load=Image.open(self.namefile).resize(((int(lineW)+3)*20,(int(lineH)+7)*6))
            # self.load=Image.open(self.namefile).resize((52,32))
            self.render=ImageTk.PhotoImage(self.load)
            self.img=tk.Label(c,image=self.render)
            self.img.pack()
            c.mainloop()
            
        if '.pdf' in self.namefile:
            lineH=self.lineEdit_2.text()
            lineW=self.lineWimage.text()
            
            self.images = convert_from_path(self.namefile,poppler_path=r"C:\poppler-0.68.0\bin")
            for i in range(len(self.images)):
                self.images[i].save("C:/Users/Phatcharawut/Desktop/FINAL PROJECT/NEW_PROJECT/Used folder/pdfpcb.jpg")
            self.pixmapgerber = QPixmap("C:/Users/Phatcharawut/Desktop/FINAL PROJECT/NEW_PROJECT/Used folder/pdfpcb.jpg")
            self.screen.setScaledContents(True)
            self.screen_2.setScaledContents(True)
            self.screen.setPixmap(self.pixmapgerber)
            self.screen_2.setPixmap(self.pixmapgerber)
            root=Tk()
            c=tk.Toplevel()
            c.geometry('%dx%d+1980+%d'%(2500,472,0))
            self.load=Image.open(r"C:/Users/Phatcharawut/Desktop/FINAL PROJECT/NEW_PROJECT/Used folder/pdfpcb.jpg").resize(((int(lineW)+2)*19,((int(lineH))+2)*6))
            
            self.render=ImageTk.PhotoImage(self.load)
            self.img=tk.Label(c,image=self.render)
            self.img.pack()
            c.mainloop()
            
        if '.dxf' in self.namefile:
            default_img_format = '.png'
            default_img_res = 86
            default_bg_color = '#000000' #White
            names = self.namefile
            dwg = ezdxf.readfile(names)
            witgh=[]
            high=[]
            for i in dwg.header['$EXTMAX']:
                witgh.append(i)
            for i in dwg.header['$EXTMIN']:
                high.append(i)
            realWight = witgh[0]-high[0]
            high = witgh[1]
            print(realWight)
            print(witgh[1])
            wig = math.ceil(realWight)
            hig = math.ceil(high)
            print(wig)
            print(hig)
            # print ('EXTMAX ', dwg.header['$EXTMAX'])
            # print ('EXTMIN ', dwg.header['$EXTMIN'])
            print ('LIMMAX ', dwg.header['$LIMMAX'])
            print ('LIMMIN ', dwg.header['$LIMMIN'])

            clr=default_bg_color
            img_format=default_img_format
            img_res=default_img_res
            doc = ezdxf.readfile(names)


            msp = doc.modelspace()
            auditor = doc.audit()
            path = "C:/Users/Phatcharawut/Desktop/FINAL PROJECT/NEW_PROJECT/Used folder/dxfconpng"
            if len(auditor.errors) != 0:
                raise Exception("This DXF document is damaged and can't be converted! --> ", path)
                name = name =+ 1
            else :
                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                ctx = RenderContext(doc)
                ctx.set_current_layout(msp)
                ezdxf.addons.drawing.properties.MODEL_SPACE_BG_COLOR = clr
                out = MatplotlibBackend(ax)
                Frontend(ctx, out).draw_layout(msp, finalize=True)
                img_name = path # select the image name that is the same as the dxf file name
                first_param = ''.join(img_name) + img_format  #concatenate list and string
                fig.savefig(first_param, dpi=img_res)
                print(path," Converted Successfully")

            self.pixmapgerber = QPixmap("C:/Users/Phatcharawut/Desktop/FINAL PROJECT/NEW_PROJECT/Used folder/dxfconpng.png")
            self.screen.setScaledContents(True)
            self.screen_2.setScaledContents(True)
            self.screen.setPixmap(self.pixmapgerber)
            self.screen_2.setPixmap(self.pixmapgerber)
            root=Tk()
            c=tk.Toplevel()
            c.geometry('%dx%d+1980+%d'%(2500,472,0))
            self.load=Image.open("C:/Users/Phatcharawut/Desktop/FINAL PROJECT/NEW_PROJECT/Used folder/dxfconpng.png").resize(((int(wig)+3)*20,(int(hig)+5)*6))
            self.render=ImageTk.PhotoImage(self.load)
            self.img=tk.Label(c,image=self.render)
            self.img.pack()
            c.mainloop()

        
            
       


if __name__ == "__main__":
    obj = Myclass()
    MainWindow.show()
    sys.exit(app.exec_())