#Author: Sruti Sahani
# Deep Learning for Hindi Mood Classification
# April 2, 2016
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
import pickle

###
# Class contains setter and getter of all song (Link of song, link of lyrics image and category)
###

class songlinks:
    def __init__(self, songlink, categories):
        self.songlink = songlink
        self.categories = categories
    def addImage(self, lyricImage):
        self.lyricImage = lyricImage
    def getImage(self):
        return self.lyricImage
    def addText(self, text):
        self.text = text
    def getText(self):
        return self.text
    def getCategory(self):
        return self.categories
    def getLink(self):
        return self.songlink

def main():

    ###
    # Traverses year-wise and fetches song data and sets it to the song object
    ###

    browser = webdriver.PhantomJS(executable_path=r'C:\Python34\phantomjs-2.1.1-windows\bin\phantomjs.exe')#Firefox()
    # browser = webdriver.Firefox()
    browser.get('http://www.hindigeetmala.net/movie/2013.php')
    output = open('finalsong2013.txt', 'w', encoding="utf8")
    try:
        tbl = browser.find_element_by_xpath('.//table[@class="b1 w760 alcen"]')
        rows = tbl.find_elements_by_tag_name('tr')
        movielinks=[]
        allSongLinks = []
        for i in range(0,len(rows)-1):
            try:
                if i != 1 and i!= 2:
                    tds = (rows[i].find_elements_by_tag_name('td'))
                    if i == 0:
                        movielinks.append(tds[0].find_element_by_css_selector('a').get_attribute('href'))
                        movielinks.append(tds[1].find_element_by_css_selector('a').get_attribute('href'))
                    else:
                        for j in range(0, len(tds)):
                            movielinks.append(tds[j].find_element_by_css_selector('a').get_attribute('href'))
            except:
                continue

        ###
        # for each movie gets all the song links and respective category
        ###

        for eachmovie in movielinks:
            try:
                browser1 = webdriver.PhantomJS(
                    executable_path=r'C:\Python34\phantomjs-2.1.1-windows\bin\phantomjs.exe')  # Firefox()
                # browser1 = webdriver.Firefox()
                browser1.get(eachmovie)
                movietbl = browser1.find_elements_by_xpath('.//table[@class="b1 w760 pad2 allef"]')
                movierows = movietbl[0].find_elements_by_tag_name('tr')
                link = (movierows[0].find_elements_by_tag_name('td')[0].find_element_by_css_selector('a').get_attribute('href'))
                category = movierows[0].find_elements_by_tag_name('td')[5].text
                allSongLinks.append(songlinks(link,category))
                movierows1 = movietbl[1].find_elements_by_tag_name('tr')
                for i in range(0,len(movierows1)):
                    link=(movierows1[i].find_elements_by_tag_name('td')[0].find_element_by_css_selector('a').get_attribute('href'))
                    category = movierows1[i].find_elements_by_tag_name('td')[5].text
                    allSongLinks.append(songlinks(link,category))
                browser1.close()
            except:
                continue
        browser.close()
        songdict={}
        print ("Song length is %d" % len(allSongLinks))

        ###
        # After getting all the song links, traverses through each of them to get the lyrics image link
        ###

        for eachObject in allSongLinks:
            # print(eachObject.songlink + " " + eachObject.categories + "\n")
            try:
                browser = webdriver.PhantomJS(executable_path=r'C:\Python34\phantomjs-2.1.1-windows\bin\phantomjs.exe')#Firefox()
                # browser = webdriver.Firefox()
                browser.get(eachObject.songlink)
                if browser.find_element_by_xpath('.//div[@class="song"]/span/img').get_attribute('src') != '':
                    lyricImg = browser.find_element_by_xpath('.//div[@class="song"]/span/img').get_attribute('src')
                    eachObject.addImage(lyricImg)
                else:
                    eachObject.addImage("No Image")
                browser.close()

                # break
            except:
                print("ImaggeBreak")
                # if eachObject.getImage() == '':
                eachObject.addImage("No Image")
                browser.close()
                continue

        ###
        # Traverses through all song objects again to use OCR and the text representation of each song
        ###

        for eachObject in allSongLinks:
        # if(1):
            try:
                browser2 = webdriver.PhantomJS(executable_path=r'C:\Python34\phantomjs-2.1.1-windows\bin\phantomjs.exe')#Firefox()
                # browser2 = webdriver.Firefox()
                browser2.get('https://www.newocr.com/')
                # browser3.get('http://www.hindigeetmala.net/lyrics_png/73159_kar_gayi_chull.png')
                # print(eachObject.getImage())
                if eachObject.getImage()!='No Image':
                    browser3 = webdriver.PhantomJS(executable_path=r'C:\Python34\phantomjs-2.1.1-windows\bin\phantomjs.exe')#Firefox()
                    # browser3 = webdriver.Firefox()
                    browser3.get(eachObject.getImage())
                    # print(eachObject.getImage())
                    img = browser3.find_element_by_tag_name("img")
                    loc1 = img.location
                    size1 = img.size
                    browser3.save_screenshot('C:\\Users\\LENOVO\\Desktop\\img.png')
                    img2 = Image.open('C:\\Users\\LENOVO\\Desktop\\img.png')
                    left = loc1['x']
                    top = loc1['y']
                    right = loc1['x'] + size1['width']
                    bottom1 = loc1['y'] + size1['height']

                    ###
                    # Crops the image
                    ###

                    img2 = img2.crop((left + (size1['width'] / 2), top, right, bottom1))
                    img2.save('C:\\Users\\LENOVO\\Desktop\\img.png')
                    browser3.quit()
                    # browser3.close()

                    ###
                    # Uploads the image
                    ###

                    browser2.find_element_by_css_selector('input[type="file"]').clear()
                    browser2.find_element_by_css_selector('input[type="file"]').send_keys('C:\\Users\\LENOVO\\Desktop\\img.png')
                    browser2.find_element_by_css_selector('input[type="file"]').submit()

                    action = webdriver.ActionChains(browser2)
                    action.move_to_element(browser2.find_element_by_id('preview'))
                    action.perform()

                    lang = browser2.find_element_by_xpath(".//div[@class='chosen-container chosen-container-multi']/ul/li")
                    lang.find_element_by_class_name("search-choice-close").click()
                    lang = browser2.find_element_by_xpath(".//div[@class='chosen-container chosen-container-multi']/ul/li")
                    lang.find_element_by_tag_name("input").click()
                    lang.find_element_by_tag_name("input").send_keys("Hindi")
                    lang.find_element_by_tag_name("input").send_keys(Keys.ENTER)
                    browser2.find_element_by_xpath(".//*[contains(text(), 'Page layout analysis - split multi-column text into columns')]").click()
                    browser2.find_element_by_id("ocr").click()
                    element = WebDriverWait(browser2, 10).until(
                        EC.presence_of_element_located((By.ID, "ocr-result"))
                    )
                    text = browser2.find_element_by_id("ocr-result").text
                    eachObject.addText(text)

                    ###
                    # Appending each songs with their categories into a dictionary
                    ###

                    songdict[text] = eachObject.getCategory()
                    # print(text + "  "+ eachObject.getCategory())
                    browser2.close()
                else:
                    print("In Else")
                    browser2.close()
                    continue
            except:
                print("Last No Image")
                continue

        ###
        # Writing the dictionary into a file
        ###

        print("SongDict Length:%d" % len(songdict))
        output.write(str(songdict))

    except:
       print('In Exception !!')


if __name__ == "__main__":
    main()
