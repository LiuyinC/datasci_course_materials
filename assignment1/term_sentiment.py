import sys
import json


def hw():
    print 'Hello, world!'


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
    non_sentiment = {}  # The keys are the words not showing up in afinn file, and values are their scores.
    for tweet in tweet_file:
        fp = json.loads(tweet)
        tweet_score = 0  # initialize the tweet score
        if 'text' in fp.keys():
            text = fp['text']
            word_list = text.replace('.', ' ')  # Replace character '.' by ' '
            word_list = word_list.split()  # Split the tweet into a words list
            for word in word_list:      # This calculate the tweet score given the afinn file
                if word in scores.keys():
                    tweet_score += scores[word]
                elif word not in non_sentiment.keys():
                    non_sentiment[word] = 0.0  # If a word is not in non_sentiment, initialize its score as zero
            for word in word_list:
                if word in non_sentiment.keys():
                    non_sentiment[word] += tweet_score  # Calculate non_sentiment word's score by the tweet's scores.
    afinn_file.close()
    tweet_file.close()
    for word, score in non_sentiment.items():
        print word, score

if __name__ == '__main__':
    main()
