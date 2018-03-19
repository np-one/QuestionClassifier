import nltk

QWords= ["how", "what", "name", "when", "why", "who", "which", "where", "on", "to", "define", "give", "whose", "whom", "is", "does", "will", "can", "do", "could", "would", "has", "would", "are"]
postags=["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS", "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$", "RB", "RBR", "RBS", "RP", "SYM", "TO", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB"]

def extract(inputfile):
	global QWords
	global postags
	f=open(inputfile,"r")
	outputfilename=inputfile.replace(".txt","")+"Ques_one_Windowed.txt"
	out=open(outputfilename,"w")
	for line in f.readlines():
		part=line.split(",,,")
		
		ques=part[0]
		tag=part[1]

		queswords=nltk.word_tokenize(ques)
		pos_tag_dic= dict(nltk.pos_tag(queswords))

		QwordIndx=-100
		index=0
		for word in queswords:
			# print word
			if word in QWords:
				QwordIndx=index
				index+=1
				if(index!=1 and word=="is"):
					continue
				break
			index+=1
		if QwordIndx!=-100:
			out.write(str(queswords[QwordIndx])+" "+str(queswords[QwordIndx+1])+" "+pos_tag_dic[queswords[QwordIndx]]+" "+pos_tag_dic[queswords[QwordIndx+1]]+" "+"\t"+str(part[1]))
	f.close()
	out.close()
	return outputfilename