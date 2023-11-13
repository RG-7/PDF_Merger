#   Project PDF Merger

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfMerger

merger = PdfMerger()
pdfiles = ["1.pdf", "2.pdf", "3.pdf"]

for filename in pdfiles:
    with open(filename, 'rb') as pdfFile:
        merger.append(pdfFile)

with open('merged.pdf', 'wb') as mergedFile:
    merger.write(mergedFile)

