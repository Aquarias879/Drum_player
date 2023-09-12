from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class checknote_drum_lv1:
    def __init__(self, cord):
         self.note_scene = None
    
    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
    
    def drum_correct1(self,pitch,new_pos,cord,note_pos,type):
        y = 80
        for i in range(len(self.cord)):
            remainder = cord[i][1] % 5
            pos = cord[i][1] + 2 if remainder == 3 else cord[i][1] + 3 if remainder == 2 else cord[i][1]
            
            if new_pos.x() == pos and cord[i][0] == pitch:
                if pitch == ['D2'] and type[i] == '4':
                    D2 = QGraphicsTextItem("𝅘𝅥")
                    D2.setDefaultTextColor(Qt.green)
                    font = QFont()
                    font.setPointSize(30)
                    D2.setFont(font)
                    D2.setPos(cord[i][1]-5, y - 55)
                    self.notation_note_scene.addItem(D2)

                if pitch == ['D2'] and type[i] == '8':
                    D2 = QGraphicsTextItem("♪")
                    D2.setDefaultTextColor(Qt.green)
                    font = QFont()
                    font.setPointSize(30)
                    D2.setFont(font)
                    D2.setPos(cord[i][1]-5, y - 48)
                    self.notation_note_scene.addItem(D2)
                
    def drum_correct2(self,pitch,new_pos,cord,note_pos,type):
        y = 80
        adjustments = {4:1,3: 2, 2: 3 ,1:4}

        for i in range(len(cord)):
            remainder = cord[i][1] % 5
            pos = cord[i][1] + adjustments.get(remainder, 0)
            
            if new_pos.x() == pos and cord[i][0] == pitch:
                if pitch == ['D2'] and type[i] == '4':
                    D2 = QGraphicsTextItem("𝅘𝅥")
                    D2.setDefaultTextColor(Qt.green)
                    font = QFont()
                    font.setPointSize(30)
                    D2.setFont(font)
                    D2.setPos(cord[i][1] - 5, y - 55)
                    self.notation_note_scene.addItem(D2)

                if pitch == ['D2'] and type[i] == '8':
                    D2 = QGraphicsTextItem("♪")
                    D2.setDefaultTextColor(Qt.green)
                    font = QFont()
                    font.setPointSize(30)
                    D2.setFont(font)
                    D2.setPos(cord[i][1] - 5, y - 48)
                    self.notation_note_scene.addItem(D2)

    def drum_correct3(self,pitch,new_pos,cord,note_pos,type):
        y = 80
        adjustments = {4:1,3: 2, 2: 3 ,1:4}

        for i in range(len(cord)):
            remainder = cord[i][1] % 5
            pos = cord[i][1] + adjustments.get(remainder, 0)

            if new_pos.x() == pos and cord[i][0] == pitch:
                    print(type[i])
                    if pitch == ['D2'] and type[i] == '4':
                        D2 = QGraphicsTextItem("𝅘𝅥")
                        D2.setDefaultTextColor(Qt.green)
                        font = QFont()
                        font.setPointSize(30)
                        D2.setFont(font)
                        D2.setPos(cord[i][1] - 5, y - 55)
                        self.notation_note_scene.addItem(D2)

                    if pitch == ['D2'] and type[i] == '8':
                        D2 = QGraphicsTextItem("♪")
                        D2.setDefaultTextColor(Qt.green)
                        font = QFont()
                        font.setPointSize(30)
                        D2.setFont(font)
                        D2.setPos(cord[i][1] - 5, y - 48)
                        self.notation_note_scene.addItem(D2)

                    if pitch == ['B1'] and type[i] == '4':
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1] + 25, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                    
                    
                    if pitch == ['B1'] and type[i] == '8':
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1] + 25, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                        
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1] - 3, y+70) # adjust position of rest note
                        layer.setRotation(160)

                        transform = QTransform()
                        transform.scale(-1, 1) # Flip horizontally
                        layer.setTransform(transform)
                        self.notation_note_scene.addItem(layer)

    def drum_correct4(self,pitch,new_pos,cord,note_pos,type):
        y = 80
        adjustments = {4:1,3: 2, 2: 3 ,1:4}
        for i in range(len(cord)):
            remainder = cord[i][1] % 5
            pos = cord[i][1] + adjustments.get(remainder, 0)
            if new_pos.x() == pos and cord[i][0] == pitch:
                    if pitch == ['D2'] and type[i] == '4':
                        D2 = QGraphicsTextItem("𝅘𝅥")
                        D2.setDefaultTextColor(Qt.green)
                        font = QFont()
                        font.setPointSize(30)
                        D2.setFont(font)
                        D2.setPos(cord[i][1] - 5, y - 55)
                        self.notation_note_scene.addItem(D2)

                    if pitch == ['D2'] and type[i] == '8':
                        D2 = QGraphicsTextItem("♪")
                        D2.setDefaultTextColor(Qt.green)
                        font = QFont()
                        font.setPointSize(30)
                        D2.setFont(font)
                        D2.setPos(cord[i][1] - 5, y - 48)
                        self.notation_note_scene.addItem(D2)

                    if pitch == ['B1'] and type[i] == '4':
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1] + 25, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                    
                    if pitch == ['B1'] and type[i] == '8':
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1] + 25, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                        
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1] - 3, y+70) # adjust position of rest note
                        layer.setRotation(160)

                        transform = QTransform()
                        transform.scale(-1, 1) # Flip horizontally
                        layer.setTransform(transform)
                        self.notation_note_scene.addItem(layer)
       
    def drum_correct5(self,pitch,new_pos,cord,note_pos,type):
        y = 80
        adjustments = {4:1,3: 2, 2: 3 ,1:4}
        for i in range(len(cord)):
            remainder = cord[i][1] % 5
            pos = cord[i][1] + adjustments.get(remainder, 0)
            if new_pos.x() == pos and cord[i][0] == pitch:
                    print(type[i])
                    if pitch == ['D2'] and type[i] == '4':
                        D2 = QGraphicsTextItem("𝅘𝅥")
                        D2.setDefaultTextColor(Qt.green)
                        font = QFont()
                        font.setPointSize(30)
                        D2.setFont(font)
                        D2.setPos(cord[i][1] - 5, y - 55)
                        self.notation_note_scene.addItem(D2)

                    if pitch == ['D2'] and type[i] == '8':
                        D2 = QGraphicsTextItem("♪")
                        D2.setDefaultTextColor(Qt.green)
                        font = QFont()
                        font.setPointSize(30)
                        D2.setFont(font)
                        D2.setPos(cord[i][1] - 5, y - 48)
                        self.notation_note_scene.addItem(D2)
                    
                    if pitch == ["A2"] and type[i] == '4':
                        A2 = QGraphicsTextItem("𝅘𝅥")
                        A2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        A2.setFont(font)
                        A2.setPos(cord[i][1] - 5, y-63) # adjust position of rest note
                        self.notation_note_scene.addItem(A2)
                      
                    if pitch == ["A2"] and type[i] == '8':
                        A2 = QGraphicsTextItem("𝅘𝅥𝅮")
                        A2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        A2.setFont(font)
                        A2.setPos(cord[i][1] - 5, y-63) # adjust position of rest note
                        self.notation_note_scene.addItem(A2)
                
                    if pitch == ['B1'] and type[i] == '4':
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1] + 25, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)

    def drum_correct6(self,pitch,new_pos,cord,note_pos,type):
        #print(pitch,new_pos,cord,note_pos,type)
        y = 80
        adjustments = {4:1,3: 2, 2: 3 ,1:4}
        for i in range(len(cord)):
            remainder = cord[i][1] % 5
            pos = cord[i][1] + adjustments.get(remainder, 0)
            if new_pos.x() == pos and cord[i][0] == pitch:
                    
                    if pitch == ['D2'] and type[i] == '4':
                        D2 = QGraphicsTextItem("𝅘𝅥")
                        D2.setDefaultTextColor(Qt.green)
                        font = QFont()
                        font.setPointSize(30)
                        D2.setFont(font)
                        D2.setPos(cord[i][1] - 5, y - 55)
                        self.notation_note_scene.addItem(D2)

                    if pitch == ['D2'] and type[i] == '8':
                        D2 = QGraphicsTextItem("♪")
                        D2.setDefaultTextColor(Qt.green)
                        font = QFont()
                        font.setPointSize(30)
                        D2.setFont(font)
                        D2.setPos(cord[i][1] - 5, y - 48)
                        self.notation_note_scene.addItem(D2)
                    
                    if pitch == ["A2"] and type[i] == '4':
                        A2 = QGraphicsTextItem("𝅘𝅥")
                        A2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        A2.setFont(font)
                        A2.setPos(cord[i][1] - 5, y-63) # adjust position of rest note
                        self.notation_note_scene.addItem(A2)
                      
                    if pitch == ["A2"] and type[i] == '8':
                        A2 = QGraphicsTextItem("𝅘𝅥𝅮")
                        A2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        A2.setFont(font)
                        A2.setPos(cord[i][1] - 5, y-63) # adjust position of rest note
                        self.notation_note_scene.addItem(A2)
                
                    if pitch == ['B1'] and type[i] == '4':
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1] + 25, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                    
                    if pitch == ['B1'] and type[i] == '8':
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1] + 30, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                        
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1] +2, y+70) # adjust position of rest note
                        layer.setRotation(160)

                        transform = QTransform()
                        transform.scale(-1, 1) # Flip horizontally
                        layer.setTransform(transform)
                        self.notation_note_scene.addItem(layer)
                
                    if pitch == ["G2"] and type[i] == "4":
                        G2 = QGraphicsTextItem("𝅘𝅥")
                        G2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        G2.setFont(font)
                        G2.setPos(cord[i][1]+25, y+60) # adjust position of rest note
                        G2.setRotation(180)
                        self.notation_note_scene.addItem(G2)
                      
                    if pitch == ["D3"] and type[i] == "8":
                        A2 = QGraphicsTextItem("𝅘𝅥𝅮")
                        A2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        A2.setFont(font)
                        A2.setPos(cord[i][1], y-83) # adjust position of rest note
                        self.notation_note_scene.addItem(A2)
                    
                    if pitch == ["D3"] and type[i] == "4":
                        A2 = QGraphicsTextItem("𝅘𝅥")
                        A2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        A2.setFont(font)
                        A2.setPos(cord[i][1]-5, y-83) # adjust position of rest note
                        self.notation_note_scene.addItem(A2)
                   
                   