def wrap_in_tag(a, b):
    return f"<{a}>{b}</{a}>"
print(wrap_in_tag('p', 'hello'))
print(wrap_in_tag('b', 'world'))