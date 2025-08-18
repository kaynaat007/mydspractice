import kotlin.math.max

var n = 10
val negativeInfinity = -1

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


/**
 *  builds a heap from n/2+1, n/2+2, ....0
 */
fun buildMaxHeap(arr: IntArray){

    for ( i in  n/2 downTo 0) {
        heapify(arr, i)
    }
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
 * EXTRACT MAX
 */
fun extractMax(arr: IntArray): Int {

    val maximumElement = arr[0]
    arr[0] = arr[n-1]
    heapify(arr, 0)
    arr[n-1] = negativeInfinity
    n = n-1
    return maximumElement
}

/**
 * increases a value at key indexed at i by amount value. Value must be >= arr[i]
 */
fun increaseKey(arr: IntArray, i: Int, value: Int) {

    /**
     *  trying to access out of bounds index
     */
    if (i >= n) {
        return
    }
    /**
     *  if value  < arr[i], this is our condition ele heap property will not hold at i.
     */
    if (value < arr[i]) {
        return
    }

    arr[i] = value
    var k  = i
    // follow a simple path from index i up to the root unless heap property is established
    while (k >=0 && parent(k) >=0  && parent(k) < n && arr[parent(k)] < arr[k]) {
        println("k = %s, parent = %s".format(k, parent(k)))
        val temp = arr[parent(k)]
        arr[parent(k)] = arr[k]
        arr[k] = temp
        k = parent(k)
    }

}

// inserts key value into the heap
fun insertKey(arr: IntArray, value: Int) {
    n += 1
    arr[n-1] = negativeInfinity  // -ve infinity
    increaseKey(arr,  n-1, value)
}

fun printHeapSize(){
    println("heap size = ")
    println(n)
}

/**
 *  extract maximum element
 */
fun printMax(arr: IntArray) {
    println("maximum element: ")
    println(arr[0])
}

val arr = IntArray(50){negativeInfinity}
for ( i in 0..n-1){
    arr[i] = i
}

buildMaxHeap(arr)
println("heap is built")
insertKey(arr, 20)
insertKey(arr, 30)
printMax(arr)
printHeapSize()

/**
println(extractMax(arr))
printHeapSize()
println(extractMax(arr))
printHeapSize()
insertKey(arr, 20)
printMax(arr)
printHeapSize()
**/


