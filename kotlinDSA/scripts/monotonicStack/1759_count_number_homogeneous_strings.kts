import java.io.File

/**
 *  Distinct k groups we need to find.
 *  in each of K groups, we need to count possible subarrays.
 *  if size of subgroup is n, then (n * n + 1)/2 possible subarrays are present.
 */
val MOD = 1_000_000_007

fun countHomogenousUtil(s: String): Int {
    var stack = ArrayDeque<Int>()
    var countPerElement = mutableMapOf<Long, Long>()
    val n = s.length
    stack.addLast(0)
    var i = 1
    var k = 0L
    countPerElement.put(k, 1)
    while( i <= n-1) {
            if (!stack.isEmpty() &&  i <= n-1 &&  s[i] != s[stack.last()]) {
                stack.addLast(i)
                k += 1
                countPerElement.put(k, 1)
                i = i + 1
            }
            else {
                var count = 1L
                while (!stack.isEmpty() && i <= n-1 && s[i] == s[stack.last()]) {
                    stack.addLast(i)
                    count += 1
                    i += 1
                }
                countPerElement.put(k, count)
            }
    }
    var total = 0L
    //countPerElement.forEach { entry -> println("%s: %s".format(s[entry.key], entry.value))}
    val iter = countPerElement.iterator()
    while (iter.hasNext()) {
        val count = iter.next().value
        total = (total   + ((count * count + count)/2) % MOD)% MOD
    }
    return total.toInt()
}

fun processFile(): String {

    val path = "1759_large_input.txt" // file path
    val content = File(path).readText() // read entire file as string
    return content
}
val largeString = processFile()
println(largeString[largeString.length-1])
//  499949969,
//  999949973
val s = "aaaaaaaaaaaaaabbbbbccccccccccccaaaabababababababababababababaaaababababaa"
println(countHomogenousUtil(largeString))