import requests
from bs4 import BeautifulSoup


url = "https://kenh14.vn/tiem-banh-ngot-an-kieng-noi-tieng-o-ha-noi-ngung-ban-sau-loat-lum-xum-nhan-vien-noi-dang-bao-tri-20230326170559079.chn"

# http request method
# - GET: lấy thông tin từ server
# - POST: đẩy thông tin lên server nếu được phép


def get_page_content(link):
    page_content = requests.get(link)
    soup = BeautifulSoup(page_content.text, "html.parser")
    return soup


# output: lấy đơcj title của bài báo này riêng
# lấy được sapo (description) riêng


def get_page_title(soup):
    page_title = soup.find_all("title")
    print(page_title)


def get_page_something(soup):
    page_something = soup.find("meta", attrs={"property": "og:image"})
    print(page_something)


def main():
    soup = get_page_content(url)
    get_page_something(soup)


if __name__ == "__main__":
    main()


# bw1: đưa tất cả title, description, og:image vào dictionary
# bw2: lấy toàn bộ link trong 1 chuyên mục trên kenh14
# bw3: lấy toàn bộ các sản phẩm trong 10 trang đầu tiên trong daily discovery Shopee. Lấy title và giá sản phẩm
