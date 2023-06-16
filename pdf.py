import argparse
import os
import re
from pdf_manager_lucapl.pdfManagers import *

# def get_pdfs(dir_path):
#     to_return = []
#     for dir, dirname, filename in os.walk(dir_path):
#         if not filename is None and filename re.match(""):
#             to_return.append(dir+filename)
#         if not dirname is None:
#             to_return += get_pdfs(dirname)
#     return to_return
def main():
    parser = argparse.ArgumentParser(
        prog='PdfManager',
        description='Performs various operations on pdf files',
        epilog='Pdfs are like bread')
    parser.add_argument("filenames",
                        action="extend",
                        help="pdfs to perform actions on",
                        nargs="+",
                        type=str)
    parser.add_argument("-v", "--verbose",
                        action="store_true",
                        help="be more verbose")
    parser.add_argument("-m", "--merge",
                        action="store_true",
                        help="merge pdfs into one")
    parser.add_argument("-d", "--delete",
                        action="extend",
                        help="deletes selected pages of the pdfs",
                        nargs="+",
                        type=int)
    parser.add_argument("-O", "--output",
                        default="./output/output.pdf",
                        action="store",
                        help="named of the output file")

    args = parser.parse_args()
    pdfs = args.filenames



    #pdfs = [item for item in pdfs if not os.path.isdir(item)]
    new_pdfs = list(filter(lambda pdf: not os.path.isdir(pdf),pdfs))
    pdf_end = re.compile(r'.*\.pdf$')
    for item in pdfs:
        if not os.path.isdir(item):
            break
        for dir, dirname, filename in os.walk(item):
            new_pdfs += [dir+"\\"+file for file in filename if filename is not None and re.match(pdf_end, file)]
    pdfs = new_pdfs

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


if __name__ == '__main__':
    print(main())
