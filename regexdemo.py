import re

traindata=open('/Users/shilpagulati/DataEngineer/regex_sum_42.txt')
testdata=open('/Users/shilpagulati/DataEngineer/regex_sum_test.txt')
number_list_train= re.findall('([0-9]+)',traindata.read())
number_list_test= re.findall('([0-9]+)',testdata.read())

sum_traindata=sum(list(map(int,number_list_train)))
sum_testdata=sum(list(map(int,number_list_test)))

print (sum_traindata)
print (sum_testdata)
