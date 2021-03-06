# Word prefix tree and anagram solver

### [Demo](http://mfbx9da4.github.io/projects/Word-tree/static/)

### Aim
Often people learning a foreign language have problems remembering the difference between similarly spelt or similarly sounding words.
This project aims to help people disambiguate similarly spelt words.

### Run
Run a server (using e.g. `ws` or `python -m SimpleHTTPServer`) in the root folder and visit [http://localhost:8000/static](http://localhost:8000/static)

### Method
- `words.py` generates `tree.json` and `anagrams.json`.
- `tree.json` contains a letter by letter prefix tree (trie) of all the words in the dictionary.
- `anagrams.json` contains all angrams in the dictionary, indexed by the sorted strings.
- `main.js` loads `tree.json` and `anagrams.json` into memory.
- `index.html` contains a recursive template for displaying the tree.
- Selecting a word causes a request to the wikipedia API and consults the anagrams dict.
- Also note I used some CSS3 flexbox magic, so I hope your browser supports that.
