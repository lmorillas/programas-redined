# coding: utf-8

def lcs(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])

    return lcs_set


def extrae_centro(dc_cont):
    try:
        #if len(dc_cont) > 1:
        rawcentro = dc_cont[-2]
        return rawcentro.split(';')[0]
    except:
        print '-->', dc_cont
    return ''


def centro(datos):
    try:
        d = datos.split(';')[0]
        x = d.find('(')
        if x != -1:
            d = d[:x]
        return d.strip()
    except:
        print '---> ', datos
    return ''

def centro_dir(datos):
    return ', '.join(datos.split(';')[1:3]).strip()

import json
centros = json.load(open('../centros_loc.json'))
red = json.load(open('../redined.json'))

def latlon(direccion):
    cen = centros.get(direccion)
    if cen:
        return "{},{}".format(cen[0], cen[1])
    else:
        return ''


def crea_item(dato):
    item = {}
    item['label'] = dato.get('DC__title')[0]
    item['centro'] = [centro(c) for c in dato.get('centro_ed')]
    item['año'] = dato.get('DCTERMS__issued')
    item['latlon'] = [latlon(centro_dir(c))  for c in dato.get('centro_ed')]
    item['nivel'] = dato.get('nivel')
    item['pdf'] = dato.get('citation_pdf_url')
    item['url'] = dato.get('citation_abstract_html_url')
    item['destinatarios'] = dato.get('audiencia')
    item['medio'] = dato.get('DCTERMS__medium')
    item['uri'] = dato.get('DC__identifier')[0]
    item['temas'] =dato.get('DC__subject')
    return item

items = []

for r in red:
    items.append(crea_item(r))

datamodel = {'properties': {'url': {'valueType': 'url' }, 'pdf': {'valueType': 'url'}},
                        'types' : {'Item': {'label': 'proyecto', 'pluralLabel': 'proyectos'}}}


datos = {'items': items}
datos.update(datamodel)

json.dump(datos, open('programas_redined.js', 'w'))
