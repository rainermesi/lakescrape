from selenium import webdriver
from selenium.webdriver.common.keys import Keys #?
from selenium.webdriver.support.ui import Select #helps select dropdown menus
from bs4 import BeautifulSoup #?
import re #regex
import pandas as pd
import os #interact with OS

#create empty list to store dictionaries   
data_list = []
#create empty dictionary for reference
dict2 = {
    'Veekogu nimetus':[],
    'Registrikood':[],
    'Asukoht':[],
    'Keskpunkti koordinaadid X':[],
    'Keskpunkti koordinaadid Y':[],
    'Ristkoordinaat N':[],
    'Ristkoordinaat E':[],
    'Veepeegli pindala':[],
    'Pikkus, km':[],
    'Saarte pindala':[],
    'Laius':[],
    'Pindala kokku':[],
    'Maht, tuh m³':[],
    'Keskmine sügavus':[],
    'Kaldajoone pikkus':[],
    'Suurim sügavus':[],
    'Avalik kasutatavus':[],
    }

#record homepage url
url = "http://register.keskkonnainfo.ee/envreg/main#HTTPeT7IfPPf3c1F9ZVUDvmJmpWOpsXzwW"

# create a new Chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)

#select and click 'veekogud' from homepage
veekogud = driver.find_element_by_xpath('//*[@id="front-col1"]/div/div/div[3]/ul[1]/li[6]/b/a') #veekogud
veekogud.click() #click veekogud link
# find the dropdown menu
select = Select(driver.find_element_by_id('m.f0.menu.f0.selected.f0.selected.f0.list.form.tyypSelect'))
# select the dropdown element
select.select_by_visible_text('Looduslik järv')
#select and click 'otsi' button
otsi = driver.find_element_by_id('m.f0.menu.f0.selected.f0.selected.f0.list.form.filter') #otsi
otsi.click() #click otsi
#select and click 'kuva' kõik
kuva = driver.find_element_by_xpath('//*[@id="body2-col2"]/div[2]/p[1]/a[13]')
kuva.click() #click kuva

#set counter to use with while loop & with link selector
#2 is the table index for the first entry 1536 is the index for the last+1 entry
countx = 2

