def faulty_find_max(data):
    max_val = data[0]
    for i in range(1, len(data) + 1): # Index Error 발생
        if data[i] > max_val:
            max_val = data[i]
    return max_val

def main():
    my_list = [5, 3, 9, 1, 7]
    print("디버깅 시작 : main 함수 호출")
    max_value = faulty_find_max(my_list)
    print("최대값:", max_value)

if __name__ == '__main__': # 직접 실행 시에만 main() 호출
    main()