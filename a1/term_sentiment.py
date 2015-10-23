import sys
import json
import re

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

def streaming_sent(tweets, ratings):
    for record in tweets:
        if u'text' in record.keys():
            #print(record[u'text'].split())
            sentiment = 0
            for word in record[u'text'].split():
                word1 = re.sub(u'[^A-Za-z\s]*', u'', word)
                if word1.lower() in ratings.keys():
                    sentiment += ratings[word1.lower()]

            for word in record[u'text'].split():
                word1 = re.sub(u'[^A-Za-z\s]*', u'', word)
                if word1.lower() not in ratings.keys():
                    if word1:
                        print '%s %f' % (word1.lower(), sentiment)

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]

    ratings = affin(sent_file)
    tweets = parsed_json(tweet_file)

    streaming_sent(tweets, ratings)


if __name__ == '__main__':
    main()
