'''
백준 9184 신나는 함수 실행
https://www.acmicpc.net/problem/9184

메모이제이션 : 동일한 연산을 반복해야 할 때 이전에 연산한 값을 메모리에 미리 저장해 둠으로써 계산의 반복수행을 제거하여 프로그램 실행 속도를 향상시키는 기술
'''
import sys

MAX = 21
# 메모이제이션을 위한 list 할당 / dp[][][]
dp = [[[0]*MAX for _ in range(MAX)] for __ in range(MAX)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # 값이 이미 존재한다면 그 값을 바로 리턴.
    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]

    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + \
        w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]


while True:
    a, b, c = list(map(int, sys.stdin.readline().split(' ')))

    if a == -1 and b == -1 and c == -1:
        break

    print('w(%d, %d, %d) = %d' % (a, b, c, w(a, b, c)))
