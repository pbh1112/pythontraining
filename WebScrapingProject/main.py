from extract import (
    number_of_processed_page,
    build_shopee_url,
    get_page_source,
    get_product_info,
    presented_in_data_frame,
)


def main():
    nums = number_of_processed_page()
    for num in range(1, nums + 1):
        url = build_shopee_url(num)
        page_source = get_page_source(url)
        product_info = get_product_info(page_source)
        presented_in_data_frame(product_info, num)
        num += 1
    return


if __name__ == "__main__":
    main()
