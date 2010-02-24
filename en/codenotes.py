import sys

loc = float(sys.argv[1])

pages = loc / 80
sqft = (pages * 8.5 * 11) / 144
dimensions = 8, 8, sqft / 64

print "lines of code: ", loc
print "pages: ", pages
print "sqft: ", sqft
print "dimensions: ", dimensions
