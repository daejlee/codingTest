# 뒷 기능이 앞 기능보다 먼저 완성되면 앞 기능과 함께 배포된다.
# progresses: 배포되는 순서대로 진도가 적힌 정수 리스트
# speeds: 각 작업의 개발 속도가 적힌 정수 리스트
# 배포마다 몇 개의 기능이 배포되는지 리스트로 반환

# 반복하며 각 작업에 정해진 속도대로 진도를 더한다.
# 최상단 작업이 완료되면 이후 작업들까지 체크하여 모두 배포하고, answer에 기록한다.
# 위 과정을 작업이 모두 완료될 때 까지 반복


def solution(progresses, speeds):
    answer = []
    while len(progresses):
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            j = 0
            while j < len(progresses) and progresses[j] >= 100:
                j += 1
            progresses = progresses[j:]
            speeds = speeds[j:]
            answer.append(j)
    return answer
