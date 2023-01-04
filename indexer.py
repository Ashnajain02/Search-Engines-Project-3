#Ashna Jain
#Project 3: Inverted Index

import gzip
import json
import os
import sys
import time 


#indexer shakespeare-scenes.json.gz wills-index trainQueries.tsv results/

inverted_index = dict()

#takes in a phrase and a delim that specifies play or scene
def findPlaySceneWherePhraseExists(phrase, delim):
    playSceneSet = set()
    if(phrase[0] not in inverted_index.keys()):
        return playSceneSet
    #go through all the scenes for each play
    for play in inverted_index[phrase[0]]:
        for scene in inverted_index[phrase[0]][play]:
            #for each location of the word in the scene,
            for loc in inverted_index[phrase[0]][play][scene]:
                #go through the other parts of the phrase, and check if their inverted-index contains the
                #the next correct location in order for the phrase to be continuous 
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
        #print(playScene)
        resultOR = resultOR | playScene
    return sorted(list(resultOR))

def AAND(input, delim):
    resultAND1 = []
    resultAND2 = []
    switch = False
    for phrase in input:
        phraseArr = phrase.split()
        playScene = findPlaySceneWherePhraseExists(phraseArr, delim)
        #print(playScene)
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
        #print(playScene)
        result = result & playScene
    return sorted(list(result))

if __name__ == '__main__':
    # Read arguments from command line, or use sane defaults for IDE.
    argv_len = len(sys.argv)
    inputFile = sys.argv[1] if argv_len >= 2 else 'shakespeare-scenes.json.gz'
    queriesFile = sys.argv[2] if argv_len >= 3 else 'trainQueries.tsv'
    outputFolder = sys.argv[3] if argv_len >= 4 else 'results/'
    if not os.path.isdir(outputFolder):
        os.mkdir(outputFolder)

    with gzip.open(inputFile, "rt") as file:
        data = json.load(file)
        for elem in data['corpus']:
            playID = elem['playId']
            sceneID = elem['sceneId']
            sceneNum = elem['sceneNum']
            text = elem['text'].split()
            
            position = 0

            for word in text: 
                if inverted_index.get(word) == None: 
                    inverted_index[word] = dict()
                    inverted_index[word][playID] = dict() 
                    inverted_index[word][playID][sceneID] = [position]
                elif word in inverted_index and playID not in inverted_index[word].keys():
                    inverted_index[word][playID] = dict() 
                    inverted_index[word][playID][sceneID] = [position]
                elif word in inverted_index and sceneID not in inverted_index[word][playID].keys():
                    inverted_index[word][playID][sceneID] = [position]
                else:
                    inverted_index[word][playID][sceneID] += [position]
                position += 1

        with open(queriesFile, "r") as file:
            for query in file: 
                x1 = time.time()
                elem = query.rstrip().split('\t')
                queryName = outputFolder+ '/' + elem[0]+'.txt'
                scenePlay = elem[1]
                AndOr = elem[2]
                inputPhrase = elem[3:]

                if AndOr.lower() == 'and':
                    result = AND(inputPhrase, scenePlay)
                elif AndOr.lower() == 'or':
                    result = OR(inputPhrase, scenePlay)
                
                with open(queryName, 'w') as f:
                    for x in result: 
                        f.write(x)
                        f.write('\n')
                y1 = time.time()
                print(y1-x1)
                
            