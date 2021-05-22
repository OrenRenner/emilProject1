#!/usr/bin/python
# -*- coding: utf8 -*-

with open('in.txt', 'w') as file:
    file.write('Она пришла под утро.\
\n Вошла осторожно,     тихо,,,,,,,, ...........бесшумно ступая, плывя по комнате, словно призрак, привидение, а единственным звуком, выдававшим ее движение, был шорох накидки, прикасавшейся к голому телу. Однако именно этот исчезающе тихий, едва уловимый шелест разбудил ведьмака, а может, только вырвал из полусна, в котором он мерно колыхался, словно погруженный в бездонную топь, висящий между дном и поверхностью спокойного моря, среди легонько извивающихся нитей водорослей.')

with open('out.txt', 'w') as outfile:
    with open('in.txt', 'r') as file:
        f = file.read()
        f = f.lower()
        p = f.split('\n')
        d = ' '.join(p)
        print(d)
        a = d.split(' ')
        c = a.copy()
        for i in a:
            if i in '':
                c.remove(i)
        for index, value in enumerate(c):
            if value.isalpha() is False:
                if value[0].isalpha() is False:
                    temp = list(value)
                    while temp[0] in ',.!&;:?-\ nt\'@#$%^*()_+=':
                        temp.pop(0)
                    t = ''.join(temp)
                    c[index] = t
                if value[-1] in ',.!&;:?-\ nt\'@#$%^*()_+=':
                    temp = list(value)
                    while temp[-1] in ',.!&;:?-\ nt\'@#$%^*()_+=':
                        temp.pop()
                    t = ''.join(temp)
                    c[index] = t
        c.sort()
        d = list()
        for i in c:
            counter = 0
            for j in c:
                if i == j and i not in d:
                    counter += 1
            if i not in d:
                d.append(i)
                outfile.write(f'{i} - {counter}\n')

