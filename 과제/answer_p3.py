def solve_game():
    # (1) 각 행동마다 선택 가능한 4가지 행동 정의
    action_data = [
        {"name": "몸통 박치기", "energy": 0, "damage": 800},
        {"name": "크게 할퀴기", "energy": -50, "damage": 1000},
        {"name": "강력한 공격", "energy": -130, "damage": 2000},
        {"name": "휴식", "energy": +90, "damage": 0}
    ]

    # (2) 모든 가능한 8회 행동 조합 생성 
    possible_strategies = [[]]
    for turn in range(8):
        updated_strategies = []
        for existing_strategy in possible_strategies:
            for action_index in range(4):
                updated_strategies.append(existing_strategy + [action_index])
        possible_strategies = updated_strategies

    # (3) 최적값 저장 변수 지정
    # [3-1]
    max_damage_3_1 = -1
    best_actions_3_1 = None
    energy_left_3_1 = -1

    # [3-2]
    max_energy_3_2 = -1
    best_actions_3_2 = None
    damage_dealt_3_2 = -1

    # (4) 모든 전략에 대해 하나씩 시뮬레이션하며 검증
    for action_index in possible_strategies:
        current_energy = 100        # 시작 기력
        total_damage = 0            # 누적 데미지
        strong_attack_count = 0     # 강력한 공격 사용 횟수 (최대 1회 제한)
        is_penalty_active = False   # 강력한 공격 사용 여부 판별
        is_strategy_valid = True    # 해당 전략의 유효성 판별
        action_name_history = []    # 실제 수행한 행동들의 이름 기록

        for idx in action_index:
            current_action = action_data[idx]

            # [rule 1] 강력한 공격은 한 번만 사용할 것
            if current_action["name"] == "강력한 공격":
                if strong_attack_count >= 1:
                    is_strategy_valid = False
                    break
                strong_attack_count += 1

            # [rule 2] 기력 소모 계산 (음수->기력소모 / 양수->기력충전)
            energy_cost = -current_action["energy"]
            if is_penalty_active == True:
                energy_cost += 30
            
            current_energy -= energy_cost

            # [rule 3] 기력이 0 미만일 경우 해당 전략 실패
            if current_energy < 0:
                is_strategy_valid = False
                break

            # 결과 누적 및 이름 기록
            total_damage += current_action["damage"]
            action_name_history.append(current_action["name"])

            # 강력한 공격 사용 시 페널티 부여 (다음 턴부터 기력+30)
            if strong_attack_count >= 1:
                is_penalty_active = True
        
        # 위 규칙을 모두 지킨 경우만 고려
        if is_strategy_valid:
            # [3-1] 데미지가 가장 강한 경우의 행동 리스트
            if total_damage > max_damage_3_1:
                max_damage_3_1 = total_damage
                best_actions_3_1 = action_name_history
                energy_left_3_1 = current_energy

            # [3-2] 데미지가 5000 이상이면서 기력이 가장 많이 남는 경우
            if total_damage >= 5000:
                if current_energy > max_energy_3_2:
                    max_energy_3_2 = current_energy
                    best_actions_3_2 = action_name_history
                    damage_dealt_3_2 = total_damage

    print(f"문제 3-1: 최적 체력 감소")
    print(f"행동 조합 : {best_actions_3_1}")
    print(f"최종 상대 체력 : {50000 - max_damage_3_1}")
    print(f"최종 남은 기력 : {energy_left_3_1}")

    print("\n")
    print(f"문제 3-2: 최적 기력")
    print(f"행동 조합 : {best_actions_3_2}")
    print(f"최종 상대 체력 : {50000 - damage_dealt_3_2}")
    print(f"최종 남은 기력 : {max_energy_3_2}")
            









    # (5) 결과 출력

solve_game()