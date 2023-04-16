from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep


def number_of_processed_page():
    nums = int(input("* Number of page to crawl: "))
    return nums


def build_shopee_url(num):
    # build shopee url
    url = f"https://shopee.vn/daily_discover?pageNumber={str(num)}"
    print("-" * 10)
    print(f"Page {num}: {url}")

    return url


def get_page_source(url):
    # open chrome browser by webdriver
    driver = webdriver.Chrome()
    driver.get(url)
    sleep(3)

    # load page source into the program
    page_source = BeautifulSoup(driver.page_source, "html.parser")

    return page_source


def get_product_info(page_source):
    # get all products in this "Daily Discover" page
    parents_tags = page_source.find_all("div", class_="tIJtcv row")

    # get all information of all products
    for result in parents_tags:
        all_name_result = result.find_all("div", class_="ie3A+n Cve6sh")
        all_price_result = result.find_all("span", class_="juCMSo")
        all_solds_result = result.find_all("div", class_="r6HknA dQAXj1")

    # create list for each column of data frame
    list_product_name = []
    list_product_price = []
    list_product_solds = []

    # get detailed information of each product
    for item in range(len(all_name_result)):
        # extract text in div . tag
        name_item = all_name_result[item].text
        price_item = all_price_result[item].text
        solds_item = all_solds_result[item].text

        list_product_name.append(name_item)
        list_product_price.append(price_item)
        list_product_solds.append(solds_item)

        item += 1

    # collect data into a returned list
    product_info = []
    product_info.append(list_product_name)
    product_info.append(list_product_price)
    product_info.append(list_product_solds)

    return product_info


def presented_in_data_frame(product_info, num):
    # use pandas method
    df = pd.DataFrame()
    df["name"] = product_info[0]  # list_product_name
    df["price"] = product_info[1]  # list_product_price
    df["solds"] = product_info[2]  # list_product_sold

    # set up path to export file csv
    path = f"/Users/hello/Downloads/export{str(num)}.csv"
    return df.to_csv(path, index=False, header=True)
