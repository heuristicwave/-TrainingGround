import sys
input = sys.stdin.readline


def main():
    origin, interest, year = map(str, input().split())
    interest_divide = float(interest) / 100

    answer = int(origin)
    for _ in range(int(year)):
        answer *= (1+interest_divide)

    print(format(answer, ".2f"))


main()
