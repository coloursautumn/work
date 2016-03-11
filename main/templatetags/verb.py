from django import template

register = template.Library()

@register.filter(name='chek')
def chek(object): 
	if object.value:
		return object

register.tag('chek', chek)
