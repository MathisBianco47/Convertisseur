from markdown import *
fichiermd = open('/Users/mathisbianco/Documents/Convertisseur /index.md') 
fichierHTML = open('fichierHTMLconverti.html','w') 
for texte in fichiermd:    
	html = markdown(texte)  
	fichierHTML.write(html) 