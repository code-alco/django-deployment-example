from django import template

register=template.library()

def cut_it(value,string):
    """
    it cuts string from value given
    """
    value.replace(string,'')
    return value
 registe.filter('cut',cut_it)    
