import pypdf
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = pypdf.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('supa.pdf')

pdf_combiner(inputs)