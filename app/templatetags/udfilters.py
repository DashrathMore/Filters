from django import template
register=template.Library()

def count(value,arg):
    """"
    c,i=0,0
    l=len(arg)
    while i<len(value):
        if value[i:i+l]==arg:
            c+=1
        i+=1
    return c
    """
    """
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg)]==arg:
            c+=1
    return c
    """
    import re
    l=re.findall(arg, value)
    return len(l)

def swap(value):
    return value.swapcase()

register.filter('swap',swap)
register.filter('count', count)