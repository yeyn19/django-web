from django import template

register = template.Library() 

@register.filter
def my_filter(x):
    return (x % 5 == 0)


@register.simple_tag
def my_html(info):
    temp_html = "<table>  </table>"
    return mark_safe(temp_html)