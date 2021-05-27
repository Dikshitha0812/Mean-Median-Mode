import csv
with open("data.csv",newline="") as f :
    reader=csv.reader(f)
    file_data=list(reader)

# Deleting the first row in list file data that are column  names
file_data.pop(0)

# Bringing Height data into new list
height=[]
for i in range(len(file_data)):
    data=file_data[i][1]
    height.append(data)

#Calculating Mean
sum =0
for i in height:
    sum=sum+float(i)

values=len(height)
mean=sum/values
print(mean)

# Calculaating Median
height.sort()
if values%2 ==0 :
    num1=float(height[values//2])
    num2=float(height[values//2-1])
    median=(num1+num2)/2

else :
    median=height[values//2]

print(median)

# Calculating Mode
range1=0
range2=0
range3=0

for i in range(len(height)):
    if 50<float(height[i])<60:
        range1=range1+1
    elif 60<float(height[i])<70:
        range2=range2+1
    elif 70<float(height[i])<80:
        range3=range3+1


mode=(60+70)/2
print(mode)