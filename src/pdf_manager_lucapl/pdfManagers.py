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
        pdf_reader_args = {"stream": pdf} | pdf_reader_args if pdf_reader_args else {"stream": pdf}
        self.infile = PdfReader(**pdf_reader_args)
        self.writer = PdfWriter()
        self.output = output
        self.verbose = verbose
        self.pages = sorted(tuple(
            set(range(self.infile.numPages)) - set(pages)
        ))

    def delete_pages(self):
        for i in self.pages:
            if self.verbose:
                print("Preserving page:", i)
            p = self.infile.pages[i]
            self.writer.add_page(p)

        if self.verbose:
            print("Saving...")
        self.writer.write(self.output)

        print(f"Generated: {self.output}")

        return 0
