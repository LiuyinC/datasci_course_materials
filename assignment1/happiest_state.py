__author__ = 'LiuyinC'
import sys
import json


def max_in_value(dic):
    value = list(dic.values())
    key = list(dic.keys())
    max_key = key[value.index(max(value))]
    return max_key


def lines(fp):
    print str(len(fp.readlines()))


def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # sentiment_file = open('AFINN-111.txt')
    # tweet_file = open('problem_1_submission.txt')
    scores = {}  # initialize an empty dictionary
    for line in sentiment_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    sentiment_file.close()
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    happiness_index = {}
    for state in states.keys():
        happiness_index[state] = 0  # Initialize the state's happiness index as zero
    for tweet in tweet_file:
        fp = json.loads(tweet)
        if 'text' in fp.keys() and 'place' in fp.keys():
            if fp['place'] is not None and fp['place']['country_code'] == 'US':  # Limit the scope in USA
                state_ab = fp['place']['full_name'].split(', ')[1]  # Get the tweet's location in term of state
                encode_state = state_ab.encode('utf-8')
                if encode_state in happiness_index.keys():
                    text = fp['text']
                    word_list = text.replace('.', ' ')
                    word_list = word_list.split()
                    tweet_score = 0
                    for word in word_list:  # Calculate the tweet's sentiment score
                        if word in scores.keys():
                            tweet_score += scores[word]
                    happiness_index[encode_state] += tweet_score  # Update state's happiness score
    print max_in_value(happiness_index)
    tweet_file.close()


if __name__ == '__main__':
    main()