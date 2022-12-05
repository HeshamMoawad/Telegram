from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import  NoSuchElementException
from MyPyQt5 import QThread,QObject,pyqtSignal
import typing , time , sqlite3 , datetime , os


# https://web.telegram.org/?legacy=1#/im?p=@Profasdasd
# https://t.me/Profasdasd

class JavaScriptCodeHandler(object):
    GET_ALL_MEMBER = """
    members = document.querySelectorAll("a[class='row no-wrap row-with-padding row-clickable hover-effect chatlist-chat chatlist-chat-abitbigger']");return members;
    """
    GET_GROUP_MEMBERS_COUNT = """
    info = document.querySelector("div[class='info']");info.click() ;return info.lastChild.textContent ;
    """
    SCROLL_DOWN = """h = document.querySelector("div[class='scrollable scrollable-y no-parallax']");h.scrollTo(0,10000000000) """

    GET_NAME = """return document.querySelector("span[data-peer-id='ID']").textContent;"""

    GET_MEMBER_ID = """return members[index].getAttribute("data-peer-id")"""

    def __init__(self,driver:WebDriver) -> None:
        self.driver = driver
    
    def jscode(self,command):
        return self.driver.execute_script(command)
    

    def WaitingElement(self,timeout:int,val:str,by:str=By.XPATH)->typing.Optional[WebElement]:
        end_time = time.time() + timeout
        while True:
            if time.time() > end_time :
                print("TimedOut and Breaked")
                break
            try:
                result = self.driver.find_element(by,val)
                break
            except NoSuchElementException :
                QThread.msleep(100)
        return result
    
    def WaitingElements(self,timeout:int,val:str,by:str=By.XPATH)->typing.Optional[typing.List[WebElement]]:
        end_time = time.time() + timeout
        while True:
            if time.time() > end_time :
                print("TimedOut and Breaked")
                break
            try:
                result = self.driver.find_elements(by,val)
                break
            except NoSuchElementException :
                QThread.msleep(100)
        return result
            
    def WaitingMethod(self,timeout:int,func):
        end_time = time.time() + timeout
        while True:
            if time.time() > end_time :
                print("TimedOut and Breaked")
                break
            try:
                result = func()
            except Exception as e :
                pass
        return result

    def getCurrentHandle(self)-> str:
        """ Return Handle From Current Link or UserID if Handle Not Found"""
        return self.driver.current_url.split("k/#")[-1]
    
    def getMembersCount(self)-> int:        #'79 484 members, 2 752 online' 
        """ Return Count Of Members In Group"""
        return int(str(self.jscode(self.GET_GROUP_MEMBERS_COUNT)).split(",")[0].replace(" ","").replace("members",""))
        
    def getMembers(self) -> typing.List[WebElement]:
        """ Return List Of Current Group Members [WebElements] """#With selenium
        return self.jscode(self.GET_ALL_MEMBER)
    
    def scrolldown(self, round:int=1 )->None:
        """ Scrolling Down In Page """
        for i in range(round):
            self.jscode(self.SCROLL_DOWN)


    def getName(self,id:str)-> WebElement: #print(self.GET_NAME.replace("ID",str(id)))# self.jscode(self.GET_NAME.replace("ID",str(id)))
        """ Return WebElement of Name of ID"""
        return self.WaitingElement(
            timeout = 10 ,
            val = f"//span[@class='peer-title'][@data-peer-id='{id}']"
        )

    def getIDfromElm(self,index) -> str :
        return self.jscode(self.GET_MEMBER_ID.replace("index",f"{index}"))
    
    

