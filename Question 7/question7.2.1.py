def code2index(x1,x2,x3,x4,x5,x6,L1=4,L2=8,L3=5,L4=9,L5=6):
    index = L1*L2*L3*L4*L5*x6 + L1*L2*L3*L4*x5 + L1*L2*L3*x4 + L1*L2*x3 + L1*x2 + x1
    return index

def readcoordinates():
    with open("../../Question 7/Question 7.2/input_coordinates_7_2.txt", "r") as f:
        data = f.read()
        coordinates_data = data.split()
        coordinates_data = coordinates_data[6:]
        coordinates_data = list(map(int, coordinates_data))
        x1 = coordinates_data[::6]
        x2 = coordinates_data[1::6]
        x3 = coordinates_data[2::6]
        x4 = coordinates_data[3::6]
        x5 = coordinates_data[4::6]
        x6 = coordinates_data[5::6]
        return x1,x2,x3,x4,x5,x6


def main():
    x1,x2,x3,x4,x5,x6 = readcoordinates()
    index = []
    for i in range(len(x1)):
        ind = code2index(x1[i],x2[i],x3[i],x4[i],x5[i],x6[i])
        index.append(ind)

    index.insert(0, 'index')
    print(index)

    file = open('output_index_7_2.txt', 'w')
    for i in range(len(index)):
        s = str(index[i]).replace('[', '').replace(']', '').replace("'", '').replace(',', '') + '\n'
        file.write(s)
    file.close()

if __name__ == '__main__':
    main()