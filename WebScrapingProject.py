import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from time import sleep

def get_page_content(link):
    page_content = requests.get(link)
    soup = BeautifulSoup(page_content.text, "html.parser")
    return soup

def page_analytics(soup):
    fields = ["og:title", "og:description", "og:image"]
    collected_data = {}

    for field in fields:
        for tag in soup.find_all("meta"):
            if tag.get("property") == field:
                collected_data[field] = tag.get("content")
        
    return collected_data

# bw1: đưa tất cả title, description, og:image vào dictionary
def hw1():
    print(f"\n---------------\nHW1: Add swapped data to new dictionary")

    url = "https://kenh14.vn/tiem-banh-ngot-an-kieng-noi-tieng-o-ha-noi-ngung-ban-sau-loat-lum-xum-nhan-vien-noi-dang-bao-tri-20230326170559079.chn"
    soup = get_page_content(url)
    collected_data = page_analytics(soup)

    for key, value in collected_data.items():
        print(f"\n- {key}: {value}")
    
    sleep(1)

# bw2: lấy toàn bộ link trong 1 chuyên mục trên kenh14
def hw2():
    print(f"\n---------------\nHW2: Collect all article links in a category on Kenh14")

    url = "https://kenh14.vn/musik/au-my.chn"
    print(f"* Category Link: {url}\n")

    soup = get_page_content(url)
    titles = soup.find_all('h3', class_ = "knswli-title")

    links = []
    for link in titles:
        result = link.find('a').attrs["href"]
        links.append(result)

        print(f"{titles.index(link) + 1}: {result}\n")

    sleep(1)

# bw3: lấy toàn bộ các sản phẩm trong 10 trang đầu tiên trong daily discovery Shopee. Lấy title và giá sản phẩm
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
    hw1()
    hw2()
    hw3()

if __name__ == "__main__":
    main()