from MyPyQt5 import QSideMenuNewStyle,MyQMainWindow,MyThread ,QEventLoop, pyqtSignal ,typing ,Validation
from pages import Page1 , Page2 , Page3
from styles import Styles
from mainclass import Telegram , AsyncMethods
import asyncio


class Window(MyQMainWindow):
    def SetupUi(self):
        self.setStyleSheet("""background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.227364, y2:0.858, stop:0 rgba(0, 0, 0, 255), stop:0.988636 rgba(68, 90, 25, 203));color:white;""")
        self.resize(650,600)
        self.setFrameLess()
        self.Menu = QSideMenuNewStyle(
            self.mainWidget,
            ButtonsCount=3 ,
            PagesCount= 3 ,
            ButtonsFixedHight=50 ,
            ButtonsFrameFixedwidth=100 ,
            MiniButtonIconPath= "Data\Icons\icons8-subtract-30.png",
            MaxButtonIconPath= "Data\Icons\icons8-full-screen-50.png",
            Mini_MaxButtonIconPath="Data\Icons\icons8-collapse-26.png",
            ExitButtonIconPath="Data\Icons\icons8-close-window-96.png",
        )
        self.Page1 = Page1(self.Menu.GetPage(0))
        self.Page2 = Page2(self.Menu.GetPage(1))
        self.Page3 = Page3(self.Menu.GetPage(2))
        self.valid = Validation.TelegramValidation()

        ## First Page
        self.scraperPageButton = self.Menu.GetButton(0)
        self.scraperPageButton.setText("Scraper")
        self.scraperPageButton.setStyleSheet(Styles.BUTTON)
        self.scraperPageButton.clicked.connect(lambda: self.Menu.setCurrentPage(0))
        
        ## Second Page
        self.channelPageButton = self.Menu.GetButton(1)
        self.channelPageButton.setText("Channel Options")
        self.channelPageButton.setStyleSheet(Styles.BUTTON)
        self.channelPageButton.clicked.connect(lambda: self.Menu.setCurrentPage(1))
        
        ## Third Page
        self.settingPageButton = self.Menu.GetButton(2)
        self.settingPageButton.setText("Setting")
        self.settingPageButton.setStyleSheet(Styles.BUTTON)
        self.settingPageButton.clicked.connect(lambda: self.Menu.setCurrentPage(2))

        ## ScraperThread Part 
        self.ScraperThread = ScraperThread()
        self.ScraperThread.setMainClass(self)
        self.ScraperThread.statues.connect(self.Menu.MainLabel.setText)
        self.ScraperThread.LeadSignal.connect(self.Page1.treewidget.appendData)
        self.ScraperThread.message.connect(self.Page1.msg.showInfo)
        self.Page1.start.clicked.connect(self.ScraperThread.start)
        self.Page1.stop.clicked.connect(lambda : self.ScraperThread.kill(True))

        ## AddingThread Part
        self.AddingThread = AddingThread()
        self.AddingThread.setMainClass(self)
        self.AddingThread.statues.connect(self.Menu.MainLabel.setText)
        self.AddingThread.PersntageSignal.connect(self.Page2.bar.setValue)
        self.AddingThread.Counter.connect(self.Page2.Counter)
        self.AddingThread.message.connect(self.Page2.msg.showInfo)
        self.Page2.start.clicked.connect(self.AddingThread.start)
        self.Page2.stop.clicked.connect(lambda : self.AddingThread.kill(True))
        self.setAppIcon("Data\Icons\\app.jpg")
        return super().SetupUi()
    
    


