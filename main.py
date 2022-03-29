import json
import most_retweeted

DB_PATH = 'farmers-protest-tweets-2021-03-5.json'


def main(option = 1):
    file = open(DB_PATH, 'r')
    data = json.load(file)
    print(most_retweeted.most_retweeted(data))

if __name__ == '__main__':
    main()
