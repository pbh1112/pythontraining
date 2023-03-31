from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

def hw3():
    print(f"\n---------------\nHW1: Add swapped data to new dictionary\n")

    nums = int(input("* Number of page to crawl: "))
    for num in range(1,nums + 1):

        # build shopee url
        url = (f"https://shopee.vn/daily_discover?pageNumber={str(num)}")
        print(f"\n----------\nPage {num}: {url}")

        # open chrome browser by webdriver
        driver = webdriver.Chrome()
        driver.get(url)
        sleep(5)

        # load page source into the program
        page_source = BeautifulSoup(driver.page_source, "html.parser")
            
        # get all products in this "Daily Discover" page
        parents_tags = page_source.find_all("div", class_ = 'tIJtcv row')

        for result in parents_tags: 
            name_result = result.find_all("div", class_ = "ie3A+n Cve6sh")
            price_result = result.find_all("span", class_ = "juCMSo")
            solds_result = result.find_all("div", class_ = "r6HknA dQAXj1")

        list_product_names = []
        list_product_price = []
        list_product_solds = []

        for item in range(len(name_result)):
            # extract text in div . tag
            name_item = name_result[item].text
            price_item = price_result[item].text
            solds_item = solds_result[item].text
                
            list_product_names.append(name_item)
            list_product_price.append(price_item)
            list_product_solds.append(solds_item)
            item = item + 1
            
        df = pd.DataFrame()
        df["name"] = list_product_names
        df["price"] = list_product_price
        df["solds"] = list_product_solds
        print(df)

        num += 1        

def main():
    hw3()

if __name__ == "__main__":
    main()

