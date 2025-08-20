
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


fun lisNogN(inputArray: IntArray) {
    var n = inputArray.size
    var target: Int
    var j: Int
    var size: Int
    var output = mutableListOf<Int>()
    output.add(inputArray[0])
    var k = 0
    for (i in 1..n-1) {
        size = output.size
        k = 0
        j = size-1
        target = inputArray[i]
        var result = IntArray(1){-1}
        leastGreaterElement(output, size, k, j, target, result)
        if (result[0] == -1){
            output.add(inputArray[i])
        }
        else {
            output[result[0]] = inputArray[i]
        }

    }

//    println("----- output-----")
//    for ( e  in output) {
//        print(e)
//        print(" ")
//    }
}

//  1,2,5,8,9,10,12
//var inputArray  = intArrayOf(2,5,8,9,10)

//var inputArray  = intArrayOf(6, 1, 4, 9, 2, 3,4,5,6,7)

var inputArray  = intArrayOf(7,7,7,7,7,7,7)

lisNogN(inputArray)