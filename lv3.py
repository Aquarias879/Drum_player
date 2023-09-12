from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class lv3_drum_1:
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
  
    def draw_lv3(self, pitch, x, y,symbols):
        #print(pitch)
        for i in range(len(pitch)):
            if pitch[i] == ["F#2"] and symbols[i] == "8":
                F2 = QGraphicsTextItem("𝅃")
                F2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                F2.setFont(font)
                F2.setPos(x[i]*155, y-88) # adjust position of rest note
                self.notation_note_scene.addItem(F2)
                self.cord.append(((['B1','F#2']),round(x[i]*155-50)+5))
                self.cord.append((pitch[i],round(x[i]*155-50)+5))
                self.note_pos.append(x[i]*155)
                
                l = QGraphicsTextItem("𝇁")
                l.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                l.setFont(font)
                l.setPos(x[i]*155+8, y-88) # adjust position of rest note
                self.notation_note_scene.addItem(l)

                layer = QGraphicsTextItem("𝅮")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*155+8, y-91) # adjust position of rest note
                layer.setRotation(-10)
                self.notation_note_scene.addItem(layer)
                self.sym.append("8")
            
            if pitch[i] == ["B1"] and symbols[i] == "4":
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*155-50, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],round(x[i]*155-50)))
                self.note_pos.append(x[i]*155-50)
                self.sym.append("4")
            
            if pitch[i] == ["D2"] or pitch[i] == ["E2"] and symbols [i] == 8:
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*155-75, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],round(x[i]*155-75)+30))
                self.cord.append(((['D2','F#2']),round(x[i]*155-75)+30))
                self.note_pos.append(x[i]*155-75)
                self.sym.append("8")
            
                rest = QGraphicsTextItem("𝄽")
                rest.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                rest.setFont(font)
                rest.setPos(x[i]*155-75, y+5) # adjust position of rest note
                self.notation_note_scene.addItem(rest)
                
class lv3_drum_2:
    def __init__(self, cord):
        self.cord = []
        self.note_scene = None

    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
  
    def draw_lv3(self, pitch, x, y,symbols):
        indices_and_symbols = [6,13,20,27,34,41,48,55,62,69,76,83,90,97,104,111]

        for index in indices_and_symbols:
           symbols[index] = '8'

        for i in range(len(pitch)):
            print(pitch[i],x[i],symbols[i],i)
            if pitch[i] == ["F#2"] and symbols[i] == "8":
                F2 = QGraphicsTextItem("𝅃")
                F2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                F2.setFont(font)
                F2.setPos(x[i]*155, y-88) # adjust position of rest note
                self.notation_note_scene.addItem(F2)
                
                self.cord.append((pitch[i],round(x[i]*155)+30))
                self.note_pos.append(x[i]*155)
                self.sym.append("8")
                
                l = QGraphicsTextItem("𝇁")
                l.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                l.setFont(font)
                l.setPos(x[i]*155+8, y-88) # adjust position of rest note
                self.notation_note_scene.addItem(l)

                layer = QGraphicsTextItem("𝅮")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*155+8, y-91) # adjust position of rest note
                layer.setRotation(-10)
                self.notation_note_scene.addItem(layer)
                
            if pitch[i] == ["B1"] and symbols[i] == "4":
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*155-50, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],round(x[i]*155-50)))
                self.sym.append("4")
                self.cord.append(((['B1','F#2']),round(x[i]*155)-50))
                self.sym.append("4")
                self.note_pos.append(x[i]*155-50)
               
            
            if pitch[i] == ["B1"] and symbols[i] == "8":
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*155-50, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],round(x[i]*155-45)))
                self.sym.append("8")
                self.cord.append(((['B1','F#2']),round(x[i]*155)-45))
                self.sym.append("8")
                self.note_pos.append(x[i]*155-45)
                
                layer = QGraphicsTextItem("𝅮")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*155-50-28, y+70) # adjust position of rest note
                layer.setRotation(160)
                transform = QTransform()
                transform.scale(-1, 1) # Flip horizontally
                layer.setTransform(transform)
                self.notation_note_scene.addItem(layer)
            
            if pitch[i] == ["D2"] or pitch[i] == ["E2"] and symbols [i] == 8:
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*155-75, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],round(x[i]*155-75)+30))
                self.note_pos.append(x[i]*155-75)
                self.sym.append("8")
                self.cord.append(((['D2','F#2']),round(x[i]*155-75)+30))
                self.sym.append("8")
            
                rest = QGraphicsTextItem("𝄾")
                rest.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                rest.setFont(font)
                rest.setPos(x[i]*155-75, y+5) # adjust position of rest note
                self.notation_note_scene.addItem(rest)

