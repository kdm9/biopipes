from Bio.Sequencing.Applications import (
    BwaAlignCommandline,
    BwaSampeCommandline,
    BwaSamseCommandline,
    BwaBwaswCommandline,
    )
import pipes
import logging
from biopipes.samtools import (
   sam_to_ubam,
   sort_bam,
   index_bam,
   )

def fastq_to_sai(index, read_file, args={}, debug=False, pipeline=None):
    if not pipeline:
        pipeline = pipes.Template()
    if debug:
        pipeline.debugging = 1
    # bwa aln ...
    aln_cmd = BwaAlignCommandline(reference=index, read_file=read_file, **args)
    pipeline.prepend(str(aln_cmd), '.-')
    return pipeline

def sai_to_se_sam(index, read_file, args={}, pipeline=None):
    if not pipeline:
        pipeline = pipes.Template()
    # bwa samse ...
    samse_cmd = BwaSamseCommandline(reference=index, read_file=read_file,
            sai_file="$IN", **args)
    pipeline.append(str(samse_cmd), 'f-')



def fastq_se_to_sorted_bam(index, read_file, aln={}, samse={}, view={},
        sort={}, debug=False):
    pipeline = fastq_to_sai(index, read_file, args=aln, debug=debug)
    pipleine = sai_to_se_sam(index, read_file, args=samse, pipeline=pipeline)
    pipeline = sam_to_ubam(sam='$IN', args=view, pipeline=pipeline)
    pipeline = sort_bam(bam='$IN', args=view, pipeline=pipeline)
    return pipeline

