def testing():
    print("hugo carcamo")

#example 1 read file
def read_data(filename):
    # pipe a text line in a file with a Python code
    fileuser = open(filename, 'r')

    #use a loop to go over each line in fileuser
    for each in fileuser:
        print(each)

#EXERCISE

def email_read():
    try:
        with open("user_email.txt", "r") as infile:
            gmail_count = 0
            yahoo_count = 0
            hotmail_count = 0
            for line in infile:
                email = line.strip().lower()
                if "@gmail" in email:
                    gmail_count += 1
                elif "@yahoo" in email:
                    yahoo_count += 1
                elif "@hotmail" in email:
                    hotmail_count += 1
        with open("reportemail.txt", "w") as outfile:
            outfile.write(f"gmail = {gmail_count}\n")
            outfile.write(f"yahoo = {yahoo_count}\n")
            outfile.write(f"hotmail = {hotmail_count}\n")
    except:
        print("Error reading file")