class  lv3_drum_3:
    def __init__(self, cord):
        self.cord = []
        self.note_scene = None

    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
  
    def draw_lv3(self, pitch, x, y,symbols):
        for i in range(len(pitch)):
            #print(pitch[i],x[i],symbols[i],i)
            if pitch[i] == ["F#2"] and symbols[i] == "8":
                F2 = QGraphicsTextItem("𝅃")
                F2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                F2.setFont(font)
                F2.setPos(x[i]*155, y-88) # adjust position of rest note
                self.notation_note_scene.addItem(F2)
                self.cord.append((pitch[i],round(x[i]*155)+30))
                self.note_pos.append(x[i]*155)
                
                l = QGraphicsTextItem("𝇁")
                l.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                l.setFont(font)
                l.setPos(x[i]*155+8, y-88) # adjust position of rest note
                self.notation_note_scene.addItem(l)

                layer = QGraphicsTextItem("𝅮")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*155+8, y-91) # adjust position of rest note
                layer.setRotation(-10)
                self.notation_note_scene.addItem(layer)
                self.sym.append("8")
            
            if pitch[i] == ["B1"] :
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*155-10, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],round(x[i]*155)-5))
                self.note_pos.append(x[i]*155-10)
                self.sym.append("8")
                self.cord.append(((['B1','F#2']),round(x[i]*155)-5))
                self.sym.append("8")

                layer = QGraphicsTextItem("𝅮")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*155-10-28, y+70) # adjust position of rest note
                layer.setRotation(160)

                transform = QTransform()
                transform.scale(-1, 1) # Flip horizontally
                layer.setTransform(transform)
                self.notation_note_scene.addItem(layer)
            
            if pitch[i] == ["D2"] or pitch[i] == ["E2"] and symbols [i] == '8':
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*155-75, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],round(x[i]*155-75)+30))
                self.cord.append(((['D2','F#2']),round(x[i]*155-75)+30))
                self.note_pos.append(x[i]*155-75)
                self.sym.append("8")
            
                rest = QGraphicsTextItem("𝄽")
                rest.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                rest.setFont(font)
                rest.setPos(x[i]*155-75, y+5) # adjust position of rest note
                self.notation_note_scene.addItem(rest)
      
class  lv3_drum_4:
    def __init__(self, cord):
        self.cord = []
        self.note_scene = None

    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
  
    def draw_lv3(self, pitch, x, y,symbols):
        
        indices_and_pos = [13,27,41,55,69,83,97,111]
        for i in indices_and_pos:
           symbols[i] = '8'
        
        indices_and_symbols = [10,24,38,52,66,80,94,108]
        for index in indices_and_symbols:
           symbols[index] = '8'

        for i in range(len(pitch)):
            #print(pitch[i],x[i],symbols[i],i)
            if pitch[i] == ["F#2"] and symbols[i] == "8":
                F2 = QGraphicsTextItem("𝅃")
                F2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                F2.setFont(font)
                F2.setPos(x[i]*155, y-88) # adjust position of rest note
                self.notation_note_scene.addItem(F2)
                self.cord.append((pitch[i],round(x[i]*155)+30))
                self.note_pos.append(x[i]*155)
                
                l = QGraphicsTextItem("𝇁")
                l.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                l.setFont(font)
                l.setPos(x[i]*155+8, y-88) # adjust position of rest note
                self.notation_note_scene.addItem(l)

                layer = QGraphicsTextItem("𝅮")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*155+8, y-91) # adjust position of rest note
                layer.setRotation(-10)
                self.notation_note_scene.addItem(layer)
                self.sym.append("8")
            
            if pitch[i] == ["B1"] and symbols[i] == '8' : #actually it is 4 but use 8 to catch will easy to catch 
                #print(pitch[i],x[i],symbols[i],i)
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*155-50, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],round(x[i]*155-45)))
                self.note_pos.append(x[i]*155-50)
                self.sym.append("4")
                self.cord.append(((['B1','F#2']),round(x[i]*155-45)))
                self.sym.append("4")

            if pitch[i] == ["B1"] and symbols[i] == '4': # same actually it is 8 
                #print(pitch[i],x[i],symbols[i],i)
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*155-10, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],round(x[i]*155)-5))
                self.note_pos.append(x[i]*155-50)
                self.sym.append("8")
                self.cord.append(((['B1','F#2']),round(x[i]*155)-5))
                self.sym.append("8")

                layer = QGraphicsTextItem("𝅮")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*155-10-28, y+70) # adjust position of rest note
                layer.setRotation(160)

                transform = QTransform()
                transform.scale(-1, 1) # Flip horizontally
                layer.setTransform(transform)
                self.notation_note_scene.addItem(layer)

            if pitch[i] == ["D2"] and symbols[i] == '4':
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*155-40, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],round(x[i]*155-10)))
                self.note_pos.append(x[i]*155-10)
                self.sym.append("4")
                self.cord.append(((['D2','F#2']),round(x[i]*155-10)))
                self.sym.append("4")
        
                rest = QGraphicsTextItem("𝄾")
                rest.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                rest.setFont(font)
                rest.setPos(x[i]*155-40, y+5) # adjust position of rest note
                self.notation_note_scene.addItem(rest)

            if pitch[i] == ["D2"] and symbols [i] == '8':
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*155-80, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],round(x[i]*155-45)))
                self.note_pos.append(x[i]*155-75)
                self.sym.append("8")
                self.cord.append(((['D2','F#2']),round(x[i]*155-45)))
                self.sym.append("8")
            
                rest = QGraphicsTextItem("𝄽")
                rest.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                rest.setFont(font)
                rest.setPos(x[i]*155-80, y+5) # adjust position of rest note
                self.notation_note_scene.addItem(rest)

