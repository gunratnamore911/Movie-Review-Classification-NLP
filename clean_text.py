#!/usr/bin/env python
# coding: utf-8

# In[28]:


sampler_text = """ just fuck this movie is beautiful and stronlgy ....i just don't like this movie because this is just a remake of tollywood movie they always copy their stories ."""
import nltk
nltk.download('stopwords')


# In[29]:


from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords


# In[30]:


# Init objects 
tokenizer = RegexpTokenizer(r'\w+')

en_stopwords = set(stopwords.words('english'))

ps =PorterStemmer()


# In[31]:


def getstemmedReview (review):
    review = review.lower()
    
   #tokenize
    tokens =tokenizer.tokenize(review)
    
    new_tokens = [token for token in tokens if token not in en_stopwords]
    
    stemmed_tokens = (ps.stem(token) for token in new_tokens)
    
    clean_review = ' '.join(stemmed_tokens)
    
    return clean_review

    
    


# In[26]:


getstemmedReview(sampler_text)


# In[27]:


def getStemmedDocument(inputfile,outputfile):
    out = open(outputfile,'w',endcoding="utf8")
    with open(inputfile,encoding ="utf8") as f:
        reviews = f.readlines()
    
    for review in reviews:
        cleaned_review = getstemmedReview(review)
        print((cleaned_review),file=out)
    out.close()
    
    

