



## How many measurements are larger than the previous measurement?

## Algorithm
##
## initialize a counter in 0
## Loop through all lines
## 1st value does not add
## start at second value and compare to first if the second is bigger add 1 count to the counter
## continue to loop thru the file and compare the previous value and the current adding only when current is bigger until it finish the file
## show the value at the end

# myFile = open('day1-data.txt', 'r')
# Lines = myFile.readlines()
# counter = 0

# for line in Lines:
#   counter += 1
#   print("Line{}: {}".format(counter, line.strip()))

# print('The program run currently')


depth_array = []
increased_depth_counter = 0
with open('day1-data.txt', 'r') as my_file:
  for line in my_file.readlines():
    depth_array.append(int(line.replace('\n','')))


for index in range(len(depth_array)):
  if index == 0:
    continue

  prev_depth = depth_array[index-1]
  current_depth = depth_array[index]

  if prev_depth < current_depth:
    increased_depth_counter +=1

print('Increse value is')
print (increased_depth_counter)