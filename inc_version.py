import fileinput, re, sys, os

version = os.getenv('RELEASE_VERSION')
for line in fileinput.input(inplace=True):
    m = re.search(r"#define MYAPP_VERSION ", line)
    if m:        
        sys.stdout.write(f"#define MYAPP_VERSION {version}\n")
    else:
        sys.stdout.write(line)
