# Beak
A tool for efficiently downloading anchor tag linked resources from
a webpage.

## Setup
1. Install dependencies with `pip3 install -r requirements.txt`.
2. Navigate to the `src/` directory.
3. Start beak by running `python3 main.py <args>...` where `<args>...`
are the flags described [here](#flags).

## Flags
Available flag options:
- `-d/--dry-mode` Perform a dry run of all resources that will
be installed without actually downloading them.
- `-o/--output-dir` Directory where resources will be saved.
- `-r/--regex` An optional regex expression to download a subset
of resources. *Note the regrex expression is tested against the
absolute url*.
- `-u/--url` The webpage from which the resources should be extracted.

## Sample Usage
Example of beak being run against Stanford CS161's online site to
download all lecture notes to the current directory.
```sh
python3 main.py -u 'https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/'
-o . -r '.*lecture[0-9]{1,}.pdf'
```