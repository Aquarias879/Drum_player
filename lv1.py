from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class lv1_drum_1:
    def __init__(self, cord):
        self.cord = []
        self.note_pos = []
        self.sym = []
        self.note_scene = None

    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
  
    def draw_lv1(self, pitch, x, y,symbols):
        x[10] = 6
        x[11] = 6.65
        symbols[11] = '8'

        test = x[:10]
        x = x[10:]
        for j in range(len(test)):
            n = test[j] + 0.375
            x.append(n)
    
        x = sorted(x)

        for i in range(len(pitch)):
            if pitch[i] == ["D2"] and symbols[i] == "4":
                D2 = QGraphicsTextItem("𝅘𝅥")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*100, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],round(x[i]*100)+5))
                self.note_pos.append(x[i]*100)
                self.sym.append("4")

            if pitch[i] == ["D2"] and symbols[i] == "8":
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*100, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],round(x[i]*100)+5))
                self.note_pos.append(x[i]*100)
                self.sym.append("8")

            D2 = QGraphicsTextItem("𝅘𝅥")
            D2.setDefaultTextColor(Qt.black)
            font = self.font()
            font.setPointSize(30)
            D2.setFont(font)
            D2.setPos(11.625*100, y-55) # adjust position of rest note
            self.notation_note_scene.addItem(D2)
            self.cord.append((['D2'],round(11.625*100)+5))
            self.note_pos.append(11.625*100)
            self.sym.append("4")

            Q1 = QGraphicsTextItem("𝄾")
            Q1.setDefaultTextColor(Qt.black)
            font = self.font()
            font.setPointSize(30)
            Q1.setFont(font)
            Q1.setPos(0.375*100, y-28) # adjust position of rest note
            self.notation_note_scene.addItem(Q1)

            Q2 = QGraphicsTextItem("𝄾")
            Q2.setDefaultTextColor(Qt.black)
            font = self.font()
            font.setPointSize(30)
            Q2.setFont(font)
            Q2.setPos(6.4*100, y-28) # adjust position of rest note
            self.notation_note_scene.addItem(Q2)

            Q3 = QGraphicsTextItem("𝄾")
            Q3.setDefaultTextColor(Qt.black)
            font = self.font()
            font.setPointSize(30)
            Q3.setFont(font)
            Q3.setPos(6.9*100, y-28) # adjust position of rest note
            self.notation_note_scene.addItem(Q3)
     
class lv1_drum_2:
    def __init__(self, cord):
        self.cord = []
        self.note_scene = None

    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
  
    def draw_lv1(self, pitch, x,y,symbols):
        x = [round(x, 3) for x in x]
        x[5] = 4.35
        x[6] = 4.785

        groups = [x[9:12], x[12:15], x[15:18], x[18:]]

        x = x[:9]

        increments = [0.549, 0.749, 0.889, 1.089]

        for group, increment in zip(groups, increments):
            for value in group:
                x.append(value + increment)

        for i in range(len(pitch)):
            #print(pitch[i],x[i],i)
            if pitch[i] == ["D2"] and symbols[i] == "4":
                D2 = QGraphicsTextItem("𝅘𝅥")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*100, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],round(x[i]*100)+5))
                self.note_pos.append(x[i]*100)
                self.sym.append("4")

            if pitch[i] == ["D2"] and symbols[i] == "8":
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*100, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],round(x[i]*100)+5))
                self.note_pos.append(x[i]*100)
                self.sym.append("8")
                
            R1 = QGraphicsTextItem("𝄾")
            R1.setDefaultTextColor(Qt.black)
            font = self.font()
            font.setPointSize(30)
            R1.setFont(font)
            R1.setPos(6.461*100, y-28) # adjust position of rest note
            self.notation_note_scene.addItem(R1)
            
            R2 = QGraphicsTextItem("𝄾")
            R2.setDefaultTextColor(Qt.black)
            font = self.font()
            font.setPointSize(30)
            R2.setFont(font)
            R2.setPos(7.952*100, y-28) # adjust position of rest note
            self.notation_note_scene.addItem(R2)

            R3 = QGraphicsTextItem("𝄾")
            R3.setDefaultTextColor(Qt.black)
            font = self.font()
            font.setPointSize(30)
            R3.setFont(font)
            R3.setPos(9.332*100, y-28) # adjust position of rest note
            self.notation_note_scene.addItem(R3)

