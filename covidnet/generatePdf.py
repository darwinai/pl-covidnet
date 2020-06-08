import pdfkit
import os

with open("pdftemplate/pdftemplate.html") as f:
    txt = f.read()
    txt = txt.replace("${PREDICTION_CLASSIFICATION}", 'normal')
    txt = txt.replace("${X-RAY-IMAGE}", 'ex-covid.jpeg')
    print(txt)
    with open("pdftemplate/specific.html", 'w') as writeF:
      writeF.write(txt)

pdfkit.from_file(['pdftemplate/specific.html'], 'out.pdf')

# cleanup
os.remove("pdftemplate/specific.html")
