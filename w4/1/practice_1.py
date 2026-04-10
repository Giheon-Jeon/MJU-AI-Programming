def faulty_find_max(data):
    """
    리스트에서 최대값을 찾는 함수입니다.
    현재 range 범위 설정 오류로 인해 IndexError가 발생합니다.
    디버거를 사용하여 i의 변화를 관찰하고 수정해 보세요!
    """
    max_val = data[0]
    
    # 힌트: 리스트의 인덱스는 0부터 시작하며, 마지막 인덱스는 len(data) - 1 입니다.
    # range(start, stop)에서 stop은 포함되지 않습니다.
    for i in range(1, len(data) + 1): # 이 줄에서 에러가 발생합니다.
        if data[i] > max_val:
            max_val = data[i]
            
    return max_val

def main():
    my_list = [5, 3, 9, 1, 7]
    print("--- 실습 1: IndexError 해결하기 ---")
    print(f"입력 리스트: {my_list}")
    
    try:
        max_value = faulty_find_max(my_list)
        print(f"최대값 찾기 결과: {max_value}")
    except IndexError as e:
        print(f"\n[에러 발생!] {e}")
        print("디버그 모드(F5)를 실행하여 'Variables' 창에서 i의 값을 확인해 보세요.")

if __name__ == '__main__':
    main()
