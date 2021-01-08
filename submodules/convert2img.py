from pdf2image import convert_from_path, convert_from_bytes
import pathlib
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


curDir = pathlib.Path(__file__).parent.absolute()
## fig3a will takes a lot of time
#nameL = ["alg1","fig1","fig2a","fig2b","fig3a","fig3b","tab1","tab2","notation"]
#nameL = ["alg1","fig1","fig2a","fig2b","fig3b","tab1","tab2","notation"]
for name in nameL:
    images = convert_from_path(curDir.joinpath("{0}/{0}.pdf".format(name)))
    images[0].save(curDir.joinpath("{0}/{0}.png".format(name)),"png")
    print("{0}.pdf done".format(name))
print("done")