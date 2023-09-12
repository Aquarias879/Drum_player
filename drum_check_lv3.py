from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class checknote_drum_lv3:
    def __init__(self, cord):
         self.note_scene = None
    
    def drawed(self):
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
    
    def drum_correct1(self, pitch, new_pos, cord, note_pos, type):
        y=80
        def add_text_item(note, color, x_pos, pos_y, font_size):
            text_item = QGraphicsTextItem(note)
            text_item.setDefaultTextColor(color)
            font = self.font()
            font.setPointSize(font_size)
            text_item.setFont(font)
            text_item.setPos(x_pos, pos_y)
            self.notation_note_scene.addItem(text_item)

        tolerance = 1  # Adjust this tolerance value as needed
        
        for i in range(len(cord)):
            if cord[i][1] % 5 == 0:
                pos = cord[i][1] + 0
            elif cord[i][1] % 5 == 1:
                pos = cord[i][1] + 4
            elif cord[i][1] % 5 == 2:
                pos = cord[i][1] + 3
            elif cord[i][1] % 5 == 3:
                pos = cord[i][1] + 2
            elif cord[i][1] % 5 == 4:
                pos = cord[i][1] + 1
            
            
            if cord[i][0] == pitch:
                #print(type[i])
                if abs(new_pos.x() - pos) <= tolerance:
                    if pitch == ["F#2"] :
                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                    if pitch == ["D2","F#2"]:
                        add_text_item("𝅘𝅥𝅮", Qt.green, cord[i][1]-30, y - 55, 30)

                        add_text_item("𝅃", Qt.green, cord[i][1]-28, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-20, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-20, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                    if pitch == ["B1","F#2"]:
                        add_text_item("𝅃", Qt.green, cord[i][1]-28, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-20, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-20, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1]+2, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                    
                    if pitch == ["B1"]:
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1], y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                    
                    if pitch == ["D2"] and type[i] == '8':
                        add_text_item("𝅘𝅥𝅮", Qt.green, cord[i][1]-30, y - 55, 30)
 
    def drum_correct2(self, pitch, new_pos, cord, note_pos, type):
        y=80
        def add_text_item(note, color, x_pos, pos_y, font_size):
            text_item = QGraphicsTextItem(note)
            text_item.setDefaultTextColor(color)
            font = self.font()
            font.setPointSize(font_size)
            text_item.setFont(font)
            text_item.setPos(x_pos, pos_y)
            self.notation_note_scene.addItem(text_item)

        tolerance = 1  # Adjust this tolerance value as needed
        
        for i in range(len(cord)):
            if cord[i][1] % 5 == 0:
                pos = cord[i][1] + 0
            elif cord[i][1] % 5 == 1:
                pos = cord[i][1] + 4
            elif cord[i][1] % 5 == 2:
                pos = cord[i][1] + 3
            elif cord[i][1] % 5 == 3:
                pos = cord[i][1] + 2
            elif cord[i][1] % 5 == 4:
                pos = cord[i][1] + 1

            if cord[i][0] == pitch:
                if abs(new_pos.x() - pos) <= tolerance:
                    if pitch == ["F#2"] :
                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                    if pitch == ["D2","F#2"]:
                        add_text_item("𝅘𝅥𝅮", Qt.green, cord[i][1]-30, y - 55, 30)

                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                    if pitch == ["B1","F#2"] and type[i] == '4':
                        add_text_item("𝅃", Qt.green, cord[i][1]-25, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-18, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-18, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1], y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                    
                    if pitch == ["B1","F#2"] and type[i] == '8':
                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1]-5, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)

                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-35, y+70) # adjust position of rest note
                        layer.setRotation(160)

                        transform = QTransform()
                        transform.scale(-1, 1) # Flip horizontally
                        layer.setTransform(transform)
                        self.notation_note_scene.addItem(layer)
                    
                    if pitch == ["B1"] and type[i] == '4':
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1], y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                    
                    if pitch == ["B1"] and type[i] == "8":
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1]-5, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                      
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-32, y+70) # adjust position of rest note
                        layer.setRotation(160)

                        transform = QTransform()
                        transform.scale(-1, 1) # Flip horizontally
                        layer.setTransform(transform)
                        self.notation_note_scene.addItem(layer)
                    
                    if pitch == ["D2"] or pitch == ['E2'] and type[i] == '8':
                        add_text_item("𝅘𝅥𝅮", Qt.green, cord[i][1]-30, y - 55, 30)
        
    def drum_correct3(self, pitch, new_pos, cord, note_pos, type):
        y=80
        def add_text_item(note, color, x_pos, pos_y, font_size):
            text_item = QGraphicsTextItem(note)
            text_item.setDefaultTextColor(color)
            font = self.font()
            font.setPointSize(font_size)
            text_item.setFont(font)
            text_item.setPos(x_pos, pos_y)
            self.notation_note_scene.addItem(text_item)

        tolerance = 1  # Adjust this tolerance value as needed
        
        for i in range(len(cord)):
            if cord[i][1] % 5 == 0:
                pos = cord[i][1] + 0
            elif cord[i][1] % 5 == 1:
                pos = cord[i][1] + 4
            elif cord[i][1] % 5 == 2:
                pos = cord[i][1] + 3
            elif cord[i][1] % 5 == 3:
                pos = cord[i][1] + 2
            elif cord[i][1] % 5 == 4:
                pos = cord[i][1] + 1

            if cord[i][0] == pitch:
                if abs(new_pos.x() - pos) <= tolerance:
                    if pitch == ["F#2"] :
                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                    if pitch == ["D2","F#2"]:
                        add_text_item("𝅘𝅥𝅮", Qt.green, cord[i][1]-30, y - 55, 30)

                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                    if pitch == ["B1","F#2"] and type[i] == '8':
                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1]-5, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)

                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-35, y+70) # adjust position of rest note
                        layer.setRotation(160)

                        transform = QTransform()
                        transform.scale(-1, 1) # Flip horizontally
                        layer.setTransform(transform)
                        self.notation_note_scene.addItem(layer)
                    
                    if pitch == ["B1"] and type[i] == '4':
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1], y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                    
                    if pitch == ["B1"] and type[i] == "8":
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1]-5, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                      
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-32, y+70) # adjust position of rest note
                        layer.setRotation(160)

                        transform = QTransform()
                        transform.scale(-1, 1) # Flip horizontally
                        layer.setTransform(transform)
                        self.notation_note_scene.addItem(layer)
                    
                    if pitch == ["D2"] or pitch == ['E2'] and type[i] == '8':
                        add_text_item("𝅘𝅥𝅮", Qt.green, cord[i][1]-30, y - 55, 30)
    
    def drum_correct4(self, pitch, new_pos, cord, note_pos, type):
        y=80
        def add_text_item(note, color, x_pos, pos_y, font_size):
            text_item = QGraphicsTextItem(note)
            text_item.setDefaultTextColor(color)
            font = self.font()
            font.setPointSize(font_size)
            text_item.setFont(font)
            text_item.setPos(x_pos, pos_y)
            self.notation_note_scene.addItem(text_item)

        tolerance = 1  # Adjust this tolerance value as needed
        
        for i in range(len(cord)):
            if cord[i][1] % 5 == 0:
                pos = cord[i][1] + 0
            elif cord[i][1] % 5 == 1:
                pos = cord[i][1] + 4
            elif cord[i][1] % 5 == 2:
                pos = cord[i][1] + 3
            elif cord[i][1] % 5 == 3:
                pos = cord[i][1] + 2
            elif cord[i][1] % 5 == 4:
                pos = cord[i][1] + 1

            if cord[i][0] == pitch:
                if abs(new_pos.x() - pos) <= tolerance:
                    if pitch == ["F#2"] :
                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                    if pitch == ["D2","F#2"]:
                        add_text_item("𝅘𝅥𝅮", Qt.green, cord[i][1]-30, y - 55, 30)

                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)
                    
                    if pitch == ["B1","F#2"] and type[i] == '4':
                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1]-5, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)

                    if pitch == ["B1","F#2"] and type[i] == '8':
                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1]-5, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)

                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-32, y+70) # adjust position of rest note
                        layer.setRotation(160)

                        transform = QTransform()
                        transform.scale(-1, 1) # Flip horizontally
                        layer.setTransform(transform)
                        self.notation_note_scene.addItem(layer)
                    
                    if pitch == ["B1"] and type[i] == '4':
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1]-5, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                    
                    if pitch == ["B1"] and type[i] == "8":
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1]-5, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                      
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-32, y+70) # adjust position of rest note
                        layer.setRotation(160)

                        transform = QTransform()
                        transform.scale(-1, 1) # Flip horizontally
                        layer.setTransform(transform)
                        self.notation_note_scene.addItem(layer)
                    
                    if pitch == ["D2"] or pitch == ['E2'] and type[i] == '8':
                        add_text_item("𝅘𝅥𝅮", Qt.green, cord[i][1]-30, y - 55, 30)
                        
    def drum_correct5(self, pitch, new_pos, cord, note_pos, type):
        y=80
        def add_text_item(note, color, x_pos, pos_y, font_size):
            text_item = QGraphicsTextItem(note)
            text_item.setDefaultTextColor(color)
            font = self.font()
            font.setPointSize(font_size)
            text_item.setFont(font)
            text_item.setPos(x_pos, pos_y)
            self.notation_note_scene.addItem(text_item)

        tolerance = 1  # Adjust this tolerance value as needed
        
        for i in range(len(cord)):
            if cord[i][1] % 5 == 0:
                pos = cord[i][1] + 0
            elif cord[i][1] % 5 == 1:
                pos = cord[i][1] + 4
            elif cord[i][1] % 5 == 2:
                pos = cord[i][1] + 3
            elif cord[i][1] % 5 == 3:
                pos = cord[i][1] + 2
            elif cord[i][1] % 5 == 4:
                pos = cord[i][1] + 1
            
            

            if cord[i][0] == pitch:
                if abs(new_pos.x() - pos) <= tolerance:
                    #print(cord[i],pos,type[i])
                    if pitch == ["F#2"] :
                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                    if pitch == ["D2","F#2"]:
                        add_text_item("𝅘𝅥𝅮", Qt.green, cord[i][1]-35, y - 55, 30)

                        add_text_item("𝅃", Qt.green, cord[i][1]-33, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-25, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-25, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)
                    
                    if pitch == ["B1"] and type[i] == '4':
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1]-5, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                    
                    if pitch == ["B1","F#2"] and type[i] == '4':
                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1]-5, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                    
                    if pitch == ["B1"] and type[i] == "8":
                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1]-5, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)
                      
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-32, y+70) # adjust position of rest note
                        layer.setRotation(160)

                        transform = QTransform()
                        transform.scale(-1, 1) # Flip horizontally
                        layer.setTransform(transform)
                        self.notation_note_scene.addItem(layer)

                    if pitch == ["B1","F#2"] and type[i] == '8':
                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1]-5, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)

                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-32, y+70) # adjust position of rest note
                        layer.setRotation(160)

                        transform = QTransform()
                        transform.scale(-1, 1) # Flip horizontally
                        layer.setTransform(transform)
                        self.notation_note_scene.addItem(layer)
                    
                    if pitch == ["D2"] or pitch == ['E2'] and type[i] == '8':
                        add_text_item("𝅘𝅥𝅮", Qt.green, cord[i][1]-30, y - 55, 30)

