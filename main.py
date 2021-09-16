from language_processing import TwitterSentiment

if __name__ == '__main__':
    sentiment_analyzer = TwitterSentiment()
    s = input('Enter the sentence to analyze: ')
    result = sentiment_analyzer.analyze(s)
    print(result)
