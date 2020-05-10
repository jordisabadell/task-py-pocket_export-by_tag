import os

def saveItemToFileByTag(fileName, title, url):
    '''
    '''
    f = open(fileName, "a")
    f.write(title + "\n" + url + "\n\n")
    f.close()