class  lv3_drum_5:
    def __init__(self, cord):
        self.cord = []
        self.note_scene = None

    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
  
    def draw_lv3(self, pitch, x, y,symbols):
        indices_and_symbols = [2,16,30,44,58,72,86,100]

        for index in indices_and_symbols:
           symbols[index] = '8'

        for i in range(len(pitch)):
            #print(pitch[i],x[i],symbols[i],i)
            if pitch[i] == ["F#2"] and symbols[i] == "8":
                F2 = QGraphicsTextItem("𝅃")
                F2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                F2.setFont(font)
                F2.setPos(x[i]*155, y-88) # adjust position of rest note
                self.notation_note_scene.addItem(F2)
                self.cord.append((pitch[i],round(x[i]*155)+30))
                self.note_pos.append(x[i]*155)
                
                l = QGraphicsTextItem("𝇁")
                l.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                l.setFont(font)
                l.setPos(x[i]*155+8, y-88) # adjust position of rest note
                self.notation_note_scene.addItem(l)

                layer = QGraphicsTextItem("𝅮")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*155+8, y-91) # adjust position of rest note
                layer.setRotation(-10)
                self.notation_note_scene.addItem(layer)
                self.sym.append("8")
            
            if pitch[i] == ["D2"] or pitch[i] == ["E2"] and symbols[i] == "8":
                D2 = QGraphicsTextItem("𝅘𝅥𝅮")
                D2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                D2.setFont(font)
                D2.setPos(x[i]*155-40, y-55) # adjust position of rest note
                self.notation_note_scene.addItem(D2)
                self.cord.append((pitch[i],round(x[i]*155)-5))
                self.sym.append("8")
                self.cord.append(((['D2','F#2']),round(x[i]*155)-5))
                self.note_pos.append(x[i]*155-75)
                self.sym.append("8")
            
                rest = QGraphicsTextItem("𝄾")
                rest.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                rest.setFont(font)
                rest.setPos(x[i]*155-40, y+5) # adjust position of rest note
                self.notation_note_scene.addItem(rest)
        
            if pitch[i] == ["B1"] and symbols[i] == "8":
                #print(pitch[i],x[i],symbols[i],i)
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*155-50, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],round(x[i]*155-45)))
                self.sym.append("4")
                self.cord.append(((['B1','F#2']),round(x[i]*155-45)))
                self.sym.append("4")
                self.note_pos.append(x[i]*155-50)
        
            if pitch[i] == ["B1"] and symbols[i] == '4': # same actually it is 8 
                #print(pitch[i],x[i],symbols[i],i)
                C2 = QGraphicsTextItem("𝅘𝅥")
                C2.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(30)
                C2.setFont(font)
                C2.setPos(x[i]*155-10, y+75) # adjust position of rest note
                C2.setRotation(180)
                self.notation_note_scene.addItem(C2)
                self.cord.append((pitch[i],round(x[i]*155-5)))
                self.note_pos.append(x[i]*155-5)
                self.sym.append("8")
                self.cord.append(((['B1','F#2']),round(x[i]*155-5)))
                self.sym.append("8")

                layer = QGraphicsTextItem("𝅮")
                layer.setDefaultTextColor(Qt.black)
                font = self.font()
                font.setPointSize(28)
                layer.setFont(font)
                layer.setPos(x[i]*155-10-28, y+70) # adjust position of rest note
                layer.setRotation(160)

                transform = QTransform()
                transform.scale(-1, 1) # Flip horizontally
                layer.setTransform(transform)
                self.notation_note_scene.addItem(layer)
           
       