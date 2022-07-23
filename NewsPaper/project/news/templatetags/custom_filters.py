from django import template


register = template.Library()


@register.filter(name='censor')
def censor(value:str):
    if not isinstance(value, str):
        value = str(value)

    for word in word_list:
        if word.lower() not in word_list:
            continue
        value = value.replace(word[1:], '*' * (len(word)-1))
    return value