#starter of program
import os,shutil
#creating dictionary with file extention
dict_extentions={
    'audio_extention':('.mp3','.mpa'),
'video_extention':('.mp4','.mkv'),
'image_extention':('.jpg','.png'),
'doc_extention':('.txt','.pdf'),
}
#getting folder path from user for working
folderpath=input('enter path for sort file')
#defining function wich return list of same extention
def file_finder(folder_path,file_extentions):
    files=[]
    for file in os.listdir(folder_path):
        for extention in file_extentions:
            if file.endswith(extention):
                files.append(file)
    return files
#creating folder name and folder path
for name_extention,extention_tuple in dict_extentions.items():
    # print('calling Tuple')
    # print(file_finder(folderpath,extention_tuple))
    #creating folder and folder path
    folder_name=name_extention.split('_')[0] + 'Files'
    folder_path=os.path.join(folderpath,folder_name)
    os.makedirs(folder_path)
    #creating path for files and moving them in folder
    for item in file_finder(folderpath,extention_tuple):
        #print(item) --> print all files from folder path
        ##creating file path
        item_path=os.path.join(folderpath,item)
        new_path=os.path.join(folder_path,item)
        #moving file to new path or created folder path
        shutil.move(item_path,new_path)