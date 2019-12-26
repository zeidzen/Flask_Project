import requests
from bs4 import BeautifulSoup
import database as db
import datetime
import shutil
import summarize

class websites () :
    
    def __init__(self) : 
        #create opject form database class
        self.con = db.DataBase()
        
        #Get WebSites
        sql='Select * from website;'
        self.websites=self.con.Select_Data_More_Row(sql)
        
        #Get Categories
        sql='Select name , Id  from Term Where type=1 ;'
        self.Categories =dict (self.con.Select_Data_More_Row(sql))
        
        #Get tag
        sql='Select name , Id  from Term Where type=0 ;'
        self.tags =dict (self.con.Select_Data_More_Row(sql))
        
        #create object from  summarize
        self.summary=summarize.extraction('arabic')
        
    def download_image(self ,url ,Id):
        #get Image 
            request = requests.get( url , stream=True)
            if request.status_code == 200:
                name_image = "image/"+str(Id)+'.jpeg'
                with open(name_image, 'wb') as f:
                    request.raw.decode_content = True
                    shutil.copyfileobj(request.raw, f)
                    return name_image
        



class aljazeera (websites):
    
    def __init__(self) : 
        super().__init__()
                    
        
    def get_urls (self,website:list , Categories:dict) :
        urls=dict()
        #Get URLS From  Website
        sql ='select  Source from article where Id_Website ={} ; '.format(website[0])
        Sources = self.con.Select_Data_More_Row(sql)
        Source_list=[]
        for Source in Sources :
            Source_list.append(Source[0])
        for  Categorie ,Id   in Categories.items() : 
            url_page = website [3]+str(Categorie)
            urls_Categorie=[] #List to store url of the website 
            page = requests.get(url_page)
            soup = BeautifulSoup(page.content,'html.parser')
            for Id , a in enumerate (soup.findAll('a',href=True)):
                 url=a['href']
                 if url_page in url : 
                     if url in Source_list : 
                         pass
                     else : urls_Categorie.append(url)
                     
            urls_Categorie= list(dict.fromkeys(urls_Categorie))   
            urls[Categorie]=urls_Categorie
        return urls


    def get_article (self , website_info , Categorie , urls):
            
            data=dict()
            data['Id_Website']=website_info [0]
            data['Id_Categories'] = self.Categories [Categorie]
            
            for  url in urls :         
                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')
                #GET tITLE 
                title= soup.find(class_= website_info[5])
                title=title.get_text()
                #GET url Image                 
                image= soup.findAll('img' ) [2]
                url_image='https://www.aljazeera.net'+image.get("src") 
                if 'jazeraLogo'  in url_image :            
                    image= soup.findAll('img' ) [3]
                    url_image='https://www.aljazeera.net'+image.get("src")
                #get Text
                text=''
                for paragraph in soup.find_all('p') :
                    text =text + paragraph.get_text()
                
                #get tag 
                tag_list=[]
                tag= soup.find(class_='tags')
                for text_tag in tag.find_all('li') :
                    tag_list.append(text_tag.get_text().strip('\n'))
                    
                #Insert Data in  article table
                data['Source'] = url
                data['Title'] = title
                data['Text'] = text
                data['Summary'] = self.summary.extraction_summarize(article = text) 
                data['ReleaseDate'] = str (datetime.datetime.now().date())
                self.con.Insert_Data('article',**data)    
                
                #get ID article
                sql='SELECT max(Id) FROM article GROUP BY id ORDER BY Id DESC;'
                Id_article = self.con.Select_Data_One_Row(sql)
                
                #insert Image in article table 
                name_image = self.download_image(url_image ,int (Id_article[0]))
                self.con.Update_Data_one_Coulmn ('article',Id_article[0] ,'Image',name_image)
                
                #Insert Data in term_relation table               
                term_relation = {'Id_Term' :data['Id_Categories'], 'Id_Article' : Id_article[0]}
                self.con.Insert_Data('term_relation',**term_relation)
                
                #insert Tag in database
                for tag in tag_list : 
                    if tag in self.tags.keys() :
                        term_relation = {'Id_Term' :self.tags[tag], 'Id_Article' : Id_article[0]}
                    else : 
                        term= {'Name_ar' : tag ,'Type' : 2 }
                        self.con.Insert_Data('term',**term)
                        #get ID article
                        sql='SELECT max(Id) FROM term GROUP BY id ORDER BY Id DESC;'
                        Id_term = self.con.Select_Data_One_Row(sql)
                        term_relation = {'Id_Term' :Id_term[0], 'Id_Article' : Id_article[0]}
                    self.con.Insert_Data('term_relation',**term_relation)
                

                
                


    def scrap_last_News_aljazeera (self) : 
        for website in self.websites : 
            urls =self.get_urls(self.websites[0] ,self.Categories)
            for Categorie , url in urls.items() :
                self.get_article (self.websites[0] , Categorie , url)
                
                
                
                
                
                
            
class roya (websites):
    
    def __init__(self) : 
        super().__init__()
        
    def get_urls (self,website:str , Categories:dict) :
        urls=dict()
        #Get URLS From  Website
        sql ='select  Source from article '
        Sources = self.con.Select_Data_More_Row(sql)
        
        for  Categorie ,Id   in Categories.items() : 
            url_page = website+str(Categorie)
            urls_Categorie=[] #List to store url of the website 
            page = requests.get(url_page)
            soup = BeautifulSoup(page.content,'html.parser')
            for Id , a in enumerate (soup.findAll('a',href=True)):
                 url=a['href']
                 if url_page in url : 
                     if url_page in Sources : 
                         pass
                     else : urls_Categorie.append(url)
                     
            urls_Categorie= list(dict.fromkeys(urls_Categorie))   
            urls[Categorie]=urls_Categorie
        return urls
    
       
o1=aljazeera()
x= o1.scrap_last_News_aljazeera ()

