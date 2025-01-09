# [75] https://leetcode.com/problems/sort-colors/
# Dutch National Flag question
# Notion: https://www.notion.so/Sort-Colors-Dutch-National-Flag-ac990085440043a984fc76a47b1415be?pvs=4
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are
# adjacent, with the colors in the order red, white and blue.
# Modify in-place = don't return anything
def sortColors(nums):
    red, white, blue = 0, 0, len(nums) - 1

    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1