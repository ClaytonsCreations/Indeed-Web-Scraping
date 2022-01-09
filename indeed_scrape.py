from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    jobs = {}

    url = "https://www.indeed.com/jobs?as_and&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l=Catalina%20Island%2C%20CA&fromage=any&limit=10&sort&psf=advsrch&from=advancedsearch&vjk=cb501a684babcc31"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    jobs["Job_Title"] = soup.find("h2", class_="jobTitle").get_text()
    jobs["Company_Name"] = soup.find("span", class_="companyName").get_text()
    jobs["Job_Location"] = soup.find("div", class_="companyLocation").get_text()
    jobs["Job_Pay"] = soup.find("div", class_="attribute-snippet").get_text()
    jobs["Job_Type"] = soup.find("div", class_="metadata").get_text()

    # Quit the browser
    browser.quit()

    return jobs
