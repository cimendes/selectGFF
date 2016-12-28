import os, argparse, sys

def parseID(filename):
	gffIDs=[]
	with open(filename, 'r') as in_handle:
		for line in in_handle:
			line=line.strip()
			gffIDs.append(line)
	return gffIDs


def parserGFF(gffFile, IDlist):
	#parser for GFF3 files, retrieving the geneIDs and sequence coords

	#cleaning temp files if they exist
	if os.path.isfile('temp_genes_gff.txt'):
		os.remove('temp_genes_gff.txt')
	if os.path.isfile('temp_contigs.fasta'):
		os.remove('temp_contigs.fasta')
	if os.path.isfile('selected_gff.gff'):
		os.remove('selected_gff.gff')

	#separating the gff into 2 different files: one with the annotations and another with the conting sequences
	with open(gffFile, 'r') as in_handle, open('temp_genes_gff.txt', 'a') as temp_genes, open('temp_contigs.fasta', 'a') as temp_contigs, open('selected_gff.gff', 'w') as finalGFF:
		for line in in_handle: 
			if not line.startswith('##'):
				if '\t' in line:
					temp_genes.write(line)
				else:
					temp_contigs.write(line)
			else:
				if 'FASTA' in line:
					pass
				else:
					finalGFF.write(line)

	#parsing the feature file into a dictionary
	with open('temp_genes_gff.txt', 'r') as temp_genes, open('selected_gff.gff', 'a') as finalGFF:
		for line in temp_genes:
			items=line.split('\t')
			ID=items[-1].split(';')[0]
			ID=ID.split('=')[1]
			if ID in IDlist:
				finalGFF.write(line)

		
	#parsing the sequence file into a SeqIO dictionary. one contig per entry
	handle = open("temp_contigs.fasta", "rU")
	finalGFF=open('selected_gff.gff', 'a')
	finalGFF.write("##FASTA\n")
	for line in handle:
		finalGFF.write(line)
	handle.close()
	finalGFF.close()

	#removing temp files
	os.remove('temp_genes_gff.txt')
	os.remove('temp_contigs.fasta')

def main():

	version='0.0.1'

	parser = argparse.ArgumentParser(description='Select features in a GFF file based on a set of IDs of interest,', epilog='by C I Mendes (cimendes@medicina.ulisboa.pt)')
	parser.add_argument('-i', '--ids', help='txt file with the IDs of interest, one per line.')
	parser.add_argument('-g', '--gff', help='GFF file.')
	parser.add_argument('--version', help='Display version, and exit.', default=False, action='store_true')

	args = parser.parse_args()

	#version
	if args.version:
		print sys.stdout, "Current version: %s" %(version)
		sys.exit(0)

	#START

	print 'parsing ID file...'
	IDs=parseID(args.ids)

	print 'parsing gff files...'
	parserGFF(args.gff, IDs)

	print "Finished"
	sys.exit(0)


if __name__ == "__main__":
    main()