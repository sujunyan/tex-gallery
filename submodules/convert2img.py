from pdf2image import convert_from_path, convert_from_bytes
import pathlib
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


curDir = pathlib.Path(__file__).parent.absolute()
nameL = ["1","2a","2b","3a","3b","4","5","6","notation"]
#nameL = ["notation"]
for name in nameL:
    images = convert_from_path(curDir.joinpath("{0}/{0}.pdf".format(name)))
    images[0].save(curDir.joinpath("{0}/{0}.png".format(name)),"png")
    print("{0}.pdf done".format(name))
print("done")