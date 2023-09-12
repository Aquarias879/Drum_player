from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class lv2_drum_1:
    def __init__(self, cord):
        #self.line_length = line_length
        self.cord = []
        self.note_pos = []
        self.sym = []
        self.note_scene = None

    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
  
    def draw_lv2(self, pitch, x, y,symbols):
        indices_and_values = [
            (2, 0.75), (3, 0.875), (4, 1.0), (5, 1.125), (6, 1.25),
            (7, 1.75), (8, 2.25), (9, 2.5), (10, 2.75), (11, 3.0),
            (12, 3.125), (13, 3.25), (14, 3.375), (15, 3.5), (16, 4.0),
            (17, 4.5), (18, 5.0), (19, 5.25), (20, 5.5), (21, 5.625),
            (22, 5.75), (23, 5.875), (24, 6.125), (25, 6.375),
            (26, 6.5), (27, 6.625), (28, 6.75)
        ]

        for index, value in indices_and_values:
            if 0 <= index < len(x):
                x[index] = value

        for i in range(len(pitch)):
            #print(pitch[i],x[i],symbols[i],i)
            if pitch[i] == ["D2"] and symbols[i] == '4':
                E2 = QGraphicsTextItem("𝅘𝅥")
                E2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                E2.setFont(font)
                E2.setPos(x[i]*165, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(E2)
                self.cord.append((pitch[i],round(x[i]*165)))
                self.note_pos.append(x[i]*165)
                self.sym.append("4")

            if pitch[i] == ["D2"] and symbols[i] == '8':
                E2 = QGraphicsTextItem("𝅘𝅥𝅮")
                E2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                E2.setFont(font)
                E2.setPos(x[i]*165, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(E2)
                self.cord.append((pitch[i],round(x[i]*165)))
                self.note_pos.append(x[i]*165)
                self.sym.append("8")
            
            if pitch[i] == ["D2"] and symbols[i] == '16':
                E2 = QGraphicsTextItem("𝅘𝅥𝅯")
                E2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                E2.setFont(font)
                E2.setPos(x[i]*165, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(E2)
                self.cord.append((pitch[i],round(x[i]*165)+5))
                self.note_pos.append(x[i]*165)
                self.sym.append("16")
            
            E2 = QGraphicsTextItem("𝅘𝅥")
            E2.setDefaultTextColor(Qt.black)
            font = self.font()
            font.setPointSize(30)
            E2.setFont(font)
            E2.setPos(6.875*165, y-55) # adjust position of rest note
            self.notation_note_scene.addItem(E2)
            self.cord.append((pitch[i],round(6.875*165)))
            self.note_pos.append(x[i]*165)
            self.sym.append("4")

            C = QGraphicsTextItem("𝄽")
            C.setDefaultTextColor(Qt.black)
            font = self.font()
            font.setPointSize(30)
            C.setFont(font)
            C.setPos(7.375*165, y-55) # adjust position of rest note
            self.notation_note_scene.addItem(C)
        
class lv2_drum_2:
    def __init__(self, cord):
        self.cord = []
        self.note_scene = None

    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
  
    def draw_lv2(self, pitch, x, y,symbols):
        odd_indices = [index for index in range(len(symbols)) if index % 2 == 1 and index != 1]

        for index in reversed(odd_indices):
            symbols.pop(index)
            pitch.pop(index)
            x.pop(index)

        x = [value + 0.125 for value in x] 

        indices_and_symbols = [
            (0, '4'), (2, '16'), (3, '8'), (6, '4'), (12, '8'),
            (13, '8'), (15, '4'), (18, '8'), (20, '16'), (21, '8'),
            (24, '4'), (25, '8'), (26, '8'), (27, '8'), (29, '4')
        ]

        for index, symbol in indices_and_symbols:
            if 0 <= index < len(symbols):
                symbols[index] = symbol

        test = x[24:]
        x = x[:24]
        x.extend([n + 0.125 for n in test])

        for i in range(len(pitch)):
            #print(pitch[i],x[i],symbols[i],i)
            if pitch[i] == ["D2"] and symbols[i] == "4":
                D2 = QGraphicsTextItem("𝅘𝅥")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*165, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*165))))
                self.note_pos.append(x[i]*165)
                self.sym.append("4")

            if pitch[i] == ["D2"] and symbols[i] == "8":
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*165, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*165))))
                self.note_pos.append(x[i]*165)
                self.sym.append("8")

            if pitch[i] == ["D2"] and symbols[i] == "8":
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*165, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*165))))
                self.note_pos.append(x[i]*165)
                self.sym.append("8")
            
            if pitch[i] == ["D2"] and symbols[i] == "16":
                D2 = QGraphicsTextItem("𝅘𝅥𝅯")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*165, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*165))))
                self.note_pos.append(x[i]*165)
                self.sym.append("16")

            if pitch[i] == ["B1"] and symbols[i] == "4":
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*165+20, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],(round(x[i]*165)-10)))
                self.note_pos.append(x[i]*165)
                self.sym.append("4")

            if pitch[i] == ["B1"] and symbols[i] == "8":
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*165+20, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],(round(x[i]*165)-10)))
                self.note_pos.append(x[i]*165)
                self.sym.append("8")

                layer = QGraphicsTextItem("𝅮")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*165-7, y+70) # adjust position of rest note
                layer.setRotation(160)

                transform = QTransform()
                transform.scale(-1, 1) # Flip horizontally
                layer.setTransform(transform)
                self.notation_note_scene.addItem(layer)
            
            if pitch[i] == ["B1"] and symbols[i] == "16":
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*165+20, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],(round(x[i]*165)-10)))
                self.note_pos.append(x[i]*165)
                self.sym.append("16")

                layer = QGraphicsTextItem("𝅯")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*165-5, y+75) # adjust position of rest note
                layer.setRotation(170)

                transform = QTransform()
                transform.scale(-1, 1) # Flip horizontally
                layer.setTransform(transform)
                self.notation_note_scene.addItem(layer)

