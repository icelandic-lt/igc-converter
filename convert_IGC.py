"""
A script to convert IGC subcorpora to JSONL format, either all of them or one subcorpus at a time. 
The script uses the XMLToJsonlConverter class to convert the XML files to JSONL format.
The IGC subcorpora are divided into four types, each with a different directory structure, which are accounted for in the conversion. 

The subcorpora are divided as follows:

Type1
Adjud, Journals, Law

Type2
Books, Parla, Wiki

Type3
News1, News2

Type4
Social
"""

import os
import argparse
from scripts import XMLToJsonlConverter

# These types reflect the different directory structure of the IGC subcorpora. If new subcorpora are added, they need to be listed here.
corpus_types = {
    "Adjud": 1,
    "Journals": 1,
    "Law": 1,
    "Books": 2,
    "Parla": 2,
    "Wiki": 2,
    "News1": 3,
    "News2": 3,
    "Social": 4,
}


def main(arguments):
    input_path = arguments.input_path
    version = arguments.version
    all_corpora = arguments.all_corpora
    corpus = arguments.corpus
    output_path = arguments.output_path if arguments.output_path else "./output/"

    if all_corpora:
        print(f"Converting IGC version {version}. Output path is {output_path}")
        for corpus in corpus_types:
            converter = XMLToJsonlConverter(
                corpus,
                os.path.join(input_path, f"IGC-{corpus}-{version}.TEI/"),
                output_path,
            )
            converter.create_jsonl(corpus_types[corpus])

    elif corpus:
        if corpus.startswith("IGC-"):
            corpus = corpus.split("IGC-")[1]
        print(
            f"Converting IGC-{corpus} version {version}. Output path is {output_path}"
        )
        converter = XMLToJsonlConverter(
            corpus,
            os.path.join(input_path, f"IGC-{corpus}-{version}.TEI/"),
            output_path,
        )
        converter.create_jsonl(corpus_types[corpus])
    else:
        print("Please provide either --all-corpora or --corpus")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Convert IGC XML files to JSONL format"
    )
    parser.add_argument(
        "--input-path",
        "-i",
        type=str,
        help="Path to the directory containing the IGC XML files",
        required=True,
    )
    parser.add_argument(
        "--version",
        "-v",
        type=str,
        help="Version of the IGC data",
        default="22.10",
        required=False,
    )
    parser.add_argument(
        "--all-corpora",
        "-a",
        action="store_true",
        help="Convert all IGC subcorpora",
        required=False,
    )
    parser.add_argument(
        "--corpus",
        "-c",
        type=str,
        help="The IGC subcorpus to convert",
        required=False,
    )
    parser.add_argument(
        "--output-path", "-o", type=str, help="Output path", required=False
    )
    args = parser.parse_args()
    main(args)
