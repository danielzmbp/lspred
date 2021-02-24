
#!/usr/bin/env python3
""" Lifestyle predictor """

import pandas as pd
import argparse
import os
import tensorflow as tf
from typing import NamedTuple, TextIO, List
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

class Args(NamedTuple):
    """ Command-line arguments """
    files: List[TextIO]
    file_format: str
    outfile: TextIO


def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Predict lifestyle',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input genome-properties file(s)')

    parser.add_argument('-f',
                        '--format',
                        help='Output format',
                        metavar='format',
                        choices=['tsv', 'csv', 'xlsx', 'html'],
                        default='tsv')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=str,
                        default='out.tsv')

    args = parser.parse_args()

    return Args(files=args.file,
                file_format=args.format,
                outfile=args.outfile)

def main() -> None:

    classes = ["saprotroph", "necrotroph", "hemibiotroph", "biotroph"]
    args = get_args()

    l=[]
    for i in args.files:
        t = pd.read_csv(i,"\t",usecols=["step_name","step_value"])
        name = i.name.split("TABLE_")[-1].split(".")[0]
        t.columns = ["name",name]
        t.set_index("name",inplace=True)
        l.append(t)

    x_t = pd.concat(l,axis=1)
    x_t = x_t.transpose()
    model = tf.keras.models.load_model('lspred_15_2_21.h5')

    pred = model.predict(x_t)

    p = pd.DataFrame(pred)
    p.columns = classes
    p.index = x_t.index

    print(p)

    output = args.outfile.split(".")[0] + "." + args.file_format

    getattr(p, 'to_' + args.file_format)(output)

    print("Output file written to " + output)

if __name__ == '__main__':
        main()