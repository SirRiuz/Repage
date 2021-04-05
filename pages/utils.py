

# Python
from operator import itemgetter
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
    """
      Retorna una lista de archivos. Esta lista 
      sera utilizada para mostrar los archivos en 
      el panel de administracion de una pagina
    """
    dataList = []
    for file in os.listdir(path):
        preority = 'b'
        nameType = 'Archivo'
        isDir = False
        tempPathFile = path+file
        typeFile = mimetypes.guess_type(file)[0]

        if os.path.isdir(tempPathFile):
            isDir = True
            preority = 'a'
            nameType = 'Carpeta'

        data = ({
            'name':file,
            'type':typeFile,
            'isDir':isDir,
            'preority':preority,
            'nameType':nameType
            })
            
        dataList.append(data)

    return sorted(dataList,key=itemgetter('preority'))

