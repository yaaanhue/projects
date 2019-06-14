#!/usr/bin/env python3
import zipfile
newZip = zipfile.ZipFile('/root/Downloads/estatisticas.zip', 'w')
newZip.write('Caracteristicas_Gerais.zip', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('Educacao.zip', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('Leia-me.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('Leia-Me Caracteristicas_Gerais.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('Leia-Me Educacao.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('Leia-me Leia-me Saude.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('Leia-me Saude.zip', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('Leia-me Trabalho.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('Trabalho.zip', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()