# Scraping-a-dynamic-website-Practice
Here, I scraped and extracted data from a dynamic website as a practice work using **selenium** and **geckodriver** and later did data analysis using the **pandas** library.

The source of the data was this [website](https://research.com/scientists-rankings/computer-science).

This project aimed to scrape and extract data for data analysis on Computer Science scientists' ranking data and their other relevant information. This analysis was done to get insights into the data like Which school/university/organization has the best scientists, from which country most of them are from, and more.

## Excel File (Data Example):

Excel file link: [File](https://github.com/RezuwanHassan262/Scraping-a-dynamic-website-Practice/blob/main/data/cs_scientist_ranks.xlsx)


| World Rank | National Rank |         Name       |                      Affiliation             |     Country     |    D-Index    | Citations | Number of Publications |                          Image URLs                 |
|------------|---------------|--------------------|----------------------------------------------|-----------------|---------------|-----------|------------------------|-----------------------------------------------------|
|      1     |        1      |  Anil K. Jain      |             Michigan State University        |  United States  |        203    |  250990   |            970         |  https://s.research.com/images/2a967b4499197336...  |
|      2     |        1      |  Yoshua Bengio     |               University of Montreal         |  United States  |        200    |  491250   |            909         |  https://s.research.com/images/aec914cd458a74e2...  |
|      3     |        2      |   Jiawei Han       |  University of Illinois at Urbana-Champaign  |  United States  |        186    |  209445   |            1177        |  https://s.research.com/images/42382fdef4ef0953...  |
|      4     |        3      | Michael I. Jordan  |               University of California       |  United States  |        176    |  220056   |            776         |  https://s.research.com/images/56e4335ff90165e8...  |
|      5     |        1      |  Andrew Zisserman  |               University of Oxford           |  United Kingdom |        175    |  255987   |            698         |  https://s.research.com/images/2a3913cff9795e86...  |


