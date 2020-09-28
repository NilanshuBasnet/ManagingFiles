#Simple Files management program using python

import os,shutil #importing os helps us to deal with folders in our computer and shutil helps in moving files in the folder
#Creating a dictionary which indicates the folders to be created
#You can add your own folder name and extentions below
Folders={
        'Audios':['.wav','.mp3','.3gp','.aa','.msv','wma'],
        'Videos':['.mp4','.mkv','.flv','.avi','.wmv','.m4v','.m4p'],
        'Images':['.png','.jpg','.bmp','.gif','.jpeg','.bat'],
        'Documents':['.doc','.xlsx','.xls','.pdf'],
        'Compressed':['.zip','.rar']
        }

#Creating function to check in which key the ext value is stored
def folder_creation(ext,file_name):
    available=False;#If the given extention is not defined in our dictionary
    for folder_name in Folders:
        if "."+ext in Folders[folder_name]:
            #Checking whether the folder name same as the key name is available or not
            if folder_name in files_folders:#If available copy the file to the folder
                shutil.move(os.path.join(Location,file_name),os.path.join(Location,folder_name))
                break
            else:#If not available create a folder and copy the file
                os.mkdir(os.path.join(Location,folder_name))
                shutil.move(os.path.join(Location,file_name),os.path.join(Location,folder_name))
                available=True;
                break
    if available==False:#If the given exenion is not available in our dictionary than store it in the file named Others
    #Cheking if others folder is available or not
        if "Others" in files_folders:#If found copy file
            shutil.move(os.path.join(Location,file_name),os.path.join(Location,"Others"))
        else:#If not found create folder and copy
            os.mkdir(os.path.join(Location,"Others"))
            shutil.move(os.path.join(Location,file_name),os.path.join(Location,"Others"))

valid=False;
while valid==False:
    #Asking the location of unmanaged folder with user
    Location=input("Enter the path of folder: ")
    if os.path.isdir(Location)==True:
        valid=True;
        files_folders=os.listdir(Location)#Stores all the files and folder of given location in a list
    else:
        print("Error! Invalid folder path.")

#Dealing only with files and excluding the folders available in given location
for i in files_folders:
    if os.path.isfile(os.path.join(Location,i))==True:
        folder_creation(i.split(".")[-1],i)#passing the value of ext and file_name
