#pip3 install pymupdf
import fitz
doc = fitz.open("yadgiri.pdf")
for i in range(len(doc)):
    for img in doc.getPageImageList(i):
        xref = img[0]#integer unique identification for the objects in pdf(address of he image location)
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:       # this is GRAY or RGB (pix.n is bytes per pixel >5then the images is not a gray or rgb image then we convert the image into the gray or rgb image)
            pix.writePNG("p%s-%s.png" % (i, xref))
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("p%s-%s.png" % (i, xref))
            pix1 = None
        pix = None
print("Successfully created the .png file of the finger print in the given document")