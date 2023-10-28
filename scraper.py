from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd


columns = ["World Rank", "National Rank", "Name", "Affiliation", "Country", "D-Index", "Citations", "Number of Publications", "Image URLs"]

all_data = []

webdriver_path = "geckodriver"
options = Options()
options.set_preference('profile', webdriver_path)
driver = Firefox(options=options)

def get_contents(row):

    contents = {}
    items = row.text.split('\n')
    aff_and_country = items[3].split(",")

    contents["World Rank"] = items[0]
    contents["National Rank"] = items[1]
    contents["Name"] = items[2]
    contents["Affiliation"] = aff_and_country[0]
    contents["Country"] = aff_and_country[1]
    contents["D-Index"] = items[4]
    contents["Citations"] = items[5]
    contents["Number of Publications"] = items[6]
    contents["Image URLs"] = row.find_element(By.CLASS_NAME, 'lazyload').get_attribute('src')

    return contents



def add_data(url):


    driver.get(url)
    rankings = driver.find_element(By.ID, "rankingItems")
    rows = rankings.find_elements(By.CLASS_NAME, "cols")

    for idx, row in enumerate(rows):
        if idx%4 == 0:
            all_data.append(get_contents(row))

    time.sleep(30)
    #driver.close()

def main():



    for c in range(0,2):

        if c == 0:
            url = "https://research.com/scientists-rankings/computer-science"
            add_data(url)
            c += 1
        else:
            for page_id in range(2,21,1):
                url = f"https://research.com/scientists-rankings/computer-science?page={page_id}"
                add_data(url)


    df = pd.DataFrame(data=all_data, columns=columns)
    print(df)

    


    df.to_csv('cs_scientist_ranks.csv')


    return


if __name__ == "__main__":
    main()
