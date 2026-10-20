
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


def main():
    word_lists = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        ["", ""],
        ["a"]
    ]
    for words in word_lists:
        print(f"{words} -> {group_anagrams(words)}")


if __name__ == "__main__":
    main()