'''
                    
                    if pitch == ["B1","F#2"] and type[i] == '4':
                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1]-5, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)

                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-32, y+70) # adjust position of rest note
                        layer.setRotation(160)

                        transform = QTransform()
                        transform.scale(-1, 1) # Flip horizontally
                        layer.setTransform(transform)
                        self.notation_note_scene.addItem(layer)
                    
                        if pitch == ["B1","F#2"] and type[i] == '8':
                        add_text_item("𝅃", Qt.green, cord[i][1]-30, y - 88, 30)
                        add_text_item("𝇁", Qt.green, cord[i][1]-22, y - 88, 30)
                        layer = QGraphicsTextItem("𝅮")
                        layer.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(28)
                        layer.setFont(font)
                        layer.setPos(cord[i][1]-22, y-91) # adjust position of rest note
                        layer.setRotation(-10)
                        self.notation_note_scene.addItem(layer)

                        C2 = QGraphicsTextItem("𝅘𝅥")
                        C2.setDefaultTextColor(Qt.green)
                        font = self.font()
                        font.setPointSize(30)
                        C2.setFont(font)
                        C2.setPos(cord[i][1]-5, y+75) # adjust position of rest note
                        C2.setRotation(180)
                        self.notation_note_scene.addItem(C2)

                    '''
                    
                    