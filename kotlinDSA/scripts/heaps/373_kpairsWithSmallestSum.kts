import java.util.PriorityQueue

/**
 * pq.add(42)       // Inserts element
 * pq.peek()        // Views the head without removing
 * pq.poll()        // Retrieves and removes the head
 * pq.isEmpty()     // Checks if empty
 * pq.remove(42)    // Removes a specific element
 */
data class Element(val i: Int, val j: Int, val total: Int)

fun kSmallestPairsUtil(nums1: IntArray, nums2: IntArray, k: Int): List<List<Int>> {

    val taskQueue = PriorityQueue<Element>(compareBy { it.total }) // Min priority first
    val output: MutableList<MutableList<Int>> = mutableListOf()
    val seenPairs: MutableSet<Pair<Int, Int>> = mutableSetOf()

    val m = nums1.size
    val n = nums2.size


    taskQueue.add(Element(0, 0, nums1[0] + nums2[0]))
    var count = 0
    seenPairs.add(Pair(0, 0))
    while (taskQueue.isNotEmpty()  && count < k) {
        val r = taskQueue.poll()
//        println("sum : %s".format(r.total))
        val e = mutableListOf<Int>()
        e.add(nums1[r.i])
        e.add(nums2[r.j])
        output.add(e)
//        println("i=%s, j=%s".format(r.i, r.j))
//        println("before: %s".format(seenPairs))
        if(r.j + 1 < n) {
                if (!seenPairs.contains(Pair(r.i, r.j+1)) ) {
                    val t = Element(r.i, r.j + 1, nums1[r.i] + nums2[r.j + 1])
                    taskQueue.add(t)
                    seenPairs.add(Pair(r.i, r.j+1))
//                    println("added:  %s, %s".format(r.i, r.j+1))
                }

        }
        if (r.i + 1 < m) {
            if (!seenPairs.contains(Pair(r.i+1, r.j))) {
                val s = Element(r.i + 1, r.j, nums1[r.i + 1] + nums2[r.j])
                taskQueue.add(s)
                seenPairs.add(Pair(r.i+1, r.j))
//                println("added:  %s, %s".format(r.i+1, r.j))
            }
        }
        count += 1
//        println("after: %s".format(seenPairs))
    }
    return output
}


val nums1 = intArrayOf(1, 2, 3)
val nums2 = intArrayOf(10)
kSmallestPairsUtil(nums1, nums2,3)
