inverted_index = dict()

data = {
    "playId" : "p1",
    "sceneId" : "s0",
    "sceneNum" : 0,
    "text" : "the quick brown fox jumps over the laxy dog"
    },  {
    "playId" : "p2",
    "sceneId" : "s1",
    "sceneNum" : 1,
    "text" : "ashna is the coolest person ever the end"
    }, {
    "playId" : "p3",
    "sceneId" : "s2",
    "sceneNum" : 2,
    "text" : "ashna jain the quick brown fox jumps over the laxy dog"
    },


for elem in data:
    playID = elem['playId']
    sceneID = elem['sceneId']
    sceneNum = elem['sceneNum']
    text = elem['text'].split()
    
    position = 0

    for word in text: 
        if inverted_index.get(word) == None: 
            inverted_index[word] = dict()
            inverted_index[word][playID] = dict() 
            inverted_index[word][playID][sceneNum] = [position]
        elif word in inverted_index and playID not in inverted_index[word].keys():
            inverted_index[word][playID] = dict() 
            inverted_index[word][playID][sceneNum] = [position]
        elif word in inverted_index and sceneNum not in inverted_index[word][playID].keys():
            inverted_index[word][playID][sceneNum] = [position]
        else:
            inverted_index[word][playID][sceneNum] += [position]
        position += 1

print(inverted_index)
#-----------------------------
def ORPhrase(input):
    resultOR = set()
    for phrase in input:
        phraseArr = phrase.split()
        playScene = findPlaySceneWherePhraseExists1(phraseArr)
        resultOR = resultOR | playScene
    return resultOR

def ANDPhrase(input):
    resultAND1 = []
    resultAND2 = []
    switch = False
    for phrase in input:
        phraseArr = phrase.split()
        playScene = findPlaySceneWherePhraseExists1(phraseArr)
        if switch == True:
            resultAND2 += playScene
        else:
            resultAND1 += playScene
        switch = not switch
    return set(resultAND1).intersection(set(resultAND2))

def playOrScene(input):
    result = []
    for x in input: 
        if playBool == True: 
            result += [x[0]]
        else:
            result += [x[1]]
    return [*set(result)]

def findPlaySceneWherePhraseExists1(phrase):
    playSceneSet = set()
    for play in inverted_index[phrase[0]]:
        phraseLen = 0
        for scene in inverted_index[phrase[0]][play]:
            for loc in inverted_index[phrase[0]][play][scene]:
                phraseLen += 1
                for p in range(1, len(phrase)):
                    wordX = phrase[p]
                    if(play not in inverted_index[wordX].keys()):
                        break
                    if(scene not in inverted_index[wordX][play].keys()):
                        break
                    if(loc+p not in inverted_index[wordX][play][scene]):
                        break
                    else:
                        phraseLen += 1
                if phraseLen == len(phrase):
                    playSceneSet.add((play, scene))
    return playSceneSet
#-----------------------------

def findPlaySceneWherePhraseExists(phrase, delim):
    playSceneSet = set()
    if(phrase[0] not in inverted_index.keys()):
        return playSceneSet
    for play in inverted_index[phrase[0]]:
        for scene in inverted_index[phrase[0]][play]:
            for loc in inverted_index[phrase[0]][play][scene]:
                for p in range(1, len(phrase)):
                    wordX = phrase[p]
                    if(wordX not in inverted_index.keys()):
                        break
                    if(play not in inverted_index[wordX].keys()):
                        break
                    if(scene not in inverted_index[wordX][play].keys()):
                        break
                    if(loc+p not in inverted_index[wordX][play][scene]):
                        break
                else:
                    if delim == 'play':
                        playSceneSet.add((play))
                    elif delim == 'scene':
                        playSceneSet.add((scene))
                
    return playSceneSet

def OR(input, delim):
    resultOR = set()
    for phrase in input:
        phraseArr = phrase.split()
        playScene = findPlaySceneWherePhraseExists(phraseArr, delim)
        print(playScene)
        resultOR = resultOR | playScene
    return sorted(list(resultOR))

def AAND(input, delim):
    resultAND1 = []
    resultAND2 = []
    switch = False
    for phrase in input:
        phraseArr = phrase.split()
        playScene = findPlaySceneWherePhraseExists(phraseArr, delim)
        print(playScene)
        if switch == True:
            resultAND2 += playScene
        else:
            resultAND1 += playScene
        switch = not switch
    return sorted(list(set(resultAND1).intersection(set(resultAND2))))

def AND(input, delim):
    phraseArr = input[0].split()
    result = findPlaySceneWherePhraseExists(phraseArr, delim)
    for p in range(1, len(input)):
        phraseArr = input[p].split()
        playScene = findPlaySceneWherePhraseExists(phraseArr, delim)
        print(playScene)
        result = result & playScene
    return sorted(list(result))

input = ["quick brown fox", 'ashna jain']
playBool = False

print(" ")
#print(findPlaySceneWherePhraseExists(input[0].split(), 'scene'))
res = AND(input, 'play')
print(res)


                
                    







