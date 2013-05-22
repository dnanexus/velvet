<!-- dx-header -->
# Velvet (DNAnexus Platform App)

Short read de novo assembler using de Bruijn graphs

This is the source code for an app that runs on the DNAnexus Platform.
For more information about how to run or modify it, see
http://wiki.dnanexus.com/.
<!-- /dx-header -->

## What does this app do?

This app runs the [Velvet](http://www.ebi.ac.uk/~zerbino/velvet/) *de novo* sequence assembler (including the Pebble and Rock Band algorithms integrated in it).

## What are typical use cases for this app?

Velvet can perform pure and hybrid *de novo* assemblies of transcriptomic, bacterial, and other small to medium sized NGS datasets.

## What data are required for this app to run?

This app requires one or more files with reads in a format recognized by Velvet (one of `fasta`, `fastq`, `raw`, `sam`, or `bam`, compressed with gzip (e.g. `fastq.gz`) or bzip2 (e.g. `fastq.bz2`). See the [Velvet manual](http://www.ebi.ac.uk/~zerbino/velvet/Manual.pdf) for more information.

## What does this app output?

This app outputs a gzipped FASTA file with the sequence assembly.

TODO: MORE OUTPUTS

## How does this app work?

This app runs the `velveth` and `velvetg` executables from the Velvet software package. For more information, see the [Velvet Manual](http://www.ebi.ac.uk/~zerbino/velvet/Manual.pdf).
