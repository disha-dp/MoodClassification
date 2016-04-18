import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pickle

class songlinks:
    def __init__(self, songlink, categories):
        self.songlink = songlink
        self.categories = categories
    def addImage(self, lyricImage):
        self.lyricImage = lyricImage
    def getImage(self):
        return self.lyricImage

def main():
    '''
    browser = webdriver.Firefox()
    browser.get('http://www.hindigeetmala.net/movie/2016.php')
    try:
        tbl = browser.find_element_by_xpath('.//table[@class="b1 w760 alcen"]')
        rows = tbl.find_elements_by_tag_name('tr')
        movielinks=[]
        allSongLinks = []
        for i in range(0,len(rows)-1):
            if i != 1 and i!= 2:
                tds = (rows[i].find_elements_by_tag_name('td'))
                if i == 0:
                    movielinks.append(tds[0].find_element_by_css_selector('a').get_attribute('href'))
                    movielinks.append(tds[1].find_element_by_css_selector('a').get_attribute('href'))
                # else:
                #     for j in range(0, len(tds)):
                #         movielinks.append(tds[j].find_element_by_css_selector('a').get_attribute('href'))

        for eachmovie in movielinks:
            browser1 = webdriver.Firefox()
            browser1.get(eachmovie)
            movietbl = browser1.find_elements_by_xpath('.//table[@class="b1 w760 pad2 allef"]')
            movierows = movietbl[0].find_elements_by_tag_name('tr')
            link = (movierows[0].find_elements_by_tag_name('td')[0].find_element_by_css_selector('a').get_attribute('href'))
            category = movierows[0].find_elements_by_tag_name('td')[5].text
            allSongLinks.append(songlinks(link,category))
            movierows1 = movietbl[1].find_elements_by_tag_name('tr')
            for i in range(0,len(movierows1)):
                link=(movierows1[i].find_elements_by_tag_name('td')[0].find_element_by_css_selector('a').get_attribute('href'))
                category = movierows1[i].find_elements_by_tag_name('td')[0].text
                allSongLinks.append(songlinks(link,category))
            browser1.close()
        browser.close()
        for eachObject in allSongLinks:
            browser = webdriver.Firefox()
            browser.get(eachObject.songlink)
            lyricImg = browser.find_element_by_xpath('.//div[@class="song"]/span/img').get_attribute('src')
            eachObject.addImage(lyricImg)
            browser.close()
            break

'''
    if(1):
        browser2 = webdriver.Firefox()
        browser2.get('https://www.newocr.com/')
        #for eachObject in allSongLinks:
        if(1):
            inpt = browser2.find_element_by_xpath(".//div[@class='input-prepend']")
            print("test")
           #inpt.find_element_by_tag_name("input").send_keys(eachObject.getImage())
            inpt.find_element_by_tag_name("input").send_keys('http://www.hindigeetmala.net/lyrics_png/73159_kar_gayi_chull.png')
            print("test2")
            browser2.find_element_by_id("preview").click()
            lang = browser2.find_element_by_xpath(".//div[@class='chosen-container chosen-container-multi']/ul/li")
            lang.find_element_by_class_name("search-choice-close").click()
            lang = browser2.find_element_by_xpath(".//div[@class='chosen-container chosen-container-multi']/ul/li")
            lang.find_element_by_tag_name("input").click()
            lang.find_element_by_tag_name("input").send_keys("Hindi")
            lang.find_element_by_tag_name("input").send_keys(Keys.ENTER)
            browser2.find_element_by_xpath(".//*[contains(text(), 'Page layout analysis - split multi-column text into columns')]").click()
            div = browser2.find_element_by_xpath('/html/body/div[3]')
            actions.move_to_element(div)
            actions.move_by_offset(119, 0)
            actions.click_and_hold(on_element=None)
            actions.move_by_offset(350, 0)
            actions.release(on_element=None)
            actions.perform()
            #actions.drag_and_drop_by_offset(div, 50, 50)
            #actions.perform()
    #except:
    #    print('In Exception !!')

if __name__ == "__main__":
    main()

