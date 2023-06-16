import sys
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from pathlib import Path


class Merger:

    def __init__(self, pdfs, output="output", verbose=False):
        self.pdfs = pdfs
        self.output = output
        self.merger = PdfMerger()
        self.verbose = verbose

    def merge(self):
        for pdf in self.pdfs:
            if self.verbose:
                print("Merging:", pdf)
            self.merger.append(pdf)
        if self.verbose:
            print("Saving...")
        self.merger.write(self.output)
        self.merger.close()

        print(f"Generated: {self.output}")


class Deleter:

    def __init__(self, pdf, pages, pdf_reader_args=None, output="output.pdf", verbose=False):
        pdf_reader_args = {"stream": pdf} | pdf_reader_args
        self.infile = PdfReader(pdf, **pdf_reader_args)
        self.writer = PdfWriter()
        self.output = output
        self.verbose = verbose
        self.pages = sorted(tuple(
            set(range(self.infile.numPages)) - set(map(int, pages))
        ))

    def delete_pages(self):
        for i in self.pages:
            if self.verbose:
                print("Deleting page:", i)
            p = self.infile.pages[i]
            self.writer.add_page(p)

        with open(self.output, 'wb') as f:
            self.writer.write(f)

        return 0
