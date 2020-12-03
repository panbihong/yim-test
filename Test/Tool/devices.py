from appium import webdriver

def shebei1(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = 'GWY0217408003753'
    desired_caps['appPackage'] = 'com.yidejia.yim.test'
    desired_caps['appActivity'] = 'com.yidejia.yim.SplashActivity'
    desired_caps['noReset'] =True
    desired_caps['dontStopAppOnReset'] =True
    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    self.driver.implicitly_wait(30)

def shebei2(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1.0'
    desired_caps['deviceName'] = '10.12.1.148:5555'
    desired_caps['appPackage'] = 'com.yidejia.yim.test'
    desired_caps['appActivity'] = 'com.yidejia.yim.SplashActivity'
    desired_caps['noReset'] = True
    desired_caps['dontStopAppOnReset'] =True
    self.driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps)
    self.driver.implicitly_wait(30)

