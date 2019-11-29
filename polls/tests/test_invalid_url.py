from selenium import webdriver
import requests


def get_links(url):
    """Find all links on page at the given url.
       Return a list of all link addresses, as strings.
    """
    browser = webdriver.Chrome(
        executable_path='D:/Download/chromedriver_win32/chromedriver.exe')
    browser.get(url)
    elements = browser.find_elements_by_tag_name("a")
    all_links = [elem.get_attribute('href') for elem in elements]
    browser.close()
    return all_links


def invalid_urls(urllist):
    invalid_list = []
    for url in urllist:
        r = requests.head(url)
        if r.status_code == 404:
            invalid_list.append(url)
    return invalid_list


if __name__ == "__main__":
    link_list = get_links("https://cpske.github.io/ISP/")
    for url in link_list:
        print("Valid: " + url)
    print()
    invalid_url = invalid_urls(link_list)
    for inv_url in invalid_url:
        print("Invalid: " + inv_url)
