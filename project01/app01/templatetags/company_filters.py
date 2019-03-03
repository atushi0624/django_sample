from django import template
 
register = template.Library()
 
@register.filter
def company_ID(querydict):
    company_ID = querydict.get('name')
 
    return "" if company_ID is None else company_ID