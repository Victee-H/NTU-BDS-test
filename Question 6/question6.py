"""
ray method:
Draw a ray from the test point
Calculate how many points the ray intersects the boundary of the polygon
If it is an odd number, it means that the test point is in the polygon, otherwise it is not
"""


def crossing_number(x0,y0,polygon):
    crossings = 0
    for i in range(polygon.count-1):
        slope = (polygon.y[i+1]-polygon.y[i])/(polygon.x[i+1]-polygon.x[i])
        cond1 = (polygon.x[i]<=x0) and (x0<polygon.x[i+1])
        cond2 = (polygon.x[i+1]<=x0) and (x0<polygon.x[i])
        above = (y0 < slope * (x0 - polygon.x[i]) + polygon.y[i])
        if (cond1 or cond2) and above:
            crossings += 1
    if crossings % 2 != 0:
        state = 'inside'
    else:
        state = 'outside'
    return state


class polygon():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.count = len(x)


def main():
    with open("../../Question 6/input_question_6_polygon.txt", "r") as f:
        data = f.read()  # 读取文件
        polygon_data = data.split()
        polygon_data = list(map(int, polygon_data))
        x = polygon_data[::2]
        y = polygon_data[1::2]

    with open("../../Question 6/input_question_6_points.txt", "r") as f:
        pdata = f.read()
        point_data = pdata.split()
        point_data = list(map(int, point_data))
        px = point_data[::2]
        py = point_data[1::2]
        print(px)
        print(py)

        polygons = polygon(x,y)
        file = open('output_question_6.txt', 'w')
        for i in range(len(px)):
            state = crossing_number(px[i],py[i],polygons)
            print(px[i],py[i],state)
            s = str(px[i]).replace("'", '').replace(',', '') + ' ' +str(py[i]).replace("'", '').replace(',', '') + ' '+ str(state).replace("'", '') +'\n'
            file.write(s)
        file.close()


if __name__ == "__main__":
    main()