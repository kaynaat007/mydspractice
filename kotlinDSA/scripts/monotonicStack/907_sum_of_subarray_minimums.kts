/**
 * two solution are presented here
 *
 * Solution 1: Contribution of each element is stored in a data class which tells the range of an element.
 *
 *
 * Solution 2: Contribution of each element is stored directly in left[] and right[] arrays [ YT video ]
 *
 *  https://www.youtube.com/watch?v=5Hag64mLXac
 *
 *  why left[i] * right[i] is number of possible subarrays which 1 present.
 *  *
 *  * [3, 1, 2, 4]
 *  *  left[1] = 2 which means 1 is minimum  till element 3
 *  *  right[1] = 3  which means 1 is minimum till 1,2,4
 *  *  Number of subarrays which are contributing - 2  * 3 = 6
 *  *  Think of 3 and {} element to the left of 1
 *  *  and include 1 itself while calculating right[1]
 *  *  if 2 elements are to left of 1, then for each element to left of 1, all elements of right can be chosen to form
 *  *  subarrrays which consists of 1.
 *  * 3, {}, 1, 2,,4
 *
 *  Mistake was to take LongArrays to store ranges of elements.
 *  Due to this last test case was not passing.
 */

import java.io.File
val MOD = 1_000_000_007


data class RangePerElement(var x: Long, var y: Long)


fun calculateMinRanges(nums: IntArray): Int {

    val stack = ArrayDeque<Int>()
    val n = nums.size
    var minRangePerElement = mutableMapOf<Int, RangePerElement>()
    var i = 0
    stack.add(0)
    for ( i in 0..n-1) {
        minRangePerElement.put(i, RangePerElement(i.toLong(), i.toLong()))
    }
    i = 1
    while ( i < n) {

        val currElement = nums[i]
        if  ( !stack.isEmpty() && currElement <= nums[stack.last()] ) {

            while (!stack.isEmpty() && currElement <= nums[stack.last()]) {
                /**
                 *  updates incoming element range if it's > stack top
                 *  remove stack top
                 */
                val topStackElementRange = minRangePerElement[stack.last()]
                val currentElementRange = minRangePerElement[i]
                currentElementRange?.x = topStackElementRange?.x!!
                stack.removeLast()

                if (!stack.isEmpty() ) {
                    minRangePerElement[stack.last()]?.y = topStackElementRange?.y!!
                }

            }
            stack.addLast(i)
        }
        else if ( !stack.isEmpty() && currElement > nums[stack.last()] ) {
            val topStackElementRange = minRangePerElement[stack.last()]
            /**
             *  since incoming element is larger than stack's top element,
             *  The y range of stack's top element will increase by incoming element's y range.
             */
            //topStackElementRange?.y = minRangePerElement[i]?.y!!
            stack.addLast(i)
        }
        i += 1
    }

    /**
     *  process a increasing stack here
     *  The top's element right range becomes the next element's y range as next element
     *  is always <  top element since stack is increasing  at this point.
     */
    var stackTopRange = minRangePerElement[stack.last()]
    stack.removeLast()
    while ( !stack.isEmpty()) {
        val currentMinPerRange = minRangePerElement[stack.last()]
        currentMinPerRange?.y = stackTopRange?.y!!
        stackTopRange = currentMinPerRange
        stack.removeLast()
    }

    //println("--- min Range per element ----")
    var minSum = 0L
    for ( i in 0..n-1) {

        val x = minRangePerElement[i]?.x!!
        val y = minRangePerElement[i]?.y!!

       // val totalSubArrays = ((y-x) % MOD    + ( (i - x)   * (y-i)  ) % MOD  ) % MOD
       // minSum = (minSum % MOD   + (totalSubArrays * nums[i]) % MOD ) % MOD
        minSum = (minSum   + ( nums[i] *  ((i - x + 1) * ( y - i + 1) ) % MOD) % MOD)%MOD
        //println("%s :  %s".format(nums[i], minRangePerElement[i]))
    }

    return minSum.toInt()

}

/**
 *  an element i in the array is contributing left[i]
 *  left[i] = the number of elements which are greater than i to the left of i
 *  This is till where ith element spans  to the left.
 *  right[i] = number of elements to the right which are greater
 *  contributions of i = left[i] * right[i]
 *  1,4,8,3,2
 *
 *  left[3] = 3
 *  right[3] = 1
 *  subarrays where 3 is minimum:
 *  [3]
 *  [8, 3]
 *  [4, 8, 3]
 *  Total = 3
 *
 */

fun printArray(nums: LongArray) {
    for ( e in nums) {
        print("%s ".format(e))
    }
    println()
}

fun sumSubarrayMinsUtil2(arr: IntArray): Int {
    var stack = ArrayDeque<Int>()
    val n  = arr.size
    var left = LongArray(n){1}
    var right = LongArray(n){1}

    /**
     *  calculates left[i]
     */
    stack.addLast(0)
    for (i in 1..n-1) {
        if ( !stack.isEmpty() &&  arr[i] > arr[stack.last()]) {
                  stack.addLast(i)
        }
        else {
              while (!stack.isEmpty() && arr[i] < arr[stack.last()]) {
                    left[i] = left[i] + left[stack.last()]
                    stack.removeLast()
              }
              stack.addLast(i)
        }
    }

    /**
     *  calculates right[i]
     *  Duplicates are handled here. Only once, either in left or in right.
     */
    stack.clear()
    stack.addLast(n-1)
    for (i in n-2 downTo 0) {
        if ( !stack.isEmpty() &&  arr[i] > arr[stack.last()]) {
            stack.addLast(i)
        }
        else {
            while (!stack.isEmpty() && arr[i] <= arr[stack.last()]) {
                right[i] = right[i] + right[stack.last()]
                stack.removeLast()
            }
            stack.addLast(i)
        }
    }
    //printArray(left)
    //printArray(right)

    // calculates the answer
    var total = 0L
    for  ( i in 0..n-1) {
        total = (total  + (arr[i] *  (left[i] * right[i]) % MOD)% MOD)%MOD
    }

    return total.toInt()
}

fun sumSubarrayMinsUtil(arr: IntArray): Int {
    var currSum = 0
    /**
    for (e  in arr) {
        currSum = (currSum  + e)
    }
    **/
    currSum = 0
    return  (calculateMinRanges(arr) + currSum) % MOD
}

fun processFile(): IntArray {

        val path = "907_large_input.txt" // file path
        val content = File(path).readText() // read entire file as string

        val numbers = content
            .split(",")                  // split by commas
            .map { it.trim().toInt() }    // trim whitespace and convert to Int
            .toIntArray()                 // convert to IntArray

       return numbers
}
val largeNums = processFile()
//println("%s ".format(largeNums.size))
val nums = intArrayOf(1,4, 8, 3, 2)
val nums2 = intArrayOf(1,1, 2, 1, 5, 6, 9, 8, 4, 7, 7)
// expected:  667452382
// output:    372485114
println(sumSubarrayMinsUtil2(largeNums))
/**
 *
 *  output :  1221109448
 *  expected:  221109441
 *
 */