import sys
import json
import re

all_words = {}

def lines(fp):
    print str(len(fp.readlines()))

def affin(fp):
    scores = {} # initialize an empty dictionary
    with open(fp) as sent_file:
        for line in sent_file:
            term, score  = line.split("\t")
            scores[term] = int(score)
    return scores

def parsed_json(fp):
    tweets = []
    with open(fp) as tweet_file:
        for line in tweet_file:
            tweets.append(json.loads(line))
    return tweets

def make_the_earth(tweets):
    for record in tweets:
        if u'text' in record.keys():
            for word in record[u'text'].split():
                word1 = re.sub(u'[^A-Za-z\s]*', u'', word)
                if word1:
                    if word1.lower() in all_words.keys():

                        all_words[word1.lower()] += 1
                    else:
                        all_words[word1.lower()] = 1

def main():
    #sent_file = sys.argv[1]
    tweet_file = sys.argv[1]

    #ratings = affin(sent_file)
    tweets = parsed_json(tweet_file)

    make_the_earth(tweets)
    for w in all_words:
        print '%s %f' % (w, all_words[w])

if __name__ == '__main__':
    main()
