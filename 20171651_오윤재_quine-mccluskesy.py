#각 이진수끼리 비교 함수
def compare(item_1, item_2):
    cnt = 0
    final_item = ""
    for i in range(len(item_1)):
        if cnt >= 2:
            break

        if item_1[i] == item_2[i]:
            final_item += item_1[i]
        else: 
            final_item += "-"
            cnt += 1
    
    if cnt == 1:
        return final_item
    else: return None

#pi 구하는 함수(재귀적으로 실행)
def get_pi(num_dict):
    total_dict = {}

    #pi 구하기
    for item_1 in num_dict:
        for item_2 in num_dict:
            if item_1[0] == item_2[0]:
                continue
            pi = compare(item_1[0], item_2[0])
            #print(item_1[0], item_2[0])
            if pi != None:
                total_dict[pi] = (item_1[1] + item_2[1])
    
    total_dict = sorted(total_dict.items(), key=lambda item: item[1])
    
    if len(total_dict) == 0 :
        return

    #result_dict = get_pi(total_dict)
    

    # for item_1 in num_dict:
    #     for item_2 in total_dict:
    #         set1 = set([item_1[1]])
    #         set2 = set([item_2[1]])

    #         if set1 in set2:
    #             continue
    #         else: total_dict.append([item_1[0], item_1[1]])

    # print(total_dict)
    
    return total_dict


#입력받은 값들을 dict형태로 정리하는 함수
def get_dict(m):
    #정리된 2진수들
    num_dict = {}
    for item in m:

        #2진수를 key로, 10진수값을 value(tuple 형태)로 저장한다.
        num_dict[item] = (int(item, 2), )

    #숫자 크기대로 오름차순 정렬
    num_dict = sorted(num_dict.items(), key=lambda item: item[1])
    #print(num_dict)

    return num_dict
    
    

#전체 입력값들 저장한 list
#입력되는 값들의 비트수는 동일하다고 정함
m = ['0000', '0001', '0010', '1000', '0101', '0110', '1001', '1100', '0111', '1101', '1111']
num_dict = get_dict(m)
# total_dict = get_pi(num_dict)
# final_dict = get_pi(total_dict)
print(get_pi(num_dict))