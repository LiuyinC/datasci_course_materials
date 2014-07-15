__author__ = 'LiuyinC'
import sys
import json
import heapq
import operator


def lines(fp):
    print str(len(fp.readlines()))


def main():
    tweet_file = open(sys.argv[1])
    # tweet_file = open('problem_1_submission.txt')
    hashtag_occurence = {}  # Initialize an empty dictionary of hashtag and its appearance.
    for tweet in tweet_file:
        fp = json.loads(tweet)
        if 'entities' in fp.keys():
            hashtags = fp['entities']['hashtags']
            for tags in hashtags:  # Accumulate occurrences of a hashtag
                tag = tags['text']
                if tag not in hashtag_occurence.keys():
                    hashtag_occurence[tag] = 1.0
                else:
                    hashtag_occurence[tag] += 1.0
    top_10_list = heapq.nlargest(10, hashtag_occurence.iteritems(), key=operator.itemgetter(1))
    for hashtag in top_10_list:
        print hashtag[0], hashtag[1]
if __name__ == '__main__':
    main()
