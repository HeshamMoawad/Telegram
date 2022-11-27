from MyPyQt5 import QSideMenuNewStyle,MyQMainWindow
from pages import Page1 , Page2 , Page3
from styles import Styles


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
        self.scraperPageButton = self.Menu.GetButton(0)
        self.scraperPageButton.setText("Scraper")
        self.scraperPageButton.setStyleSheet(Styles.BUTTON)
        self.scraperPageButton.clicked.connect(lambda: self.Menu.setCurrentPage(0))
        self.channelPageButton = self.Menu.GetButton(1)
        self.channelPageButton.setText("Channel Options")
        self.channelPageButton.setStyleSheet(Styles.BUTTON)
        self.channelPageButton.clicked.connect(lambda:self.pop.addUserPopUp("ss"))#lambda: self.Menu.setCurrentPage(1)
        self.settingPageButton = self.Menu.GetButton(2)
        self.settingPageButton.setText("Setting")
        self.settingPageButton.setStyleSheet(Styles.BUTTON)
        self.settingPageButton.clicked.connect(lambda: self.Menu.setCurrentPage(2))

        
        return super().SetupUi()
    








w = Window()


