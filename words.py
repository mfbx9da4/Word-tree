#!/usr/bin/python

import simplejson as json


class WordTree(object):
    """WordTree contains the letter paths of words given to it"""
    def __init__(self):
        self.words = {}

    def update(self, word):
        """
        Update tree.

        Iterate letters in the word, each time "recursively" adding each letter
        of the word as a key. When finished iterating the word set the key '_'
        and its value to the full word.

        (_ is used because it is not a word in the dictionary)

        e.g. the example word "happy" becomes
            {'h': {'ha': {'hap': {'happ': {'happy': {'_': 'happy'}}}}}}

        """
        current = self.words
        word = word
        for i, let in enumerate(word):
            key = word[0:i + 1]
            if i + 1 == len(word):
                current[key] = {'_': word}
            else:
                current[key] = current.get(key, {})
            current = current[key]


tree = WordTree()
anagrams_dict = {}
f = open("words")
for word in f.xreadlines():
    word = word.split('\n')[0].lower().decode('utf-8')
    tree.update(word)

    sorted_word = ''.join(sorted(word)).replace("'", '')
    anagrams = anagrams_dict.get(sorted_word) or []
    if not anagrams.count(word):
        anagrams.append(word)
        anagrams_dict[sorted_word] = anagrams

out = open('static/data/tree.json', 'wr+')
out.write(json.dumps(tree.words))
out.close()

out = open('static/data/anagrams.json', 'wr+')
out.write(json.dumps(anagrams_dict))
out.close()
f.close()
