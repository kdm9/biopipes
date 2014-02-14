from Bio.Sequencing.Applications import (
    SamtoolsViewCommandline,
    SamtoolsSortCommandline,
    SamtoolsIndexCommandline,
    )
import pipes
import logging

def sam_to_ubam(sam='$IN', args={}, pipeline=None):
    if not pipeline:
        pipeline = pipes.Template()
    # samtools view
    view_cmd = SamtoolsViewCommandline(sam='$IN', u=True, S=True,
            **args)
    pipeline.append(str(view_cmd), 'f-')

def sort_bam(bam='$IN', args={}, pipeline=None):
    if not pipeline:
        pipeline = pipes.Template()
    # samtools sort
    sort_cmd = SamtoolsSortCommandline(input_bam='$IN', out_prefix="tmp",
            o=True, **args)
    pipeline.append(str(sort_cmd), 'f-')

def index_bam(bam='$IN', args={}, pipeline=None)
    if not pipeline:
        pipeline = pipes.Template()
    sort_cmd = SamtoolsIndexCommandline(input_bam='$IN', out_prefix="tmp",
            o=True, **args)
    pipeline.append(str(sort_cmd), 'f-')
