path = "file/l1_2.txt"
matrix_size = None

def mass_to_matrix(mass):
    global matrix_size
    matrix_size = int(mass.pop(0))
    matrix = []
    for i in mass:
        matrix.append([int(x) for x in i.split(" ") if x.isdigit()])
    return matrix
def txt_reader(path):
    file = open(path, "r")
    text = file.read()
    mass = text.split("\n")
    return mass_to_matrix(mass)

def matrix_to_list(matrix):
    lst_of_links = []
    for x in range(matrix_size):
        for y in range(matrix_size):
            if matrix[x][y] != 0:
                lst_of_links.append((matrix[x][y], y + 1, x + 1))
            else:
                continue
    return lst_of_links

def kruskal(lst):
    lstSorted = sorted(lst, key=lambda x: x[0])
    links = set()
    dictionary = {}
    edge = []

    for i in lstSorted:
        if i[1] not in links or i[2] not in links:
            if i[1] not in links and i[2] not in links:
                dictionary[i[1]] = [i[1], i[2]]
                dictionary[i[2]] = dictionary[i[1]]
            else:
                if not dictionary.get(i[1]):
                    dictionary[i[2]].append(i[1])
                    dictionary[i[1]] = dictionary[i[2]]
                else:
                    dictionary[i[1]].append(i[2])
                    dictionary[i[2]] = dictionary[i[1]]

            edge.append(i)
            links.add(i[1])
            links.add(i[2])

    for i in lstSorted:
        if i[2] not in dictionary[i[1]]:
            edge.append(i)
            gr1 = dictionary[i[1]]
            dictionary[i[1]] += dictionary[i[2]]
            dictionary[i[2]] += gr1
    return edge

def result(mass):
    for i in mass:
        print(f"{i[1]} - {i[2]} = {i[0]}")

if __name__ == '__main__':
    matrix = txt_reader(path)
    lst = matrix_to_list(matrix)
    res = kruskal(lst)
    result(res)


