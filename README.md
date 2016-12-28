# selectGFF

Tool for selecting features of interest from a GFF file.

Given a list of IDs of interest, it generates a new GFF file containign only the features with these IDs. 

## Usage
	usage: selectGFF.py [-h] [-i IDS] [-g GFF] [--version]

	Select features in a GFF file based on a set of IDs of interest,

	optional arguments:
		-h, --help         show this help message and exit
		-i IDS, --ids IDS  txt file with the IDs of interest, one per line.
		-g GFF, --gff GFF  GFF file.
		--version          Display version, and exit.

by C I Mendes (cimendes@medicina.ulisboa.pt)


# getIDs

Tool for retieving all gff IDs from a list of gene group IDs from Roary's (https:/sanger-pathogens.github.io/Roary) gene presence and absence csv file.
Outputs a tsv file. 

## Usage
	usage: getIDs.py [-h] [-i IDS] [-g GENES] [-o OUTPUT] [--version]

	Fetches all GFF IDs from a list of gene group IDs.

	optional arguments:
		-h, --help			show this help message and exit
		-i IDS, --ids IDS 	txt file with the gene group IDs of interest, one per
							line.
		-g GENES, --genes GENES 	Input gene presence/absence table (comma-separated-
  							values) from Roary (https:/sanger-pathogens.github.io/Roary)
		-o OUTPUT, --output OUTPUT
  							output file name
		--version					Display version, and exit.

	by C I Mendes (cimendes@medicina.ulisboa.pt)

# Contact
Catarina Mendes (cimendes@medicina.ulisboa.pt)
