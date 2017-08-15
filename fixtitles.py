import re

inputfile="biblio.bib.copy"


f = open(inputfile)
lines = f.readlines()
for line in lines:
  if ( line.find("title")  != -1 and line.find("=") != -1 and line.find("howpublished") == -1  ):
    if ( line.find('book')  == -1 ):
      if ( line.find('"{')  == -1 ):
        newline = line.replace('{','\"{')
        newline = newline.replace('}','}\"')
        if ( newline.find('{') == -1 ):
          newnewline = re.sub(r'title(\s?)=(\s?)"','title = "{',newline)
          newnewnewline = re.sub('"\s?,','}",',newnewline)
          print newnewnewline,
        else:
          print newline,
  else:
    print line,
