def faulty_build_list(data):
    """
    입력 리스트의 각 요소에 대해 (인덱스 + 값)의 누적합을 구하여 튜플로 반환하는 함수입니다.
    예: [10, 20] -> (10, 31)  # (0+10), (10+(1+20))
    
    현재 두 가지 주요 버그가 있습니다:
    1. 튜플(tuple)은 요소를 추가(append)할 수 없는 불변 객체입니다.
    2. 누적합 계산 로직이 의도와 다를 수 있습니다.
    """
    total = 0
    result = () # 버그 1: 수정이 불가능한 튜플로 시작합니다.
    
    for i, item in enumerate(data):
        # 버그 2: total에 현재 인덱스와 값을 더한 결과를 '누적'해야 합니다.
        # 현재는 단순히 마지막 계산값만 유지될 수 있습니다.
        total = i + item 
        
        # 튜플에는 append 메서드가 없습니다!
        result.append(total) 
        
    return result

def main():
    sample_data = [10, 20, 30, 40]
    print("--- 실습 2: 누적합 튜플 생성하기 ---")
    print(f"입력 데이터: {sample_data}")
    print("예상 결과: (10, 31, 63, 107) 또는 (10, 21, 32, 43) 중 실습 의도에 맞춰 수정")
    
    try:
        built_result = faulty_build_list(sample_data)
        print(f"최종 결과: {built_result}")
    except AttributeError as e:
        print(f"\n[에러 발생!] {e}")
        print("힌트: 리스트(list)로 먼저 작업한 후 마지막에 tuple()로 변환해 보세요.")

if __name__ == '__main__':
    main()
