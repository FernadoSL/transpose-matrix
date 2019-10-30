import pandas as pd

def readFile(filePath, delimiter):
    matrix = pd.read_table(filePath, delimiter, header=None)
    if matrix.shape[0] != matrix.shape[1]:
        raise pd.errors.ParserError
    
    return matrix

def writeFile(filePath, newMatrix): 
    newFilePath = filePath + 'new.txt'
    newMatrix.to_csv(newFilePath, header = False, index = False)
    return newFilePath

def replaceAllChar(old, new, matrix):
    matrix = matrix.replace(to_replace = old, value = new)
    return matrix

def replacePoint(pointA, pointB, matrix):
    temp = matrix[pointA[0]][pointA[1]]
    matrix[pointA[0]][pointA[1]] = matrix[pointB[0]][pointB[1]]
    matrix[pointB[0]][pointB[1]] = temp
    return matrix

def main():
    try:
        filePath = input("Input file path: ")
        delimiter = input("Input delimiter: ")
        while True:
            matrix = readFile(filePath, delimiter)
            option = input("Choose a option: 1 - Transpose, 2 - Replace All, 3 - Replace Point, Else - break")

            if option == '1':
                matrix = matrix.T

            elif option == '2':
                oldChar = input("Input char to replace: ")
                newChar = input("Input new value: ")
                matrix = replaceAllChar(oldChar, newChar, matrix)

            elif option == '3':
                oldPointX = int(input("Input old x: "))
                oldPointY = int(input("Input old y: "))
                newPointX = int(input("Input new x: "))
                newPointY = int(input("Input new y: "))
                matrix = replacePoint((oldPointX, oldPointY), (newPointX, newPointY), matrix)

            else:
                break

            print(matrix)
            filePath = writeFile(filePath, matrix)

    except FileNotFoundError:
        print("File not found.")

    except pd.errors.ParserError:
        print("Array is not square")

if __name__ == "__main__":
    main()