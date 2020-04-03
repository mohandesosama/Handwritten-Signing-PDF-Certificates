import PyPDF2 as pypdf
import os
import os.path
from os import listdir
from os.path import isfile, join
from random import random
def merge_two_files(inFile,signFile):
    certificate = pypdf.PdfFileReader(inFile)
    certificate_bkgnd = certificate.getPage(0)
    signature = pypdf.PdfFileReader(signFile).getPage(0)

    # merge the first two pages
    certificate_bkgnd.mergePage(signature)

    # add all pages to be signed to a writer
    writer = pypdf.PdfFileWriter()
    for i in range(certificate.getNumPages()):
        page = certificate.getPage(i)
        writer.addPage(page)

    return writer
def merge_multiple_files(cert_folder_path,sign_file_path):
    out_folder_name='signed_certificates_output_'+str(random()).replace('.','')
    if not os.path.exists(out_folder_name):
        os.mkdir(out_folder_name)
    out_folder_path=out_folder_name+"\\"
    # list only files (no directory) and file is of .pdf extension
    onlypdffiles = [f for f in listdir(cert_folder_path) if isfile(join(cert_folder_path, f)) and '.pdf' in f]
    nfiles=len(onlypdffiles)
    counter=1
    
    #print(onlypdffiles)
    for cert_filename in onlypdffiles:
        with open(cert_folder_path+cert_filename, "rb") as inFile, open(sign_file_path, "rb") as signFile:
            writer=merge_two_files(inFile,signFile)
            # write everything in the writer to a file
            with open(out_folder_path + cert_filename.replace('.pdf','')+'_signed.pdf', "wb") as outFile:
                writer.write(outFile)
        print("Finished .... ",round(counter/nfiles*100),"%")
        counter += 1
    
if __name__ == "__main__":
    # go put all the certificates you want to sign into the certs folder
    sign_file="sign.pdf"
    cert_folder_path = "put_certificates_tobe_signed_here\\"
    merge_multiple_files(cert_folder_path,sign_file)