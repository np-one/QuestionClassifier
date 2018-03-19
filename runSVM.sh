echo "-----------------------Training Started------------------------------------------------"
libsvm-3.22/svm-train -s 0 -t 1 -d 2 -q LabelledDataQues_one_Windowed_vector.txt model/xxxxxmodel2
echo "-----------------------Training Completed----------------------------------------------"
echo "-----------------------Testing Model---------------------------------------------------"
libsvm-3.22/svm-predict LabelledDataQues_one_Windowed_vector.txt model/xxxxxmodel2 model/QCout 