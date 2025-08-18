import java.io.File
val MOD = 1_000_000_007

fun getMinimum(arr: IntArray, i: Int, j: Int): Int {

    var minNum = arr[i]
    for  ( k in i + 1..j) {
        if ( arr[k] < minNum) {
            minNum = arr[k]
        }
    }
    return minNum
}

fun sumSubarrayMins(arr: IntArray): Int {

    val n = arr.size
    var k = 1
    var totalAns = 0
    while (k <= n) {
        var i = 0
        var j = k-1
        while ( j <= n-1) {
//             println("checking %s, %s".format(i, j))
             val minNum = getMinimum(arr, i, j)
             totalAns = (totalAns % MOD   + minNum % MOD) % MOD
             j += 1
             i += 1
         }
        k += 1
    }
    return totalAns
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
println("%s ".format(largeNums.size))
val nums = intArrayOf(1,1, 2, 1, 5, 6, 9, 8, 4, 7, 7)
// expected:  667452382
// output:    372485114
println(sumSubarrayMins(largeNums))