headers = [
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Referer": "https://www.google.com/",
    },
    {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                      "Version/17.0 Safari/605.1.15",
        "Accept-Language": "en-US,en;q=0.8",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Referer": "https://www.google.com/",
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/118.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.7",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Referer": "https://www.google.com/",
    },
]

negative_words = [
    "not", "no", "never", "n't", "cannot", "without",
    "can't", "wasn't", "won't", "wouldn't", "shouldn't",
    "couldn't", "don't", "doesn't", "didn't", "isn't",
    "aren't", "wasn't", "weren't", "hasn't", "haven't",
    "hadn't", "mustn't", "mightn't", "shan't"
]

stop_words = [
    'as', 'during', 'once', 'than', 'above', 'is', 'mightn', 'has', 's', 'further', 'up', "should've",
    'i', 'ours', 'few', 'by', "i'm", 'them', "he's", 'him', 'weren', 'but', 'his', 'hers', 'do', 
    "they'd", 'nor', 'whom', "it'll", 'or', 'while', 'of', 'each', 't', 'down', 'some', "you'll", 
    'y', 'yourselves', 'shan', 'such', 'me', 'theirs', 'should', 'will', 'before', 'mustn', 'what', 
    'those', 'which', 'my', "needn't", 'where', 'he', 'her', "we'll", 'from', 'you', 'these', 'were', 
    'being', 'other', 'hadn', 'a', 'm', 're', 'off', 'both', 'when', 'himself', 'have', 'same', 've', 
    "we're", 'its', 'having', 'can', "i'll", 'haven', 'your', 'too', 'themselves', "he'll", "they're", 
    "she'll", "it'd", "that'll", 'been', 'between', 'she', "they've", 'why', 'we', 'the', 'ma', 'most', 
    'are', 'through', 'to', 'against', 'any', 'on', 'aren', 'because', 'after', "i've", 'and', 'o', 
    'myself', 'about', 'yourself', 'don', 'll', 'isn', 'then', 'hasn', 'needn', 'wouldn', 'this', 'for', 
    'out', "they'll", 'at', 'was', 'had', 'herself', "i'd", 'here', 'all', 'if', "it's", 'again', 'an', 
    'that', 'into', 'over', 'they', 'in', 'only', 'how', "we'd", 'd', 'just', 'does', 'it', 'there', 
    "you've", 'did', 'very', 'yours', 'am', 'doing', 'more', 'who', 'under', 'be', 'ain', 'below', 
    'our', 'itself', 'their', 'now', 'own', 'so', 'with', "you're", 'ourselves',
    "<s>", "</s>", "one", "two",
    # Added single letters a-z
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",
]


