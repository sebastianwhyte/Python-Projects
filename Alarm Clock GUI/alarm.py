import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime


alarms = []


class Window( QWidget ):


    def __init__( self ):
        super(Window, self).__init__()  # Use super to inherit from the "Window" class
        self.initUI()


    def initUI( self ):

        self.setGeometry( 300, 300, 500, 600 )
        self.setWindowTitle( "My Alarm Clock GUI - by Sebastian Whyte" )
        self.label = QLabel( self )
        self.label.setText( "<h1>Alarm Clock</h1>" )
        self.label.setAlignment( Qt.AlignCenter )


        self.b1 = QPushButton( self )
        self.b1.setText( "Create New Alarm" )
        self.b1.clicked.connect( self.create_alarm_clicked )

        self.b2 = QPushButton( self )
        self.b2.setText( "Remove Alarm" )
        self.b2.clicked.connect( self.remove_alarm_clicked )

        self.b3 = QPushButton( self )
        self.b3.setText( "View Alarms" )
        self.b3.clicked.connect( self.view_alarm_clicked )

        self.b4 = QPushButton( self )
        self.b4.setText( "Quit" )
        self.b4.clicked.connect( self.quit_clicked )


        self.label_image = QLabel( self )
        self.pixmap = QPixmap( "clock_pic_copy.png" )
        self.label_image.setPixmap( self.pixmap )
        self.label_image.setAlignment( Qt.AlignTop | Qt.AlignHCenter )


        self.date_label = QLabel( self )
        self.date_label.setAlignment( Qt.AlignCenter )
        self.time_label = QLabel( self )
        self.time_label.setAlignment( Qt.AlignCenter )


        timer = QTimer( self )
        timer.timeout.connect( self.DateAndTime )
        timer.start( 1000 )


        layout = QVBoxLayout( )
        layout.setAlignment( Qt.AlignCenter )
        layout.addWidget( self.label_image )
        layout.addWidget( self.label )
        layout.addWidget( self.date_label )
        layout.addWidget( self.time_label )
        layout.addWidget( self.b1 )
        layout.addWidget( self.b2 )
        layout.addWidget( self.b3 )
        layout.addWidget( self.b4 )
        self.setLayout(layout)


    def DateAndTime(self):

        now = datetime.now()
        self.current_date = now.strftime("%a, %x")
        self.current_time = now.strftime("%X")

        # converting QDate & QTime object to string
        self.label_time = self.current_time
        self.label_date = self.current_date

        # showing it to the label
        self.date_label.setText(self.label_date)
        self.time_label.setText( self.label_time )



    # Create Alarm button functions
    def create_alarm_clicked( self ):

        global alarms

        # Make QDialogButtonBox a subclass of QDialog
        dialog = QDialog(self)
        dialog.setGeometry( 425, 500, 200, 200 )
        dialog.setWindowTitle( "Create Alarm" )


        self.buttonBox = QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QRect(10, 350, 161, 41))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons( QDialogButtonBox.Cancel |
                                          QDialogButtonBox.Ok )
        self.buttonBox.setObjectName( "buttonBox" )


        self.buttonBox.accepted.connect( self.accept )
        self.buttonBox.rejected.connect( dialog.reject )


        self.create_alarm_label = QLabel( self )
        self.create_alarm_label.setText( "<h3>Please select time for the alarm<:/h3>" )

        self.create_alarm_text = QLabel(self)
        self.create_alarm_text.setText( "Note: This app uses 24-hour time.")


        sbox = QSpinBox( self )
        sbox.valueChanged.connect( self.updateSpin1 )
        sbox.setMaximum(23)
        self.s_label = QLabel( '0', self )


        sbox2 = QSpinBox(self)
        sbox2.valueChanged.connect( self.updateSpin2 )
        sbox2.setMaximum(59)
        self.s2_label = QLabel( '0', self )


        dialog.horizontalLayout = QHBoxLayout()
        dialog.horizontalLayout.addWidget(sbox)
        dialog.horizontalLayout.addWidget(sbox2)


        # Follow this template to make additional layouts
        dialog.layout = QVBoxLayout()
        dialog.layout.setAlignment( Qt.AlignCenter )
        dialog.layout.addWidget( self.create_alarm_label )
        dialog.layout.addWidget(self.create_alarm_text)
        dialog.layout.addLayout(dialog.horizontalLayout)
        dialog.layout.addWidget( self.buttonBox )


        dialog.setLayout( dialog.layout )     # This allows you to have another layout set, even with "def initUI" has a layout. Use "self.nameOfMethod.setLayout(additionalLayout)


        dialog.exec_()  # Executes the QDialog



    # View Alarm functions
    def view_alarm_clicked( self, value ):

        # Start with empty array that will store appended alarms
        global alarms


        self.view_messagebox = QMessageBox( self )
        self.view_messagebox.setGeometry( 425, 500, 400, 400 )
        self.view_messagebox.setWindowTitle( "View Alarms" )
        self.view_messagebox.setStandardButtons( QMessageBox.Cancel | QMessageBox.Ok )
        self.view_messagebox.setDefaultButton( QMessageBox.Ok )


        if len(alarms) <= 0:
            self.view_messagebox.setText( "<h3>You have no alarms</h3>" )

            self.view_messagebox.show()
            self.view_messagebox.exec()


        if len(alarms) > 0:

            self.view_messagebox.setText( "<h3>You have alarms for:</h3> " + str(alarms))

            self.view_messagebox.show()
            self.view_messagebox.exec()



    # Remove Alarm functions
    def remove_alarm_clicked( self ):

        global alarms


        if len(alarms) == 0:

            self.remove_messagebox = QMessageBox( self )
            self.remove_messagebox.setGeometry( 425, 500, 400, 400 )
            self.remove_messagebox.setWindowTitle( "Remove Alarms" )
            self.remove_messagebox.setStandardButtons( QMessageBox.Cancel | QMessageBox.Ok )
            self.remove_messagebox.setDefaultButton( QMessageBox.Ok )


            self.remove_messagebox.setText( "<h3>You have no alarms to delete.</h3>" )


            self.remove_messagebox.show()
            self.remove_messagebox.exec()


        if len(alarms) > 0:

            self.remove_alarm_dialog = QDialog( self )
            self.remove_alarm_dialog.setGeometry( 425, 500, 200, 200 )
            self.remove_alarm_dialog.setWindowTitle( "Remove Alarm" )


            self.buttonBox2 = QDialogButtonBox( self.remove_alarm_dialog )
            self.buttonBox2.setGeometry( QRect( 10, 350, 161, 41 ) )
            self.buttonBox2.setOrientation( Qt.Horizontal )
            self.buttonBox2.setStandardButtons( QDialogButtonBox.Cancel |
                                                QDialogButtonBox.Ok )
            self.buttonBox2.setObjectName( "buttonBox2" )

            self.buttonBox2.accepted.connect( self.remove_confirm )
            self.buttonBox2.rejected.connect( self.remove_cancel )


            self.remove_alarm_label = QLabel( self )
            self.remove_alarm_label.setText( "<h3>Please select alarm you'd like to remove:</h3>" )


            self.remove_alarm_text = QLabel( self )
            self.remove_alarm_text.setText("You will have to exit and reopen this window to see changes.")

            self.listwidget = QListWidget( self )


            for alarm in alarms:
                self.listwidget.addItem( alarm )


            self.listwidget.itemSelectionChanged.connect( self.remove_selection )


            self.remove_alarm_dialog.layout = QVBoxLayout()
            self.remove_alarm_dialog.layout.setAlignment( Qt.AlignCenter )
            self.remove_alarm_dialog.layout.addWidget( self.remove_alarm_label )
            self.remove_alarm_dialog.layout.addWidget( self.remove_alarm_text )
            self.remove_alarm_dialog.layout.addWidget( self.listwidget )
            self.remove_alarm_dialog.layout.addWidget( self.buttonBox2 )


            self.remove_alarm_dialog.setLayout( self.remove_alarm_dialog.layout )


            self.remove_alarm_dialog.show()
            self.remove_alarm_dialog.exec_()



    # Updates the Spin Box
    def updateSpin1( self, value ):

        self.s_label.setText( str( value ) )



    def updateSpin2( self, value ):
        self.s2_label.setText( str( value ) )


    def accept( self ):

        self.create_alarm_text.setText( "Alarm Saved!" )

        print( "Accepted!" )
        self.new_time = self.s_label.text().zfill( 2 ) + ":" + self.s2_label.text().zfill( 2 )
        print( self.new_time )
        alarms.append( self.new_time )
        print( alarms )


    def reject( self ):

        self.dialog.close()


    def remove_confirm ( self ):
        self.remove_alarm_dialog.close()


    def remove_cancel ( self ):
        self.remove_alarm_dialog.close()


   
    def remove_selection( self):

        selected_item = self.listwidget.currentItem()
        print("Removed!")
        print("You have selected: ", selected_item.text())
        alarms.remove(selected_item.text())
        print(alarms)


    # Quit Button functions
    def quit_clicked( self ):
        self.close()


    def ring_alarm( self ):
        pass


def run():
    app = QApplication( [ ] )
    GUI = Window()
    GUI.show()
    sys.exit( app.exec_() )

run()
