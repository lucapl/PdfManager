import sys
from PyPDF2 import PdfMerger
from pathlib import Path


class Merger:

    def __init__(self, pdfs, output="output"):
        self.pdfs = pdfs
        self.output = output
        self.merger = PdfMerger(self.output)

    def merge(self):
        for pdf in self.pdfs:
            print("Merging:", pdf)
            self.merger.append(pdf)
        print("Saving...")
        self.merger.write(f".\\output\\{self.output}.pdf")
        self.merger.close()
        print(f"Generated: {self.output}.pdf")