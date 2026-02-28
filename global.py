from collections import defaultdict
import heapq

class TrieNode:
    def __init__(self):
        self.children = {}
        self.top_words = []  # Min heap (frequency, word)

class AutocompleteSystem:
    def __init__(self):
        self.root = TrieNode()
        self.frequency = defaultdict(int)

    def insert(self, word):
        self.frequency[word] += 1
        freq = self.frequency[word]

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

            # Maintain top 5 suggestions
            heapq.heappush(node.top_words, (freq, word))
            if len(node.top_words) > 5:
                heapq.heappop(node.top_words)

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        return [word for freq, word in sorted(node.top_words, reverse=True)]