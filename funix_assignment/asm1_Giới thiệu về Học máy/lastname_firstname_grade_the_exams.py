"""grade_the_exams.
 Dau vao la du lieu chua bai thi cua tat ca hoc sinh trong 1 lop. 
 Chuong trinh tinh diem thi, thong ke diem, cuoi cung tra ve 1 file text chua ket qua.
 Luu y: Cac du lieu khong hop le se bi bo qua

"""

import numpy as np

file_name = input("Enter a class file to grade,\
 must have extension of the file (i.e. .txt): ")
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
split_line = []
tot_invalid = 0
tot_valid = 0
result = []
display_res = []


def check_data(tot_invalid, tot_valid):
    """Kiem tra su hop le cua tung dong du lieu
    
    Neu khong hop le se khong duoc xu ly o cac buoc tiep theo
    
    Args:
        tot_invalid: tong so du lieu bi sai
        tot_valid: tong so du lieu hop le
    Returns:
        tot_invalid: tong so du lieu bi sai
        tot_valid: tong so du lieu hop le
    """
    for i in range(len(split_line)):
        if len(split_line[i]) != 26:
            print('Invalid line of data: does not contain exactly 26 values:\n', read_data[i])
            tot_valid -= 1
            tot_invalid += 1
            split_line[i].append('ERROR')
        else:
            if split_line[i][0][0] != 'N':
                print('Invalid line of data: N# is invalid\n', split_line[i][0])
                tot_valid -= 1
                tot_invalid += 1
                split_line[i].append('ERROR')
            elif not split_line[i][0][1:].isnumeric() or len(split_line[i][0][1:]) != 8:
                print('Invalid line of data: N# is invalid\n', split_line[i][0])
                tot_valid -= 1
                tot_invalid += 1
                split_line[i].append('ERROR')
    if tot_invalid == 0:
        print('No errors found!')
    return tot_invalid, tot_valid


def grade_class(split_line, answer_key):
    """Cham diem mot lop chua nhieu hoc sinh
    
    Args:
        split_line: xu ly file text tro thanh list chua bai thi cua hoc sinh
        answer_key: ket qua de cho diem bai thi
    Returns:
        result: 1 mang chua ket qua cua toan bo hoc sinh trong lop do
    """
    list_ans = answer_key.split(",")
    for line in split_line:
        score = score_test(line, list_ans)
        if score is not None:
            result.append(score)
            display_res.append(line[0] +','+ str(score))
    return result


def score_test(test_list, answer_key):
    """cham diem cho tung hoc sinh
    
    Args:
        test_list: bai thi cua tung hoc sinh trong lop
        answer_key: ket qua de cho diem bai thi
    Returns:
        score: diem cua tung hoc sinh 
    """
    if len(answer_key) != 25:
        print("Answer key is invalid")
        return -1
    elif test_list[-1] == 'ERROR':
        return None
    else:
        score = 0
        for i in range(len(answer_key)):
            test_item = test_list[i + 1]
            if len(test_item) == 0:
                score += 0
            elif test_item == answer_key[i]:
                score += 4
            else:
                score -= 1
    return score


def score_stat(result):
    """thong ke diem cua lop hoc
    
    Args:
        result: mang numpy chua ket qua hoc sinh trong lop
    Returns:
        max_score: diem cao nhat
        min_score: diem thap nhat
        avg_score: trung binh
        median_res: trung vi
        range_score: mien gia tri cua diem (cao nhat tru thap nhat)
    """
    np_result = np.array(result)
    max_score = np.max(np_result)
    min_score = np.min(np_result)
    avg_score = np.average(np_result)
    median_res = int(np.median(np_result))
    range_score = max_score - min_score
    return max_score, min_score, avg_score, median_res, range_score


try:
    with open("raw_data/"+file_name, 'r') as file:
        for i, l in enumerate(file):
            tot_valid += 1
        file.seek(0)
        read_data = file.read().split('\n')
        for d in read_data:
            d = d.split(',')
            split_line.append(d)

    print('Successfully opened', file_name)
except:
    raise

print('**** ANALYZING ****')
tot_invalid, tot_valid = check_data(tot_invalid, tot_valid)
    
print('**** REPORT ****')
print('Total valid lines of data: ', tot_valid)
print('Total invalid lines of data: ', tot_invalid)

result = grade_class(split_line, answer_key)
max_score, min_score, avg_score, median_res, range_score = score_stat(result)

print('Mean (average) score:', "{:.2f}".format(avg_score))
print('Highest score:', max_score)
print('Lowest score:', min_score)
print('Range of scores:', range_score)
print('Median score:', median_res)
