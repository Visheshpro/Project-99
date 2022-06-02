import shutil,time,os

path = "D:\PROJECTS\Python\Class Works"
days = 30*24*60*60*1000
deleteTime = time.time()-days

for root,folders,files in os.walk(path):
    for file in files:
        print(file)
        ctime = os.stat(root+'/'+file).st_ctime
        print(ctime)
        if ctime > deleteTime:
            print("true")
            os.remove(root+'/'+file)

        