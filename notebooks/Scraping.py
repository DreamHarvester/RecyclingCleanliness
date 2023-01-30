

import pandas as pd

urls = pd.read_csv(r"C:\Users\z_wil\Documents\TACO\data\all_image_urls.csv", header = 0, names = ['jpg', 'png'])

urls2 = [n for n in urls['jpg']]

import urllib.request

destinationPath = "C:/Users/z_wil/Documents/TACO Data/"

#urllib.request.urlretrieve(urls2[0], "C:/Users/z_wil/Documents/TACO Data/picture1.jpg")

num = 0
for url in urls2[:4492]:
    filename = destinationPath+"picture"+str(num)+".jpg"
    try:
        urllib.request.urlretrieve(url,filename)
    except ValueError:
        pass
    except TypeError:
        print("TypeError")
        pass
    num += 1















from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# What you enter here will be searched for in
# Google Images
query = "dirty plastic bottle"

# Creating a webdriver instance
driver = webdriver.Chrome(r"C:\Users\z_wil\Documents\chromedriver_win32\chromedriver.exe")

# Maximize the screen
driver.maximize_window()

# Open Google Images in the browser
driver.get('https://images.google.com/')

# Finding the search box
box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

# Type the search query in the search box
box.send_keys(query)

# Pressing enter
box.send_keys(Keys.ENTER)


download_path = r"C:\Users\z_wil\Documents\Recycling Clean\Google Images"

# Function for scrolling to the bottom of Google
# Images results
def scroll_to_bottom():

	last_height = driver.execute_script('\
	return document.body.scrollHeight')

	while True:
		driver.execute_script('\
		window.scrollTo(0,document.body.scrollHeight)')

		# waiting for the results to load
		# Increase the sleep time if your internet is slow
		time.sleep(3)

		new_height = driver.execute_script('\
		return document.body.scrollHeight')

		# click on "Show more results" (if exists)
		try:
			driver.find_element(By.CSS_SELECTOR, ".YstHxe input").click()

			# waiting for the results to load
			# Increase the sleep time if your internet is slow
			time.sleep(3)

		except:
			pass

		# checking if we have reached the bottom of the page
		if new_height == last_height:
			break

		last_height = new_height


# Calling the function

# NOTE: If you only want to capture a few images,
# there is no need to use the scroll_to_bottom() function.
scroll_to_bottom()

suffix = "gs"

# Loop to capture and save each image
for i in range(1, 500):

	# range(1, 50) will capture images 1 to 49 of the search results
	# You can change the range as per your need.
	try:

        #'//*[@id="islrg"]/div[1]/div[' +
	# XPath of each image
		img = driver.find_element(By.XPATH,
            '//*[@id="islrg"]/div[1]/div[' +
		str(i) + ']/a[1]/div[1]/img')

		# Enter the location of folder in which
		# the images will be saved
		img.screenshot(download_path + "\\" +
					suffix + '(' + str(i) + ').png')
		# Each new screenshot will automatically
		# have its name updated

		# Just to avoid unwanted errors
		time.sleep(0.2)

	except:
		
		# if we can't find the XPath of an image,
		# we skip to the next image
		continue

# Finally, we close the driver
driver.close()










