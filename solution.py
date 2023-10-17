def solution(A, F, M):
    missedRolls = []

    noOfRolls = len(A) + F

    arrayF = (noOfRolls * M) - sum(A)

    initialValue = arrayF

    while initialValue > 0:
        subtractedValue = min(initialValue, 6)
        missedRolls.append(subtractedValue)
        initialValue -= subtractedValue
    return missedRolls

print(solution([3,2,4,3], 2, 4))
print(solution([1, 5, 6], 4, 3))
print(solution([1, 2, 3, 4], 4, 6))
print(solution([6, 1], 1, 1))
print(solution([6], 10, 4))