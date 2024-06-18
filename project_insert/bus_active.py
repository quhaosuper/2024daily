import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def act_intention_notice():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://10.0.168.47:9000/bus-center/#/login")
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, "departmentName").send_keys("jgadmin")
    driver.find_element(By.NAME, "password").send_keys("123qwe!@#")
    driver.find_element(By.XPATH, "//*[@type='button' and @class='el-button login_btn el-button--primary']").click()
    driver.find_element(By.ID, "path-missionItem").click()
    driver.find_element(By.XPATH, "//*[@type='text' and @placeholder='请输入内容']").send_keys('采购意向公开')
    driver.find_element(By.XPATH, "//*[text()=' 检索 ' ]/parent::button").click()
    time.sleep(5)
    el = driver.find_element(By.XPATH, '//*[@class="el-table__fixed-right"]//*[@id="table-row_0_column_6"]//*[name('
                                       ')="svg"][2]')

    el.click()
    driver.quit()


def act_require_compilation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://10.0.168.47:9000/bus-center/#/login")
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, "departmentName").send_keys("jgadmin")
    driver.find_element(By.NAME, "password").send_keys("123qwe!@#")
    driver.find_element(By.XPATH, "//*[@type='button' and @class='el-button login_btn el-button--primary']").click()
    driver.find_element(By.ID, "path-missionItem").click()
    driver.find_element(By.XPATH, "//*[@type='text' and @placeholder='请输入内容']").send_keys('采购需求编制数仓同步')
    driver.find_element(By.XPATH, "//*[text()=' 检索 ' ]/parent::button").click()
    time.sleep(3)
    el = driver.find_element(By.XPATH, '//*[@class="el-table__fixed-right"]//*[@id="table-row_0_column_6"]//*[name('
                                       ')="svg"][2]')
    el.click()
    time.sleep(3)
    driver.quit()


def act_universal_row0(search):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://10.0.168.47:9000/bus-center/#/login")
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, "departmentName").send_keys("jgadmin")
    driver.find_element(By.NAME, "password").send_keys("123qwe!@#")

    driver.find_element(By.XPATH, "//*[@type='button' and @class='el-button login_btn el-button--primary']").click()
    driver.find_element(By.ID, "path-missionItem").click()
    driver.find_element(By.XPATH, "//*[@type='text' and @placeholder='请输入内容']").send_keys(search)
    driver.find_element(By.XPATH, "//*[text()=' 检索 ' ]/parent::button").click()
    time.sleep(5)
    el = driver.find_element(By.XPATH, '//*[@class="el-table__fixed-right"]//*[@id="table-row_0_column_6"]//*[name('
                                       ')="svg"][2]')
    el.click()
    time.sleep(2)
    driver.quit()


# act_universal_row0('采购项目信息数仓同步')


def act_universal_list_row0(search_list):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(8)
    driver.get("http://10.0.168.47:9000/bus-center/#/login")
    driver.find_element(By.NAME, "departmentName").send_keys("jgadmin")
    driver.find_element(By.NAME, "password").send_keys("123qwe!@#")
    driver.find_element(By.XPATH, "//*[@type='button' and @class='el-button login_btn el-button--primary']").click()
    driver.find_element(By.ID, "path-missionItem").click()
    for i in range(len(search_list)):
        driver.find_element(By.XPATH, "//*[@type='text' and @placeholder='请输入内容']").send_keys(search_list[i])
        driver.find_element(By.XPATH, "//*[text()=' 检索 ' ]/parent::button").click()
        time.sleep(5)
        el = driver.find_element(By.XPATH, '//*[@class="el-table__fixed-right"]//*[@id="table-row_0_column_6"]//*[name('
                                           ')="svg"][2]')
        el.click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@type='text' and @placeholder='请输入内容']").clear()
    driver.quit()


# act_universal_list_row0(['采购项目信息数仓同步', '采购包信息数仓同步'])


def act_universal_list_85_row0(search_list):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://glodon.test.com:32087/bus-center/#/login")
    driver.implicitly_wait(8)
    driver.find_element(By.NAME, "departmentName").send_keys("jgadmin")
    driver.find_element(By.NAME, "password").send_keys("123qwe!@#")
    driver.find_element(By.XPATH, "//*[@type='button' and @class='el-button login_btn el-button--primary']").click()
    driver.find_element(By.ID, "path-missionItem").click()
    for i in range(len(search_list)):
        driver.find_element(By.XPATH, "//*[@type='text' and @placeholder='请输入内容']").send_keys(search_list[i])
        driver.find_element(By.XPATH, "//*[text()=' 检索 ' ]/parent::button").click()
        time.sleep(5)
        el = driver.find_element(By.XPATH, '//*[@class="el-table__fixed-right"]//*[@id="table-row_0_column_6"]//*[name('
                                           ')="svg"][2]')
        el.click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@type='text' and @placeholder='请输入内容']").clear()
    driver.quit()


def act_universal_row0_85(search):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://glodon.test.com:32087/bus-center/#/login")
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, "departmentName").send_keys("jgadmin")
    driver.find_element(By.NAME, "password").send_keys("123qwe!@#")
    driver.find_element(By.XPATH, "//*[@type='button' and @class='el-button login_btn el-button--primary']").click()
    driver.find_element(By.ID, "path-missionItem").click()
    driver.find_element(By.XPATH, "//*[@type='text' and @placeholder='请输入内容']").send_keys(search)
    driver.find_element(By.XPATH, "//*[text()=' 检索 ' ]/parent::button").click()
    time.sleep(5)
    el = driver.find_element(By.XPATH, '//*[@class="el-table__fixed-right"]//*[@id="table-row_0_column_6"]//*[name('
                                       ')="svg"][2]')
    el.click()
    time.sleep(2)
    driver.quit()


def act_universal_row1(search):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://10.0.168.47:9000/bus-center/#/login")
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, "departmentName").send_keys("jgadmin")
    driver.find_element(By.NAME, "password").send_keys("123qwe!@#")
    driver.find_element(By.XPATH, "//*[@type='button' and @class='el-button login_btn el-button--primary']").click()
    driver.find_element(By.ID, "path-missionItem").click()
    driver.find_element(By.XPATH, "//*[@type='text' and @placeholder='请输入内容']").send_keys(search)
    driver.find_element(By.XPATH, "//*[text()=' 检索 ' ]/parent::button").click()
    time.sleep(5)
    el = driver.find_element(By.XPATH, '//*[@class="el-table__fixed-right"]//*[@id="table-row_1_column_6"]//*[name('
                                       ')="svg"][2]')
    el.click()
    time.sleep(2)
    driver.quit()


def act_universal_row1_85(search):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://glodon.test.com:32087/bus-center/#/login")
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, "departmentName").send_keys("jgadmin")
    driver.find_element(By.NAME, "password").send_keys("123qwe!@#")
    driver.find_element(By.XPATH, "//*[@type='button' and @class='el-button login_btn el-button--primary']").click()
    driver.find_element(By.ID, "path-missionItem").click()
    driver.find_element(By.XPATH, "//*[@type='text' and @placeholder='请输入内容']").send_keys(search)
    driver.find_element(By.XPATH, "//*[text()=' 检索 ' ]/parent::button").click()
    time.sleep(5)
    el = driver.find_element(By.XPATH, '//*[@class="el-table__fixed-right"]//*[@id="table-row_1_column_6"]//*[name('
                                       ')="svg"][2]')
    el.click()
    time.sleep(2)
    driver.quit()

