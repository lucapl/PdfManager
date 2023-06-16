import sys
from PyPDF2 import PdfMerger
from pathlib import Path
from natsort import natsorted


def main(argv):
    pdfs = natsorted(Path('input').glob('*.pdf'))

    if not pdfs:
        print("No input")
        sys.exit(1)

    output = argv[1] if len(argv) > 1 else "result"

    merger = PdfMerger()

    for pdf in pdfs:
        print("Merging:",pdf)
        merger.append(pdf)

    print("Saving...")
    merger.write(f".\\output\\{output}.pdf")
    merger.close()

    print(f"Generated: {output}.pdf")

if __name__ == '__main__':
    main(sys.argv)