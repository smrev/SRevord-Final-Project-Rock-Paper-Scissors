from PyQt5 import QtCore, QtGui, QtWidgets
import random

# Global variables for scores and screen outputs
ai_count = 0
player_count = 0
phrase = ''
winner = ''

#Gui created with Qt Designer
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(519, 391)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonRock = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clickrock())
        self.buttonRock.setGeometry(QtCore.QRect(90, 110, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonRock.setFont(font)
        self.buttonRock.setObjectName("buttonRock")
        self.buttonPaper = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clickpaper())
        self.buttonPaper.setGeometry(QtCore.QRect(210, 110, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonPaper.setFont(font)
        self.buttonPaper.setObjectName("buttonPaper")
        self.buttonScissors = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clickscissors())
        self.buttonScissors.setGeometry(QtCore.QRect(330, 110, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonScissors.setFont(font)
        self.buttonScissors.setObjectName("buttonScissors")
        self.buttonLizard = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clicklizard())
        self.buttonLizard.setGeometry(QtCore.QRect(150, 210, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonLizard.setFont(font)
        self.buttonLizard.setObjectName("buttonLizard")
        self.buttonSpock = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clickspock())
        self.buttonSpock.setGeometry(QtCore.QRect(270, 210, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonSpock.setFont(font)
        self.buttonSpock.setObjectName("buttonSpock")

        self.labelChampion = QtWidgets.QLabel(self.centralwidget)
        self.labelChampion.setGeometry(QtCore.QRect(90, 10, 390, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelChampion.setFont(font)
        self.labelChampion.setObjectName("labelChampion")

        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(90, 50, 350, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")

        self.labelWinner = QtWidgets.QLabel(self.centralwidget)
        self.labelWinner.setGeometry(QtCore.QRect(110,310,310,60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelWinner.setFont(font)
        self.labelWinner.setObjectName("labelWinner")

        self.labelScore = QtWidgets.QLabel(self.centralwidget)
        self.labelScore.setGeometry(QtCore.QRect(330,310,310,60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelScore.setFont(font)
        self.labelScore.setObjectName("labelScore")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 519, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonRock.setText(_translate("MainWindow", "Rock"))
        self.buttonPaper.setText(_translate("MainWindow", "Paper"))
        self.buttonScissors.setText(_translate("MainWindow", "Scissors"))
        self.buttonLizard.setText(_translate("MainWindow", "Lizard"))
        self.buttonSpock.setText(_translate("MainWindow", "Spock"))
        self.labelTitle.setText(_translate("MainWindow", "LET\'S PLAY A GAME!"))
        self.labelScore.setText(_translate("MainWindow", "SCORE"))

    # function containing game logic
    # compares players choice
    # to a randomly generated computer choice
    def gameplay(self, player):
        global phrase, winner
        computer = random.randint(1,5)
        # considers a tie game
        if player == computer:
            winner = 'Tie Game'
            if player == 1:
                phrase = 'Rock versus Rock'
            elif player == 2:
                phrase = 'Paper versus Paper'
            elif player == 3:
                phrase = 'Scissors versus Scissors'
            elif player == 4:
                phrase = 'Lizard versus Lizard'
            else:
                phrase = 'Spock versus Spock'
        elif player == 1:
            if computer == 2:
                phrase = 'Paper covers Rock'
                winner = 'You Lose'
            elif computer == 3:
                phrase = 'Rock crushes Scissors'
                winner = 'You Win'
            elif computer == 4:
                phrase = 'Rock crushes Lizard'
                winner = 'You Win'
            else:
                phrase = 'Spock vaporizes Rock'
                winner = 'You Lose'
        elif player == 2:
            if computer == 1:
                phrase = 'Paper covers Rock'
                winner = 'You Win'
            elif computer == 3:
                phrase = 'Scissors cuts Paper'
                winner = 'You Lose'
            elif computer == 4:
                phrase = 'Lizard eats Paper'
                winner = 'You Lose'
            else:
                phrase = 'Paper disproves Spock'
                winner = 'You Win'
        elif player == 3:
            if computer == 1:
                phrase = 'Rock crushes Scissors'
                winner = 'You Lose'
            elif computer == 2:
                phrase = 'Scissors cuts Paper'
                winner = 'You Win'
            elif computer == 4:
                phrase = 'Scissors decapitates Lizard'
                winner = 'You Win'
            else:
                phrase = 'Spock smashes Scissors'
                winner = 'You Lose'
        elif player == 4:
            if computer == 1:
                phrase = 'Rock crushes Lizard'
                winner = 'You Lose'
            elif computer == 2:
                phrase = 'Lizard eats Paper'
                winner = 'You Win'
            elif computer == 3:
                phrase = 'Scissors decapitates Lizard'
                winner = 'You Lose'
            else:
                phrase = 'Lizard poisons Spock'
                winner = 'You Win'
        elif player == 5:
            if computer == 1:
                phrase = 'Spock vaporizes Rock'
                winner = 'You Win'
            elif computer == 2:
                phrase = 'Paper disproves Spock'
                winner = 'You Lose'
            elif computer == 3:
                phrase = 'Spock smashes Scissors'
                winner = 'You Win'
            else:
                phrase = 'Lizard poisons Spock'
                winner = 'You Lose'
        return phrase, winner

    # function to keep track of the score
    def score(self):
        global player_count, ai_count, winner
        if winner == 'You Win':
            player_count += 1
            # if player/ai reaches 5 wins,
            if player_count >= 5:
                # a champion is announced and
                self.labelChampion.setText('You are GRAND CHAMPION!!')
                # player is asked to play again
                return 'Play Again?'
            else:
                return winner
        elif winner == 'You Lose':
            ai_count += 1
            if ai_count >= 5:
                self.labelChampion.setText('The Computer has Triumphed.')
                return 'Play Again?'
            else:
                return winner
        else:
            return winner


    def update_screen(self):
        global player_count, ai_count, phrase, winner
        # announcement of results of the match, winner, and score update
        self.labelTitle.setText(f'{phrase}!')
        self.labelWinner.setText(f'{winner}')
        self.labelScore.setText(f'{player_count} to {ai_count}')
        # if a champion has been announced, the score is reset
        # reset score will be reflected if game is continued
        if winner == 'Play Again?':
            ai_count = 0
            player_count = 0

    # main function that runs the gameplay
    # each time any button is clicked
    def clicked(self, player):
        global ai_count, player_count, phrase, winner
        # first checks to see if the champion label needs to be cleared out
        if ai_count == 0 and player_count == 0:
            self.labelChampion.setText('')
        # calls the gameplay function with the players choice to determine winner
        (phrase, winner) = self.gameplay(player)
        # calls the score function to update the score
        winner = self.score()
        # updates screen to reflect the outcome of the match
        self.update_screen()

    # remaining functions are to set the player's
    # choice - rock, paper, scissors, lizard, spock -
    # then the clicked function is called
    # with players choice, to run the game.
    def clickrock(self):
        player = 1
        self.clicked(player)

    def clickpaper(self):
        player = 2
        self.clicked(player)

    def clickscissors(self):
        player = 3
        self.clicked(player)

    def clicklizard(self):
        player = 4
        self.clicked(player)

    def clickspock(self):
        player = 5
        self.clicked(player)