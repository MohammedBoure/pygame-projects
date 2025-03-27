def point_in_rect(rect: tuple, point: tuple):
    # Check if a point is inside a rectangle
    x, y, dx, dy = rect
    xp, yp = point
    return x < xp < x + dx and y < yp < y + dy

def remove_data_repit_in_list(data_list):
    # Remove duplicate rectangles and combine their counters
    i = 0
    while i < len(data_list):
        j = i + 1
        while j < len(data_list):
            if data_list[i][0] == data_list[j][0]:
                data_list[i][1] += data_list[j][1]
                data_list.pop(j)
            else:
                j += 1
        i += 1
    return data_list

def finition(list1, list2):
    # Resolve conflicts between Player 1 and Player 2 squares
    i = 0
    while i < len(list1):
        j = 0
        while j < len(list2):
            if list1[i][0] == list2[j][0]:
                if list1[i][1] > list2[j][1]:
                    list1[i][1] -= list2[j][1]
                    list2.pop(j)
                elif list1[i][1] < list2[j][1]:
                    list2[j][1] -= list1[i][1]
                    list1.pop(i)
                    i -= 1
                    break
                else:
                    list1.pop(i)
                    list2.pop(j)
                    i -= 1
                    break
            else:
                j += 1
        i += 1

def Number_of_bounding_squares(listp1, cplistp1, cplistp2, Increasing):
    # Calculate influence of neighboring squares
    for square in listp1:
        cpt = 0
        x, y, dx, dy = square[0]
        directions = [(-dx, 0), (dx, 0), (0, -dy), (0, dy)]
        for dx, dy in directions:
            neighbor = (x + dx, y + dy, square[0][2], square[0][3])
            if neighbor in cplistp1:
                cpt += Increasing
            if neighbor in cplistp2:
                cpt -= Increasing
        square[2] = cpt