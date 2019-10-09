import pandas as pd
import glob
import os
import datetime
import argparse
import time

START = time.time()
LIST_OF_FILES = []


def main():
    args = argument_parser()

    if args:
        all_files = get_files(args)
        concat_df = concat_files(all_files)
        split_cols_df = split_columns(concat_df)
        filename = make_csv(split_cols_df, args)
        printer(filename, split_cols_df)


def argument_parser():
    parser = argparse.ArgumentParser(
    "Take a folder of CSV's and concatenate into on large CSV"
    )
    parser.add_argument("-o", "--output", help="Output filename", required=True)
    parser.add_argument(
    "-f",
    "--filename",
    help="First letters of files to be concatenated for use in startswith string method.",
    required=True,
    )
    args = parser.parse_args()
    return args

def get_files(args):
    all_files = [f for f in os.listdir(".") if f.startswith(f"{args.filename}")]
    print(f"Sample of files being concatenated: {sorted(all_files[:4])}")
    return all_files


def concat_files(all_files):

    for filename in sorted(all_files[:]):
        try:
            df = pd.read_csv(filename, sep=";", error_bad_lines=False, encoding="utf-8")
            LIST_OF_FILES.append(df)
        except UnicodeDecodeError as e:
            print(f"Skipped line {e}")

    df = pd.concat(LIST_OF_FILES, axis=0, ignore_index=True, sort=False)

    return df


def split_columns(df):
    columns = df.columns.values.tolist()

    # post process split superfluous header data to retrieve CAN id name
    new_cols = []
    for x in columns:
        if len(x.split()) < 2:
            new_cols.append(x.lower())
        if len(x.split()) > 2:
            new_cols.append(x.split()[-2].lower())

    df.columns = new_cols
    df = df.loc[:, ~df.columns.duplicated()]  # remove duplicate columns
    return df


def make_csv(df, args):
    date = datetime.datetime.now().date()
    filename = f"{date}-{args.output}.csv"
    df.to_csv(filename)
    return filename


def printer(filename, df):
    print(
        f"""
    [*] {filename} [*]

    Total files concatenated: {len(LIST_OF_FILES)}

            CSV Shape
    {df.shape[1]} Columns x {df.shape[0]} Rows

    Time Elapsed: {time.time() - START:.2f} seconds"""
    )

if __name__ == '__main__':
    main()
