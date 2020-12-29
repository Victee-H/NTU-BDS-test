def index2code(index,L1=4,L2=8,L3=5,L4=9,L5=6):
    x6 = index//(L5*L4*L3*L2*L1)
    x5 = (index-L5*L4*L3*L2*L1*x6)//(L4*L3*L2*L1)
    x4 = (index-L5*L4*L3*L2*L1*x6-L4*L3*L2*L1*x5)//(L3*L2*L1)
    x3 = (index-L5*L4*L3*L2*L1*x6-L4*L3*L2*L1*x5-L3*L2*L1*x4)//(L2*L1)
    x2 = (index-L5*L4*L3*L2*L1*x6-L4*L3*L2*L1*x5-L3*L2*L1*x4-L2*L1*x3)//L1
    x1 = index-L1*x2-L1*L2*x3-L1*L2*L3*x4-L1*L2*L3*L4*x5-L1*L2*L3*L4*L5*x6
    return x1,x2,x3,x4,x5,x6

def readindex():
    with open("../../Question 7/Question 7.2/input_index_7_2.txt", "r") as f:
        data = f.read()
        index_data = data.split()
        index_data = index_data[1:]
        index_data = list(map(int, index_data))
        return index_data


def main():
    index = readindex()
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    x6 = []
    for i in range(len(index)):
        u1,u2,u3,u4,u5,u6 = index2code(index[i])
        print(u1,u2,u3,u4,u5,u6)
        x1.append(u1)
        x2.append(u2)
        x3.append(u3)
        x4.append(u4)
        x5.append(u5)
        x6.append(u6)

    x1.insert(0, 'x1')
    x2.insert(0, 'x2')
    x3.insert(0, 'x3')
    x4.insert(0, 'x4')
    x5.insert(0, 'x5')
    x6.insert(0, 'x6')

    file = open('output_coordinates_7_2.txt', 'w')
    for i in range(len(x1)):
        s1 = str(x1[i]).replace('[', '').replace(']', '').replace("'", '').replace(',', '') + '\t'
        s2 = str(x2[i]).replace('[', '').replace(']', '').replace("'", '').replace(',', '') + '\t'
        s3 = str(x3[i]).replace('[', '').replace(']', '').replace("'", '').replace(',', '') + '\t'
        s4 = str(x4[i]).replace('[', '').replace(']', '').replace("'", '').replace(',', '') + '\t'
        s5 = str(x5[i]).replace('[', '').replace(']', '').replace("'", '').replace(',', '') + '\t'
        s6 = str(x6[i]).replace('[', '').replace(']', '').replace("'", '').replace(',', '') + '\n'
        file.write(s1)
        file.write(s2)
        file.write(s3)
        file.write(s4)
        file.write(s5)
        file.write(s6)

    file.close()


if __name__ == '__main__':
    main()