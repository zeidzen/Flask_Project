#importing libraries
import bs4 as BeautifulSoup
import urllib.request  
#importing libraries
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize ,sent_tokenize
from googletrans import Translator



"""
In this example, we want to summarize the information found on this Wikipedia article,
which just gives an overview of the major happenings during the 20th century.
To enable us to fetch the article’s text, we’ll use the Beautiful Soup library.
"""
#
#url = 'https://ar.wikipedia.org/wiki/%D8%A8%D8%A7%D9%8A%D8%AB%D9%88%D9%86' 
url = 'https://www.aljazeera.net/news/politics/2019/12/26/%D8%AA%D8%B1%D9%83%D9%8A%D8%A7-%D8%B1%D9%88%D8%B3%D9%8A%D8%A7-%D9%85%D8%AD%D8%A7%D8%AF%D8%AB%D8%A7%D8%AA-%D9%85%D9%88%D8%B3%D9%83%D9%88-%D8%B3%D9%88%D8%B1%D9%8A%D8%A7-%D9%84%D9%8A%D8%A8%D9%8A%D8%A7-%D8%B5%D8%B1%D8%A7%D8%B9' 
#fetching the content from the URL
fetched_data = urllib.request.urlopen(url)
'https://en.wikipedia.org/wiki/20th_century'

article_read = fetched_data.read()
#parsing the URL content and storing in a variable
article_parsed = BeautifulSoup.BeautifulSoup(article_read,'html.parser')
#returning <p> tags
paragraphs = article_parsed.find_all('p')

article_content = ''
#looping through the paragraphs and adding them to the variable
for p in paragraphs:  
    article_content += p.text
#==============================================================================



translator = Translator()
lang = translator.detect(article_content[:200])
print ('**'*20)
print(lang.lang)
print ('**'*20)
if lang == 'ar' : lang = 'arabic'
else : lang ='english'

def _create_dictionary_table(text_string) -> dict:    
    """
    To ensure the scrapped textual data is as noise-free as possible, we’ll perform
    some basic text cleaning.  To assist us to do the processing, we’ll import a list
    of stopwords from the nltk library.
    
    We’ll also import PorterStemmer, which is an algorithm for reducing words into 
    their root forms. For example, cleaning, cleaned, and cleaner can be reduced to the
    root clean.
    
    Furthermore, we’ll create a dictionary table having the frequency of occurrence
    of each of the words in the text. We’ll loop through the text and the corresponding 
    words to eliminate any stop words.
    """   
    #removing stop words
    stop_words = set(stopwords.words(lang))
    
    words = word_tokenize(text_string)
    
    #reducing words to their root form
    stem = PorterStemmer()
    
    #creating dictionary for the word frequency table
    frequency_table = dict()
    for wd in words:
        wd = stem.stem(wd)
        if wd in stop_words:
            continue
        if wd in frequency_table:
            frequency_table[wd] += 1
        else:
            frequency_table[wd] = 1
    return frequency_table


def _calculate_sentence_scores(sentences, frequency_table) -> dict:   
    """
    To evaluate the score for every sentence in the text, we’ll be analyzing 
    the frequency of occurrence of each term. In this case, we’ll be scoring 
    each sentence by its words; that is, adding the frequency of each important 
    word found in the sentence.
    
     to ensure long sentences do not have unnecessarily high scores over short sentences, we divided each score of a sentence by the number of words found in that sentence.

    Also, to optimize the dictionary’s memory, we arbitrarily added sentence[:7], 
    which refers to the first 7 characters in each sentence. However, for longer 
    documents, where you are likely to encounter sentences with the same first n_chars, 
    it’s better to use hash functions or smart index functions to take into account 
    such edge-cases and avoid collisions.
    """
    #algorithm for scoring a sentence by its words
    sentence_weight = dict()

    for sentence in sentences:
        #sentence_wordcount = (len(word_tokenize(sentence)))
        sentence_wordcount_without_stop_words = 0
        for word_weight in frequency_table:
            if word_weight in sentence.lower():
                sentence_wordcount_without_stop_words += 1
                if sentence[:7] in sentence_weight:
                    sentence_weight[sentence[:7]] += frequency_table[word_weight]
                else:
                    sentence_weight[sentence[:7]] = frequency_table[word_weight]

        sentence_weight[sentence[:7]] = sentence_weight[sentence[:7]] / sentence_wordcount_without_stop_words
 
    return sentence_weight



def _calculate_average_score(sentence_weight) -> int:
    """
    To further tweak the kind of sentences eligible for summarization, we’ll 
    create the average score for the sentences. With this threshold, we can avoid 
    selecting the sentences with a lower score than the average score.
    """
    #calculating the average score for the sentences
    sum_values = 0
    for entry in sentence_weight:
        sum_values += sentence_weight[entry]

    #getting sentence average value from source text
    average_score = (sum_values / len(sentence_weight))

    return average_score

def _get_article_summary(sentences, sentence_weight, threshold):
    """
    Lastly, since we have all the required parameters, we can now generate a summary for the article.
    """
    sentence_counter = 0
    article_summary = ''

    for sentence in sentences:
        if sentence[:7] in sentence_weight and sentence_weight[sentence[:7]] >= (threshold):
            article_summary += " " + sentence
            sentence_counter += 1
    return article_summary

def _run_article_summary(article):
    #creating a dictionary for the word frequency table
    frequency_table = _create_dictionary_table(article)
    """
    To split the article_content into a set of sentences, we’ll 
    use the built-in method from the nltk library.
    """
    #tokenizing the sentences
    sentences = sent_tokenize(article , language = lang)
    #algorithm for scoring a sentence by its words
    sentence_scores = _calculate_sentence_scores(sentences, frequency_table)
    #getting the threshold
    threshold = _calculate_average_score(sentence_scores)
    #producing the summary
    article_summary = _get_article_summary(sentences, sentence_scores, 1.5 * threshold)
    return article_summary



if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    data=_create_dictionary_table(article_content)
    plt.plot(list(data.values()), '-')
    plt.ylabel('some numbers')
    plt.show()
    
    summary_results = _run_article_summary(article_content)
    print(summary_results)
    data2=_create_dictionary_table(article_content)

