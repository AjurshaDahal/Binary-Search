# a funtion that takes a list and target parameter 
# multiple variables : mid , start , end , steps
# recursion or a while loop
# increase steps each time a split is done 
#conditions to track positions 


def binary_search(list,element):
    middle =0
    start=0
    end = len(list)
    steps = 0

    while (start <= end):
         print("step", steps, ":", (list [start:end+1]))

         steps = steps+1
         middle = (start+end)//2

         if element == list[middle]:
              return middle
         if element < list[middle]:
              end = middle-1
         else:
              start = middle +1 

    return -1
         
List=[90,3,4,1,5,7,9,8,6,3,4,5,6]

target = 7
binary_search(List, target)

         
 