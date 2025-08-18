import kotlin.math.min

/**
 *  find minimum +ve sum in a list of numbers of size k
 */
fun findMinimumPositiveSumForGivenSize(nums: List<Int>, k: Int): Int {

    var i = 0
    var currSum = 0
    var minSum = Int.MAX_VALUE
    while (i < k) {
        currSum += nums[i]
        i += 1
    }
    if (currSum > 0) {
        minSum = currSum
    }
    else {
        minSum = Int.MAX_VALUE
    }
    var j = k
    i = 0
//    println("j: %s, size: %s, minSum: %s".format(j, nums.size, minSum))
    while (j < nums.size) {
        if ( currSum > 0) {
            minSum = minOf(minSum, currSum)
        }
        currSum = currSum + nums[j] - nums[i]
        j += 1
        i += 1
    }
    // last check
    if ( currSum > 0 ) {
        minSum = minOf(minSum, currSum)
    }
    return minSum
}

fun minimumSumSubarray(nums: List<Int>, l: Int, r: Int): Int {

    //return findMinimumPositiveSumForGivenSize(nums, 3)

    var minSum = Int.MAX_VALUE
    for ( k in l..r) {
        val currMinSumForSizeK = findMinimumPositiveSumForGivenSize(nums, k)
        if (currMinSumForSizeK > 0 && currMinSumForSizeK < minSum) {
            minSum = currMinSumForSizeK
        }
    }
    if (minSum < Int.MAX_VALUE) {
        return minSum
    }
    return -1
}

var nums = listOf<Int>(8, 9, 10, 1, -1, 2, -1)
println(minimumSumSubarray(nums, 2,4))