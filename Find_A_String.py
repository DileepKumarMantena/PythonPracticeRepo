
string=str(input())
sub_string=str(input())
count=0
for i in range(0,len(string)):
    str_i=string[i:i+len(sub_string)]
    if str_i ==sub_string:
        count=count+1
print(count)

