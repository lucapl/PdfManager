import argparse

def main():
    parser = argparse.ArgumentParser(
                        prog='PdfManager',
                        description='Performs various operations on pdf files',
                        epilog='Pdfs are like bread')

    args = parser.parse_args()
    print(args)
    return 0

if __name__ == '__main__':
    print(main())