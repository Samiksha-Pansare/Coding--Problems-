def find_pairs_of_numbers(num_list,n):
    count = 0
    for num in num_list:
        for i in range(num_list.index(num)+1,len(num_list)):
            if (num + num_list[i]==n):
                print("Num and Num_list[I]:",num,num_list[i])
                count = count+1
    return count

num_list=[1, 2, 4, 5, 6]
n=10
print(find_pairs_of_numbers(num_list,n))

# Another approach is 
# Sort the array
# if  sum - num -> present
# else no pair