import pandas as pd

def readFile(filePath, delimiter):
    matrix = pd.read_table(filePath, delimiter, header=None)
    if matrix.shape[0] != matrix.shape[1]:
        raise pd.errors.ParserError
    
    return matrix

def writeFile(filePath, newMatrix):
    file = open(filePath.replace(".txt", "-new.txt"), "w") 
    file.write(newMatrix.to_string()) 
    file.close() 

def main():
    try:
        filePath = input("Input file path: ")
        delimiter = input("Input delimiter: ")

        matrix = readFile(filePath, delimiter)
        writeFile(filePath, matrix.T)

    except FileNotFoundError:
        print("File not found.")

    except pd.errors.ParserError:
        print("Array is not square")

if __name__ == "__main__":
    main()