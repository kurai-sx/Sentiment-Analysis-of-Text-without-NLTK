import string
from collections import Counter
import matplotlib.pyplot as plt
def get_tweets():
    import GetOldTweets3 as got
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus') \
        .setSince("2020-05-01") \
        .setUntil("2024-09-30") \
        .setMaxTweets(1000)

    #List of objects gets stored in 'tweets' variable
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    #Iterating through tweets list. Storing them in tweet variable.
    #Get text and store it as a list inside text_tweets
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets

text = ""
text_tweets = get_tweets()
length = len(text_tweets)

for i in range(0,length):
    text = text_tweets[i][0] + " " + text



#text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower()

#str1 = Specifies the list of characters that need to be replaced
#str2 = Specifies the list of characters with which the characters need to be replaced
#str3 = Specifies the list of characters that needs to be deleted

cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

tokenized_words = cleaned_text.split()
#print(tokenized_words)

stop_words=['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and',
    'any', 'are', 'aren\'t', 'as', 'at', 'be', 'because', 'been', 'before', 'being',
    'below', 'between', 'both', 'but', 'by', 'can\'t', 'cannot', 'could', 'couldn\'t',
    'did', 'didn\'t', 'do', 'does', 'doesn\'t', 'doing', 'don\'t', 'down', 'during',
    'each', 'few', 'for', 'from', 'further', 'had', 'hadn\'t', 'has', 'hasn\'t',
    'have', 'haven\'t', 'having', 'he', 'he\'d', 'he\'ll', 'he\'s', 'her', 'here',
    'here\'s', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'how\'s', 'i',
    'i\'d', 'i\'ll', 'i\'m', 'i\'ve', 'if', 'in', 'into', 'is', 'isn\'t', 'it', 'it\'s',
    'its', 'itself', 'let\'s', 'me', 'more', 'most', 'mustn\'t', 'my', 'myself', 'no',
    'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our',
    'ours', 'ourselves', 'out', 'over', 'own', 'same', 'shan\'t', 'she', 'she\'d',
    'she\'ll', 'she\'s', 'should', 'shouldn\'t', 'so', 'some', 'such', 'than', 'that',
    'that\'s', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there',
    'there\'s', 'these', 'they', 'they\'d', 'they\'ll', 'they\'re', 'they\'ve', 'this',
    'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'wasn\'t',
    'we', 'we\'d', 'we\'ll', 'we\'re', 'we\'ve', 'were', 'weren\'t', 'what', 'what\'s',
    'when', 'when\'s', 'where', 'where\'s', 'which', 'while', 'who', 'who\'s', 'whom',
    'why', 'why\'s', 'with', 'won\'t', 'would', 'wouldn\'t', 'you', 'you\'d', 'you\'ll',
    'you\'re', 'you\'ve', 'your', 'yours', 'yourself', 'yourselves' ]

final_words = []

#To remove stop_words

for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

#print(final_words)

# NLP Emotions Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#    - open the emotion file
#    - Loop through each line and clear it
#    - Extract the word and emotion using split
# 2) If the word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list

emotion_list = []

with open('emotion.txt','r') as file:
    for line in file:
        clear_line = line.replace("\n",'').replace(",",'').replace("'",'').strip()
        #From the emotion file word is seperated from where ':' is their, whatever after this is stored in emotion file
        word, emotion = clear_line.split(':')
        #print("Word :" + word + " " + "Emotion :" + emotion)

        if word in final_words:
            emotion_list.append(emotion)
#print(emotion_list)

#Counting the emotions from the list
w = Counter(emotion_list)
print(w)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()