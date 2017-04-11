import os

def rename():
    files = os.listdir(r'D:\web developer\files')
    
    path = os.getcwd()
    print('Current working path: ', path)
    os.chdir(r'D:\web developer\files')
    path = os.getcwd()
    print('Current working path: ', path)
    print(os.listdir(os.getcwd()))
    #os.rename('Konachan.com - 210845 blue_eyes blue_hair bubbles fuyu_no_yoru_miku hatsune_miku kyod+ long_hair snow twintails vocaloid.jpg', 
    #          '210845 blue_eyes blue_hair bubbles fuyu_no_yoru_miku hatsune_miku kyod+ long_hair snow twintails vocaloid.jpg')
    for file in files:
        lett = str.join('', [n for n in file if not n.isdigit()])

        os.rename(file, lett)
    
    
    
rename()