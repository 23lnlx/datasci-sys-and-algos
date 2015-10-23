import sys
import json

all_hashes = {}

def parsed_json(fp):
    tweets = []
    with open(fp) as tweet_file:
        for line in tweet_file:
            tweets.append(json.loads(line))
    return tweets

def streaming_hashes(tweets):
    for record in tweets:
        if u'entities' in record.keys():
            if record[u'entities'][u'hashtags']:
                for word in record[u'entities'][u'hashtags']:
                    if word[u'text'].lower() in all_hashes.keys():
                        all_hashes[word[u'text'].lower()] += 1
                    else:
                        all_hashes[word[u'text'].lower()] = 1



def main():
    tweet_file = sys.argv[1]

    tweets = parsed_json(tweet_file)

    streaming_hashes(tweets)

    more_hashes = []

    for val in all_hashes:
        more_hashes.append([all_hashes[val], val])
    more_hashes.sort()

    i=0
    while (i <10) and (i < len(more_hashes)):
        print more_hashes[i][1],
        print more_hashes[i][0]
        i+=1

if __name__ == '__main__':
    main()
