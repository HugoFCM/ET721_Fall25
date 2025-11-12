def testing():
    print("hugo carcamo")


# example 1 read file
def read_data(filename):
    # pipe a text line in a file with a Python code
    fileuser = open(filename, "r")

    # use a loop to go over each line in fileuser
    for each in fileuser:
        print(each)


# EXERCISE


def email_read():
    try:
        fileuser = open("user_email.txt", "r")
        gmail = 0
        yahoo = 0
        hotmail = 0
        for each in fileuser:
            if "@gmail" in each:
                gmail += 1
            elif "@yahoo" in each:
                yahoo += 1
            elif "@hotmail" in each:
                hotmail += 1
        fileuser.close()
        report = open("reportemail.txt", "w")
        report.write("gmail = " + str(gmail) + "\n")
        report.write("yahoo = " + str(yahoo) + "\n")
        report.write("hotmail = " + str(hotmail) + "\n")
        report.close()
    except:
        print("error reading file")
