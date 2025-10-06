def testing():
    print("hugo carcamo")

#example 1 read file
def read_data(filename):
    # pipe a text line in a file with a Python code
    fileuser = open(filename, 'r')

    #use a loop to go over each line in fileuser
    for each in fileuser:
        print(each)