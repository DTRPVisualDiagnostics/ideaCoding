import os, csv

LIST_OF_TRANSCRIPTS_INFO = [('../datasets/DTRS2015-dataset/tsv', 1, '\t', 0, None), ('../datasets/DTRS2016-dataset/csv', 3, ',', 6, 0), ('../datasets/dschool-dataset/csv', 3, ',', 1, 1)]
LIST_OF_MODAL_VERBS= ["could", "might", "can", "how about", "what if", "maybe we could", "maybe we should", "perhaps we could", "perhaps we should", "what about"]

def loadFileIntoList(path, index, delimiter, skipLines, moveIndex):
	doc = []
	with open(path, 'rt') as csvfile:
		csvReader = csv.reader(csvfile, delimiter=delimiter)
		for x in range(skipLines):
			next(csvReader,None)
		if moveIndex == None:	
			idx = 1		
		for row in csvReader:	
			if len(row) >= index and row[index]:
				cleaned_line = cleanLine(row[index])
				if (cleaned_line != ""):
					if moveIndex == None:
						idx += 1
						doc.append((idx, cleaned_line.rstrip('\n')))
					else:
						doc.append((row[moveIndex], cleaned_line.rstrip('\n')))

	return doc

def printIndicesOfModalVerbs(text, transcriptPath):
	print(transcriptPath)
	for line in text:
		for modal_verb in LIST_OF_MODAL_VERBS:
			if modal_verb in line[1]:
				print(str(line[0]) + "," + modal_verb)
				break;

def cleanLine(line):
	lower_line = line.lower()
	cleaned_line = lower_line.replace(":"," ")
	cleaned_line = cleaned_line.replace("."," ")
	cleaned_line = cleaned_line.replace("!"," ")
	cleaned_line = cleaned_line.replace("?"," ")
	cleaned_line = cleaned_line.replace(","," ")
	cleaned_line = cleaned_line.replace("-"," ")
	cleaned_line = cleaned_line.replace("_"," ")
	cleaned_line = cleaned_line.replace("“"," ")
	cleaned_line = cleaned_line.replace("\""," ")
	cleaned_line = cleaned_line.replace("\'"," ")
	return cleaned_line

for info in LIST_OF_TRANSCRIPTS_INFO:		
	for transcriptPath in os.listdir(info[0]):
		text = loadFileIntoList(info[0] + "/" + transcriptPath, info[1], info[2], info[3], info[4])
		printIndicesOfModalVerbs(text, transcriptPath)