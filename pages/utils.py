
import base64
import os
import mimetypes


def fileData(path:str) -> (dict):
    file = open(path,'r')

    contend = file.read().replace('\n','')
    #contend = base64.encodebytes(file.read().encode('utf-8'))
    typeFile = mimetypes.guess_type(path)[0]
    fileName = file.name
    file.close()
    return ({
        'type':typeFile,
        'contend':contend
    })


def pathRecursiveFile(path:str) -> (list):
    dataList = []
    for file in os.listdir(path):
        isDir = False
        tempPathFile = path+file
        typeFile = mimetypes.guess_type(file)[0]

        if os.path.isdir(tempPathFile):
            isDir = True

        data = ({'name':file,'type':typeFile,'isDir':isDir  })
        dataList.append(data)

    return dataList



#pathRecursiveFile('C:\\Users\Mateo Jimenez\Desktop\\repage\env\\repage\media\\0ea838d91149404cafb3cf563198c199\\styles')
#fileData('C:\\Users\Mateo Jimenez\Desktop\\repage\env\\repage\media\\0ea838d91149404cafb3cf563198c199\\index.html')



