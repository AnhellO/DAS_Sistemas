#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  historicas.py
#  
#  Copyright 2017 clemente <clemente@clemente-K53E>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from bs4 import BeautifulSoup
import requests
#~ import PyPDF2
import urllib.request  as request
import urllib.response as response
import re
import time
def main():
    
    #~ download_file("http://www.historicas.unam.mx/publicaciones/revistas/novohispana/pdf/novo44/533.pdf")
    #~ pdfObject = open('document.pdf', 'rb')
    #~ pdfReader = PyPDF2.PdfFileReader(pdfObject)
    #~ print(pdfReader.numPages)
    #~ pageObject = pdfReader.getPage(3)
    #~ print(pageObject.extractText())
    
    #~ print(type(pdfReader))
    
    
    #~ for i in range(pdfReader.numPages):
        #~ page = pdfReader.getPage(i)
        #~ print(page.extractText())
        #~ print('*'*80)

    #~ r = requests.get('http://www.historicas.unam.mx/publicaciones/revistas/novohispana/novoabc.html')
    #~ variable = 'pdf/novo07/0073.pdf'
    #~ download_file('http://www.historicas.unam.mx/publicaciones/revistas/novohispana/' + variable,str(3))

    #~ with open('pagina.html','r+') as f:
        #~ a = f.read()
    
    with open('requirements.txt','r+') as g:
        h = g.read()
    
    i = 420
    for line in h.splitlines():
        download_file('http://www.historicas.unam.mx/publicaciones/revistas/novohispana/' + line,str(i))
        time.sleep(10)
        i+=1
       
    #~ b = BeautifulSoup(a,'lxml')
    
    #~ lista = b.find_all(attrs={'target':'_blank'})
    #~ lista = b.find_all(string = 'pdf')
    #~ r = open("requirements.txt",'w')
    
    #~ for i in lista:
        #~ if re.search('pdf$',i['href']):        
            #~ print(i['href'])
            #~ r.write(i['href'])
            #~ r.write('\n')

        #~ else:
            #~ print(re.search('pdf',i.text))
            #~ print(i['href'])

   #~ print(b.find_all('a'))
    
def download_file(download_url,i):
    response = request.urlopen(download_url)
    file = open("./pdf/document" + i + ".pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed")    
    
if __name__ == '__main__':
    main()
