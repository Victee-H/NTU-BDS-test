def code2index(x1,x2,L1=50):
    index = L1*x2 + x1
    return index

def readcoordinates():
    with open("../../Question 7/Question 7.1/input_coordinates_7_1.txt", "r") as f:
        data = f.read()
        coordinates_data = data.split()
        coordinates_data = coordinates_data[2:]
        coordinates_data = list(map(int, coordinates_data))
        x1 = coordinates_data[::2]
        x2 = coordinates_data[1::2]
        return x1,x2


def main():
    x1,x2 = readcoordinates()
    index = []

    for i in range(len(x1)):
        ind = code2index(x1[i],x2[i])
        index.append(ind)

    index.insert(0, 'index')
    print(index)

    file = open('output_index_7_1.txt', 'w')
    for i in range(len(index)):
        s = str(index[i]).replace('[', '').replace(']', '').replace("'", '').replace(',', '') + '\n'
        file.write(s)
    file.close()


if __name__ == '__main__':
    main()