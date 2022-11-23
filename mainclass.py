from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
# from selenium.common.exceptions import JavascriptException
from MyPyQt5 import QThread,QObject,pyqtSignal
import typing , os


class JavaScriptCodeHandler(object):
    GET_ALL_MEMBER = """
    members = document.querySelectorAll("a[class='chatlist-chat']") ;return members;
    """
    GET_USER_INFO = """
    document.querySelector("div[class='chat-info']").click()
    """

    def __init__(self,driver:WebDriver) -> None:
        self.driver = driver
    
        
    def jscode(self,command):
        return self.driver.execute_script(command)
    
    def getCurrentHandle(self):
        return self.driver.current_url.split("k/#")[-1]
    
    @typing.overload
    def getMembers(self)-> typing.List[WebElement] :
        return self.jscode(self.GET_ALL_MEMBER)
            
    
        
    @typing.overload
    def getMembers(self,limit:int) -> typing.List[WebElement]:

        

        pass
    
    
        

    


class Telegram(QObject):
    


    LeadSignal = pyqtSignal(list)



    def __init__(self,headless,DarkMode:typing.Optional[bool]=False) -> None:
        self.headless = headless
        option = Options()
        option.headless = self.headless
        option.add_experimental_option("excludeSwitches", ["enable-logging"])
        option.add_argument('--disable-logging')
        option.add_argument('--force-dark-mode') if DarkMode != False else None
        profile = os.path.join(os.getcwd(), "profiles", "TelegramAccount")
        option.add_argument(f"user-data-dir={profile}")
        self.driver = Chrome(ChromeDriverManager().install(),options=option)
        self.driver.maximize_window()
        self.driver.get("https://web.telegram.org/k/")
        self.wait = WebDriverWait(self.driver, 500)
        self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='animated-menu-icon']")))   
        self.leadCount = 0
        QThread.sleep(5)
        super().__init__()
    

    def wait_elms(
        self,
        val:str,
        by:str=By.XPATH,
        timeout:int=30,
        )->typing.List[WebElement]:
        
        """ waiting elements """
        self.wait = WebDriverWait(self.driver, timeout=timeout)
        return self.wait.until(EC.presence_of_all_elements_located((by,val)))


    def wait_elm(self,val:str,by:str=By.XPATH,timeout:int=30)->WebElement:
        self.wait = WebDriverWait(self.driver, timeout=timeout)
        arg = (by,val)
        return self.wait.until(EC.presence_of_element_located(arg))

    def scrapeHandlesFromGroup(self,grouphandle:str):
        self.driver.get()


        pass
