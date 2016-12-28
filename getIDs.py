import os, argparse, sys, csv

def parseGroupID(filename):
	groupIDs={}
	with open(filename, 'r') as in_handle:
		for line in in_handle:
			line=line.strip()
			groupIDs[line]=[]
	return groupIDs

def genePAfile (filename, IDs):
	#parser for Roary's gene_presence_absence.csv file

	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile)
		filenames=reader.next()#[14:] #save all filenames
		for row in reader:
			if row[0] in IDs.keys():
				#geneID starts in the 15th col
				for item in row[14:]:
					if '\t' in item: #in case of paralogss
						item=item.split('\t')
						out=','.join(item)
						IDs[row[0]].append(out)
					else:
						IDs[row[0]].append(item)
	return IDs

def main():

	version='0.0.1'

	parser = argparse.ArgumentParser(description='Fetches all GFF IDs from a list of gene group IDs.', epilog='by C I Mendes (cimendes@medicina.ulisboa.pt)')
	parser.add_argument('-i', '--ids', help='txt file with the gene group IDs of interest, one per line.')
	parser.add_argument('-g','--genes', help='Input gene presence/absence table (comma-separated-values) from Roary (https:/sanger-pathogens.github.io/Roary)')
	parser.add_argument('-o', '--output', help='output file name')
	parser.add_argument('--version', help='Display version, and exit.', default=False, action='store_true')

	args = parser.parse_args()

	#version
	if args.version:
		print sys.stdout, "Current version: %s" %(version)
		sys.exit(0)

	#START

	print 'parsing Group ID file...'
	IDs=parseGroupID(args.ids)

	print 'parsing gene presence absence file...'
	data=genePAfile(args.genes, IDs)


	with open(args.output +'.tsv','w') as outfile:
		for key, value in data.items():
			outfile.write(str(key) + '\t')
			outfile.write('\t'.join(value) + '\n')


	print "Finished"
	sys.exit(0)


if __name__ == "__main__":
    main()