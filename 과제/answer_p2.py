def anomaly_temp(temp_list):
    # 연속된 인덱스를 그룹화하는 함수
    def get_groups(index):
        # 리스트가 빈 경우
        if not index:
            return []

        groups = [] #최종적으로 묶인 그룹을 담는 큰 리스트
        current_group = [index[0]] # 연속되는 숫자를 임시로 담는 리스트, 첫 번째 숫자 넣고 시작

        # 조건 검사
        for i in range(1, len(index)):
            # 바로 앞의 숫자보다 정확히 1 큰지
            if index[i] == index[i-1] + 1:
                current_group.append(index[i])

            # 아닌 경우에는 체인 끊기
            else:
                groups.append(current_group)
                current_group = [index[i]]

        groups.append(current_group)
        return groups

    # (1) 이상한 온도 - 너무 높은 온도 (50도 이상)
    high_temp = [i for i, t in enumerate(temp_list) if t >= 50]
    for g in get_groups(high_temp):
        print(f"이상한 온도 - 너무 높은 온도: {g[0]+1}시 ~ {g[-1]+1}시")

    # (2) 이상한 온도 - 너무 낮은 온도 (10도 이하)
    low_temp = [i for i, t in enumerate(temp_list) if t <= 10]
    for g in get_groups(low_temp):
        print(f"이상한 온도 - 너무 낮은 온도: {g[0]+1}시 ~ {g[-1]+1}시")

    # (3) 이상한 온도 변화 - 너무 급격히 높아짐 (1시간동안 5도 이상 증가)
    inc_temp = [i for i in range(len(temp_list)-1) if (temp_list[i+1] - temp_list[i]) >= 5]
    for g in get_groups(inc_temp):
        print(f"이상한 온도 변화 - 너무 급격히 높아짐: {g[0]+1}시 ~ {g[-1]+2}시")

    # (4) 이상한 온도 변화 - 너무 급격히 낮아짐 (1시간동안 5도 이상 감소)
    dec_temp = [i for i in range(len(temp_list)-1) if (temp_list[i+1] - temp_list[i]) <= -5]
    for g in get_groups(dec_temp):
        print(f"이상한 온도 변화 - 너무 급격히 낮아짐: {g[0]+1}시 ~ {g[-1]+2}시")

# 온도 리스트 생성 후 함수 호출
temp_list = [
    20.0, 20.0, 20.0, 20.0, 20.0, 20.0,
            26.0, 32.0, 38.0, 39.0,
            39.0, 39.0, 39.0, 39.0,
            33.0, 27.0, 26.0,
            39.0, 39.0, 39.0, 39.0, 39.0, 39.0, 38.0
]

anomaly_temp(temp_list)