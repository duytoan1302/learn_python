aliendictionary = {
    "we are": "jdfskl",
    "attack": "nviebjf",
    "shoot": "jfslajfj",
    "rocket": "kijkbfb",
    "tank": "jvjdjnb",
    "airplane": "hfniue",
    "boat": "jfkgih",
    "hello": "jgirttt",
    "kill": "cdsajl",
    "run": "ljfl",
    "you are": "safdjh",
    "go": "kiklrs",
    "gun": "sdhvudui",
    "earth": "ifdsfddf,"}
englishphrase = input("please fill in some word in english")
englishwords = englishphrase.lower().split()
alienWords = {}
for word in englishwords:
    if word in aliendictionary:
        alienWords.append(aliendictionary[word])
    else:
        alienWords.append(word)
print("The aliens word spell is:","".join(alienWords(word)))