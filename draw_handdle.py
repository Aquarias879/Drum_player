from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class draw_handdle:
    def __init__(self, cord):
        #self.line_length = line_length
        self.cord = []
        self.used_positions = []
        self.note_scene = None
    def drawed(self):
        self.note_button_scene = QGraphicsScene()
        self.note_button_view = QGraphicsView(self.note_button_scene)
        self.note_button_view.setFixedSize(880, 230)
         
    def draw_handle_drum(self,pitch,new_pos):
        print(pitch,new_pos.x())
        y = 80
        for i in range(len(pitch)):    
            if pitch[i] == "D2" : # snare (D)
                D2 = QGraphicsTextItem("𝅘")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(20)
                D2.setFont(font)
                D2.setPos(new_pos.x()-5, y-40) # adjust position of rest note
                self.note_button_scene.addItem(D2)
             
            if pitch[i] == "B1" or pitch[i] == "C2" : #bass drum (B)
                B1 = QGraphicsTextItem("𝅘")
                B1.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(20)
                B1.setFont(font)
                B1.setPos(new_pos.x()-5 , y) # adj
                self.note_button_scene.addItem(B1)
            
            if pitch[i] == "F#2" : # crash (A)1
                F2 = QGraphicsTextItem("𝅘")
                F2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(20)
                F2.setFont(font)
                F2.setPos(new_pos.x()-5 , y-75) # adjust position of rest note
                self.note_button_scene.addItem(F2)
                
            if pitch[i] == 'G2':
                C2 = QGraphicsTextItem("𝅘")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(20)
                C2.setFont(font)
                C2.setPos(new_pos.x()-5 , y-20) # adjust position of rest note
                self.note_button_scene.addItem(C2)

            if pitch[i] == 'D3':
                D3 = QGraphicsTextItem("𝅘")
                D3.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(20)
                D3.setFont(font)
                D3.setPos(new_pos.x()-5 , y-70) # adjust position of rest note
                self.note_button_scene.addItem(D3)

            if pitch[i] == "A2":
                A2 = QGraphicsTextItem("𝅘")
                A2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(20)
                A2.setFont(font)
                A2.setPos(new_pos.x()-5 , y-50) # adjust position of rest note
                self.note_button_scene.addItem(A2)
