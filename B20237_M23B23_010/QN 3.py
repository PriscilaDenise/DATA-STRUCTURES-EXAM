# Quesion 3

"""BUBBLE SORT"""
def bubble_sort(unsorted_list): #Defining a function with parameter unsorted_list
    for i in range(len(unsorted_list)-1, 0, -1): # loop will run from 8 to 0
        for j in range(i): 
            if unsorted_list[j]>unsorted_list[j+1]: # If the condition is true, we swap values
                temporary_value = unsorted_list[j]  # Keeping value in temp variable
                unsorted_list[j] = unsorted_list[j+1] # Swapping values
                unsorted_list[j+1] = temporary_value

    return f'Sorted list is: {unsorted_list}'

unsorted_list = [14, 27, 8, -42, 11, 35, -9, 56, 23]
print(bubble_sort(unsorted_list))
# The complexity class for bubble sort is O(n^2), Quadratic time. this is because it has two for loops 
# for which each loop runs n times

# """SELECTION SORT"""
def selection_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        min_index = i
        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i] # Swapping values
    return unsorted_list

unsorted_list = [14, 27, 8, -42, 11, 35, -9, 56, 23]
print(f'Sorted list is: {selection_sort(unsorted_list)}')

# # The time complexity for selection sort is O()

