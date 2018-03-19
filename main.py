from extract_feature_window import extract
from vectorize_input import vectorize
import os



tags=["unknown", "what", "when", "who", "affirmation"]
def loadGloveModel(gloveFile):
    # print "Loading Glove Model"
    f = open(gloveFile,'r')
    model = {}
    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        embedding = [float(val) for val in splitLine[1:]]
        model[word] = embedding
    return model
print "-------------------Loading Embeddings-------------------"
model=loadGloveModel("/home/prajpoot/Downloads/embeddings/glove/glove.6B.100d.txt")   #SETACCORDINGLY
print "-------------------Extracting Features------------------"
interfile1=extract("LabelledData.txt")
print "-------------------Vectorizing Features-----------------"
interfile2=vectorize(interfile1,model)

os.system("sh runSVM.sh ")

print "\nStarting test: \n"

while(1):
	print "Enter sentence:"
	sentence=raw_input()
	f=open("run_file.txt","w")
	f.write(sentence.lower()+",,,"+"what")
	f.close()
	interfile1=extract("run_file.txt")
	f_temp=open(interfile1,"r")
	if len(f_temp.readline().strip().split(" "))==1:
		print "unknown"
	else:
		interfile2=vectorize(interfile1,model)
		os.system("sh runtest.sh | tail -0 ")
		f=open("model/testOut","r")
		l=f.readline().strip()
		print tags[int(l)]
