import kotlin.math.max

fun parent(i: Int) : Int{
    if (i%2 == 0) {
        return i/2 - 1
    }
    return i/2
}

fun left(i: Int): Int {
    return 2 * i + 1
}

fun right(i: Int): Int {
    return 2 * i + 2
}

fun getMaxOfThree(arr: IntArray, i: Int, l: Int, r: Int): Int {

    if (arr[i] > maxOf(arr[l],  arr[r])){
        return i
    }
    else if ( arr[l] > arr[r] ) {
        return l
    }
    else {
        return r
    }
}

fun getMaxOfTwo(arr: IntArray, i: Int, j: Int): Int{

    if(arr[i] > arr[j]) {
        return i
    }
    return j
}

fun heapify(arr: IntArray, i: Int) {

    val leftIndex = left(i)
    val rightIndex = right(i)
    val n = arr.size
    var maxNumIndex: Int = i
    if (leftIndex < n && rightIndex < n) {
        maxNumIndex = getMaxOfThree(arr, i, leftIndex, rightIndex)
    }
    else if (leftIndex < n) {
        maxNumIndex = getMaxOfTwo(arr, i, leftIndex)
    }
    else if ( rightIndex < n ){
        maxNumIndex = getMaxOfTwo(arr, i, rightIndex)
    }
    if (maxNumIndex != i) {
        val temp  = arr[i]
        arr[i] = arr[maxNumIndex]
        arr[maxNumIndex] = temp
        heapify(arr, maxNumIndex)
    }
}

/**
 *  builds a heap from n/2+1, n/2+2, ....0
 */
fun buildMaxHeap(arr: IntArray){
    val n = arr.size
    for ( i in  n/2 downTo 0) {
        heapify(arr, i)
    }
}

/**
 *  extract maximum element
 */
fun printMax(arr: IntArray): Int {
    return arr[0]
}



val arr = intArrayOf(3, 6, 1, 2)
buildMaxHeap(arr)
printMax(arr)



