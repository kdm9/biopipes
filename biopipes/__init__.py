import pipes
import logging

def run_pl_to_file(outfile_name, pl):
    with pl.open("", "r") as pl_fh:
        with open(outfile_name, "wb") as ofh:
            while True:
                kb = pl_fh.read(1024)
                if not kb:
                    break
                ofh.write(kb)

