#!/usr/bin/env python

import os, sys, subprocess
import dxpy

def run_shell(command):
    logging.debug("Running "+command)
    subprocess.check_call(command, shell=True)

@dxpy.entry_point('main')
def main(hash_length, **kwargs):
    velveth_cmd = "velveth velvet_wd {hash_length} -fmtAuto".format(hash_length=hash_length)

    if kwargs['mergeShortPaired']:
        dxpy.download_dxfile(kwargs['short']["$dnanexus_link"], 'short')
        dxpy.download_dxfile(kwargs['shortPaired']["$dnanexus_link"], 'shortPaired')
        run_shell("shuffleSeqs-fast short shortPaired shortPairedMerged")
        del kwargs['short'], kwargs['shortPaired']
        velveth_cmd += ' -shortPaired shortPairedMerged'
    if kwargs['mergeShortPaired2']:
        dxpy.download_dxfile(kwargs['short2']["$dnanexus_link"], 'short2')
        dxpy.download_dxfile(kwargs['shortPaired2']["$dnanexus_link"], 'shortPaired2')
        run_shell("shuffleSeqs-fast short2 shortPaired2 shortPairedMerged2")
        del kwargs['short2'], kwargs['shortPaired2']
        velveth_cmd += ' -shortPaired2 shortPairedMerged2'
    if kwargs['mergeLongPaired']:
        dxpy.download_dxfile(kwargs['long']["$dnanexus_link"], 'long')
        dxpy.download_dxfile(kwargs['longPaired']["$dnanexus_link"], 'longPaired')
        run_shell("shuffleSeqs-fast long longPaired longPairedMerged")
        del kwargs['long'], kwargs['longPaired']
        velveth_cmd += ' -longPaired longPairedMerged'

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