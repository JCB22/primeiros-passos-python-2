import xml.dom.minidom


if __name__ == '__main__':
    domtree = xml.dom.minidom.parse('data.xml')
    group = domtree.documentElement

    persons = group.getElementsByTagName('person')

    """
    
    Mostrando no console as informações contidas no arquivo XML
    
    """

    for person in persons:
        print("-----PERSON-----")
        if person.hasAttribute('id'):
            print(F"ID: {person.getAttribute('id')}")

        print(f"NAME: {person.getElementsByTagName('name')[0].childNodes[0].data}")
        print(f"AGE: {person.getElementsByTagName('age')[0].childNodes[0].data}")
        print(f"WEIGHT: {person.getElementsByTagName('weight')[0].childNodes[0].data}")
        print(f"HEIGHT: {person.getElementsByTagName('height')[0].childNodes[0].data}")

    """
    
    Editando as informações do arquivo XML
    
    """

    # persons[2].getElementsByTagName('name')[0].childNodes[0].nodeValue = "New Name"
    # persons[0].setAttribute('id', '100')
    # persons[3].getElementsByTagName('age')[0].childNodes[0].nodeValue = "-10"
    # domtree.writexml(open('data.xml', 'w'))

    """
    
    Adicionando novas informações ao arquivo XML
    
    """

    newperson = domtree.createElement('person')
    newperson.setAttribute('id', '6')

    name = domtree.createElement('name')
    name.appendChild(domtree.createTextNode('Paul Green'))
    age = domtree.createElement('age')
    age.appendChild(domtree.createTextNode('33'))
    weight = domtree.createElement('weight')
    weight.appendChild(domtree.createTextNode('99'))
    height = domtree.createElement('height')
    height.appendChild(domtree.createTextNode('203'))

    newperson.appendChild(name)
    newperson.appendChild(age)
    newperson.appendChild(weight)
    newperson.appendChild(height)

    group.appendChild(newperson)

    domtree.writexml(open('data.xml', 'w'))