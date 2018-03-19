tags=["unknown", "what", "when", "who", "affirmation"]
postags=["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS", "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$", "RB", "RBR", "RBS", "RP", "SYM", "TO", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB"]

def vectorize(filename,model):
	global tags
	global postags
	f=open(filename,"r")
	outfilename=filename.replace(".txt","")+"_vector.txt"
	out=open(outfilename,"w")

	for line in f.readlines():
		part=line.split("\t")

		ques=part[0]
		queswords=ques.split(" ")
		res=""
		index=1
		for i in model[queswords[0]]:
			res= res+" "+str(index)+":"+str(i)
			index+=1

		if queswords[1] in model:
			for i in model[queswords[1]]:
				res= res+" "+str(index)+":"+str(i)
				index+=1
		else:
			for i in model["object"]:
				res= res+" "+str(index)+":"+str(i)
				index+=1

		if queswords[3] in postags:
			out.write(str(tags.index(part[1].strip()))+" "+res+" 201:"+str(postags.index(queswords[2]))+" 202:"+str(postags.index(queswords[3]))+"\n")

		else:
			out.write(str(tags.index(part[1].strip()))+" "+res+" 201:"+str(postags.index(queswords[2]))+" 202:"+str(40)+"\n")


	f.close()
	out.close()
	return outfilename