# prices를 순회하며 큐에 값을 삽입 [값, 순서].
# 만약 가격이 떨어지면, 뒤에서부터 떨어진 만큼 pop하여 덜어낸다.
#   덜어낼 때는 큐에 삽입된 값의 순서를 찾아 비교하여 살아남은 시간을 측정한다.

from collections import deque

def solution(prices):
    q = deque()
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        curr_price = prices[i]

        while len(q) > 0 and q[-1][0] > curr_price:
            answer[q[-1][1]] = i - q[-1][1]
            q.pop()
        q.append([curr_price, i])
    while len(q) > 0:
        val, seq = q.pop()
        answer[seq] = len(prices) - seq - 1
                    
    return answer