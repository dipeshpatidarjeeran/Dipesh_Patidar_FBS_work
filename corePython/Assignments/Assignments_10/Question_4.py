"""
    Write a program to reverse the list.
"""
li = [10,20,30,40,50,60,70]
beg = 0
end = len(li) - 1
while(beg < end):
    li[beg],li[end] = li[end],li[beg]
    beg += 1
    end -= 1

print(li)