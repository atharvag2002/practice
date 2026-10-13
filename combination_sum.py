
def combination_sum(candidates, target):
    result = []
    
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])
            current.pop()
    
    backtrack(0, [], target)
    return result


def main():
    candidates = [2, 3, 6, 7]
    target = 7
    print(f"Candidates: {candidates}, Target: {target}")
    print(f"Combinations: {combination_sum(candidates, target)}")


if __name__ == "__main__":
    main()
