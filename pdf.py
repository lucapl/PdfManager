import argparse
from src.pdf_manager_lucapl.pdfManagers import *


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
    output = args.output

    print(args)

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
