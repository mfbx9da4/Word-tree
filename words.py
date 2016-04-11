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
        for i, letter in enumerate(word):
            prefix = word[0:i + 1]
            if i + 1 == len(word):
                current[prefix] = {'_': word}
            else:
                current[prefix] = current.get(prefix, {})
            current = current[prefix]


def update_anagrams(anagrams_dict, word):
    """
    Use the sorted word as a hash to a list of anagrams
    matching the sorted word.
    """
    # sort word
    sorted_word = ''.join(sorted(word)).replace("'", '')

    # find existing anagrams of this word
    anagrams = anagrams_dict.get(sorted_word) or []

    # include this word if it is not already listed
    if not anagrams.count(word):
        anagrams.append(word)
        anagrams_dict[sorted_word] = anagrams


# open dictionary words file
f = open("words")

# init
tree = WordTree()
anagrams_dict = {}

for word in f.xreadlines():
    word = word.split('\n')[0].lower().decode('utf-8')

    # update word tree
    tree.update(word)

    # update the anagrams dict
    update_anagrams(anagrams_dict, word)

out = open('static/data/tree.json', 'wr+')
out.write(json.dumps(tree.words))
out.close()

out = open('static/data/anagrams.json', 'wr+')
out.write(json.dumps(anagrams_dict))
out.close()
f.close()
