# Junta fonte.html + imagens de img/ -> pagina.html (link) e Eu-Tambem-Jogo.html (ficheiro para a escola)
import base64, json, os, glob
d = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(d, 'fonte.html'), encoding='utf-8').read()
imgs = {os.path.basename(p)[:-5]: 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
        for p in sorted(glob.glob(os.path.join(d, 'img', '**', '*.webp'), recursive=True))}
hs = open(os.path.join(d, 'historias-sensoriais.json'), encoding='utf-8').read()
page = src.replace('{/*IMAGENS*/}', json.dumps(imgs)).replace('[/*HISTORIAS_SENSORIAIS*/]', hs.replace('</', '<\\/'))
open(os.path.join(d, 'pagina.html'), 'w', encoding='utf-8').write(page)
open(os.path.join(d, 'Eu-Tambem-Jogo.html'), 'w', encoding='utf-8').write(
    '<!doctype html><html lang="pt-PT"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    '<style>body{margin:0}[hidden]{display:none!important}</style></head><body>' + page + '</body></html>')
os.makedirs(os.path.join(d, 'site'), exist_ok=True)
open(os.path.join(d, 'site', 'index.html'), 'w', encoding='utf-8').write(open(os.path.join(d, 'Eu-Tambem-Jogo.html'), encoding='utf-8').read())
print(len(imgs), 'imagens;', len(page)//1024, 'KB')
