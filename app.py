from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from textblob import TextBlob, Word
import random
import time

app=Flask(__name__)
Bootstrap(app)

# routing
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse',methods=['POST'])
def analyse():
    start=time.time()
    summary={}
    final_time=time.time()
    len_of_words=0
    if request.method=='POST':
        rawtext = request.form['rawtext']
        blob = TextBlob(rawtext)
        recieved_text=blob
        blob_sentiment, blob_subjectivity=blob.sentiment.polarity, blob.sentiment.subjectivity
        number_of_tokens = len(list(blob.words))
        nouns = list()
        for word, tag in blob.tags:
            if tag=='NN':
                nouns.append(word.lemmatize())
                len_of_words=len(nouns)
                rand_words=random.sample(nouns,len_of_words)
                final_word=list()
                for item in rand_words:
                    word=Word(item).pluralize()
                    final_word.append(word)
                    summary = final_word
                    end = time.time()
                    final_time = end-start
    return render_template('index.html',recieved_text=recieved_text,number_of_tokens=number_of_tokens,blob_sentiment=blob_sentiment,blob_subjectivity=blob_subjectivity,summary=summary,final_time=final_time,len_of_words=len_of_words)

if __name__ == '__main__':
    app.run(debug=True)