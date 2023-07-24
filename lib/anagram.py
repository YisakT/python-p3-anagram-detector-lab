class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, potential_matches):
        matches = []
        for word in potential_matches:
            if sorted(word.lower()) == sorted(self.word) and word.lower() != self.word:
                matches.append(word)
        return matches
