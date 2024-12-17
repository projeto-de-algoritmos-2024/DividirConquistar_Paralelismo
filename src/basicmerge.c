// this is a rewrite of the following code found on the
// wikipedia article for the mergesort

/* function merge_sort(list m) is
    // Base case. A list of zero or one elements is sorted, by definition.
    if length of m ≤ 1 then
        return m

    // Recursive case. First, divide the list into equal-sized sublists
    // consisting of the first half and second half of the list.
    // This assumes lists start at index 0.
    var left := empty list
    var right := empty list
    for each x with index i in m do
        if i < (length of m)/2 then
            add x to left
        else
            add x to right

    // Recursively sort both sublists.
    left := merge_sort(left)
    right := merge_sort(right)

    // Then merge the now-sorted sublists.
    return merge(left, right)

In this example, the merge function merges the left and right sublists.

function merge(left, right)
is
    var result : = empty list

                   while left is not empty and
                   right is not empty do if first (left) ≤ first(right) then
                       append
                       first(left)
to result
    left : = rest(left) else append
           first(right)
to result
    right : = rest(right)

            // Either left or right may have elements left; consume them.
            // (Only one of the following loops will actually be entered.)
            while left is not empty do append
            first(left)
to result
    left : = rest(left) while right is not empty do append
           first(right)
to result
    right : = rest(right) return result
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{

    return 0;
}