class ScraperThread(MyThread):
    LeadSignal = pyqtSignal(list)
    message = pyqtSignal(str)
    def run(self) -> None:
        self.statues.emit("Scraper Mode Starting ")
        channelName = self.MainClass.Page1.channelLineEdit.text()
        self.MainClass.Page1.channelLineEdit.clear()
        limit = self.MainClass.Page1.spinBox.value()
        user = self.MainClass.Page3.comboBox.currentText()
        self.statues.emit(f"Current Openning User : {user}")
        try:
            self.Telegram = Telegram(
                headless = self.MainClass.Menu.Hidetoggle.isChecked() ,
                darkMode = self.MainClass.Menu.DarkModetoggle.isChecked() ,
                userProfile = user,
            )
            self.statues.emit(f"Opened {user} Succecfully")
            con = True
        except Exception as e :
            print(e)
            self.message.emit(f"Can't Opinnig this User {user}")
            con = False
        if con:
            self.Telegram.LeadSignal.connect(self.LeadSignal.emit)
            self.statues.emit(f" Scraping ... ")
            collect = limit
            while True :
                print("Start Time")
                self.Telegram.scrapeHandlesFromGroup(
                    grouphandle = self.MainClass.valid.channelNameOrLinkToHandle(channelName),
                    limit = limit ,
                    collect= collect
                )
                if self.MainClass.Page1.treewidget._ROW_INDEX >= limit :
                    break
                collect += collect
            self.statues.emit("Ending Good Luck Next Time -_^")
            self.Telegram.exit()
            self.message.emit("حبيب اخوك ابقى تعالى تانى")

    def setMainClass(self,main:Window):
        self.MainClass = main

    def mainClass(self):
        return self.MainClass 

    def kill(self, msg: typing.Optional[bool]):
        try:
            self.Telegram.exit()
        except Exception as e :
            print(e)
        return super().kill(msg)








class AddingThread(ScraperThread):
    PersntageSignal = pyqtSignal(int)
    Counter = pyqtSignal(int,int,int)
    def run(self) -> None:
        self.statues.emit("Adding Mode Starting ")
        channelName = self.MainClass.Page2.channelLineEdit.text()
        self.MainClass.Page2.channelLineEdit.clear()
        limit = self.MainClass.Page2.spinBox.value()
        user = self.MainClass.Page3.comboBox.currentText()
        self.MainClass.Page1.setkey(self.MainClass.valid.channelNameOrLinkToHandle(channelName))
        self.statues.emit(f"Current Openning User : {user}")
        try:
            loop = asyncio.new_event_loop()
            self.AsyncMethods = AsyncMethods()
            self.AsyncMethods.PersntageSignal.connect(self.PersntageSignal.emit)
            self.AsyncMethods.Counter.connect(self.Counter.emit)
            self.AsyncMethods.status.connect(self.statues.emit)
            asyncio.set_event_loop(loop)
            self.AsyncMethods.AddingToChannelAsync(
                channelHandle = self.MainClass.valid.channelNameOrLinkToHandle(
                    channelName
                    ),
                handlesList = self.MainClass.Page2.getHandlesList()[:limit],
                client=user,
                )
            con = False
        except Exception as e :
            print(e)
            con = True
            self.message.emit(f"Can't Run API in this Thread {e}")
        if con:
            try : 
                self.Telegram = Telegram(
                    headless = self.MainClass.Menu.Hidetoggle.isChecked() ,
                    darkMode = self.MainClass.Menu.DarkModetoggle.isChecked() ,
                    userProfile = user,
                )
                self.statues.emit(f"Opened {user} Succecfully")
                con = True
            except Exception as e :
                print(e)
                self.message.emit(f"Can't Opinnig this User {user}")
                con = False
            if con:
                self.Telegram.LeadSignal.connect(self.LeadSignal.emit)
                self.Telegram.PersntageSignal.connect(self.PersntageSignal.emit)
                self.statues.emit(f"Start Adding Handles")
                self.Telegram.addMembersToChannel(
                    channelHandle = self.MainClass.valid.channelNameOrLinkToHandle(channelName) ,
                    handlesList = self.MainClass.Page2.getHandlesList()[:limit],
                )
                self.Telegram.exit()
        self.statues.emit("Ending Good Luck Next Time -_^")
        self.message.emit("حبيب اخوك ابقى تعالى تانى")
        try:
            self.AsyncMethods.app.stop()
        except Exception as e :
            pass

    def kill(self, msg: typing.Optional[bool]):
        self.AsyncMethods.app.stop(False)
        return super().kill(msg)
if __name__ == "__main__":
    w = Window()


