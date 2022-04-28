import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #add title
        self.setWindowTitle('Rock, Paper, Scissors')

        #set layout
        self.setLayout(qtw.QVBoxLayout())

        # Creat A label
        labelPick = qtw.QLabel('Pick a Box')
        labelPick.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(labelPick)

        #create buttons for the choices
        buttonRock = qtw.QPushButton('Rock', clicked = lambda: press_it())
        self.layout().addWidget(buttonRock)
        buttonPaper = qtw.QPushButton('Paper')
        self.layout().addWidget(buttonPaper)
        buttonScissors = qtw.QPushButton('Scissors')
        self.layout().addWidget(buttonScissors)
        buttonLizard = qtw.QPushButton('Lizard')
        self.layout().addWidget(buttonLizard)
        buttonSpock = qtw.QPushButton('Spock')
        self.layout().addWidget(buttonSpock)

        #show the app
        self.show()

        #what happens with you click
        def press_it():
            labelPick.setText(f'You win with Rock!')





app = qtw.QApplication([])
mw = MainWindow()

#run the app
app.exec_()
