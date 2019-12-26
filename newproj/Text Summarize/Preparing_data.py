import bs4 as BeautifulSoup
import urllib.request  

class preparing :
    
    #def __init__(self , url) :
    #    self.url=url
        
    def load_data (self,url) : 
        # Fetching the content from the URL
        fetched_data = urllib.request.urlopen(url)
        article_read = fetched_data.read()
    
        # Parsing the URL content and storing in a variable
        article_parsed = BeautifulSoup.BeautifulSoup(article_read,'html.parser')
        
        # Returning <p> tags
        paragraphs = article_parsed.find_all('p')
        
        article_content = ''
        
        # Looping through the paragraphs and adding them to the variable
        for p in paragraphs:  
            article_content += p.text
            
        return article_content