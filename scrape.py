 
import gzip
import json
import matplotlib.pyplot as plt

with gzip.open('shakespeare-scenes.json.gz', "rt") as file:
    data = json.load(file)
    youArr = []
    theethouArr = []
    sceneArr = []
    for elem in data['corpus']:
        youCount = 0
        theethouCount = 0
        playID = elem['playId']
        sceneID = elem['sceneId']
        sceneNum = elem['sceneNum']
        text = elem['text'].split()

        for word in text:
            if word == 'you':
                youCount += 1
            if word == 'thee' or word == 'thou':
                theethouCount += 1

        if youCount == 0 and theethouCount == 0:
            continue
        
        youArr += [youCount]
        theethouArr += [theethouCount]
        sceneArr += [sceneNum]




width = 0.35 # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(sceneArr, youArr, width, label='# of occurrences of you in each scene')
ax.bar(sceneArr, theethouArr, width, bottom=youArr, label='# of occurrences of thee thou in each scene')

ax.set_ylabel('Frequency')
ax.set_title('occurances of you vs thee/thou in scenes')
ax.legend()

plt.savefig('graph.png')
