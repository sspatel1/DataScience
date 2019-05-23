from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time


def init_browser():
    # Set the chromedriver path - for Windows Users
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)



def scrape():

    # Debug flag. Set it to "True" or "False"
    debug = False

    browser = init_browser()


    #####################################################
    #                                                   #
    #                   NASA MARS NEWS                  #
    #                   ===============                 #
    #                                                   #
    #####################################################
    
    # Visit the following URL using splinter.Browser module
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(10)

    # HTML Object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')


    # Retrieve the latest element that contains news title and news_paragraph
    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='article_teaser_body').text

    if debug:
        # Display scrapped data 
        print(news_title)
        print(news_p)

    
    #####################################################
    #                                                   #
    #     JPL Mars Space Images - Featured Image        #
    #     ======================================        #
    #                                                   #
    #####################################################

    # Visit the following URL using splinter.Browser module
    jpl_mars_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_mars_url)
    
    time.sleep(6)

    # HTML Object 
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Scrape the image path from soup
    image_path = soup.find('a', class_='button fancybox')['data-fancybox-href']
    # section = soup.find("section", class_="grid_gallery module grid_view")
    #a = section.find('a', class_='fancybox')
    #image_path = a["data-fancybox-href"]

    # JPL url 
    jpl_url = 'https://www.jpl.nasa.gov'

    # Concatenate jpl_url with scrapped image_path
    featured_image_url = jpl_url + image_path

    if debug:
        # Display url to featured image
        print(featured_image_url)
    


    #####################################################
    #                                                   #
    #                   MARS WEATHER                    #
    #                   ============                    #
    #                                                   #
    #####################################################
    
    # Visit the following URL using splinter.Browser module
    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)

    time.sleep(6)

    # HTML Object 
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Scrape the latest Mars weather
    section = soup.find("div", class_="js-tweet-text-container")
    p = section.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text") 

    # Extract "a" tag from inside the "p" tag
    p.a.extract()
    mars_weather = p.text

    if debug:
        # Print mars weather
        print(mars_weather)



    #####################################################
    #                                                   #
    #                   MARS FACTS                      #
    #                   ==========                      #
    #                                                   #
    #####################################################

    # Mars facts url
    facts_url = "https://space-facts.com/mars/"

    # Use Panda's read_html to read the first table
    mars_facts_df = pd.read_html(facts_url)[0]

    # Name the columns
    mars_facts_df.columns = ["description","value"]

    # Set the index to description
    mars_facts_df.set_index("description", inplace=True)

    # Save df as html
    mars_facts_html = mars_facts_df.to_html(classes='table1')
    #mars_facts_html = mars_facts_html.replace("\n", "")

    if debug:
        # Display mars_df
        print(mars_facts_df)



    #####################################################
    #                                                   #
    #                   MARS HEMISPHERES                #
    #                   ================                #
    #                                                   #
    #####################################################

    # Visit the following URL using splinter.Browser module
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)

    time.sleep(6)

    # HTML Object
    html_hemispheres = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_hemispheres, "html.parser")

    # Scrape information of all the hemispheres
    hemispheres = soup.find_all("div", class_="item")

    # Main url
    main_url = "https://astrogeology.usgs.gov"

    # Empty list 
    hemisphere_image_urls = []


    # Loop through all the hemispheres
    for hemisphere in hemispheres: 
    
        # Scrap relative image path
        image_path = hemisphere.find('a', class_='itemLink product-item')["href"]
    
        # Complete image url
        image_url = main_url + image_path
    
        # Visit a specific hemispehre URL using splinter.Browser module
        browser.visit(image_url)
    
        # HTML Object
        html_full_image = browser.html
    
        # Parse a specific hemisphere information website 
        soup = BeautifulSoup(html_full_image, 'html.parser')
    
        # Scrape relative image path
        image_path = soup.find('img', class_='wide-image')['src']
    
        # Full url 
        image_url = main_url + image_path
    
        # Scrap the title
        title = hemisphere.find('h3').text
    
        # Append title and image url as dictionary 
        hemisphere_image_urls.append({"title" : title, "img_url" : image_url})
     

    
    # Store all the above scraped data in to a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_facts_html": mars_facts_html,
        "hemisphere_image_urls": hemisphere_image_urls 
    }

    # Close the browser after scraping
    browser.quit()

    if debug:
        # Print hemispheree urls and mars data
        print(hemisphere_image_urls)
        print(mars_data)

    if (not debug):
        # Return results if debug is false
        return mars_data
        
    
    
if __name__ == "__main__":
    scrape()
