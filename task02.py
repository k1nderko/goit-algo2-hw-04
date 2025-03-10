class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def put(self, key, value=None):
        if not isinstance(key, str) or not key:
            raise TypeError(f"Illegal argument for put: key = {key} must be a non-empty string")

        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        if current.value is None:
            self.size += 1
        current.value = value if value is not None else True  

    def has_node(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def keys(self):
        def collect(node, prefix):
            if node.value is not None:
                yield prefix
            for char, child in node.children.items():
                yield from collect(child, prefix + char)

        return list(collect(self.root, ""))


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""

        prefix = strings[0]
        for word in strings[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


if __name__ == "__main__":
    trie = LongestCommonWord()
    
    strings = ["flower", "flow", "flight"]
    result = trie.find_longest_common_word(strings)
    print(f"Longest common prefix of {strings}: {result} (Expected: 'fl')")
    assert result == "fl"

    strings = ["interspecies", "interstellar", "interstate"]
    result = trie.find_longest_common_word(strings)
    print(f"Longest common prefix of {strings}: {result} (Expected: 'inters')")
    assert result == "inters"

    strings = ["dog", "racecar", "car"]
    result = trie.find_longest_common_word(strings)
    print(f"Longest common prefix of {strings}: {result} (Expected: '')")
    assert result == ""