class lv2_drum_3:
    def __init__(self, cord):
        self.cord = []
        self.note_scene = None

    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
  
    def draw_lv2(self, pitch, x, y,symbols):
        dup_note = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64]
        for index in sorted(dup_note, reverse=True):
            if 0 <= index < len(symbols):
                symbols.pop(index)
                pitch.pop(index)
                x.pop(index)

        indices_and_symbols = [
            (0, '16'), (4, '4'), (6, '8'), (8, '16'), (12, '4'),
            (14, '8'), (16, '16'), (20, '4'), (23, '16'), (31, '4')
        ]

        for index, symbol in indices_and_symbols:
            if 0 <= index < len(symbols):
                symbols[index] = symbol
    
        x = [value + 0.1875 for value in x] 

        for i in range(len(pitch)):
            #print(pitch[i],x[i],symbols[i],i)
            if pitch[i] == ["D2"] and symbols[i] == "4":
                D2 = QGraphicsTextItem("𝅘𝅥")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*150, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*150))))
                self.note_pos.append(x[i]*150)
                self.sym.append("4")

            if pitch[i] == ["D2"] and symbols[i] == "8":
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*150, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*150))))
                self.note_pos.append(x[i]*150)
                self.sym.append("8")

            if pitch[i] == ["D2"] and symbols[i] == "16":
                D2 = QGraphicsTextItem("𝅘𝅥𝅯")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*150, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*150))))
                self.note_pos.append(x[i]*150)
                self.sym.append("16")

