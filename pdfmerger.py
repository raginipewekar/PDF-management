from PyPDF2 import PdfMerger
import os

# folder where your PDFs are stored
folder = r"C:\Users\ragin\Downloads\final pharma"

merger = PdfMerger()

# get all PDFs in the folder
for file in sorted(os.listdir(folder)):
    if file.endswith(".pdf"):
        merger.append(os.path.join(folder, file))

# save combined PDF
merger.write(os.path.join(folder, "colour_combined.pdf"))
merger.close()