class lv1_drum_3:
    def __init__(self, cord):
        self.cord = []
        self.note_scene = None

    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
  
    def draw_lv1(self, pitch, x,y,symbols):
        # Update specific indices in x
        x[3] = 3.0
        x[12] = 7.125
        x[14] = 9
        x[15] = 9.875
        x[16] = 10.75
        x[10:14] = [6.25, 7.0, 7.625, 8.3]

        # Update specific indices in symbols
        symbols[14] = symbols[10] = symbols[11] = symbols[13] = symbols[12] = '8'
        symbols[4] = symbols[6] = symbols[8] = symbols[3] = '4'

        # Modify x using slicing and loop
        test = x[4:]
        x = x[:4]
        x.extend([n + 0.375 for n in test])

        D2 = QGraphicsTextItem("𝅘𝅥")
        D2.setDefaultTextColor(Qt.black)
        font = self.font()
        font.setPointSize(30)
        D2.setFont(font)
        D2.setPos((5.625)*100, y-55) # adjust position of rest note
        self.notation_note_scene.addItem(D2)
        self.cord.append((['D2'],(round(5.625*100)+5)))
        self.note_pos.append(5.25*100)
        self.sym.append("4")

        C2 = QGraphicsTextItem("𝅘𝅥")
        C2.setDefaultTextColor(Qt.black)
        font = self.font()
        font.setPointSize(30)
        C2.setFont(font)
        C2.setPos((6)*100+20, y+75) # adjust position of rest note
        C2.setRotation(180)
        self.notation_note_scene.addItem(C2)
        self.cord.append((['B1'],(round(6*100)-5)))
        self.note_pos.append(6+20)
        self.sym.append("8")

        layer = QGraphicsTextItem("𝅮")
        layer.setDefaultTextColor(Qt.black)
        font = self.font()
        font.setPointSize(28)
        layer.setFont(font)
        layer.setPos((6)*100-7, y+70) # adjust position of rest note
        layer.setRotation(160)

        transform = QTransform()
        transform.scale(-1, 1) # Flip horizontally
        layer.setTransform(transform)
        self.notation_note_scene.addItem(layer)
            
        for i in range(len(pitch)):
            if pitch[i] == ["D2"] and symbols[i] == "4":
                D2 = QGraphicsTextItem("𝅘𝅥")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*100, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*100)+5)))
                self.note_pos.append(x[i]*100)
                self.sym.append("4")

            if pitch[i] == ["D2"] and symbols[i] == "8":
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*100, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*100)+5)))
                self.note_pos.append(x[i]*100)
                self.sym.append("8")

            if pitch[i] == ["B1"] and symbols[i] == "4":
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*100+20, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],(round(x[i]*100)-5)))
                self.note_pos.append(x[i]*100+20)
                self.sym.append("4")

            if pitch[i] == ["B1"] and symbols[i] == "8":
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*100+20, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],(round(x[i]*100-5))))
                self.note_pos.append(x[i]*100)
                self.sym.append("8")

                layer = QGraphicsTextItem("𝅮")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*100-7, y+70) # adjust position of rest note
                layer.setRotation(160)

                transform = QTransform()
                transform.scale(-1, 1) # Flip horizontally
                layer.setTransform(transform)
                self.notation_note_scene.addItem(layer)
            
class lv1_drum_4:
    def __init__(self, cord):
        self.cord = []
        self.note_scene = None

    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
  
    def draw_lv1(self, pitch, x,y,symbols):
        
        symbols_list = [0, 2, 11, 23, 25, 19, 21]
        value_to_set = '4'
        for index in symbols_list :
            if 0 <= index < len(symbols):
                symbols[index] = value_to_set

        dup_note = [1,4,6,8,10,12,14,16,18,20,22,24,28,26,30,32,34,36] #10, 20, 21, 1]
        for index in sorted(dup_note, reverse=True):
            if 0 <= index < len(symbols):
                symbols.pop(index)
                pitch.pop(index)
                x.pop(index)
        
        pos_x = [0, 7, 8, 9, 10, 11, 12, 13]
        values_to_set_x = [0.75, 5.25, 5.625, 6, 6.375, 7.125, 7.875, 8.625]

        for index, value in zip(pos_x, values_to_set_x):
            if 0 <= index < len(x):
                x[index] = value
        
        test = x[1:]
        x = x[:1]
        x.extend([n + 0.375 for n in test])

        for i in range(len(pitch)):
            if pitch[i] == ["D2"] and symbols[i] == "4":
                D2 = QGraphicsTextItem("𝅘𝅥")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*100, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*100)+5)))
                self.note_pos.append(x[i]*100)
                self.sym.append("4")

            if pitch[i] == ["D2"] and symbols[i] == "8":
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*100, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*100)+5)))
                self.note_pos.append(x[i]*100)
                self.sym.append("8")

            if pitch[i] == ["B1"] and symbols[i] == "4":
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*100+20, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],(round(x[i]*100)-5)))
                self.note_pos.append(x[i]*100+20)
                self.sym.append("4")


            if pitch[i] == ["B1"] and symbols[i] == "8":
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*100+20, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],(round(x[i]*100)-5)))
                self.note_pos.append(x[i]*100+20)
                self.sym.append("8")

                layer = QGraphicsTextItem("𝅮")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*100-8, y+70) # adjust position of rest note
                layer.setRotation(160)

                transform = QTransform()
                transform.scale(-1, 1) # Flip horizontally
                layer.setTransform(transform)
                self.notation_note_scene.addItem(layer)