class Telegram(QObject):
    LeadSignal = pyqtSignal(list)
    PersntageSignal = pyqtSignal(int)
    def __init__(
            self,
            headless:bool = False ,
            darkMode:bool = False ,
            userProfile:str="Guest", 
            ) -> None:
        
        self.con = sqlite3.connect("Data\Database.db")
        self.cur = self.con.cursor()
        option = Options()
        option.headless = True if  headless == True else False
        option.add_experimental_option("excludeSwitches", ["enable-logging"])
        option.add_argument('--disable-logging')
        option.add_argument('--force-dark-mode') if darkMode == True else None
        option.add_argument(f"user-data-dir={os.getcwd()}\\Profiles\\{userProfile}")
        self.driver = Chrome(ChromeDriverManager().install(),options=option)
        self.js = JavaScriptCodeHandler(self.driver)
        self.driver.maximize_window()
        self.driver.get("https://web.telegram.org/k/")
        self.leadCount = 0
        self.js.WaitingElement(600,"//div[@class='chat-background']")
        QThread.sleep(3)
        super().__init__()
    
        
    def exist(self,column,val):
        self.cur.execute(f"""SELECT * FROM data WHERE {column} = '{val}'; """)
        return True if self.cur.fetchall() != [] else False
    
    
    def add_to_db(self,**kwargs):
        try:
            self.cur.execute(f"""
            INSERT INTO data {str(tuple(kwargs.keys())).replace("'","")}
            VALUES {tuple(kwargs.values())}; 
            """)
            self.con.commit()
        except Exception as e:
            print(f"\n{e} \nError in Database \n")

        
    def scrapeHandlesFromGroup(
        self,
        grouphandle:str,
        limit:int ,
        collect:int ,
        ) -> None:
        print(f"{limit},{grouphandle}")
        self.driver.get(f"https://web.telegram.org/k/#{grouphandle}")
        QThread.sleep(5)
        self.js.WaitingElement(10,"//div[@class='info']")
        membersCount = self.js.getMembersCount()
        members = self.js.getMembers()
        while len(members) < collect :
            if len(members) >= membersCount :
                print("Breaked all in group")
                break
            self.js.scrolldown(2)
            members = self.js.getMembers()

        for member in members:
            if self.leadCount >= limit :
                break
            User_ID = self.js.getIDfromElm(
                index = members.index(member), 
            )
            print(f"\n{User_ID}\n")
            if not self.exist("User_ID",User_ID):
                print(f"{User_ID}")
                self.driver.get(f"https://web.telegram.org/k/#{User_ID}")
                self.js.WaitingElement(
                    timeout = 10 ,
                    val = "//div[@id='column-right']"
                )
                try:
                    Name = self.js.getName(User_ID).text
                except Exception as e :
                    Name = ""
                    print(e)
                Handle = self.js.getCurrentHandle()
                self.add_to_db(
                    User_ID = User_ID ,
                    Handle = Handle ,
                    Name = Name ,
                    Time = f"{datetime.datetime.now().date()}",
                )
                print([str(User_ID) , Handle , Name ])
                if User_ID != Handle :
                    self.LeadSignal.emit([
                        str(User_ID) , 
                        Handle , 
                        Name ,
                    ])
                    self.leadCount += 1



    def addMembersToChannel(
        self,
        channelHandle:str ,
        handlesList:typing.List[str],
        )-> None :

        self.driver.get(f"https://web.telegram.org/?legacy=1#/im?p={channelHandle}")
        self.js.WaitingElement(
            timeout = 30 , 
            val= "//a[@class='tg_head_btn']"
        ).click()
        self.js.WaitingElement(
            timeout = 30 ,
            val = "//a[@class='md_modal_section_link']"
        ).click()

        searchElement = self.js.WaitingElements(
            timeout = 30 , 
            val = "//input[@type='search']" ,
        )[1]
        for handle in handlesList:
            searchElement.send_keys(handle)
            QThread.sleep(1)
            results = self.js.WaitingElements(
                timeout = 10 , 
                val = "//div[@my-peer-link='contact.userID']"
            )
            for elm in results:
                if elm.text != 'Unsupported User':
                    elm.click()
                    self.PersntageSignal.emit(int(((handlesList.index(handle)+1)/len(handlesList))*100))

            searchElement.clear()

        self.js.WaitingElement(
            timeout = 30 ,
            val = "//button[@ng-switch-when='select']"
        ).click()
        QThread.sleep(5)

    def exit(self):
        self.driver.quit()