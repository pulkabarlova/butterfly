import sys
import sqlite3
import random
from threading import *
import time

import palette as palette
from PyQt5 import uic
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from pyqt5_plugins.examplebuttonplugin import QtGui

from ui_file import Ui_MainWindow

password = ""
login = ""
c = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = 0

mass_x = [[0, 151], [140, 181], [220, 641], [240, 501], [240, 271], [180, 261], [30, 80], [0, 221], [250, 301],
          [500, 531], [630, 661], [350, 421], [430, 537], [170, 221], [170, 301], [360, 451], [280, 801], [290, 321],
          [630, 761], [730, 761], [470, 681]]
mass_y = [[150, 190], [320, 371], [90, 130], [229, 257], [230, 291], [350, 371], [240, 290], [410, 451], [340, 511],
          [230, 431], [90, 431], [290, 361], [420, 461], [440, 641], [630, 671], [420, 521], [730, 771], [630, 741],
          [430, 471], [460, 651], [580, 621]]


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('02.ui', self)
        self.the_end = QLabel(self)
        self.finish.hide()
        self.the_end.resize(250, 100)
        self.the_end.hide()
        self.coords = QLabel(self)
        self.final_score = 11
        self.coords.setText("🦋")
        self.coords.hide()
        self.coords1 = QLabel(self)
        self.coords1.setText("🦋")
        self.coords1.hide()
        self.coords2 = QLabel(self)
        self.coords2.setText("🦋")
        self.coords2.hide()
        self.coords3 = QLabel(self)
        self.coords3.setText("🦋")
        self.coords3.hide()
        self.coords4 = QLabel(self)
        self.coords4.setText("🦋")
        self.coords4.hide()
        self.coords5 = QLabel(self)
        self.coords5.setText("🦋")
        self.coords5.hide()
        self.coords6 = QLabel(self)
        self.coords6.setText("🦋")
        self.coords6.hide()
        self.coords7 = QLabel(self)
        self.coords7.setText("🦋")
        self.coords7.hide()
        self.coords8 = QLabel(self)
        self.coords8.setText("🦋")
        self.coords8.hide()
        self.coords9 = QLabel(self)
        self.coords9.setText("🦋")
        self.coords9.hide()
        self.coords10 = QLabel(self)
        self.coords10.setText("🦋")
        self.coords10.hide()
        self.login.clicked.connect(self.log)
        self.playgame.clicked.connect(self.play)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.killer()
            self.END()
            self.coords.move(self.coords.x() + 5, self.coords.y())
            self.coords1.move(self.coords.x() + random.randint(-5, 5) + 5, self.coords.y() + random.randint(-5, 5))
            self.coords2.move(self.coords.x() + random.randint(-5, 5) + 5,
                              self.coords.y() + random.randint(-5, 5))
            self.coords3.move(self.coords.x() + random.randint(-5, 5) + 5,
                              self.coords.y() + random.randint(-5, 5))
            self.coords4.move(self.coords.x() + random.randint(-5, 5) + 5,
                              self.coords.y() + random.randint(-5, 5))
            self.coords5.move(self.coords.x() + random.randint(-10, 10) + 5,
                              self.coords.y() + random.randint(-10, 10))
            self.coords6.move(self.coords.x() + random.randint(-10, 10) + 5,
                              self.coords.y() + random.randint(-10, 10))
            self.coords7.move(self.coords.x() + random.randint(-10, 10) + 5,
                              self.coords.y() + random.randint(-15, 15))
            self.coords8.move(self.coords.x() + random.randint(-15, 15) + 5,
                              self.coords.y() + random.randint(-15, 15))
            self.coords9.move(self.coords.x() + random.randint(-20, 20) + 5,
                              self.coords.y() + random.randint(-20, 20))
            self.coords10.move(self.coords.x() + random.randint(-25, 25) + 5,
                               self.coords.y() + random.randint(-25, 25))
            self.update()
        elif event.key() == Qt.Key_Left:
            self.killer()
            self.END()
            self.coords.move(self.coords.x() - 5, self.coords.y())
            self.coords1.move(self.coords.x() + random.randint(-5, 5) - 5, self.coords.y() + random.randint(-5, 5))
            self.coords2.move(self.coords.x() + random.randint(-5, 5) - 5,
                              self.coords.y() + random.randint(-5, 5))
            self.coords3.move(self.coords.x() + random.randint(-5, 5) - 5,
                              self.coords.y() + random.randint(-5, 5))
            self.coords4.move(self.coords.x() + random.randint(-5, 5) - 5,
                              self.coords.y() + random.randint(-5, 5))
            self.coords5.move(self.coords.x() + random.randint(-10, 10) - 5,
                              self.coords.y() + random.randint(-10, 10))
            self.coords6.move(self.coords.x() + random.randint(-10, 10) - 5,
                              self.coords.y() + random.randint(-10, 10))
            self.coords7.move(self.coords.x() + random.randint(-15, 15) - 5,
                              self.coords.y() + random.randint(-15, 15))
            self.coords8.move(self.coords.x() + random.randint(-15, 15) - 5,
                              self.coords.y() + random.randint(-15, 15))
            self.coords9.move(self.coords.x() + random.randint(-20, 20) - 5,
                              self.coords.y() + random.randint(-20, 20))
            self.coords10.move(self.coords.x() + random.randint(-25, 25) - 5,
                               self.coords.y() + random.randint(-25, 25))
        elif event.key() == Qt.Key_Down:
            self.killer()
            self.END()
            self.coords.move(self.coords.x(), self.coords.y() + 5)
            self.coords1.move(self.coords.x() + random.randint(-5, 5), self.coords.y() + random.randint(-5, 5) + 5)
            self.coords2.move(self.coords.x() + random.randint(-5, 5),
                              self.coords.y() + random.randint(-5, 5) + 5)
            self.coords3.move(self.coords.x() + random.randint(-5, 5),
                              self.coords.y() + random.randint(-5, 5) + 5)
            self.coords4.move(self.coords.x() + random.randint(-5, 5),
                              self.coords.y() + random.randint(-10, 10) + 5)
            self.coords5.move(self.coords.x() + random.randint(-10, 10),
                              self.coords.y() + random.randint(-10, 10) + 5)
            self.coords6.move(self.coords.x() + random.randint(-10, 10),
                              self.coords.y() + random.randint(-10, 10) + 5)
            self.coords7.move(self.coords.x() + random.randint(-15, 15),
                              self.coords.y() + random.randint(-15, 15) + 5)
            self.coords8.move(self.coords.x() + random.randint(-15, 15),
                              self.coords.y() + random.randint(-15, 15) + 5)
            self.coords9.move(self.coords.x() + random.randint(-20, 20),
                              self.coords.y() + random.randint(-20, 20) + 5)
            self.coords10.move(self.coords.x() + random.randint(-25, 25),
                               self.coords.y() + random.randint(-25, 25) + 5)

    def checker(self, p):
        c1 = 0
        c2 = 0
        if len(p) <= 8:
            return "Ваш пароль слишком короткий (8 символов)"
        for i in p:
            if i.isdigit():
                c1 += 1
            else:
                c2 += 1
        if c1 == 0 or c2 == 0:
            return "Ваш пароль не содержит букв или цифр"
        return "ok"

    def log(self):
        global score
        global login
        access = 0
        password = self.password_take.toPlainText()
        login = self.login_take.toPlainText()
        con = sqlite3.connect("base_fly.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
            login TEXT,
             password TEXT, 
             score BIGINT)""")
        score = 0
        cur.execute("SELECT login FROM users")
        base = [i[0] for i in cur.fetchall()]
        if login not in base:
            if self.checker(password) != "ok":
                self.error.setText(self.checker(password))
            else:
                cur.execute(f"INSERT INTO users VALUES (?, ?, ?)",
                            (login, password, score))
                con.commit()
        else:
            num_log = base.index(login)
            logins_yes = cur.execute("SELECT password FROM users").fetchall()
            base2 = [i[0] for i in logins_yes]
            if password not in base2:
                self.error.setText("Пароль неверный")
            else:
                num_pas = base2.index(password)
                if num_log != num_pas:
                    self.error.setText("Пароль неверный")
                else:
                    score_yes = cur.execute("""SELECT score FROM users""").fetchall()
                    base3 = [i[0] for i in score_yes]
                    score = base3[num_log]
                    self.error.setText("Добро пожаловать, " + str(login) + "!")
                    self.lcdNumber.display(score)
                    access = 1
        con.commit()
        if access == 1:
            self.label_2.deleteLater()
            self.label_3.deleteLater()
            self.login_take.deleteLater()
            self.password_take.deleteLater()
            self.label_25.deleteLater()
            self.get_im.deleteLater()
            self.login.deleteLater()
            self.error.move(250, 250)
            self.error.setFont(QtGui.QFont("Times", 30, QtGui.QFont.Bold))
            self.playgame.setText("PLAY")
            self.playgame.move(350, 350)
            self.playgame.show()
            self.coords1.show()
            self.coords2.show()
            self.coords3.show()
            self.coords4.show()
            self.coords5.show()
            self.coords6.show()
            self.coords7.show()
            self.coords8.show()
            self.coords9.show()
            self.coords10.show()

    def play(self):
        self.error.hide()
        self.playgame.deleteLater()
        pix = QtGui.QPixmap("kirpich.jpg")
        pix2 = QtGui.QPixmap("finish.png")
        self.finish.setPixmap(pix2)
        self.finish.show()
        self.label_4.setPixmap(pix)
        self.label_5.setPixmap(pix)
        self.label_6.setPixmap(pix)
        self.label_7.setPixmap(pix)
        self.label_8.setPixmap(pix)
        self.label_9.setPixmap(pix)
        self.label_10.setPixmap(pix)
        self.label_11.setPixmap(pix)
        self.label_12.setPixmap(pix)
        self.label_13.setPixmap(pix)
        self.label_14.setPixmap(pix)
        self.label_15.setPixmap(pix)
        self.label_16.setPixmap(pix)
        self.label_17.setPixmap(pix)
        self.label_18.setPixmap(pix)
        self.label_19.setPixmap(pix)
        self.label_20.setPixmap(pix)
        self.label_21.setPixmap(pix)
        self.label_22.setPixmap(pix)
        self.label_23.setPixmap(pix)
        self.label_24.setPixmap(pix)

    def killer(self):
        global c9, c10, c8, c7, c6, c5, c3, c2, c1, c4, c
        for i in range(21):
            if mass_x[i][0] <= self.coords.x() <= mass_x[i][1] and mass_y[i][0] <= self.coords.y() <= mass_y[i][1]:
                self.coords.hide()
                if c == 0:
                    self.final_score -= 1
                c = 1
            if mass_x[i][0] <= self.coords1.x() <= mass_x[i][1] and mass_y[i][0] <= self.coords1.y() <= mass_y[i][1]:
                self.coords1.hide()
                if c1 == 0:
                    self.final_score -= 1
                c1 = 1
            if mass_x[i][0] <= self.coords2.x() <= mass_x[i][1] and mass_y[i][0] <= self.coords2.y() <= mass_y[i][1]:
                self.coords2.hide()
                if c2 == 0:
                    self.final_score -= 1
                c2 = 1
            if mass_x[i][0] <= self.coords3.x() <= mass_x[i][1] and mass_y[i][0] <= self.coords3.y() <= mass_y[i][1]:
                self.coords3.hide()
                if c3 == 0:
                    self.final_score -= 1
                c3 = 1
            if mass_x[i][0] <= self.coords4.x() <= mass_x[i][1] and mass_y[i][0] <= self.coords4.y() <= mass_y[i][1]:
                self.coords4.hide()
                if c4 == 0:
                    self.final_score -= 1
                c4 = 1
            if mass_x[i][0] <= self.coords5.x() <= mass_x[i][1] and mass_y[i][0] <= self.coords5.y() <= mass_y[i][1]:
                self.coords5.hide()
                if c5 == 0:
                    self.final_score -= 1
                c5 = 1
            if mass_x[i][0] <= self.coords6.x() <= mass_x[i][1] and mass_y[i][0] <= self.coords6.y() <= mass_y[i][1]:
                self.coords6.hide()
                if c6 == 0:
                    self.final_score -= 1
                c6 = 1
            if mass_x[i][0] <= self.coords7.x() <= mass_x[i][1] and mass_y[i][0] <= self.coords7.y() <= mass_y[i][1]:
                self.coords7.hide()
                if c7 == 0:
                    self.final_score -= 1
                c7 = 1
            if mass_x[i][0] <= self.coords8.x() <= mass_x[i][1] and mass_y[i][0] <= self.coords8.y() <= mass_y[i][1]:
                self.coords8.hide()
                if c8 == 0:
                    self.final_score -= 1
                c8 = 1
            if mass_x[i][0] <= self.coords9.x() <= mass_x[i][1] and mass_y[i][0] <= self.coords9.y() <= mass_y[i][1]:
                self.coords9.hide()
                if c9 == 0:
                    self.final_score -= 1
                c9 = 1
            if mass_x[i][0] <= self.coords10.x() <= mass_x[i][1] and mass_y[i][0] <= self.coords10.y() <= mass_y[i][1]:
                self.coords10.hide()
                if c10 == 0:
                    self.final_score -= 1
                c10 = 1

    def END(self):
        if (750 <= self.coords.x() <= 871 and 630 <= self.coords.y() <= 731) or (
                750 <= self.coords1.x() <= 871 and 630 <= self.coords1.y() <= 731) or (
                750 <= self.coords2.x() <= 871 and 630 <= self.coords2.y() <= 731) or (
                750 <= self.coords3.x() <= 871 and 630 <= self.coords3.y() <= 731) or (
                750 <= self.coords4.x() <= 871 and 630 <= self.coords4.y() <= 731) or (
                750 <= self.coords5.x() <= 871 and 630 <= self.coords5.y() <= 731) or (
                750 <= self.coords6.x() <= 871 and 630 <= self.coords6.y() <= 731) or (
                750 <= self.coords7.x() <= 871 and 630 <= self.coords7.y() <= 731) or (
                750 <= self.coords8.x() <= 871 and 630 <= self.coords8.y() <= 731) or (
                750 <= self.coords9.x() <= 871 and 630 <= self.coords9.y() <= 731) or (
                750 <= self.coords10.x() <= 871 and 630 <= self.coords10.y() <= 731) or c == c1 == c2 == c3 == c4 == \
                c5 == c6 == c7 == c8 == c9 == c10 == 1:
            self.the_end.move(250, 250)
            self.the_end.setText("Ваш score: " + str(self.final_score))
            self.the_end.setFont(QtGui.QFont("Times", 30, QtGui.QFont.Bold))
            self.the_end.show()
            if self.final_score > score:
                con = sqlite3.connect("base_fly.db")
                cur = con.cursor()
                cur.execute("""UPDATE users
                SET score = ? WHERE login LIKE ?""", (self.final_score, login))
                con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
