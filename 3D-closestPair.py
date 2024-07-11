# This is an implementaion of the closest pair algorithm in 3D. All credit to this paper: "https://airccj.org/CSCP/vol5/csit54302.pdf"

import math

points = [[1,2,3],
          [2,3,4],
          [4,3,8],
          [121,22,2]]

point_count = len(points)

#sum, index, and distance arrays
d1= [0]*point_count
d2= [0]*point_count
d3= [0]*point_count
d4= [0]*point_count
d5= [0]*point_count
d6= [0]*point_count
sum= [0]*point_count
index= [0]*point_count
 
#min and max functions
def min(array2D, column):
    if array2D:
        min = array2D[0][column]
        for i in range(len(array2D)):
            if array2D[i][column] < min:
                min = array2D[i][column]
        return array2D[i]
    else: return ValueError

def max(array2D, column):
    if array2D:
        max = array2D[0][column]
        for i in range(len(array2D)):
            if array2D[i][column] > max:
                max = array2D[i][column]
        return array2D[i]
    else: return ValueError

p1 = min(points, 0)
p2 = max(points, 0)
p3 = min(points, 1)
p4 = max(points, 1)
p5 = min(points, 2)
p6 = max(points, 2)

# find the distance of 2 points
def distance(point1, point2):
    d = math.sqrt(math.pow(point2[0] - point1[0], 2) +
                  math.pow(point2[1] - point1[1], 2) +
                  math.pow(point2[2] - point1[2], 2)* 1.0)
    return d

for i in range(point_count):
    d1[i] = math.pow(distance(points[i], p1), 2)
    d2[i] = math.pow(distance(points[i], p2), 2)
    d3[i] = math.pow(distance(points[i], p3), 2)
    d4[i] = math.pow(distance(points[i], p4), 2)
    d5[i] = math.pow(distance(points[i], p5), 2)
    d6[i] = math.pow(distance(points[i], p6), 2)
    
# Calculate sum array and index array
for i in range(point_count):
    sum[i] = 11*d1[i] + 101*d2[i] + 547*d3[i] + 1009*d4[i] + 5501*d5[i] + 10007*d6[i]
    index[i] = i
    
# Custom mergesort
def merge(arr, index, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
    Lin = [0] * (n1)
    Rin = [0] * (n2)
    
    for i in range(0, n1):
        L[i] = arr[l + i]
        Lin[i] = index[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        Rin[j] = index[m + 1 + j]

    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            index[k] = Lin[i]
            i += 1
        else:
            arr[k] = R[j]
            index[k] = Rin[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        index[k] = Lin[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        index[k] = Rin[j]
        j += 1
        k += 1

def mergeSort(arr, index, l, r):
    if l < r:
        m = l+(r-l)//2
        
        mergeSort(arr, index, l, m)
        mergeSort(arr, index, m+1, r)
        merge(arr, index, l, m, r)
        
mergeSort(sum, index, 0, point_count-1)

min = [100000000, 0, 0]
for i in range(point_count-1):
    for j in range(1, 101):
        if i+j <= point_count-1:
            c = distance(points[index[i]], points[index[i+j]])
            if min[0] > c: 
                min[0] = c
                min[1] = index[i]
                min[2] = index[i+j]
        else:
            break
        
print(min)