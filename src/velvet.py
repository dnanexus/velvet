#!/usr/bin/env python

import os, sys, subprocess
import dxpy

def run_shell(command):
    logging.debug("Running "+command)
    subprocess.check_call(command, shell=True)

@dxpy.entry_point('main')
def main(hash_length, **kwargs):
    velveth_cmd = "velveth velvet_wd {hash_length} -fmtAuto".format(hash_length=hash_length)

    for input in 'short', 'shortPaired', 'short2', 'shortPaired2', 'long', 'longPaired':
        if input in kwargs:
            dxpy.download_dxfile(kwargs[input]["$dnanexus_link"], input)
            velveth_cmd += ' -{i} {i}'.format(i=input)

    run_shell(velveth_cmd)

    velvetg_cmd = "velvetg velvet_wd"
    for option in 'cov_cutoff', 'ins_length', 'read_trkg', 'min_contig_lgth', 'exp_cov', 'long_cov_cutoff':
        if option in kwargs:
            velvetg_cmd += " -{option} '{value}'".format(option=option, value=kwargs[option])

    run_shell(velvetg_cmd)

    assembly = dxpy.upload_local_file("velvet_wd/contigs.fa")
    output = {"assembly": dxpy.dxlink(assembly)}

    return output

dxpy.run()
