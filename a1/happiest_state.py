import sys
import json
import re

happy_states = {}


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
        if u'place' in record.keys():
            if record[u'place']:
                if u'country' in record[u'place'].keys():
                    if record[u'place'][u'country'] == 'United States':
                        if u'full_name' in record[u'place'].keys():
                                    if record[u'place'][u'full_name']:
                                        nam =  record[u'place'][u'full_name'][-2:]

                                        if u'text' in record.keys():

                                            sentiment = 0

                                            for word in record[u'text'].split():
                                                word1 = re.sub(u'[^A-Za-z\s]*', u'', word)

                                                if word1.lower() in ratings.keys():
                                                    sentiment += ratings[word1.lower()]

                                            if nam in happy_states.keys():
                                                happy_states[nam] += sentiment
                                            else:
                                                happy_states[nam] = sentiment

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]

    ratings = affin(sent_file)
    tweets = parsed_json(tweet_file)

    streaming_sent(tweets, ratings)

    more_states = []
    for val in happy_states:
        more_states.append([happy_states[val], val])

    more_states.sort()
    sys.stdout.write(more_states[0][1])

if __name__ == '__main__':
    main()
