# PROBLEM: Zotero loves to grab the URL of articles when you use the 
# zotero browser extensions to get them into the citation manager.  Then those things incorrectly show up in your 
# automatically generated citations, e.g., when using the bluebook citation format.  
# And it's really obnoxious to delete them all by hand either in the output or zotero.

# SOLUTION: use CSL json as your output for processing with pandoc or whatever (which you should be doing anyway)
# and then interpose this little script between the raw CSL json file and cleaned up CSL json file with the URLs etc. 
# stripped.

# USAGE: "python no-url.py YOUR_EXISTING_CITATION_FILE NEW_FILENAME_FOR_CLEAN_FILE"

# Assumes citation file is in CSL json produced by zotero
# Should work with python 3, probably should work with python 2 too because it's simple, but I may have forgotten 
# something

import json, sys
from copy import deepcopy

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile) as inf:  
    # NOTE: Depending on your system, you might have to change that encoding.  Or leaving it off may be fine.
    # this is a possible sort of glitches where unicode code point numbers instead of things like smart quotes 
    # appear in the output. No warranties etc.
    #
    # best bet is probably to switch in and out to latin1 actually
    incites = json.load(inf)

def fix_esses(string):
    return string.replace('\u2019S', '\u2019s')

def clean_cite(ref):
    newref = deepcopy(ref)
    if newref['type'] in ["article-journal", "chapter", "book"]:
        if 'URL' in newref:
            newref['URL'] = ""
        if 'accessed' in newref:
            newref['accessed'] = ""
    if 'title' in newref:
        newref['title'] = fix_esses(newref['title'].title())
    if 'container-title' in newref:
        newref['container-title'] = fix_esses(newref['container-title'].title())
    return newref
  
outcites = [clean_cite(reference) for reference in incites]



with open(outfile, mode='w') as outf:
    json.dump(outcites, outf, indent=4)



