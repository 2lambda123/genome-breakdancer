from lxml import etree
import StringIO
import sys
with open(sys.argv[1]+"/Testing/TAG", 'r') as TAGfile:
    dirname = TAGfile.readline().strip()
with open(sys.argv[1]+"/Testing/"+dirname+"/Test.xml", 'r') as xmlfile:
    with open(sys.argv[2], 'r') as xslfile:
        
        xmlcontent = xmlfile.read()
        xslcontent = xslfile.read()

xmldoc = etree.parse(StringIO.StringIO(xmlcontent))
xslt_root = etree.XML(xslcontent)
transform = etree.XSLT(xslt_root)

result_tree = transform(xmldoc)
print(result_tree)