class lv1_drum_5:
    def __init__(self, cord):
        self.cord = []
        self.note_scene = None

    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
  
    def draw_lv1(self, pitch, x,y,symbols):
        symbols_list = [21,22,23,24,25,26,27,28,30,31,37,38]
        value_to_set = '4'
        for index in symbols_list :
            if 0 <= index < len(symbols):
                symbols[index] = value_to_set

        dup_note = [1,4,6,8,10,12,14,17,20,22,24,26,28,30,38] #10, 20, 21, 1]
        for index in sorted(dup_note, reverse=True):
            if 0 <= index < len(symbols):
                symbols.pop(index)
                pitch.pop(index)
                x.pop(index)

        for i in range(len(pitch)):
            if pitch[i] == ["D2"] and symbols[i] == "4":
                D2 = QGraphicsTextItem("𝅘𝅥")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*100, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*100)+5)))
                self.note_pos.append(x[i]*100)
                self.sym.append("4")
            
            if pitch[i] == ["A2"] and symbols[i] == "4":
                A2 = QGraphicsTextItem("𝅘𝅥")
                A2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                A2.setFont(font)
                A2.setPos(x[i]*100, y-63) # adjust position of rest note
                self.notation_note_scene.addItem(A2)
                self.cord.append((pitch[i],(round(x[i]*100)+5)))
                self.note_pos.append(x[i]*100)
                self.sym.append("4")

            if pitch[i] == ["A2"] and symbols[i] == "8":
                A2 = QGraphicsTextItem("𝅘𝅥𝅮")
                A2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                A2.setFont(font)
                A2.setPos(x[i]*100, y-63) # adjust position of rest note
                self.notation_note_scene.addItem(A2)
                self.cord.append((pitch[i],(round(x[i]*100)+5)))
                self.note_pos.append(x[i]*100)
                self.sym.append("8")
            
            if pitch[i] == ["D2"] and symbols[i] == "8":
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*100, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*100)+5)))
                self.note_pos.append(x[i]*100)
                self.sym.append("8")

            if pitch[i] == ["B1"]:
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*100+20, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],(round(x[i]*100)-5)))
                self.note_pos.append(x[i]*100)
                self.sym.append("4")

class lv1_drum_6:
    def __init__(self, cord):
        self.cord = []
        self.note_scene = None

    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
  
    def draw_lv1(self, pitch, x,y,symbols):
        symbols_list = [1,2,4,5,8,12,13,16,30,31,32,33,34,35,36,37]
        value_to_set = '4'
        for index in symbols_list :
            if 0 <= index < len(symbols):
                symbols[index] = value_to_set
            
        dup_note = [1,5,7,9,11,17,19,21,23,25,27,29,31,33,35] #10, 20, 21, 1]
        for index in sorted(dup_note, reverse=True):
            if 0 <= index < len(symbols):
                symbols.pop(index)
                pitch.pop(index)
                x.pop(index)
        
        symbols[12] = '8'
        symbols[13] = '8'
        
        for i in range(len(pitch)):
            #print(pitch[i],x[i],symbols[i],i)
            if pitch[i] == ["D2"] and symbols[i] == "4":
                D2 = QGraphicsTextItem("𝅘𝅥")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*100, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],round(x[i]*100)+5))
                self.note_pos.append(x[i]*100)
                self.sym.append("4")
            
            if pitch[i] == ["D3"] and symbols[i] == "4":
                A2 = QGraphicsTextItem("𝅘𝅥")
                A2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                A2.setFont(font)
                A2.setPos(x[i]*100, y-83) # adjust position of rest note
                self.notation_note_scene.addItem(A2)
                self.cord.append((pitch[i],round(x[i]*100)+5))
                self.note_pos.append(x[i]*100)
                self.sym.append("4")

            if pitch[i] == ["G2"] and symbols[i] == "4":
                G2 = QGraphicsTextItem("𝅘𝅥")
                G2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                G2.setFont(font)
                G2.setPos(x[i]*100+20, y+60) # adjust position of rest note
                G2.setRotation(180)
                self.notation_note_scene.addItem(G2)
                self.cord.append((pitch[i],round(x[i]*100)-5))
                self.note_pos.append(x[i]*100)
                self.sym.append("4")

            if pitch[i] == ["D3"] and symbols[i] == "8":
                A2 = QGraphicsTextItem("𝅘𝅥𝅮")
                A2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                A2.setFont(font)
                A2.setPos(x[i]*100, y-83) # adjust position of rest note
                self.notation_note_scene.addItem(A2)
                self.cord.append((pitch[i],round(x[i]*100)))
                self.note_pos.append(x[i]*100)
                self.sym.append("8")
            
            if pitch[i] == ["D2"] and symbols[i] == "8":
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*100, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],round(x[i]*100)+5))
                self.note_pos.append(x[i]*100)
                self.sym.append("8")

            if pitch[i] == ["B1"] and symbols[i] == '4':
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*100+20, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],round(x[i]*100)-10))
                self.note_pos.append(x[i]*100)
                self.sym.append("4")

            if pitch[i] == ["B1"] and symbols[i] == "8":
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*100+20, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],(round(x[i]*100)-10)))
                self.note_pos.append(x[i]*100)
                self.sym.append("8")

                layer = QGraphicsTextItem("𝅮")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*100-8, y+70) # adjust position of rest note
                layer.setRotation(160)

                transform = QTransform()
                transform.scale(-1, 1) # Flip horizontally
                layer.setTransform(transform)
                self.notation_note_scene.addItem(layer)