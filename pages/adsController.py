


from bs4 import BeautifulSoup


class Ads:

    """
        Esta clase se encarga de insertar 
        las etiquetas y scripts para mostrar
        los modales de anuncios
    """

    def __init__(self,content:str):
        self.content = content
        self.soup = BeautifulSoup(self.content , 'html.parser')


    def insertAds(self) -> str:

        if self.soup.html != None:
            self.__insertHtmlTags()
            return str(self.soup)

        else:
            return ''

    def __insertHtmlTags(self):

        """ Inserta las etiquetas """

        # Insert to modal ads stylles
        adsStyles = self.soup.new_tag('link',href="http://localhost:8000/static/css/modals-ads.css",rel="stylesheet")
        self.soup.html.head.append(adsStyles)

        # Insert to html container modal
        adsHtmlContainer = self.soup.new_tag('div',id="modal-container")
        self.soup.body.append(adsHtmlContainer)    

        # Insert to ads Script
        adsSctip = self.soup.new_tag('script',src="http://localhost:8000/static/js/modal-ads.js")
        self.soup.body.append(adsSctip)
        
