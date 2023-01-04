Ashna Jain - Oct 30, 2022
CS 446: Search Engines - Inverted Index

Breakdown: 
    -Indexing: in program.py lines 88-110
    -Query Evaluation: in program.py lines 112-129 w/ helper functions at lines 16-78

Description: 

    The data structure I used for the inverted index was mainly a dictionary and an array. 
    This is because a dictionary allows me to quickly store items in a nested manner, and also access them using a key.
     
    Structure of my Inverted Index:
    -------------------------------
    word1:
        play5:
            scene9:[loc4, loc9, loc28, loc30]
            scene12:[loc3, loc18, loc22, loc45]
            .
            .
        play11:
            scene36:[loc14, loc21, loc29, loc45]
            .
            .
        .
        .

    where word in a dictionary, play, and scence are all keys to a their dictionary, and at the end we have a location array 
    for the position where every word occurs in the the certain play and scene. 
    
    I created the inverted index by going through the input JSON file and in the cases where the word wasnt in the dict, I added the word+play+scene+loc,
    in the cases where the word was there, but not the play, I added the play+scene+loc, in the case where the play was there but not the scene, I added the
    scene+loc, and finally in the cases where the word, play and scene were there but not the loc, I added the loc. After adding I incremented the position counter, 
    and repeated this process for all scenes in the play. 

    Query Process:
    ----------------
    I have a function findPlaySceneWherePhraseExists(phrase, delim) that takes in a phrase (ex. "quick brown fox") and a delim ("play" or "scene"),
    and returns all the plays/scenes where it occurs in exact order. It will not return if the words are in the play in a different order/spaced apart.
    For an example, if the phrase occurs in (p1, s2), (p1, s3), (p3, s5) it will return an array of all these locations based off of what delim is specified.
    The function works by going through the inverted index of the first word in the phrase. For each of the locs in a specific scene, it checks if the remaining words
    in the phrase have the next sucessive locations in their own inverted lists. My function checks for this my checking for multiple edge cases where it wouldnt be true, 
    if it passes all the edge cases, then we know the phrase exists, and we add the scene/play to our resultArr.

    I have a OR function that takes in an input of multiple phrases, and applies findPlaySceneWherePhraseExists() to each phrase.
    Each time, I OR the already existing locations with the newly returned locations.
    For an example, if I had the input ["quick brown fox", "ate grass"] where phrase1 occurs in 
    [(p1, s2), (p1, s3), (p3, s5)] and phrase2 occurs in [(p1, s2), (p1, s5), (p3, s4) (p4, s10)]
    it would return [p1, p3, p4] for plays and [s2, s3, s4, s5, s10] for scenes
    The function works by storing the locations of the phrase in a set, and then ORing that set with the previous results. 
    At the end, we convert the set to a list, and sort it.

    I use very similar logic as seen in OR for the AND function: 
    Given the input ["quick brown fox", "ate grass"] where phrase1 occurs in
    [(p1, s2), (p1, s3), (p3, s5)] and phrase2 occurs in [(p1, s2), (p1, s5), (p3, s4) (p4, s10)]
    It will return: [p1, p3] for plays and [s1] for scenes
    I store the locations of the phrase in a set, and then AND the set with the previous results.
    At the end, we convert the set to a list, and sort it.

Libraries: 
    -import gzip
    -import json
    -import os
    -import sys
    -import time

Dependencies:
    -Python 3:
    -MatplotLib:
        -Using pip:
        python -m pip install -U pip
        python -m pip install matplotlib

Building/Running:
    -After directing to the appropiate folder, type "python indexer.py indexer collection.json.gz indexname queries.tsv outputFolder" into terminal
        -After doing this, a results folder should be created holding all the outputs of the queries.
    


    