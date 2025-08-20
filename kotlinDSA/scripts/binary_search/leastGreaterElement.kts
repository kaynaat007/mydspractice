/**
 * simple binary search for Least Greater element.
 * Used in NlogN solution of LIS.
 */

fun leastGreaterElement(nums: MutableList<Int>, n: Int, i: Int, j: Int, target: Int, result: IntArray){

    var low = i
    var high = j

    if (low > high) {
        return
    }

    var mid = low + (high - low)/2

    // if it's a hit - return -1 since we don't want to proceed
    if (mid >= 0 && nums[mid] == target) {
        println("target is hit ")
        result[0] = mid //
        return
    }
    // if target is greater than mid, then target must be in right
    else if (mid >= 0  &&  high <= n-1 && nums[mid] < target) {

        leastGreaterElement(nums, n, mid + 1, high, target, result)
    }
    // if target is less than mid, then target must be in left half
    else if ( mid >= 0 && high <= n-1 &&  nums[mid] > target) {
        result[0] = mid
        leastGreaterElement(nums, n, low, mid-1, target, result)
    }
}
