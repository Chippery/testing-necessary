import random
import pygame

def insert_sort(lis):
    comparions = 0

    for i in range(1, len(lis)):
        j = i
        while j > 0:
            comparions += 1
            if rects[j].height < rects[j - 1].height:
                print(rects[j].height, rects[j - 1].height)
                rects[j].x, rects[j - 1].x = rects[j - 1].x, rects[j].x
                j -= 1
            else:
                break
    print("Sorted List: ", lis)
    print("Comparisons:", comparions)

rects = []
nums = random.sample(range(20, 601), 10)

for i in range(5):
            rects.append(pygame.Rect(20 + (20 * i), 600 - nums[i], 20, nums[i]))

new_list1 = [10, 2, 4, 1, 5, 6]
new_list = random.sample(range(1, 101), 15)
insert_sort(rects)
