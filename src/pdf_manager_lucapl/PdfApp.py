import argparse
import re
import os

from src.pdf_manager_lucapl.pdfManagers import Deleter, Merger


class PdfApp:

    def __init__(self):

        self.parser = argparse.ArgumentParser(
            prog='PdfManager',
            description='Performs various operations on pdf files',
            epilog='Pdfs are like bread')
        self.parser.add_argument("filenames",
                                 action="extend",
                                 help="pdfs to perform actions on",
                                 nargs="+",
                                 type=str)
        self.parser.add_argument("-v", "--verbose",
                                 action="store_true",
                                 help="be more verbose")
        self.parser.add_argument("-m", "--merge",
                                 action="store_true",
                                 help="merge pdfs into one")
        self.parser.add_argument("-d", "--delete",
                                 action="extend",
                                 help="deletes selected pages of the pdfs",
                                 nargs="+",
                                 type=int)
        self.parser.add_argument("-O", "--output",
                                 default="./output/output.pdf",
                                 action="store",
                                 help="named of the output file")

    def launch(self):
        args, pdfs = self.__parse_args()
        output = args.output

        if args.merge:
            Merger(
                pdfs,
                output=output,
                verbose=args.verbose
            ).merge()

        if args.delete is not None:
            Deleter(
                pdfs[0],
                args.delete,
                output=output,
                verbose=args.verbose
            ).delete_pages()

        return 0

    def __parse_args(self):
        args = self.parser.parse_args()
        pdfs = args.filenames

        # pdfs = [item for item in pdfs if not os.path.isdir(item)]
        new_pdfs = list(filter(lambda pdf: not os.path.isdir(pdf), pdfs))
        pdf_end = re.compile(r'.*\.pdf$')
        for item in pdfs:
            if not os.path.isdir(item):
                break
            for directory, dir_name, filename in os.walk(item):
                new_pdfs += [directory + "\\" + file for file in filename if
                             filename is not None and re.match(pdf_end, file)]

        return args, new_pdfs
