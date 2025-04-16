class Trie(object):

    def __init__(self):
        self.end_of_word = False
        self.key = ""
        self.children = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if not len(word):
            self.end_of_word = True
            return

        ch = word[0]

        if ch not in self.children:
            self.children[ch] = Trie()
            self.children[ch].key = ch

        self.children[ch].insert(word[1:])

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not len(word):
            return self.end_of_word

        ch = word[0]
        if ch not in self.children:
            return False

        return self.children[ch].search(word[1:])

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if not len(prefix):
            return True

        ch = prefix[0]
        if ch not in self.children:
            return False

        return self.children[ch].startsWith(prefix[1:])


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
