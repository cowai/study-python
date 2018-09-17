import string

with open('design/email_template.txt', 'r') as f:
    t = string.Template(f.read())

# with の中で定義した t はインデントの外でも使える
contents = t.substitute(name='Mike', contents='How are you?')
print(contents)