class lv2_drum_4:
    def __init__(self, cord):
        self.cord = []
        self.note_scene = None

    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
  
    def draw_lv2(self, pitch, x, y,symbols):
        dup_note = [2,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63]
        for index in sorted(dup_note, reverse=True):
            if 0 <= index < len(symbols):
                symbols.pop(index)
                pitch.pop(index)
                x.pop(index)
        x = [value + 0.125 for value in x] 
        indices_and_symbols = [
            (0, '16'), (1, '8'), (4, '4'), (8, '16'), (9, '8'),
            (12, '4'), (14, '8'), (17, '8'), (18, '8'), (20, '4'),
            (23, '8'), (24, '4'), (25, '8'), (28, '8'), (31, '4')
        ]

        for index, symbol in indices_and_symbols:
            if 0 <= index < len(symbols):
                symbols[index] = symbol
     
        for i in range(len(pitch)):
            #print(pitch[i],x[i],symbols[i],i)
            if pitch[i] == ["D2"]  and symbols[i] == "4":
                D2 = QGraphicsTextItem("𝅘𝅥")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*155, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*155))))
                self.note_pos.append(x[i]*155)
                self.sym.append("4")

            if pitch[i] == ["D2"] and symbols[i] == "8":
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*155, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*155))))
                self.note_pos.append(x[i]*155)
                self.sym.append("8")

            if pitch[i] == ["D2"] and symbols[i] == "8":
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*155, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*155))))
                self.note_pos.append(x[i]*155)
                self.sym.append("8")
            
            if pitch[i] == ["D2"] and symbols[i] == "16":
                D2 = QGraphicsTextItem("𝅘𝅥𝅯")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*155, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*155))))
                self.note_pos.append(x[i]*155)
                self.sym.append("16")
            
            if pitch[i] == ["B1"] and symbols[i] == "4":
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*155+20, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],(round(x[i]*155)-5)))
                self.note_pos.append(x[i]*155)
                self.sym.append("4")

            if pitch[i] == ["B1"] and symbols[i] == "8":
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*155+20, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],(round(x[i]*155)-5)))
                self.note_pos.append(x[i]*155)
                self.sym.append("8")

                layer = QGraphicsTextItem("𝅮")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*155-7, y+70) # adjust position of rest note
                layer.setRotation(160)

                transform = QTransform()
                transform.scale(-1, 1) # Flip horizontally
                layer.setTransform(transform)
                self.notation_note_scene.addItem(layer)
            
            if pitch[i] == ["B1"] and symbols[i] == "16":
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*155+20, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],(round(x[i]*155)-5)))
                self.note_pos.append(x[i]*155)
                self.sym.append("16")

                layer = QGraphicsTextItem("𝅯")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*155-5, y+75) # adjust position of rest note
                layer.setRotation(170)

                transform = QTransform()
                transform.scale(-1, 1) # Flip horizontally
                layer.setTransform(transform)
                self.notation_note_scene.addItem(layer)

class lv2_drum_5:
    def __init__(self, cord):
        self.cord = []
        self.note_scene = None

    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
  
    def draw_lv2(self, pitch, x, y,symbols):
        indices_and_values = [
            (1, 0.5), (2, 0.625), (3, 0.75), (8, 2.0), (9, 2.125),
            (10, 2.375), (11, 2.625), (12, 2.875), (13, 3.125), (14, 3.25),
            (15, 3.375), (16, 3.625), (17, 3.75), (18, 3.875), (19, 4.125),
            (20, 4.375), (21, 4.625), (22, 4.75), (23, 4.875), (24, 5.125),
            (25, 5.375), (26, 5.625), (27, 5.75), (28, 5.875), (29, 6.125),
            (30, 6.25), (31, 6.5), (32, 6.75), (33, 6.875), (34, 7.0),
            (35, 7.25), (36, 7.5), (37, 8.0), (38, 8.25)
        ]

        for index, value in indices_and_values:
            if 0 <= index < len(x):
                x[index] = value

        for i in range(len(pitch)):
            if pitch[i] == ["D2"] and symbols[i] == "4":
                D2 = QGraphicsTextItem("𝅘𝅥")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*150, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*150))))
                self.note_pos.append(x[i]*150)
                self.sym.append("4")

            if pitch[i] == ["D2"] and symbols[i] == "8":
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*150, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*150))))
                self.note_pos.append(x[i]*150)
                self.sym.append("8")

            if pitch[i] == ["D2"] and symbols[i] == "16":
                D2 = QGraphicsTextItem("𝅘𝅥𝅯")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*150, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],(round(x[i]*150))))
                self.note_pos.append(x[i]*150)
                self.sym.append("16")
            
            D2 = QGraphicsTextItem("𝅘𝅥𝅯")
            D2.setDefaultTextColor(Qt.black)
            font = self.font()
            font.setPointSize(30)
            D2.setFont(font)
            D2.setPos(8.375*150, y-55) # adjust position of rest note
            self.notation_note_scene.addItem(D2)
            self.cord.append((['D2'],(round(8.375*150))))
            self.note_pos.append(8.375*15)
            self.sym.append("16")