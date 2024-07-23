# Python script to brute force an encrypted file using the rockyou.txt password list.

from zipfile import ZipFile

# This line imports the ZipFile class from Python's zipfile library. This class allows you to work with ZIP files, including opening, reading, and extracting them.

def crack_password(password_list, obj):
    idx = 0
    with open(password_list, 'rb') as f:
        for line in f:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print("Password found at line", idx)
                    print("Password is", word.decode())
                    return True
                except:
                    continue
    return False

# This function tries each password from a list to see if it can unlock the ZIP file.
# 'password_list': a file containing potential passwords (one per line).
# 'obj': The 'ZipFile' object representing the ZIP file you want to crack.
# It reads each line from the password list, splits it into possible passowrds, and tries each one.
# If a password successfully unlocks the ZIP file, it prints the password and its line number, then stops searching.
# If none of the passwords work, it returns 'False'.

def main():
    password_list = "rockyou.txt"
    zip_file = "enc.zip"

    # ZipFile object initialised
    obj = ZipFile(zip_file)

    # Count of number of words present in file
    cnt = len(list(open(password_list, "rb")))

    print("There are", cnt, "passwords to test")

    if crack_password(password_list, obj) == False:
        print("[+] Password not found in list")

# This function sets up the ZIP file and password list, then calls crack_password to attempt to unlock the ZIP file.
# password_list = "rockyou.txt": The file with potential passwords.
# zip_file = "enc.zip": The encrypted ZIP file you want to crack.
# obj = ZipFile(zip_file): Creates a ZipFile object for the encrypted file.
# cnt = len(list(open(password_list, "rb"))): Counts the number of potential passwords.
# print("There are", cnt, "passwords to test"): Displays the number of passwords being tested.
# It then calls crack_password and prints a message if the password wasn’t found.

if __name__ == "__main__":
    main()

# This line ensures that the main function runs only if the script is executed directly (not imported as a module).
