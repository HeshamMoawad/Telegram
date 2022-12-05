
from PyQt5 import QtCore, QtGui, QtWidgets
import typing , os
from MyPyQt5 import MyQTreeWidget , QObject , MyMessageBox , MyCustomContextMenu 
from mainclass import Telegram
import shutil ,pyperclip
from styles import Styles
import pandas as pd
from datetime import datetime

class Page1(QObject): ## ------------------------------------------ Page 1 
    def __init__(self,parent:typing.Optional[QtWidgets.QWidget]) -> None:
        self.Name = ""
        self.msg = MyMessageBox()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(parent)
        self.verticalLayout_2.setContentsMargins(0, 3, 3, 3)
        self.verticalLayout_2.setSpacing(0)
        self.frame = QtWidgets.QFrame(parent)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.channelLabel = QtWidgets.QLabel(self.frame,text="Channel Name")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PageMainLabel = QtWidgets.QLabel(parent,text="Scraper")
        self.PageMainLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_2.addWidget(self.PageMainLabel)
        self.PageMainLabel.setFont(font)
        self.channelLabel.setFont(font)
        self.channelLabel.setToolTipDuration(-1)
        self.channelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.channelLabel)
        self.channelLineEdit = QtWidgets.QLineEdit(self.frame)
        self.channelLineEdit.setPlaceholderText("ChannelInfo (@example) Or (https://t.me/example)")
        self.channelLineEdit.setStyleSheet("""background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(68, 90, 25, 203));color:white;border-radius:6px;""")
        self.horizontalLayout.addWidget(self.channelLineEdit)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.limitLabel = QtWidgets.QLabel(self.frame_2,text="Limit")
        self.limitLabel.setFont(font)
        self.limitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_2.addWidget(self.limitLabel)
        self.spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(100000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setStyleSheet("""background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(68, 90, 25, 203));color:white;border-radius:6px;""")#background-color:transparent;border:2px solid qlineargradient(spread:pad, x1:0.716, y1:0, x2:0.517, y2:0.613409, stop:0.289773 rgba(151, 133, 210, 223), stop:0.926136 rgba(0, 183, 232, 239));
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.start = QtWidgets.QToolButton(self.frame_3)
        self.start.setIcon(QtGui.QIcon("Data\Icons\icons8-play-96.png"))
        self.start.setIconSize(QtCore.QSize(50,50))
        self.start.setGraphicsEffect(self.shadow())
        self.start.setShortcut("Enter")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.start.setSizePolicy(sizePolicy)
        self.horizontalLayout_3.addWidget(self.start)
        self.stop = QtWidgets.QToolButton(self.frame_3)
        self.stop.setIcon(QtGui.QIcon("Data\Icons\icons8-unavailable-96.png"))
        self.stop.setGraphicsEffect(self.shadow())
        self.stop.setIconSize(QtCore.QSize(50,50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.stop.setSizePolicy(sizePolicy)
        self.horizontalLayout_3.addWidget(self.stop)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(parent)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout.setSpacing(5)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.treewidget = MyQTreeWidget(self.frame_4,self.label)
        self.treewidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.treewidget.customContextMenuRequested.connect(lambda :self.contextMenu())
        self.treewidget.setColumns([" ID","Handle","Name"])
        self.treewidget.setColumnWidth(0,150)
        self.treewidget.setColumnWidth(1,200)
        self.treewidget.setColumnWidth(2,130)
        self.treewidget.setStyleSheet("""color:white;""")
        self.treewidget.header().setStyleSheet("""color:black;""")
        self.verticalLayout.addWidget(self.treewidget)
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 4)

    def shadow(self):
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(-10,10)
        shadow.setColor(QtGui.QColor("white"))
        return shadow

    def setkey(self,name:str):
        self.Name = name

    def contextMenu(self):
        menu = MyCustomContextMenu([
        "Copy ID", # 0    
        "Copy Handle", # 1
        "Copy Name", # 2
        "Delete Row" , # 3
        "Export All To Excel", # 4
        "Copy IDs List", # 5
        "Copy Handles List", # 6
        "Copy Names List", # 7
        "Copy IDs and Handles", # 8
        "Copy All", # 9
        "Clear Results", # 10
        ])
        menu.multiConnect(functions=[
            lambda : self.copy(0), # 0
            lambda : self.copy(1), # 1
            lambda : self.copy(2), # 2
            lambda: self.delete() , # 3
            lambda: self.export(self.Name) , # 4
            lambda : pyperclip.copy(self.treewidget.extract_data_to_string(0)) if self.treewidget._ROW_INDEX != 0 else self.msg.showWarning(text="No Data In Column !") , # 5
            lambda : pyperclip.copy(self.treewidget.extract_data_to_string(1)) if self.treewidget._ROW_INDEX != 0 else self.msg.showWarning(text="No Data In Column !"),  # 6
            lambda : pyperclip.copy(self.treewidget.extract_data_to_string(2)) if self.treewidget._ROW_INDEX != 0 else self.msg.showWarning(text="No Data In Column !"), # 7
            lambda: pyperclip.copy(self.treewidget.extract_data_to_DataFrame(range_of=range(0,2)).to_string(index=False)) if self.treewidget._ROW_INDEX != 0 else self.msg.showWarning(text="No Data Found !") , # 8
            lambda: pyperclip.copy(self.treewidget.extract_data_to_DataFrame().to_string(index=False)) if self.treewidget._ROW_INDEX != 0 else self.msg.showWarning(text="No Data Found !") , # 9
            lambda: self.treewidget.clear() , # 10
        ])
        menu.show()

    def copy(self , index:int):
        try :
            pyperclip.copy(self.treewidget.currentItem().text(index))
        except :
            self.msg.showWarning(text="No Item Selected please Select one !")

    def delete(self):
        try:
            self.treewidget.takeTopLevelItem(self.treewidget.indexOfTopLevelItem(self.treewidget.currentItem()))
        except:
            self.msg.showWarning(text="No Item Selected please Select one !")

    def export(self,name:typing.Optional[str]):
        if self.treewidget._ROW_INDEX > 0 :
            self.treewidget.extract_data_to_DataFrame().to_excel(f"Data/Exports/{name}[{datetime.now().date()}].xlsx",index=False)
            self.msg.showInfo(text=f"Exported Succecfully to 'Data/Exports/{name}[{datetime.now().date()}].xlsx'")
        else :
            self.msg.showWarning(text="No Data In App Please Try Again Later")




class Page2(QObject): ## ------------------------------------------ Page 2
    def __init__(self,parent:typing.Optional[QtWidgets.QWidget]) -> None:
        self.msg = MyMessageBox()
        self.df = pd.DataFrame()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(parent)
        self.verticalLayout_2.setContentsMargins(0, 3, 3, 3)
        self.verticalLayout_2.setSpacing(0)
        self.frame = QtWidgets.QFrame(parent)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.channelLabel = QtWidgets.QLabel(self.frame,text="Channel Name")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PageMainLabel = QtWidgets.QLabel(parent,text="Add Members")
        self.PageMainLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_2.addWidget(self.PageMainLabel)
        self.PageMainLabel.setFont(font)
        self.channelLabel.setFont(font)
        self.channelLabel.setToolTipDuration(-1)
        self.channelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.channelLabel)
        self.channelLineEdit = QtWidgets.QLineEdit(self.frame)
        self.channelLineEdit.setPlaceholderText("Channel Link example:https://t.me/example ")
        self.channelLineEdit.setStyleSheet("""background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(68, 90, 25, 203));color:white;border-radius:6px;""")
        self.horizontalLayout.addWidget(self.channelLineEdit)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.limitLabel = QtWidgets.QLabel(self.frame_2,text="Limit")
        self.limitLabel.setFont(font)
        self.limitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_2.addWidget(self.limitLabel)
        self.spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(100000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setStyleSheet("""background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(68, 90, 25, 203));color:white;border-radius:6px;""")#background-color:transparent;border:2px solid qlineargradient(spread:pad, x1:0.716, y1:0, x2:0.517, y2:0.613409, stop:0.289773 rgba(151, 133, 210, 223), stop:0.926136 rgba(0, 183, 232, 239));
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.start = QtWidgets.QToolButton(self.frame_3)
        self.start.setIcon(QtGui.QIcon("Data\Icons\icons8-play-96.png"))
        self.start.setIconSize(QtCore.QSize(50,50))
        self.start.setGraphicsEffect(self.shadow())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.start.setSizePolicy(sizePolicy)
        self.horizontalLayout_3.addWidget(self.start)
        self.stop = QtWidgets.QToolButton(self.frame_3)
        self.stop.setIcon(QtGui.QIcon("Data\Icons\icons8-unavailable-96.png"))
        self.stop.setGraphicsEffect(self.shadow())
        self.stop.setIconSize(QtCore.QSize(50,50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.stop.setSizePolicy(sizePolicy)
        self.horizontalLayout_3.addWidget(self.stop)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(parent)
        # ------------------------------
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_10.setSpacing(5)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setText("Import")
        self.label_10.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_10.addWidget(self.label_10)
        self.frame = QtWidgets.QFrame(self.frame_4)
        self.frame.setSizePolicy(sizePolicy)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_10.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_10.setSpacing(3)
        self.importLabel = QtWidgets.QLabel(self.frame)
        self.importLabel.setText("Imported @Handles : -->")
        self.importLabel.setFont(font)
        self.horizontalLayout_10.addWidget(self.importLabel)
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setIcon(QtGui.QIcon("Data\Icons\icons8-microsoft-excel-50.png"))
        self.toolButton.setIconSize(QtCore.QSize(30,30))
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.clicked.connect(lambda : self.dialog() )
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setIcon(QtGui.QIcon("Data\Icons\icons8-broom-100.png"))
        self.toolButton_2.setIconSize(QtCore.QSize(30,30))
        self.toolButton_2.clicked.connect(lambda : self.clearDF())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.verticalLayout_10.addWidget(self.toolButton_2)
        self.horizontalLayout_10.addWidget(self.toolButton)
        self.horizontalLayout_10.setStretch(0, 2)
        self.horizontalLayout_10.setStretch(1, 1)
        self.verticalLayout_10.addWidget(self.frame)
        #-----------
        self.bar = QtWidgets.QProgressBar()
        self.bar.setValue(0)
        self.bar.setStyleSheet(Styles.PROGRESSBAR)
        self.verticalLayout_10.addWidget(self.bar)
        #-----------
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        #------------------------------
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 4)

    def shadow(self):
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(-10,10)
        shadow.setColor(QtGui.QColor("white"))
        return shadow

    def dialog(self):
        file_filter = 'Data File (*.xlsx *.csv);; Excel File (*.xlsx *.xls)'
        dir = QtWidgets.QFileDialog.getOpenFileName(
            caption='Select a data file',
            filter=file_filter,
            )[0]
        self.df = pd.read_excel(dir)
        self.importLabel.setText(f"Import -> {self.df.__len__()}")

    def getHandlesList(self):
        return self.df["Handle"].to_list()

    def clearDF(self):
        self.df = pd.DataFrame()
        self.importLabel.setText("Imported @Handles : -->")
        self.bar.setValue(0)


class Page3(QObject):  ## ------------------------------------------ Page 3
    def __init__(self,parent:typing.Optional[QtWidgets.QWidget]) -> None:
        self.msg = MyMessageBox()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.verticalLayout = QtWidgets.QVBoxLayout(parent)
        self.label = QtWidgets.QLabel(parent,text="Setting")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(parent)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.label_2 = QtWidgets.QLabel(self.frame_2 ,text="Current Account : Guest")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setFont(font)
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.currentTextChanged.connect(lambda : self.currentUser())
        self.comboBox.setFont(font)
        self.comboBox.addItems([name for name in os.listdir(os.getcwd() + "\\Profiles") if os.path.isdir(f"{os.getcwd()}\\Profiles\\{name}")])#####################
        self.comboBox.setStyleSheet("""background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(68, 90, 25, 203));color:white;border-radius:6px;""")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred) ##############
        self.comboBox.setSizePolicy(sizePolicy)
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(parent)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.addbtn= QtWidgets.QToolButton(self.frame)
        self.addbtn.setIcon(QtGui.QIcon("Data\Icons\icons8-plus-math-90.png"))
        self.addbtn.setIconSize(QtCore.QSize(25,25))
        self.addbtn.clicked.connect(lambda:self.addUser())
        self.addbtn.setDisabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.addbtn.setSizePolicy(sizePolicy)
        self.horizontalLayout.addWidget(self.addbtn)
        self.deletbtn = QtWidgets.QToolButton(self.frame)
        self.deletbtn.setIcon(QtGui.QIcon("Data\Icons\icons8-remove-100.png"))
        self.deletbtn.setIconSize(QtCore.QSize(25,25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.deletbtn.setSizePolicy(sizePolicy)
        self.horizontalLayout.addWidget(self.deletbtn)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.textChanged.connect(lambda: self.lineEditFunc())
        self.lineEdit.setFont(font)
        self.lineEdit.setPlaceholderText("Enter New User Here")
        self.lineEdit.setStyleSheet("""background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(68, 90, 25, 203));color:white;border-radius:6px;""")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addWidget(self.frame)

        spacerItem = QtWidgets.QSpacerItem(20, 218, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.deletbtn.clicked.connect(lambda : self.removeUser())



    def currentUser(self):
        user = self.comboBox.currentText()
        if os.path.isdir(f"Profiles\\{user}"):
            self.label_2.setText(f"Current Account : {user}")
        else:
            self.msg.showCritical(text="No User Found")
        

    def removeUser(self):
        user = self.comboBox.currentText()
        if len(user) < 2 :
            self.msg.showInfo("No User Selected Please select one")
        else:
            userdir = f"{os.getcwd()}\\Profiles\\{user}"
            print([user,userdir])
            if os.path.isdir(userdir):
                shutil.rmtree(userdir)
                self.comboBox.removeItem(self.comboBox.currentIndex())
                self.msg.showInfo(text="Deleted Succecfully")
            else:
                self.msg.showWarning(text="Can't Find User")

    def addUser(self):
        user = self.lineEdit.text()
        self.lineEdit.clear()
        try:
            dir = f"{os.getcwd()}\\Profiles\\{user}"
            try:
                os.mkdir(dir)
            except Exception as e :
                print(e)
            tel = Telegram(
                headless= False ,
                darkMode= False ,
                userProfile = dir ,
            )
            self.comboBox.addItem(user)
            self.msg.showInfo(text=f"Nice {user} Added Succecfully")
        except Exception as e :
            shutil.rmtree(dir)
            self.msg.showCritical(text=f"Can't add User \n {e}")
        

    def lineEditFunc(self):
        if len(self.lineEdit.text()) > 2:
            self.addbtn.setDisabled(False)
        else:
            self.addbtn.setDisabled(True)
    