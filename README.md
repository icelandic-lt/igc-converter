# IGC-Converter

A conversion pipeline for converting the Icelandic Gigaword Corpus to JSONL format files. The pipeline assumes a copy of the [unannotated Icelandic Gigaword Corpus](http://hdl.handle.net/20.500.12537/253).

To run the scripts you will need a python3 environment. Install the required dependencies by running

```
pip install -r requirements.txt
```

The corpus can be converted as a whole or one subcorpus at a time. The script used to convert the corpus is `convert_IGC.py`, which has the following possible arguments:

- `--input-path`: path to the original IGC.
- `--version`: the version of the IGC which will be converted. The default version is 22.10. If the version differs, it needs to be specified because it appears in the converted output.
- `--all-corpora`: convert all subcorpora of the IGC.
- `--corpus`: convert one subcorpus of the IGC, e.g. 'Adjud'.
- `--output-path`: the path to an output directory. If this is not defined, it defaults to an `output` directory.

To convert the 22.10 version of the corpus as a whole, run 

```
python convert_IGC.py --input-path path/to/IGC --all-corpora
```

To convert the 22.10 version of the IGC-News1 subcorpus, run

```
python convert_IGC.py --input-path path/to/IGC --corpus IGC-News1
```

## Output format

The converted output, which is saved under the output directory, is twofold: for each converted subcorpus, a JSONL file is created in `datasets-info`, containing information on each converted subdirectory of the subcorpus, and the converted subcorpus itself is created as JSONL files in `converted-corpora`. The information and format of the file in `datasets-info` is the following:

```
{
    "subdirectory of the subcorpus, e.g. IGC-Adjud-Appeal": 
    {
        "path": "path to the converted corpus", 
        "quality": "quality categorization, taken from `subcorpora_categorization.tsv`, which was created by the Árni Magnússon Institute for Icelandic Studies", 
        "domain": ["a list of all relevant domains, taken from `subcorpora_categorization.tsv`"], 
        "lang": "the language of the corpus, which is 'is' for all current cases", 
        "version": "the IGC version, which is 22.10 by default"
        }
    }
```

Each XML file of the IGC subcorpus becomes a single line in the JSONL file in `converted-corpora`. The information and format of a single line is the following:

```
{
    "document": "all text of the file, with paragraph splits shown as '\n\n'", 
    "uuid": "a randomly generated ID for the json object", 
    "metadata": 
    {
        "author": "the original file's author, if available", 
        "fetch_timestamp": "the date of the conversion", 
        "xml_id": "the ID of the original XML file", 
        "publish_timestamp": "the publishing date of the text in the original XML file", 
        "title": {"offset": None, "length": None},                                                  # the offset and length of the text's title, if it is available 
        "paragraphs": [{"offset": None, "length": None}, {"offset": None, "length": None}, ...],    # the offset and length of each paragraph
        "sentences": [{"offset": None, "length": None}, {"offset": None, "length": None}, ...],     # the offset and length of each sentence 
        "source": "the source of the original text, taken from the XML file"
        }
    }
```