while countx <= 1536:
    #reload an empty dictionary on each loop
    dict2 = {
        'Veekogu nimetus':[],
        'Registrikood':[],
        'Asukoht':[],
        'Keskpunkti koordinaadid X':[],
        'Keskpunkti koordinaadid Y':[],
        'Ristkoordinaat N':[],
        'Ristkoordinaat E':[],
        'Veepeegli pindala':[],
        'Pikkus, km':[],
        'Saarte pindala':[],
        'Laius':[],
        'Pindala kokku':[],
        'Maht, tuh m³':[],
        'Keskmine sügavus':[],
        'Kaldajoone pikkus':[],
        'Suurim sügavus':[],
        'Avalik kasutatavus':[],
        }
    #select and click new table row each loop
    driver.find_element_by_xpath('//*[@id="body2-col2"]/table[2]/tbody/tr['+str(countx)+']/td[1]/a').click()
    #sub-page xpaths remain the same. write text into dictionary every loop.
    dict2['Veekogu nimetus'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/div[2]/div[1]/table/tbody/tr[1]/td[1]/div').get_attribute('innerText')
    dict2['Registrikood'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/div[2]/div[1]/table/tbody/tr[3]/td[1]/div').get_attribute('innerText')
    dict2['Asukoht'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/div[2]/div[1]/table/tbody/tr[5]/td/div').get_attribute('innerText')
    dict2['Keskpunkti koordinaadid X'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/table[1]/tbody/tr/td/div/table/tbody/tr[2]/td[2]').get_attribute('innerText')
    dict2['Keskpunkti koordinaadid Y'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/table[1]/tbody/tr/td/div/table/tbody/tr[3]/td[2]').get_attribute('innerText')
    dict2['Ristkoordinaat N'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/table[1]/tbody/tr/td/div/table/tbody/tr[2]/td[3]').get_attribute('innerText')
    dict2['Ristkoordinaat E'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/table[1]/tbody/tr/td/div/table/tbody/tr[3]/td[3]').get_attribute('innerText')
    dict2['Veepeegli pindala'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/table[3]/tbody/tr[1]/td[1]/div').get_attribute('innerText')
    dict2['Pikkus, km'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/table[3]/tbody/tr[1]/td[2]/div').get_attribute('innerText')
    dict2['Saarte pindala'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/table[3]/tbody/tr[2]/td[1]/div').get_attribute('innerText')
    dict2['Laius'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/table[3]/tbody/tr[2]/td[2]/div').get_attribute('innerText')
    dict2['Pindala kokku'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/table[3]/tbody/tr[3]/td[1]/div').get_attribute('innerText')
    dict2['Maht, tuh m³'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/table[3]/tbody/tr[3]/td[2]/div').get_attribute('innerText')
    dict2['Keskmine sügavus'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/table[3]/tbody/tr[4]/td[1]/div').get_attribute('innerText')
    dict2['Kaldajoone pikkus'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/table[3]/tbody/tr[4]/td[2]/div').get_attribute('innerText')
    dict2['Suurim sügavus'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/table[3]/tbody/tr[5]/td[1]/div').get_attribute('innerText')
    dict2['Avalik kasutatavus'] = driver.find_element_by_xpath('//*[@id="body2-col2"]/table[6]/tbody/tr/td[1]/div').get_attribute('innerText')
    data_list.append(dict2) #append dictionary to master list
    countx += 1 #add to count
    driver.back() #go back and start again
    

df = pd.DataFrame(data_list) # transform created list into a dataframe with pandas

#format column names - remove spaces, sentence case, special characters, strip whitespace
df.columns = df.columns.str.lower().str.replace(' ','_').str.replace('m³','m3').str.replace('ü','u').str.strip()

# add metric unit to col names
df.columns = df.columns.str.replace('_pikkus','_pikkus_m')
df.columns = df.columns.str.replace('_sugavus','_sugavus_m')
df.columns = df.columns.str.replace('laius','laius_m')
df.columns = df.columns.str.replace('pindala_kokku','pindala_kokku_ha')
df.columns = df.columns.str.replace('saarte_pindala','saarte_pindala_ha')
df.columns = df.columns.str.replace('_suurim_sugavus','_suurim_sugavus_m')
df.columns = df.columns.str.replace('veepeegli_pindala','veepeegli_pindala_ha')

# remove NaN and fix broken values, cast cols from str into numeric
# '\xa0' is unicode for non-space separator. 
#This was a 'thousand separator' from scraped HTML content. Pandas recognized it as a space and would not allow casting into numeric. 
df.kaldajoone_pikkus_m = df.kaldajoone_pikkus_m.str.replace(u'\xa0', u'').astype('float64')
df.keskmine_sugavus_m = df.keskmine_sugavus_m.str.replace(u'\xa0', u'').str.replace(',','.').astype('float64')
df.laius_m = df.laius_m.str.replace(u'\xa0', u'').str.replace(',','.').astype('float64')
df.pikkus_m = df.pikkus_m.str.replace(u'\xa0', u'').str.replace(',','.').astype('float64')
df.pindala_kokku_ha = df.pindala_kokku_ha.str.replace(u'\xa0', u'').str.replace(',','.').astype('float64')
df.maht_tuh_m3 = df.maht_tuh_m3.str.replace(u'\xa0', u'').str.replace(',','.').astype('float64')
df.saarte_pindala_ha = df.saarte_pindala_ha.str.replace(u'\xa0', u'').str.replace(',','.').astype('float64')
df.suurim_sugavus_m = df.suurim_sugavus_m.str.replace(u'\xa0', u'').str.replace(',','.').astype('float64')
df.veepeegli_pindala_ha = df.veepeegli_pindala_ha.str.replace(u'\xa0', u'').str.replace(',','.').astype('float64')

#convert degrees minutes seconds to lat lon coordinates

tempdf['testx'] = (tempdf.ristkoordinaat_e.str.extract('([^°]*)').replace('','0').fillna('0').astype('int16')
                      +
                      (tempdf.ristkoordinaat_e.str.extract("(?<=°)(.*?)(?=')").fillna('0').astype('int16')/60)
                      +
                      (tempdf.ristkoordinaat_e.str.extract("(?<=')(.*?)(?=\")").fillna('0').astype('int16')/3600))

# write file to disc
df.to_csv('est_lakes.csv', sep=';')

##################################################################################################

#I had trouble with the Lat/Lon conversion at first, so I wrote it out. Leaving it here as well.

# #fill nan values and replace blank values

# df['degrees_e'] = df.ristkoordinaat_e.str.extract('([^°]*)').fillna('0').replace('','0')
# df['minutes_e'] = df.ristkoordinaat_e.str.extract("(?<=°)(.*?)(?=')").fillna('0')
# df['seconds_e'] = df.ristkoordinaat_e.str.extract("(?<=')(.*?)(?=\")").fillna('0')

# df['degrees_n'] = df.ristkoordinaat_n.str.extract('([^°]*)').fillna('0').replace('','0')
# df['minutes_n'] = df.ristkoordinaat_n.str.extract("(?<=°)(.*?)(?=')").fillna('0')
# df['seconds_n'] = df.ristkoordinaat_n.str.extract("(?<=')(.*?)(?=\")").fillna('0')

# #cast str into int

# df.degrees_e = df.degrees_e.astype('int64')
# df.minutes_e = df.minutes_e.astype('int64')
# df.seconds_e = df.seconds_e.astype('int64')

# df.degrees_n = df.degrees_n.astype('int64')
# df.minutes_n = df.minutes_n.astype('int64')
# df.seconds_n = df.seconds_n.astype('int64')

# #convert degrees, minutes, seconds into lat lon coordinates

# df['Longitude'] = (df.degrees_e +
#                        (df.minutes_e/60)+
#                        (df.seconds_e/3600))

 
# df['Latitude'] = (df.degrees_n +
#                        (df.minutes_n/60)+
#                        (df.seconds_n/3600))
