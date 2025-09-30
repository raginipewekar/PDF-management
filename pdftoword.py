import glob
from pdf2docx import Converter

folder = r"C:\Users\ragin\Downloads\final pharma"

for pdf in glob.glob(folder + "/*.pdf"):
    docx = pdf.replace(".pdf", ".docx")
    cv = Converter(pdf)
    cv.convert(docx)
    cv.close()
