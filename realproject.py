###

from PyQt5 import QtCore, QtGui, QtWidgets
from Evaluateteam import Ui_EvaluateTeam
from Openteam import Ui_Openteam1
from PyQt5.QtWidgets import QMessageBox
import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="16239",database="project_fantasy")
cursor=con.cursor()

class Ui_MainWindow(object):
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.l1 = QtWidgets.QLineEdit(self.centralwidget)
        self.l1.setEnabled(False)
        self.l1.setObjectName("l1")
        self.horizontalLayout.addWidget(self.l1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.l2 = QtWidgets.QLineEdit(self.centralwidget)
        self.l2.setEnabled(False)
        self.l2.setObjectName("l2")
        self.horizontalLayout.addWidget(self.l2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.l3 = QtWidgets.QLineEdit(self.centralwidget)
        self.l3.setEnabled(False)
        self.l3.setObjectName("l3")
        self.horizontalLayout.addWidget(self.l3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.l4 = QtWidgets.QLineEdit(self.centralwidget)
        self.l4.setEnabled(False)
        self.l4.setObjectName("l4")
        self.horizontalLayout.addWidget(self.l4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.l5 = QtWidgets.QLineEdit(self.centralwidget)
        self.l5.setEnabled(False)
        self.l5.setObjectName("l5")
        self.horizontalLayout_2.addWidget(self.l5)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.l6 = QtWidgets.QLineEdit(self.centralwidget)
        self.l6.setEnabled(False)
        self.l6.setObjectName("l6")
        self.horizontalLayout_2.addWidget(self.l6)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem16)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem17)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem18)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn1 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.horizontalLayout_4.addWidget(self.btn1)
        self.btn2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.horizontalLayout_4.addWidget(self.btn2)
        self.btn3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.horizontalLayout_4.addWidget(self.btn3)
        self.btn4 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.btn1.toggled.connect(self.category)####
        self.btn2.toggled.connect(self.category)####
        self.btn3.toggled.connect(self.category)####
        self.btn4.toggled.connect(self.category)####
        self.horizontalLayout_4.addWidget(self.btn4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        self.list1.setObjectName("list1")
        self.list1.itemDoubleClicked.connect(self.removelist1)####
        self.verticalLayout_2.addWidget(self.list1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem19)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem20)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.l7 = QtWidgets.QLineEdit(self.centralwidget)
        self.l7.setEnabled(False)
        self.l7.setObjectName("l7")
        self.l7.setText("Team_name")
        self.horizontalLayout_5.addWidget(self.l7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setObjectName("list2")
        self.list2.itemDoubleClicked.connect(self.removelist2)        ####
        self.verticalLayout_3.addWidget(self.list2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem21)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.menuManage_Teams.setFont(font)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menuManage_Teams.addSeparator()
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)####

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "FANTASY 11"))
        self.label_2.setText(_translate("MainWindow", " Batsman (BAT) "))
        self.label_3.setText(_translate("MainWindow", " Bowler (BOWL) "))
        self.label_4.setText(_translate("MainWindow", " All-Rounder (A-R)"))
        self.label_5.setText(_translate("MainWindow", " Wicket-keeper (W-K)"))
        self.label_6.setText(_translate("MainWindow", " Points Available "))
        self.label_7.setText(_translate("MainWindow", " Points Used "))
        self.btn1.setText(_translate("MainWindow", "BOWL"))
        self.btn2.setText(_translate("MainWindow", "BAT"))
        self.btn3.setText(_translate("MainWindow", "A-R"))
        self.btn4.setText(_translate("MainWindow", "W-K"))
        self.label_8.setText(_translate("MainWindow", " Team Name"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))

    #### MENUFUNCTION
        
    def menufunction(self,action):
        txt=action.text()
        if txt=="New Team":
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.avl=1000
            self.used=0
            self.list1.clear()
            self.list2.clear()
            self.showstatus()
            text, ok = QtWidgets.QInputDialog.getText(MainWindow, 'Fantasy Cricket Game', 'Enter name of team:')
            if ok:
                self.l7.setText(str(text))
                
        if txt=='Save Team':
            selected=""
            count=self.list2.count()
            for i in range(count):
                selected=selected+self.list2.item(i).text()
                if i<count-1:
                    selected=selected+","
            self.save_team(self.l7.text(),selected,self.used)
            
        if txt=="Open Team":
            self.window1 = QtWidgets.QWidget()
            self.ui = Ui_Openteam1()
            self.ui.setupUi(self.window1)
            self.window1.show()
            

        if txt=="Evaluate Team":
            self.window2 = QtWidgets.QWidget()
            self.ui = Ui_EvaluateTeam()
            self.ui.setupUi(self.window2)
            self.window2.show()

    ####
    def save_team(self,nm,string,val):
        if self.bat+self.bwl+self.ar+self.wk!=11:
            self.showdlg("Insufficient players")
            return
        query="insert into team (name, players, value) VALUES ('"+nm+"','"+string+"','"+str(val)+"');"
        try:
            cursor.execute(query)
            con.commit()
            self.showmsg("Team saved successfully")
        except:
            self.showmsg("error !")
            con.rollback()

        
    ####
    def category(self):
        category=""
        if self.btn1.isChecked()==True: category="BWL"
        if self.btn2.isChecked()==True: category="BAT"
        if self.btn3.isChecked()==True: category="AR"
        if self.btn4.isChecked()==True: category="WK"
        self.fillList(category)
    
    def fillList(self,category):
        self.list1.clear()
        if self.l7.text()=="Team_name":
            self.showmsg("ENTER TEAM NAME FIRST")
            return
        record=[]
        cursor=con.cursor()
        query="select player from stat where category='"+category+"';"
        cursor.execute(query)
        row=cursor.fetchall()
        a=0
        for x in row:
            record.append(row[a])
            txt=str(row[a])
            text=txt.replace(",","").replace("'","").replace("(","").replace(")","")
            self.list1.addItem(text)
            a+=1

    ####
    def logic(self,category,item):
        txt=item.text()
        msg=""
        if category=="BWL" and self.bwl>=5:
            msg="Bowler not more than 5"
            self.showmsg(msg)
            return False
        if category=="BAT" and self.bat>=5:
            msg="Batsman not more than 5"
            self.showmsg(msg)
            return False
        if category=="AR" and self.ar>=3:
            msg="All_rounder not more than 3"
            self.showmsg(msg)
            return False
        if category=="WK" and self.wk>=1:
            msg="Wicket_keeper not more than 1"
            self.showmsg(msg)
            return False
        if msg!="" or self.avl<=0:
            msg="You have exhausted your points"
            self.showmsg(msg)
            return False

        if category=="BAT": self.bat=self.bat+1
        if category=="BWL": self.bwl+=1
        if category=="AR": self.ar+=1
        if category=="WK": self.wk+=1
        query="select value from stat where player='"+txt+"';"
        cursor.execute(query)
        row=cursor.fetchone()
        txt=str(row).replace("(","").replace(",","").replace(")","")
        self.avl=self.avl-int(txt)
        self.used=self.used+int(txt)
        return True

    ####
    def showstatus(self):
        self.l1.setText(str(self.bat))
        self.l2.setText(str(self.bwl))
        self.l3.setText(str(self.ar))
        self.l4.setText(str(self.wk))
        self.l5.setText("Available Points : {}".format(self.avl))
        self.l6.setText("Points used : {}".format(self.used))

    ####
    def showmsg(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("FANTASY CRICKET GAME")
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    ####
    def removelist1(self,item):
        category=""
        if self.btn1.isChecked()==True: category="BWL"
        if self.btn2.isChecked()==True: category="BAT"
        if self.btn3.isChecked()==True: category="AR"
        if self.btn4.isChecked()==True: category="WK"
        rec=self.logic(category,item)
        if rec==True:
            self.list1.takeItem(self.list1.row(item))
            self.list2.addItem(item.text())
            self.showstatus()
    ###
    def removelist2(self, item):
        self.list2.takeItem(self.list2.row(item))
        query="select player,value, category from stat where player='"+item.text()+"';"
        cursor.execute(query)
        row=cursor.fetchone()
        self.avl=self.avl+int(row[1])
        self.used=self.used-int(row[1])
        category=row[2]
        if category=="BAT":
            self.bat-=1
            if self.btn2.isChecked()==True:self.list1.addItem(item.text())
        if category=="BWL":
            self.bwl-=1
            if self.btn1.isChecked()==True:self.list1.addItem(item.text())
        if category=="AR":
            self.ar-=1
            if self.btn3.isChecked()==True:self.list1.addItem(item.text())
        if category=="WK":
            self.wk-=1
            if self.btn4.isChecked()==True:self.list1.addItem(item.text())
        self.showstatus()
	
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
