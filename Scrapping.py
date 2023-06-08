from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/Keerthi/Desktop/c127/pro127/chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

scarped_data = []
def scrape():
               
        # BeautifulSoup Object     
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # VERY IMP: The class "wikitable" and <tr> data is at the time of creation of this code. 
        # This may be updated in future as page is maintained by Wikipedia. 
        # Understand the page structure as discussed in the class & perform Web Scraping from scratch.

        # Find <table>
       
        
        # Find <tbody>
        

        # Find <tr>
        

        # Get data from <td>
        for row in table_rows:
            table_cols = row.find_all('td')
            # print(table_cols)
            
            temp_list = []

            for col_data in table_cols:
                # Print Only colums textual data using ".text" property
                # print(col_data.text)

                # Remove Extra white spaces using strip() method
                data = col_data.text.strip()
                # print(data)

                temp_list.append(data)

            # Append data to star_data list
            scarped_data.append(temp_list)


       
# Calling Method    
scrape()

################################################################

# IMPORT DATA to CSV




# Define Header


# Define pandas DataFrame   


#Convert to CSV
