
from collections import deque

def word_ladder(begin_word, end_word, word_list):
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    
    queue = deque([(begin_word, 1)])
    
    while queue:
        word, length = queue.popleft()
        
        if word == end_word:
            return length
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in word_set:
                    word_set.remove(next_word)
                    queue.append((next_word, length + 1))
    
    return 0


def main():
    test_cases = [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    ]
    for begin, end, word_list in test_cases:
        result = word_ladder(begin, end, word_list)
        print(f"Word ladder from '{begin}' to '{end}': {result} steps")


if __name__ == "__main__":
    main()
