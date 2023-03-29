day_dict = {'월' : 0, '화' : 1, '수' : 2, '목' : 3, '금' : 4}

def position_tolist(start_pos, end_pos):  # 312, 323
    num_between = range(start_pos, end_pos)
    pos_list = [num for num in num_between if (num % 10 < 5 and num % 10 != 0)]
    
    return pos_list    # 312, 313, 314, 321, 322, 323

def position_finder(item):
    day, start, end = item['day'], item['start_time'], item['end_time']

    start_hr = int(start[0:2])
    start_min = int(start[2:4])
    end_hr = int(end[0:2])
    end_min = int(end[2:4])

    #시작포지션
    start_first_index = (start_hr - 8) + (day_dict[day] * 10)
    start_second_index = (start_min // 15) + 1

    #끝포지션

    end_first_index = (end_hr - 8) + (day_dict[day] * 10)
    end_second_index = (end_min // 15) + 1
    
    start_pos = int(f'{start_first_index}{start_second_index}')
    end_pos = int(f'{end_first_index}{end_second_index}')
    result = position_tolist(start_pos,end_pos)
    
    return result

def position_finder_list(classtime):

    result = [position_finder(item) for item in classtime]
    return result

# print(position_finder_list([{'day' : '화', 'start_time' : '1400', 'end_time' : '1530'}, {'day' : '목', 'start_time' : '1315', 'end_time' : '1445'}]))