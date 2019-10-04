import pandas as pd
import glob
import os
import datetime
import argparse
import time

start = time.time()

# TODO: add args for absolute path to directory.
# TODO: tidy up into functions.
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


all_files = [f for f in os.listdir(".") if f.startswith(f"{args.filename}")]
print(f"Sample of files being concatenated: {sorted(all_files[:4])}")

li = []

for filename in sorted(all_files[:]):
    try:
        df = pd.read_csv(filename, sep=";", error_bad_lines=False, encoding="utf-8")
        li.append(df)
    except UnicodeDecodeError as e:
        print(f"Skipped line {e}")

df = pd.concat(li, axis=0, ignore_index=True, sort=False)

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

date = datetime.datetime.now().date()
filename = f"{date}-{args.output}.csv"

df.to_csv(filename)

end = time.time()

print(
    f"""
[*] {filename} [*]

Total files concatenated: {len(li)}

        CSV Shape
{df.shape[1]} Columns x {df.shape[0]} Rows

Time Elapsed: {end - start:.2f} seconds"""
)
