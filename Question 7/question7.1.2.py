def index2code(index,L1=50):
    x2 = index//L1
    x1 = index-L1*x2
    return x1,x2


def readindex():
    with open("../../Question 7/Question 7.1/input_index_7_1.txt", "r") as f:
        data = f.read()
        index_data = data.split()
        index_data = index_data[1:]
        index_data = list(map(int, index_data))
        return index_data


def main():
    index = readindex()
    x1 = []
    x2 = []
    for i in range(len(index)):
        u1,u2 = index2code(index[i])
        print(u1, u2)
        x1.append(u1)
        x2.append(u2)

    x1.insert(0,'x1')
    x2.insert(0,'x2')

    file = open('output_coordinates_7_1.txt', 'w')
    for i in range(len(x1)):
        s1 = str(x1[i]).replace('[', '').replace(']', '').replace("'", '').replace(',', '') + '\t'
        s2 = str(x2[i]).replace('[', '').replace(']', '').replace("'", '').replace(',', '') + '\n'
        file.write(s1)
        file.write(s2)
    file.close()


if __name__ == '__main__':
    main()