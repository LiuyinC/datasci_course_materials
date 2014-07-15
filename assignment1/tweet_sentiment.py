import sys
import json


def lines(fp):
    print str(len(fp.readlines()))


def main():
    afinn_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # afinn_file = open('AFINN-111.txt', 'r')
    # tweet_file = open('problem_1_submission.txt')
    scores = {}  # initialize an empty dictionary
    for line in afinn_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    for tweet in tweet_file:
        fp = json.loads(tweet)
        tweet_score = 0  # initialize the tweet score
        if 'text' in fp.keys():
            text = fp['text']
            word_list = text.replace('.', ' ')
            word_list = word_list.split()
            for word in word_list:
                if word in scores.keys():
                    tweet_score += scores[word]
        print tweet_score
    afinn_file.close()
    tweet_file.close()

if __name__ == '__main__':
    main()
