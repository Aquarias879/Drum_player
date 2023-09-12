import os
import sys
import time

import mido
import mido.backends.rtmidi
import pygame
import serial.tools.list_ports
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from serial import Serial

from draw_handdle import *
from drum_check_lv1 import *
from drum_check_lv2 import *
from drum_check_lv3 import *
from lv1 import *
from lv2 import *
from lv3 import *


class SerialThread(QThread):
    getdata = pyqtSignal(list)
    def __init__(self, port, baudrate,current_mode, parent=None):
        super(SerialThread, self).__init__(parent)
        self.port = port
        self.baudrate = baudrate
        self.alive = True
        self.serial = None
        self.selected_port = None
        self.current_mode = current_mode
      
        self.button_midi_maps = {
            'drum': {
                5: './note_bt\B_Drum.wav',  # bass drum
                1: './note_bt\Crash.wav',  # snare drum
                2: './note_bt\FL_Tom.wav',  # closed hi-hat
                7: './note_bt\Tom1.wav',  # tom 1
                8: './note_bt\Tom2.wav',  # tom 2
                9: './note_bt\Snare.wav',  # floor tom
                4: './note_bt\Ride.wav',  # crash cymbal 1
                3: './note_bt\HiHat.wav',  # crash cymbal 2
                6: './note_bt\Splash.wav'   # ride cymbal
                }
            }
    
    def connect(self):
        self.serial = Serial(self.port, self.baudrate)

    def disconnect(self):
        if self.serial is not None:
            self.serial.close()
            self.serial = None
    
    def play_sound(self,path):
        pygame.mixer.init()
        sounds = [pygame.mixer.Sound(file_path) for file_path in path]
        for sound in sounds:
            sound.set_volume(2.0)
            sound.play()
            
    def connect_output_port(self, selected_port):
        try:
            self.output_port = mido.open_output(selected_port)
            self.output_port_name = selected_port
           
        except OSError:
            print("Could not connect to output port "+selected_port)

    def run(self):
        pressed_buttons = set()  # Track previously pressed buttons
        while self.alive:
            try:
                data = self.serial.readline().decode()
                if not data:
                    continue

                button_states = [int(b.strip()) for b in data.split(',')]
                notes = []
                for button, state in enumerate(button_states, start=1):
                    if state == 1 and button not in pressed_buttons:
                        pressed_buttons.add(button)
                        if self.current_mode == 'drum':
                            midi_note = self.button_midi_maps[self.current_mode].get(button)
                            if midi_note:
                                notes.append(midi_note)

                if notes:
                    self.play_sound(notes)
                    self.getdata.emit(notes)

                # Clear pressed buttons after each iteration
                pressed_buttons.clear()
            except:
                pass

    def stop(self):
        self.alive = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_mode = "drum" #
        self.lv_check = None  #check lv to shoe list midi by lv
        self.current_lv = None #list midi
        self.timer = QTimer()
        self.connected = None  # Initialize self.connected to None
        self.playing_notes = []
        self.notes_list  = []
        self.cord = []
        self.note_pos = []
        self.rest_ls = []
        self.note_count = 0
        self.bpm = None
        self.pos_view = 0
        self.sym =[]

        self.midi_maps = {
            'drum': {
                35: 'B1',  # bass drum
                38: 'D2', 
                42: 'F#2',  # closed hi-hat
                48: 'C2',  # tom 1
                47: 'B2',  # tom 2
                43: 'G2',  # floor tom
                40: 'E2',  # crash cymbal 1
                45: 'A2',  # crash cymbal 2
                50: 'D3'   # ride cymbal
            },
            'piano': { 
                0:'whole',
                0:'q_rest',
                0:'e_rest',
                0:'s_rest',
                0:'rest_half',
                60: 'C4', 
                62: 'D4',  
                64: 'E4', 
                65: 'F4',
                67: 'G3',
                69: 'A4',
                71: 'B4',
                72: 'C5',
                74: 'D5',
                36: 'C2',
                40: 'E2'
                # add more mappings for piano sounds here
            },
            'conga': {
                63: 'D#4',  # high conga D#4
                64: 'E4',  # low conga E4
                62: 'D4'# muted conga D4 
                # add more mappings for conga sounds here
            }
        }

        self.midi_dir = {
            'drum': {
                'rest' : None,
                './note_bt\B_Drum.wav' : "B1",  # bass drum
                './note_bt\FL_Tom.wav' : "G2",# snare drum
                './note_bt\HiHat.wav'  :"F#2",  # closed hi-hat
                './note_bt\Ride.wav'   : "E2",  # tom 2
                "./note_bt\Snare.wav"  : "D2",
                './note_bt\Splash.wav' : "G3",  # crash cymbal 1
                './note_bt\Tom1.wav'   : "A2",  # crash cymbal 2
                './note_bt\Tom2.wav'   : "D3",   # ride cymbal
                './note_bt\Crash.wav'  : "A3"
            }}
        
        self.initUI()

    def initUI(self):
        # Create a QLabel for the background image
        '''
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 910, 620)

        # Load the background image
        background_image = QPixmap("BG.jpg")
        self.background_label.setPixmap(background_image)

        # Make the label stacked behind other widgets
        self.background_label.lower()
        '''

        # Create instrument widgets
        self.import_bt = QPushButton("Tranfer")
        self.import_bt.clicked.connect(self.import_midi)
        self.import_bt.setFixedSize(80, 30)

        # Create level frame
        self.level_frame = QFrame(self)
        self.level_frame.setFixedSize(880, 50)

        # Create level layout
        self.level_layout = QHBoxLayout(self.level_frame)

        # Create level widgets
        self.select_lv_label = QLabel("Level:")
        self.current_lv = QComboBox()
        self.current_lv.setFixedSize(200, 30)
        self.lv1_checkbox = QCheckBox("Level 1")
        self.lv2_checkbox = QCheckBox("Level 2")
        self.lv3_checkbox = QCheckBox("Level 3")
        # Create play button widget
        self.play_bt = QPushButton("Play")
        self.play_bt.setFixedSize(80, 30)
        self.play_bt.setCheckable(True)
        self.play_bt.clicked.connect(self.toggle_bt)
        
        # Add level widgets to the layout
        self.level_layout.addWidget(self.select_lv_label)
        self.level_layout.addWidget(self.lv1_checkbox,alignment=Qt.AlignLeft)
        self.level_layout.addWidget(self.lv2_checkbox,alignment=Qt.AlignLeft)
        self.level_layout.addWidget(self.lv3_checkbox,alignment=Qt.AlignLeft)
        self.level_layout.addWidget(self.current_lv,alignment=Qt.AlignLeft)
        self.level_layout.addSpacing(20)
        self.level_layout.addWidget(self.import_bt)
        self.level_layout.addWidget(self.play_bt,alignment=Qt.AlignRight)
        
        # Create connection frame
        self.connection_frame = QFrame(self)
        self.connection_frame.setFixedSize(880, 50)

        # Create connection layout
        self.connection_layout = QHBoxLayout(self.connection_frame)

        # Create connection widgets
        self.connection_label = QLabel("Connection:")
        self.port_serial = QComboBox()
        self.port_serial.setFixedSize(200, 30)
        self.port_sound = QComboBox()
        self.port_sound.setFixedSize(200, 30)
        self.refresh_bt = QPushButton("Refresh")
        self.refresh_bt.setFixedSize(80, 30)
        self.refresh_bt.clicked.connect(self.Refresh_Bt)
        self.connection_bt = QPushButton("Connect")
        self.connection_bt.setFixedSize(80, 30)
        self.connection_state = QLabel("Not Connected")
        self.connection_bt.clicked.connect(self.toggel_bt_connection)

        # Add connection widgets to the layout
        self.connection_layout.addWidget(self.connection_label)
        self.connection_layout.addWidget(self.port_serial)
        self.connection_layout.addWidget(self.port_sound)
        self.connection_layout.addWidget(self.connection_state)
        self.connection_layout.addWidget(self.connection_bt)
        self.connection_layout.addWidget(self.refresh_bt)

        # Create notation note frame
        self.notation_note_frame = QFrame(self)
        self.notation_note_frame.setFixedSize(880, 250)

        # Create notation note layout
        self.notation_note_layout = QVBoxLayout(self.notation_note_frame)

        # Create notation note graphics view
        self.notation_note_scene = QGraphicsScene()
        self.notation_note_view = QGraphicsView(self.notation_note_scene)
        self.notation_note_view.setFixedSize(880, 230)
        self.notation_note_view.scale(0.8,0.8)

        # Add graphics view to the layout
        self.notation_note_layout.addWidget(self.notation_note_view)
        self.notation_note_frame.setLayout(self.notation_note_layout)

        # Create note button frame
        self.note_button_frame = QFrame(self)
        self.note_button_frame.setFixedSize(880, 250)

        # Create note button layout
        self.note_button_layout = QVBoxLayout(self.note_button_frame)

        # Create note button graphics view
        self.note_button_scene = QGraphicsScene()
        self.note_button_view = QGraphicsView(self.note_button_scene)
        self.note_button_view.setFixedSize(880, 230)
        self.note_button_view.setVisible(True)
        self.note_button_view.scale(0.8,0.8)

        # Add note button graphics view to the layout
        self.note_button_layout.addWidget(self.note_button_view)
        self.note_button_frame.setLayout(self.note_button_layout)

        # Create central widget
        self.central_widget = QWidget(self)
        self.central_layout = QVBoxLayout(self.central_widget)

        # Add frames and layouts to the central layout
        #self.central_layout.addWidget(self.instrument_frame)
        self.central_layout.addWidget(self.level_frame)
        self.central_layout.addWidget(self.connection_frame)
        self.central_layout.addWidget(self.notation_note_frame)
        self.central_layout.addSpacing(100)
        self.central_layout.addWidget(self.note_button_frame)
        self.central_layout.addSpacing(100)

        # Set the central layout for the main window
        self.setCentralWidget(self.central_widget)

        self.lv1_checkbox.stateChanged.connect(self.set_lv)
        self.lv2_checkbox.stateChanged.connect(self.set_lv)
        self.lv3_checkbox.stateChanged.connect(self.set_lv)

        # Set the fixed window size
        self.setFixedSize(910, 620)
    
    def GetNote(self, notes):
        y = 0
        new_pos = self.animation()  # Create a new position for each note
        note_names_lst = []
    
        for note in notes:
            if note in self.midi_dir.get('drum', {}):
                note_names_lst.append(self.midi_dir['drum'][note])
            else:
                note_names_lst.append(str(note))

        self.playing_notes.append((note_names_lst, (new_pos, y)))
        self.note_count += 1
        if self.current_mode == "drum" and self.connected:
            draw_handdle.draw_handle_drum(self, note_names_lst, new_pos)
            
            drum_correct_functions = {
                './Level_3/Lv3-節奏教材1.mid': checknote_drum_lv3.drum_correct1,
                './Level_3/Lv3-節奏教材2.mid': checknote_drum_lv3.drum_correct2,
                './Level_3/Lv3-節奏教材3.mid': checknote_drum_lv3.drum_correct3,
                './Level_3/Lv3-節奏教材4.mid': checknote_drum_lv3.drum_correct4,
                './Level_3/Lv3-節奏教材5.mid': checknote_drum_lv3.drum_correct5,
                './Level_2/Level2_節奏教材1.mid': checknote_drum_lv2.drum_correct1,
                './Level_2/Level2_節奏教材2.mid': checknote_drum_lv2.drum_correct2,
                './Level_2/Level2_節奏教材3.mid': checknote_drum_lv2.drum_correct3,
                './Level_2/Level2_節奏教材4.mid': checknote_drum_lv2.drum_correct4,
                './Level_2/Level2_節奏教材5.mid': checknote_drum_lv2.drum_correct5,
                './Level_1/Level1_節奏1.mid': checknote_drum_lv1.drum_correct1,
                './Level_1/Level1_節奏2.mid': checknote_drum_lv1.drum_correct2,
                './Level_1/Level1_節奏3.mid': checknote_drum_lv1.drum_correct3,
                './Level_1/Level1_節奏4.mid': checknote_drum_lv1.drum_correct4,
                './Level_1/Level1_節奏5.mid': checknote_drum_lv1.drum_correct5,
                './Level_1/Level1_節奏6.mid': checknote_drum_lv1.drum_correct6,
            }
            
            if self.selected_file in drum_correct_functions:
                drum_correct_functions[self.selected_file](self, note_names_lst, new_pos, self.cord, self.note_pos, self.sym)

    def set_lv(self,state):
        if state == Qt.Checked:
            if self.sender() == self.lv1_checkbox:
                self.lv_check  = "level_1"
                self.lv2_checkbox.setChecked(False)
                self.lv3_checkbox.setChecked(False)
                self.UpdatePort()
                self.UpdatePortSerial()
                self.level()

            elif self.sender() == self.lv2_checkbox:
                self.lv_check  = "level_2"
                self.lv1_checkbox.setChecked(False)
                self.lv3_checkbox.setChecked(False)
                self.UpdatePort()
                self.UpdatePortSerial()
                self.level()
            
            elif self.sender() == self.lv3_checkbox:
                self.lv_check  = "level_3"
                self.lv2_checkbox.setChecked(False)
                self.lv1_checkbox.setChecked(False)
                self.UpdatePort()
                self.UpdatePortSerial()
                self.level()
            
            return self.lv_check
    
    def play_background_music(self, bg_music_path):
        pygame.mixer.music.load(bg_music_path)
        pygame.mixer.music.play(-1)
            
    def toggle_bt(self):
        if self.current_mode is None:
            QMessageBox.warning(self, "Warning", "Please select a instrument!")
            return
        
        if self.current_lv.currentText() is None or self.current_lv.currentText() == "":
            QMessageBox.warning(self, "Warning", "Please select level and instrument.")
            return
        
        if self.lv_check == 'level_1':
            selected_bg = "./Level_1/BG/" +self.current_lv.currentText() + ".wav"

        if self.lv_check == 'level_2':
            selected_bg = "./Level_2/BG/" +self.current_lv.currentText() + ".wav"
        
        if self.lv_check == 'level_3':
            selected_bg = "./Level_3/BG/" +self.current_lv.currentText() + ".wav"
        
        if self.play_bt.isChecked():
            self.sound_port = self.port_sound.currentText()
            self.play_bt.setText("Pause")
            if self.lv_check == 'level_1':
                self.play_background_music("./80.wav")
                pygame.time.wait(1350)

            if self.lv_check in ['level_2', 'level_3']:
                self.play_background_music("./120.wav")
                pygame.time.wait(900)

            pygame.mixer.music.load(selected_bg)
            pygame.mixer.music.play(-1)
            
            self.start_animation()
            self.handle_playing()
        else:
            self.play_bt.setText("Play")
            pygame.mixer.music.pause()
            self.timer.stop()
            
    def level(self):
        if self.current_mode and self.lv_check is None:
            QMessageBox.warning(self, "Warning", "Please select level and instrument")
            return
        
        self.current_lv.clear()
        # Set the directory to search in and the file pattern to match
        if self.lv_check == 'level_1':
            dir = "./Level_1"
        elif self.lv_check == 'level_2':
            dir = "./Level_2"
        elif self.lv_check == 'level_3':
            dir = "./Level_3"
        
        # create a list of MIDI file names without the file extension
        midi_files = [os.path.splitext(file)[0] for file in os.listdir(dir) if file.endswith(".mid")]

        # Add the matching files to the combo box
        self.current_lv.addItems(midi_files)

    def animation(self):
        current_pos = self.rect_bx.pos()
        self.notation_note_view.horizontalScrollBar().setValue(-40)
        self.note_button_view.horizontalScrollBar().setValue(-40)
        new_pos = current_pos + QPointF(5, 0)

        if current_pos.x() < self.staff_width:
            self.rect_bx.setPos(new_pos)
            scroll_value = self.notation_note_view.horizontalScrollBar().value() + self.pos_view
            self.notation_note_view.horizontalScrollBar().setValue(scroll_value)
            
            self.pos_view += 2
            
            if self.connected:
                current_pos_bt = self.rect_bx.pos()
                scroll_value_bt = self.note_button_view.horizontalScrollBar().value() + self.pos_view 
                self.note_button_view.horizontalScrollBar().setValue(scroll_value_bt)   
        
                if current_pos_bt.x() < self.staff_width:
                    new_pos_bt = current_pos_bt
                    self.rect_bx_bt.setPos(new_pos_bt)

        else:
            self.rect_bx.setPos(QPointF(0, 0))
            self.pos_view = 0
            if self.connected:
                self.rect_bx_bt.setPos(QPointF(0, 0))
                self.pos_view = 0

        self.x_pos = int(current_pos.x())
        self.handle_playing()
        
        return new_pos

    def handle_playing(self):
        last_pos = self.cord[-1]
        last_pos = last_pos[1]
        if last_pos % 5 == 0:
            pos = last_pos+ 0
        elif last_pos % 5 == 1:
            pos = last_pos + 4
        elif last_pos % 5 == 2:
            pos = last_pos + 3
        elif last_pos % 5 == 3:
            pos = last_pos + 2
        elif last_pos % 5 == 4:
            pos = last_pos + 1

        for i in range(len(self.cord)):
            if self.x_pos  == (pos+50):   
                self.timer.stop()
                pygame.mixer.music.stop()
                self.rect_bx.setPos(QPointF(0, 0))
                self.notation_note_view.horizontalScrollBar().setValue(-40)
                self.pos_view = 0
                self.play_bt.setText("Play")
                
            elif self.x_pos == self.cord[i][1]:
                note_name = [self.cord[i][0]]

    def start_animation(self):
        bpm = self.bpm
        # Start the animation by calling the animation function repeatedly.
        self.timer = QTimer()
        self.timer.timeout.connect(self.animation)
        self.timer.start(3600//int(bpm))
        current = self.animation()
        # move the rectangle to position 10
    
    def import_midi(self):
        self.notes_list.clear()
        if self.current_mode is None:
            QMessageBox.warning(self, "Warning", "Please select a instrument!")
            return
        if self.current_lv.currentText() is None or self.current_lv.currentText() == "":
            QMessageBox.warning(self, "Warning", "Please select level and instrument.")
            return

        self.notation_note_scene.clear()#clear scene
        if self.lv_check == 'level_1':
            # get the selected MIDI file name
            self.selected_file = "./Level_1/" +self.current_lv.currentText() + ".mid"

        elif self.lv_check == 'level_2':
            # get the selected MIDI file name
            self.selected_file = "./Level_2/" +self.current_lv.currentText() + ".mid"

        elif self.lv_check == 'level_3':
            # get the selected MIDI file name
            self.selected_file = "./Level_3/" +self.current_lv.currentText() + ".mid"

        # load the MIDI file with mido
        mid = mido.MidiFile(self.selected_file)
        tempo = None
        time_signature = None

        for msg in mid:
            if msg.type == 'set_tempo':
                tempo = msg.tempo
            if msg.type == 'time_signature':
                time_signature = msg.numerator, msg.denominator
        
        if tempo and time_signature:
            self.bpm = 60_000_000 / tempo

        # Calculate the total length of the MIDI file
        total_time = sum(message.time for message in mid)
        current_duration = 0  # initialize the duration of the current message
    
        #draw box to check note position
        pen = QPen(Qt.red)
        pen.setWidth(3)
        
        note_positions = []    
        note_symbols_list = []

        #Extract mid file to get time duration and note number velocity
        for msg in mid:
            if self.lv_check == "level_1":
                self.staff_width = total_time * 120
                
                for i in range(5):
                    self.notation_note_scene.addLine(10, 40 + i*20, self.staff_width, 40 + i*20)
                    self.note_button_scene.addLine(10, 40 + i*20, self.staff_width, 40 + i*20)
                
                if self.selected_file == "./Level_1/Level1_節奏4.mid" or self.selected_file == "./Level_1/Level1_節奏5.mid" or self.selected_file == "./Level_1/Level1_節奏6.mid": 
                    if msg.type == 'note_on':
                        current_duration += msg.time
                        if msg.time >= 0.75:
                            durations_type = '4'
                        else :
                            durations_type = '8'
                        
                        note_positions.append(current_duration)
                        note_symbols_list.append(durations_type)
                        self.notes_list.append([self.midi_maps['drum'][msg.note]])  # Change to list containing single symbol'
                        
                else:
                    if msg.type == 'note_on':
                        if msg.velocity == 0:
                            current_duration += msg.time
                            if msg.time >= 0.7:
                                durations_type = '4'
                            else :
                                durations_type = '8'
                            
                            note_positions.append(current_duration)
                            note_symbols_list.append(durations_type)
                            self.notes_list.append([self.midi_maps['drum'][msg.note]])  # Change to list containing single symbol'
                        
                        #check rest note
                        if msg.velocity > 0:
                            if msg.note == 43 and msg.time >= 0.75:
                                durations_type = '4'
                                note_positions.append(current_duration)
                                note_symbols_list.append(durations_type)
                                self.notes_list.append([self.midi_maps['drum'][msg.note]])

            if self.lv_check == "level_2":
                self.staff_width = total_time * 190
                for i in range(5):
                    self.notation_note_scene.addLine(10, 40 + i*20, self.staff_width, 40 + i*20)
                    self.note_button_scene.addLine(10, 40 + i*20, self.staff_width, 40 + i*20)
                
                if self.selected_file == "./Level_2/Level2_節奏教材2.mid" or self.selected_file == "./Level_2/Level2_節奏教材3.mid" or self.selected_file == "./Level_2/Level2_節奏教材4.mid":
                    durations_type = None 
                    if msg.type == 'note_on': 
                        #print(msg.time)
                        current_duration += msg.time
                        if msg.time >= 0.1 and msg.time < 0.2:
                            durations_type = '16'
                        if msg.time >= 0.2 and msg.time > 0.15:
                            durations_type = '8'
                        if msg.time >= 0.4 and msg.time > 0.3:
                            durations_type = '4'
                        note_positions.append(current_duration)
                        note_symbols_list.append(durations_type)
                        self.notes_list.append([self.midi_maps['drum'][msg.note]]) # Change to list containing single symbol
                
                else:
                    if msg.type == 'note_on':
                        durations_type = None 
                        current_duration += msg.time
                        if msg.velocity  == 0:  # Rest
                            if msg.time >= 0.1 and msg.time < 0.2:
                                durations_type = '16'
                            if msg.time >= 0.2 and msg.time > 0.15:
                                durations_type = '8'
                            if msg.time >= 0.4 and msg.time > 0.3:
                                durations_type = '4'
                            note_positions.append(current_duration)
                            note_symbols_list.append(durations_type)
                            self.notes_list.append([self.midi_maps['drum'][msg.note]])  # Change to list containing single symbol
        
            if self.lv_check == "level_3":
                self.staff_width = total_time * 170
                for i in range(5):
                    self.notation_note_scene.addLine(-20, 40 + i*20, self.staff_width, 40 + i*20)
                    self.note_button_scene.addLine(-20, 40 + i*20, self.staff_width, 40 + i*20)
                if msg.type == 'note_on': 
                    current_duration += msg.time
                    if msg.velocity  == 0:  # Rest
                        if msg.time >=0.01 and msg.time < 0.2 :
                            durations_type = '8'
                        if msg.time >= 0.2 and msg.time < 0.3:
                            durations_type = '4'
                        note_positions.append(current_duration)
                        note_symbols_list.append(durations_type)
                        self.notes_list.append([self.midi_maps['drum'][msg.note]])  # Change to list containing single symbol
                    
        if self.current_mode == 'drum' and self.lv_check == 'level_1':
            note =  self.notes_list
            x = note_positions
            y = 80
            self.rect_bx = QGraphicsLineItem(10, 20, 10, 140)  # Adjust coordinates as needed
            self.rect_bx.setPen(pen)
            self.notation_note_scene.addItem(self.rect_bx)

            # Draw line in note_button_scene
            self.rect_bx_bt = QGraphicsLineItem(10, 20, 10, 140)  # Adjust coordinates as needed
            self.rect_bx_bt.setPen(pen)
            self.note_button_scene.addItem(self.rect_bx_bt)
            self.rect_bx_bt.setVisible(False)
       
            #select level and send data to draw score
            if self.selected_file == "./Level_1/Level1_節奏1.mid":
                lv1_drum_1.draw_lv1(self,note,x,y,note_symbols_list)
            if self.selected_file == "./Level_1/Level1_節奏2.mid":
                lv1_drum_2.draw_lv1(self,note,x,y,note_symbols_list)
            if self.selected_file == "./Level_1/Level1_節奏3.mid":
                lv1_drum_3.draw_lv1(self,note,x,y,note_symbols_list)
            if self.selected_file == "./Level_1/Level1_節奏4.mid":  #มีnote นึงผิด กับ rest note ผิด
                lv1_drum_4.draw_lv1(self,note,x,y,note_symbols_list)
            if self.selected_file == "./Level_1/Level1_節奏5.mid": 
                lv1_drum_5.draw_lv1(self,note,x,y,note_symbols_list)
            if self.selected_file == "./Level_1/Level1_節奏6.mid": 
                lv1_drum_6.draw_lv1(self,note,x,y,note_symbols_list)
        
        if self.current_mode == 'drum' and self.lv_check == 'level_2':
            note =  self.notes_list
            x = note_positions
            y = 80

            self.rect_bx = QGraphicsLineItem(10, 20, 10, 140)  # Adjust coordinates as needed
            self.rect_bx.setPen(pen)
            self.notation_note_scene.addItem(self.rect_bx)

            # Draw line in note_button_scene
            self.rect_bx_bt = QGraphicsLineItem(10, 20, 10, 140)  # Adjust coordinates as needed
            self.rect_bx_bt.setPen(pen)
            self.note_button_scene.addItem(self.rect_bx_bt)
            self.rect_bx_bt.setVisible(False)
        
            if self.selected_file == "./Level_2/Level2_節奏教材1.mid":
                lv2_drum_1.draw_lv2(self,note,x,y,note_symbols_list)
            if self.selected_file == "./Level_2/Level2_節奏教材2.mid":
                lv2_drum_2.draw_lv2(self,note,x,y,note_symbols_list)
            if self.selected_file == "./Level_2/Level2_節奏教材3.mid":
                lv2_drum_3.draw_lv2(self,note,x,y,note_symbols_list)
            if self.selected_file == "./Level_2/Level2_節奏教材4.mid":
                lv2_drum_4.draw_lv2(self,note,x,y,note_symbols_list)
            if self.selected_file == "./Level_2/Level2_節奏教材5.mid":
                lv2_drum_5.draw_lv2(self,note,x,y,note_symbols_list)

        if self.current_mode == 'drum' and self.lv_check == 'level_3':
            note =  self.notes_list
            x = note_positions
            y = 80
            self.rect_bx = QGraphicsLineItem(-20, 20, -20, 140)  # Adjust coordinates as needed
            self.rect_bx.setPen(pen)
            self.notation_note_scene.addItem(self.rect_bx)

            # Draw line in note_button_scene
            self.rect_bx_bt = QGraphicsLineItem(-20, 20, -20, 140)  # Adjust coordinates as needed
            self.rect_bx_bt.setPen(pen)
            self.note_button_scene.addItem(self.rect_bx_bt)
            self.rect_bx_bt.setVisible(False)

            if self.selected_file == "./Level_3/Lv3-節奏教材1.mid":
                lv3_drum_1.draw_lv3(self,note,x,y,note_symbols_list)
            if self.selected_file == "./Level_3/Lv3-節奏教材2.mid":
                lv3_drum_2.draw_lv3(self,note,x,y,note_symbols_list)
            if self.selected_file == "./Level_3/Lv3-節奏教材3.mid":
                lv3_drum_3.draw_lv3(self,note,x,y,note_symbols_list)
            if self.selected_file == "./Level_3/Lv3-節奏教材4.mid":
                lv3_drum_4.draw_lv3(self,note,x,y,note_symbols_list)
            if self.selected_file == "./Level_3/Lv3-節奏教材5.mid":
                lv3_drum_5.draw_lv3(self,note,x,y,note_symbols_list)
 
    def Refresh_Bt(self):
        pen = QPen(Qt.red)
        pen.setWidth(2)
        self.rect_bx_bt = QGraphicsLineItem(0, 0, 0, 140)  # Adjust coordinates as needed
        self.rect_bx_bt.setPen(pen)
        self.note_button_scene.addItem(self.rect_bx_bt)
        if self.current_mode is None and self.lv_check is None:
            QMessageBox.warning(self, "Warning", "Please select a instrument and check the level.")
    
        else:
            self.UpdatePort()
            self.UpdatePortSerial()
            self.notation_note_scene.clear()
            self.note_button_scene.clear()
            self.notes_list.clear()
            self.cord.clear()
            self.rest_ls.clear()
            self.pos_view = 0
            self.level()
            self.bpm = 0
        
    def UpdatePort(self):
        self.port_sound.clear()
        self.notes_list.clear()
        sound_port = mido.get_output_names()
        for port in sound_port:
            self.port_sound.addItem(port)
    
    def UpdatePortSerial(self):
        port_serial = serial.tools.list_ports.comports()
        # Clear the combo box and add each port to it
        self.port_serial.clear()
        for port in port_serial:
            self.port_serial.addItem(port.device)

    def connection(self):
        port = self.port_serial.currentText()
        sound_port=self.port_sound.currentText()
        current_mode = self.current_mode
        
        if current_mode is None:
            QMessageBox.warning(self, "Warning", "Please select a instrument")
            return
        
        try:
            self.Serial_Thread = SerialThread(port,9600,current_mode)
            self.Serial_Thread.getdata.connect(self.GetNote)
            self.Serial_Thread.connect_output_port(sound_port)
            self.Serial_Thread.connect()
            self.Serial_Thread.start() 
            self.connected = True
            self.connection_state.setText(f'Connected： {port}'+ '\n' +f'Sound Port: {sound_port}')
            self.connection_bt.setText('Disconnect')

        except serial.SerialException:
            QMessageBox.warning(self,"Warning", "Can't connect your device !!")
    
    def disconnection(self):
        if self.Serial_Thread is not None:
            self.Serial_Thread.stop()
            self.Serial_Thread.disconnect()

            self.connected = False
            self.connection_state.setText("Not Connect")
            self.connection_bt.setText("Connect")

    def toggel_bt_connection(self):
        if not self.connected:
            self.connection()
        else:
            self.disconnection()

if __name__ == '__main__':
    # Initialize Pygame
    pygame.init()
    
    # Initialize PyQt application
    app = QApplication(sys.argv)
    
    # Load the MIDI file and create the main window
    window = MainWindow()
    window.show()
    
    # Start the PyQt event loop
    sys.exit(app.exec_())