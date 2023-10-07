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
    "earth": "ifdsfddf"}
englishphrase = input("please fill in some word in english")
englishword = englishphrase.lower().split()
alienword = {}
for word in englishword:
    if word in aliendictionary:
        alienword.append(aliendictionary[word])
    else:
        alienword.append(word)
print("The aliens word spell is:","".join(alienword(word)))
