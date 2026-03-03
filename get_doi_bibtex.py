import urllib.request
import re
import sys

dois = [
    "10.1602/neurorx.2.3.396",
    "10.1016/j.neuroscience.2015.10.029",
    "10.7759/cureus.45873",
    "10.1016/j.lfs.2021.120067",
    "10.3389/fncel.2017.00076",
    "10.1016/j.psychres.2025.116532",
    "10.1038/s41586-020-3008-z",
    "10.1021/acschemneuro.2c00597",
    "10.1016/j.neubiorev.2025.106086",
    "10.1007/s00540-015-2096-7",
    "10.1007/s00406-024-01770-7"
]

header = {'Accept': 'application/x-bibtex'}
doi_citekey_map = {}

for doi in dois:
    try:
        url = f"https://api.crossref.org/works/{doi}/transform/application/x-bibtex"
        req = urllib.request.Request(url, headers=header)
        with urllib.request.urlopen(req) as response:
            bibtex = response.read().decode('utf-8')
            
            # extract citekey
            match = re.search(r'@\w+\{([^,]+),', bibtex)
            if match:
                citekey = match.group(1)
                doi_citekey_map[doi] = citekey
                
                # Print output to append later or let me know
                print(f"=== {doi} -> {citekey} ===")
                print(bibtex)
            else:
                print(f"FAILED TO EXTRACT CITEKEY FOR {doi}")
    except Exception as e:
        print(f"ERROR FOR {doi}: {e}")

