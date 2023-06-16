from PyPDF2 import PdfWriter, PdfReader
import sys

def main(args):
    infile = PdfReader(args[1], 'rb')
    output = PdfWriter()
    
    print(args)

    pages = sorted(tuple(
        set(range(infile.numPages)) - set(map(int,args[2:]))
        ))
    
    print(pages)

    for i in pages:
        p = infile.pages[i] 
        output.add_page(p)

    with open('newfile.pdf', 'wb') as f:
        output.write(f)

    return 0

if __name__ == '__main__':
    print(main(sys.argv))