# Sign PDF Files with Handwritten Signature: Python script

## The problem
After giving courses in cisco academey (www.netacad.com), the course certificates introduced by the website are not signed. In some courses, more than 2000 students are enrolled. Which makes manual signing of the certificates an infeasible task,  See figure below

![without_sign_image](https://github.com/mohandesosama/Handwritten-Signing-PDF-Certificates/blob/master/images/certificate_without_sign.png)

The students are always asking for the certificate handwritten signature. The problem is that, in some courses the number of students count more than 2000. Signing more than 2000 certificates one by one is very time and effort consuming task. I have developed this python script to sign automatically thousands of certificates in a blink of an eye. Here is an example of the output (red signs are just for clarifiaction)

![without_sign_image](https://github.com/mohandesosama/Handwritten-Signing-PDF-Certificates/blob/master/images/certificate_with_sign.png)

## Solution
* Open the sign.docx file, remove the signature and put your own signature
* Save sign.docx as sign.pdf
* Put all the certificates (even thousands of certificates) you want to sign in the "put_certificates_tobe_signed_here" folder
* Run the script
* The signed certificates will be put in new folder named "signed_certificates_output_xxxxxxxxxx" where xxxxxxxx is random number
* Congratulations ... You signed all the certificates in no time. 

## Depndancies 
* PyPDF2, for merging two pdf files, [PyPDF2 Link](https://pypi.org/project/PyPDF2/)
* os, for dealing with folder creation and search
* random, to create random folder each time you run the script

## References 
* The pdf code for merging two files is obtained from [[This url]](https://stackoverflow.com/questions/13276409/how-to-add-image-to-pdf-file-in-python)

 
