dict = {
    'play1':{
        'scene1': [0, 1, 2],
        'scene2': [0, 1, 2],
        'scene10': [4, 5, 6]
    }, 
    'play2':{
        'scene1': [0, 1, 2],
        'scene2': [0, 1, 2],
        'scene10': [4, 5, 6]
    }
}

set1 = {(0,5), (0,3)}
set2 = {(1,2), (0, 5)}
inter = set1 & set2
print(inter)
for x in inter:
    print(x[0])

x = [1, 2, 3, 4, 5, 6]
z = x[2]
y = x[3:]
print(y)