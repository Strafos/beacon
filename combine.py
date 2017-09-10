import info

def combine():
    b = open('all_tweets.txt', 'r')
    a = open('gdocs_tweets.txt', 'r')
    f = open('combined_tweets.txt', 'w')

    c = 0
    for i in b.readlines():
        c = c + 1
        f.write(i)
        if c % 104 is 0:
            f.write(a.readline())

def filter1():
    f = open('combined_tweets.txt', 'r')
    g = open('first_filter.txt', 'w')
    for tweet in f.readlines():
        if any(num in tweet for num in info.nums):
            if any(kw in tweet for kw in info.help_words):
                g.write(tweet)

filter1()
def spaces():
    f = open('current.txt', 'r')
    g = open('all_tweets.txt', 'w')
    for i in f.readlines():
        if len(i) >= 5:
            g.write(i)
