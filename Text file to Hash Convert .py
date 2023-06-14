#### import library
import hashlib
import os
from tkinter import *
from tkinter import filedialog,messagebox

class Fileopen:
    def __init__(self):
        self.root = Tk()
        self.root.title("File to hash convert")
        self.file_open = Button(text="Open File", command= self.file)
        self.file_open.pack()
        self.root.geometry("400x200")
        self.quit = Button(text="Quit", command=self.root.destroy)
        self.quit.pack()
        self.root.mainloop()

    def file(self):
        fielopenss = filedialog.askopenfilename()
        return fielopenss


################################################################################################

filess = Fileopen.file(0)

#####Open password world list file
file = open(filess, 'r')
data = file.readlines()


# clean data file  save in this lists
password_Dict = []
# file data ex
for i in data:
    password_Dict.append(i[0:-1])

# convert text to hash file to save list formate
hashList = []

# using hash code algrothem Sha256
for i in password_Dict:
    message = i.encode()  # encode the string as bytes
    hash_object = hashlib.sha256(message)  # create a SHA-256 hash object
    hash_hex = hash_object.hexdigest()  # get the hash value as a hex string
    hashList.append(hash_hex)


##### marging hash sha256 and text file code ZIP TO RETURN DICT
datazip = dict(zip(password_Dict, hashList))

# Convert the dictionary to a string representation
dict_str = str(datazip)

with open('OutPut TEXT file Sha256.txt', 'w') as f:
    # Write the string to the file
    f.write(dict_str)



save_path = ("Your File Is Complete This Path Is Save ------ ", os.getcwd())

###Message info show
messagebox.showinfo("Save file", save_path)

if __name__ == '__main__':
    Fileopen()




