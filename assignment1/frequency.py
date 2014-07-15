__author__ = 'LiuyinC'
import sys
import json


def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))


def main():
    tweet_file = open(sys.argv[1])
    # tweet_file = open('problem_1_submission.txt')
    term_occurrence = {}  # Initialize an empty dictionary for term and its occurrence
    all_terms_occurrence = 0
    for tweet in tweet_file:
        fp = json.loads(tweet)
        if 'text' in fp.keys():
            text = fp['text']
            word_list = text.replace('.', ' ')
            word_list = word_list.split()
            all_terms_occurrence += len(word_list)  # Count for all terms in all tweets
            for word in word_list:
                if word in term_occurrence.keys():
                    term_occurrence[word] += 1
                else:
                    term_occurrence[word] = 1
    for term, occurrence in term_occurrence.items():
        frequency = float(occurrence) / float(all_terms_occurrence)
        print term, frequency
    tweet_file.close()

if __name__ == '__main__':
    main()
