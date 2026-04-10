"""
퀴즈 점수 분석기

초기 점수 리스트 [88, 76, 93, 100, 69]

조건 1 새 점수 84를 추가하라
조건 2 잘못 입력된 76을 제거하라
조건 3 오름차순 정렬하라
조건 4 정렬된 리스트의 최저점, 최고점, 평균을 출력하라
"""


score = [88, 76, 93, 100, 69]

#조건 1
score.append(84)

#조건 2
score.remove(76)

#조건 3
score.sort()

#조건 4
score_min = score[0]
score_max = score[-1]
score_avg = sum(score) / len(score)

print(f"최저점: {score_min}\n최고점: {score_max}\n평균: {score_avg}")