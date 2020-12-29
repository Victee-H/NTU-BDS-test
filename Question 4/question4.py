import numpy as np

"""
Seed Filling method:
a) push seed pixels into the stack
b) if stack is empty, turn to e) else turn to c)
c) pop one pixel from the stack and tag it as with the group number
check if the neighbors are 0 or tagged number,if not push them into the stack
d) turn to b)
e) end
"""


def four_connectivity(i,j,inn,m,n,image,label):
    if j-1 >= 0 and image[i][j-1] == -1:
        inn.append([i,j-1])
    if j+1 < n and image[i][j+1] == -1:
        inn.append([i,j+1])
    if i-1 >= 0 and image[i-1][j] == -1:
        inn.append([i-1,j])
    if i+1 < m and image[i+1][j] == -1:
        inn.append([i+1,j])

    if inn:
        p_label = inn.pop()
        image[p_label[0],p_label[1]] = label
        four_connectivity(p_label[0],p_label[1],inn,m,n,image,label)


def eight_connectivity(i,j,inn,m,n,image,label):
    if j-1 >= 0 and image[i][j-1] == -1:
        inn.append([i,j-1])
    if j+1 < n and image[i][j+1] == -1:
        inn.append([i,j+1])
    if i-1 >= 0 and image[i-1][j] == -1:
        inn.append([i-1,j])
    if i+1 < m and image[i+1][j] == -1:
        inn.append([i+1,j])
    if j - 1 >= 0 and i - 1 >= 0 and image[i - 1][j - 1] == -1:
        inn.append([i - 1, j - 1])
    if j + 1 < n and i - 1 >= 0 and image[i - 1][j + 1] == -1:
        inn.append([i - 1, j + 1])
    if j - 1 >= 0 and i + 1 < m and image[i + 1][j - 1] == -1:
        inn.append([i + 1, j - 1])
    if j + 1 < n and i + 1 < m and image[i + 1][j + 1] == -1:
        inn.append([i + 1, j + 1])

    if inn:
        p_label = inn.pop()
        image[p_label[0],p_label[1]] = label
        eight_connectivity(p_label[0],p_label[1],inn,m,n,image,label)


def main():
    image = np.loadtxt('../../Question 4/input_question_4.txt', dtype=int)

    image_4 = image.copy()
    image_8 = image.copy()

    index = (image == 1)
    image_4[index] = -1
    image_8[index] = -1

# four_connectivity
    m, n = image_4.shape
    label = 1
    inn = []

    for j in range(n):
        for i in range(m):
            if image_4[i][j] == -1:
                image_4[i][j] = label
                four_connectivity(i, j, inn, m, n, image_4, label)
                label += 1

    print(image_4)
    print("________")

# eight_connectivity
    m, n = image_8.shape
    label = 1
    inn = []

    for j in range(n):
        for i in range(m):
            if image_8[i][j] == -1:
                image_8[i][j] = label
                eight_connectivity(i,j,inn,m,n,image_8,label)
                label += 1

    print(image_8)
    # with open('output_question_4.txt', 'a') as f4:
    #     np.savetxt(f4, image_4, fmt="%d",footer='\n',comments='')
    #     np.savetxt(f4, image_8, fmt="%d",footer='\n',comments='')
    # f4.close()


if __name__ == "__main__":
    main()