import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import pickle

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

def main():

    browser = webdriver.Firefox()
    browser.get('http://www.hindigeetmala.net/movie/2016.php')
    try:
        '''
        Getting List of all Movies, first page
        '''
        tbl = browser.find_element_by_xpath('.//table[@class="b1 w760 alcen"]')
        rows = tbl.find_elements_by_tag_name('tr')
        movielinks=[]
        allSongLinks = []
        for i in range(0,1): #len(rows)-1):
            try:
                if i != 1 and i!= 2:
                    tds = (rows[i].find_elements_by_tag_name('td'))
                    if i == 0:
                        movielinks.append(tds[0].find_element_by_css_selector('a').get_attribute('href'))
                        movielinks.append(tds[1].find_element_by_css_selector('a').get_attribute('href'))
                    ##else:
                    #    for j in range(0, len(tds)):
                    #        movielinks.append(tds[j].find_element_by_css_selector('a').get_attribute('href'))
                else:
                    continue
            except:
                break
        '''
        #Getting List of all songs from each movie
        '''
        for eachmovie in movielinks:
            try:
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
                    if movierows1[i].find_elements_by_tag_name('td')[5].text == '':
                        category = "No Category"
                    else:
                        category = movierows1[i].find_elements_by_tag_name('td')[5].text

                    #print(link)
                    allSongLinks.append(songlinks(link,category))
                browser1.close()
            except:
                continue
        
        browser.close()
        '''
        Get lyric PNG from each song
        '''
        songdict={}
        for eachObject in allSongLinks:
            #print(eachObject.songlink + " " + eachObject.categories + "\n")
            try:
                browser = webdriver.Firefox()
                browser.get(eachObject.songlink)
                lyricImg = browser.find_element_by_xpath('.//div[@class="song"]/span/img').get_attribute('src')
                eachObject.addImage(lyricImg)
                browser.close()

                # break
            except:
                print("ImaggeBreak")
                browser.close()
                continue


        # browser2 = webdriver.Firefox()
        # browser2.get('https://www.newocr.com/')
        #print ("test")
        '''
        Using OCR on each lyric PNG
        '''
        for eachObject in allSongLinks:
        # if(1):
            try:
                browser2 = webdriver.Firefox()
                browser2.get('https://www.newocr.com/')
                browser3 = webdriver.Firefox()
                #browser3.get('http://www.hindigeetmala.net/lyrics_png/73159_kar_gayi_chull.png')
                browser3.get(eachObject.getImage())
                print(eachObject.getImage())
                img = browser3.find_element_by_tag_name("img")
                loc1 = img.location
                size1 = img.size
                print("test1")

                browser3.save_screenshot('img.png')
                img2 = Image.open('img.png')
                left = loc1['x']
                top = loc1['y']
                right = loc1['x'] + size1['width']
                bottom1 = loc1['y'] + size1['height']
                img2 = img2.crop((left + (size1['width'] / 2), top, right, bottom1))
                img2.save('img.png')
                browser3.quit()
                print("test2")
                # browser3.close()

                browser2.find_element_by_css_selector('input[type="file"]').clear()
                browser2.find_element_by_css_selector('input[type="file"]').send_keys('img.png')
                browser2.find_element_by_css_selector('input[type="file"]').submit()
                print("test3")

                # inpt = browser2.find_element_by_xpath(".//div[@class='input-prepend']")

               #inpt.find_element_by_tag_name("input").send_keys(eachObject.getImage())
                # inpt.find_element_by_tag_name("input").send_keys('http://www.hindigeetmala.net/lyrics_png/73159_kar_gayi_chull.png')

                # browser2.find_element_by_id("preview").click()

                action = webdriver.ActionChains(browser2)
                action.move_to_element(browser2.find_element_by_id('preview'))
                action.perform()
                print("test4")

                lang = browser2.find_element_by_xpath(".//div[@class='chosen-container chosen-container-multi']/ul/li")
                lang.find_element_by_class_name("search-choice-close").click()
                lang = browser2.find_element_by_xpath(".//div[@class='chosen-container chosen-container-multi']/ul/li")
                lang.find_element_by_tag_name("input").click()
                print("test4.5")
                lang.find_element_by_tag_name("input").send_keys("Hindi")
                lang.find_element_by_tag_name("input").send_keys(Keys.ENTER)
                browser2.find_element_by_xpath(".//*[contains(text(), 'Page layout analysis - split multi-column text into columns')]").click()
                browser2.find_element_by_id("ocr").click()
                print("test5")
                text = browser2.find_element_by_id("ocr-result").text
                eachObject.addText(text)
                songdict[text] = eachObject.getCategory()
                print(text + "  "+ eachObject.getCategory())
                browser2.close()
            except:
                print("testBreak")
                #print(eachObject.getImage())
                #browser2.close()
                #browser3.close()
                break

        output = open('finalsong2016.txt','w',encoding="utf8")
        output.write(str(songdict))

    except:
        #browser.close()
        print('In Exception !!')


if __name__ == "__main__":
    main()
