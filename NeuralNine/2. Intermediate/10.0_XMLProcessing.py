import xml.sax


class GroupHandler(xml.sax.ContentHandler):

    """

    Faz o cabeçalho da pessoa

    """
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("-----------PERSON-----------")
            print(f"ID: {attrs['id']}")

    """
    
    Vê a tag do XML e adiciona o conteúdo dentro para as variáveis
    
    """
    def characters(self, content):
        if self.current == 'name':
            self.name = content
        elif self.current == 'age':
            self.age = content
        elif self.current == 'weight':
            self.weight = content
        elif self.current == 'height':
            self.height = content


    """
    
    Vê a tag do XML e mostra as informações de acordo com a tag vista
    
    """
    def endElement(self, name):
        if self.current == 'name':
            print(f"Name: {self.name}")
        elif self.current == 'age':
            print(f'Age: {self.age}')
        elif self.current == 'weight':
            print(f'Weight: {self.weight}')
        elif self.current == 'height':
            print(f'Height: {self.height}')
        self.current = ""

if __name__ == '__main__':
    handler = GroupHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse('data.xml')