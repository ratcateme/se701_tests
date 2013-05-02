import random
import calendar
import string


def generate_number(min=5, max=10):
    return ''.join(random.choice(string.digits) for _ in xrange(random.randint(min, max)))

def generate_phone_number():
    buf = []
    buf.append(random.choice('+ '))
    buf.append(generate_number())

    if random.randint(0, 1) == 1:
        buf.append(' ext ')
        buf.append(generate_number())

    return ''.join(buf)

def generate_date():
    buf = []
    buf.append(str(random.randint(0, 99)))
    buf.append(random.choice(calendar.month_name[1:]))
    buf.append('{0:04}'.format(random.randint(0, 9999)))

    return ' '.join(buf)

def generate_string(min=10, max=100):
    return '"' + ''.join(random.choice(string.ascii_letters + string.digits + ' ') for _ in xrange(random.randint(min, max))) + '"'

def generate_email(min=10, max=100):
    EMAIL_NON_AT_CHARACTERS = string.ascii_letters + string.digits + '._'
    return ''.join(random.choice(EMAIL_NON_AT_CHARACTERS) for _ in xrange(random.randint(min, max))) + '@' + \
           ''.join(random.choice(EMAIL_NON_AT_CHARACTERS) for _ in xrange(random.randint(min, max)))

def generate_type():
    return random.choice(['mobile', 'home', 'work', 'other'])

class IndentingPrinter(object):
    INDENT = '    '

    def __init__(self):
        self.indent_width = 0
        self.buf = []

    def indent(self):
        self.indent_width += 1

    def dedent(self):
        self.indent_width -= 1

    def write(self, text):
        self.buf.extend(self.INDENT * self.indent_width + line + '\n' for line in text.split('\n'))

    def finish(self):
        return ''.join(self.buf)

def generate_sample(min=1, max=10):
    p = IndentingPrinter()
    p.write('addressbook ' + generate_string() + ' {')

    p.indent()

    for _ in xrange(random.randint(min, max)):
        p.write('person ' + generate_string() + ' {')
        p.indent()

        attribs = []

        if random.randint(0, 1) == 1:
            attribs.append('birthdate ' + generate_date())

        if random.randint(0, 1) == 1:
            attribs.append('email ' + generate_email())

        for _ in xrange(random.randint(0, 10)):
            attribs.append('phone(' + generate_type() + ') ' + generate_phone_number())

        for _ in xrange(random.randint(0, 10)):
            attribs.append('address(' + generate_type() + ') ' + generate_string())

        random.shuffle(attribs)

        p.write('\n'.join(attribs))

        p.dedent()
        p.write('}')

    p.dedent()

    p.write('}')

    return p.finish()

print(generate_sample())
