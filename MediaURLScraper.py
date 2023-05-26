import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import validators

def validate_url(url):
    if validators.url(url):
        return True
    else:
        return False

def get_media_urls(url):
    options = Options()
    options.add_argument("--headless")
    service = Service('your_chromedriver_path \\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    
    media_elements = driver.find_elements(By.XPATH, "//video[@src] | //audio[@src] | //source[@src]")
    
    media_urls = []
    for element in media_elements:
        src = element.get_attribute("src")
        if src:
            media_urls.append(src)

    driver.quit()
    return media_urls

def export_to_file(file_path, urls):
    with open(file_path, 'a') as file:
        for url in urls:
            file.write(url + '\n')

def main():
    urls = []

    # Get URLs from user input
    while True:
        url = input("Enter URL to scrape (or 'done' to finish): ")
        if url == "done":
            break
        if not validate_url(url):
            print("Invalid URL. Please enter a valid URL.")
            continue
        urls.append(url)

    all_media_urls = []

    for url in urls:
        media_urls = get_media_urls(url)

        if len(media_urls) == 0:
            print(f"No media URLs found for: {url}")
        else:
            print(f"Media URLs found for: {url}")
            for media_url in media_urls:
                print(media_url)
                all_media_urls.append(media_url)
        print()

    if len(all_media_urls) > 0:
        export_to_file('your_desired_file_path/media_urls.txt', all_media_urls)
        print("All media URLs exported to 'media_urls.txt'")
    else:
        print("No media URLs found.")

if __name__ == "__main__":
    main()
