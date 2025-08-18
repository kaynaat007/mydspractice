import kotlin.random.Random

data class RangePerElement(var x: Int, var y: Int)


fun calculateMinRanges(nums: IntArray): Long {

    val stack = ArrayDeque<Int>()
    val n = nums.size
    var minRangePerElement = mutableMapOf<Int, RangePerElement>()
    var i = 0
    stack.add(0)
    for ( i in 0..n-1) {
        minRangePerElement.put(i, RangePerElement(i, i))
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
                val inStackElementRange = minRangePerElement[stack.last()]
                val currentElementRange = minRangePerElement[i]
                currentElementRange?.x = inStackElementRange?.x!!
                stack.removeLast()
                if (!stack.isEmpty() ) {
                    minRangePerElement[stack.last()]?.y = inStackElementRange?.y!!
                }
            }
            stack.addLast(i)
        }
        else if ( !stack.isEmpty() && currElement > nums[stack.last()] ) {
            stack.addLast(i)
        }
        else {
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
    var currentStackIndex = stack.removeLast()
    while ( !stack.isEmpty()) {
        //println("processing %s".format(nums[stack.last()]))
        val currentMinPerRange = minRangePerElement[stack.last()]
      //  if ( nums[currentStackIndex] != nums[stack.last()] ) { // do not change range when elements are equal
            currentMinPerRange?.y = stackTopRange?.y!!
        //}
        stackTopRange = currentMinPerRange
        currentStackIndex =  stack.removeLast()
    }

    //println("--- min Range per element ----")
    var minSum = 0L
    for ( i in 0..n-1) {

        val x = minRangePerElement[i]?.x!!
        val y = minRangePerElement[i]?.y!!
        minSum += ((y-x) + (i - x) * (y-i) ) * nums[i]
        //println("%s :  %s".format(nums[i], minRangePerElement[i]))
    }

    return minSum

}

fun calculateMaxRangeSum(nums: IntArray): Long {

    val stack = ArrayDeque<Int>()
    val n = nums.size
    var maxRangePerElement = mutableMapOf<Int, RangePerElement>()
    var i = 0
    stack.add(0)
    for ( i in 0..n-1) {
        maxRangePerElement.put(i, RangePerElement(i, i))
    }
    i = 1
    while ( i < n) {

        val currElement = nums[i]
        if ( !stack.isEmpty() && currElement >= nums[stack.last()] ) {

            while (!stack.isEmpty() && currElement >= nums[stack.last()]) {
                /**
                 *  updates incoming element range if it's > stack top
                 *  remove stack top
                 */
                val inStackElementRange = maxRangePerElement[stack.last()]
                val currentElementRange = maxRangePerElement[i]
                currentElementRange?.x =  inStackElementRange?.x!!
                stack.removeLast()

                if (!stack.isEmpty() ) {
                    maxRangePerElement[stack.last()]?.y = inStackElementRange?.y!!
                }
            }
            stack.addLast(i)
        }
        else if ( !stack.isEmpty() && currElement < nums[stack.last()] ) {
            /**
             *  update stack top's element range if incoming element is smaller
             */
            stack.addLast(i)
        }
        else {
             stack.addLast(i)
        }
        i += 1
    }

    /**
     *  process a decreasing stack here
     *  The top's element right range becomes the next element's y range as next element
     *  is always > top element since stack is decreasing at this point.
     */
    var stackTopRange = maxRangePerElement[stack.last()]
    var currentStackIndex = stack.removeLast()
    while ( !stack.isEmpty()) {
        //println("processing %s".format(nums[stack.last()]))
        val currentMaxPerRange = maxRangePerElement[stack.last()]
       // if ( nums[currentStackIndex] != nums[stack.last()] ) { // do not change range when elements are equal
            currentMaxPerRange?.y = stackTopRange?.y!!
        //}
        stackTopRange = currentMaxPerRange
        currentStackIndex = stack.removeLast()
    }

    var maxSum = 0L
    for ( i in 0..n-1) {

        val x = maxRangePerElement[i]?.x!!
        val y = maxRangePerElement[i]?.y!!
        maxSum += ((y-x) + (i - x) * (y-i) ) * nums[i]
        //println("%s :  %s".format(nums[i], maxRangePerElement[i]))
    }

    return maxSum
}

fun subArrayRanges(nums: IntArray): Long {

    var maxSum = 0L
    var minSum = 0L
    maxSum = calculateMaxRangeSum(nums)
    minSum = calculateMinRanges(nums)
    println("%s, %s".format(maxSum, minSum))
    return maxSum - minSum
}

//  4,6,1,5,6,7,8,9,1,6,7,8,10,20,11,20,1
// 4,6,1,5,6,7,8,9,1
//  14279517413
//var input = 44100,-56253,-87825,85180,9757,38400,-79790,70906,-84011,-47443,7591,51955,82857,88601,-40488,50522,67401,52187,-95259,29098,-90134,89896,-77967,-22428,-28532,-90237,-99696,-62447,87981,-12925,7985,39797,-47714,-63656,-74771,22170,-23500,93592,-4531,84380,-6001,85246,-97211,-59961,94258,61193,5647,50267,-84298,-74537,93428,-65618,65642,13034,29918,71695,-73036,-77551,534,-89410,-48966,75211,-58026,80627,15452,36970,8639,24721,-69696,53800,-31659,57435,-48166,-20745,45691,27731,-58085,84151,68345,89265,-86124,-62665,3042,-91274,778,13232,14311,16015,-53543,66854,-71929,84591,-12147,-92987,14605,48389,-58397,-77052,93904,-18773,-25516,-41432,82123,-21665,-54708,-12475,30278,-67332,-26924,-15315,8680,49804,19357,-90558,80541,21961,-54950,91191,82745,-81144,49588,49217,54596,-618,78471,-18303,78836,48380,-34052,83040,27224,93503,94966,-53188,-96363,22665,-53675,-36581,72081,90508,-18263,-84327,86545,-11804,-3786,78317,96389,68162,-14903,-62461,-55365,-66125,-82587,-4308,93327,-76806,17561,53395,-64928,-42247,21804,47261,-32844,-24622,-45726,34754,29110,15750,38051,-12767,85394,18749,59426,-23824,-49666,-1690,24342,-31252,-3506,-63185,-92805,-16740,-51909,-80956,-28454,-59771,42745,-38088,20909,40377,54491,6580,-97200,-56717,55680,-22376,70854,65247,-12746,82514,56879,65217,-49417,5355,53319,63307,78552,49928,-21622,85397,-3109,-34472,-88532,37545,-87396,-22167,-78133,-69524,76682,-10739,-13888,-92714,57196,-99809,62781,-34925,24895,-6503,37424,75340,53525,-40106,28872,75499,42659,99828,-81267,-76421,-91194,-71986,15377,-24108,23000,9246,-87219,-46664,-39120,2680,54553,86907,-44211,37793,-52369,40984,-83117,89487,-95440,90367,94347,-35235,-31538,-38342,-65860,67173,-60069,-40497,-77873,42434,90335,22860,28309,-25074,-48919,64655,98456,-76009,-42841,94788,-1502,-8159,-33158,20468,32838,-70461,62674,-36618,-94199,-10011,-65259,-47358,84651,9074,-35506,15918,-36663,65790,78262,-72474,-87275,-9757,-4125,64710,85251,-15492,24729,53548,9289,50720,34291,-76939,-8976,84142,53871,-57634,-81699,-49082,52811,8794,-20580,-76504,90150,-83198,-32686,49607,74307,46813,-98412,-43808,58346,18950,72143,-95992,-99571,17346,2416,56359,9009,-81938,98957,-34143,-53695,-42578,-29657,-46722,31255,59060,69214,-64971,66461,-38996,-4668,-13508,-49576,24564,48014,925,79429,59323,86294,22145,64718,-10480,83072,-34638,21766,60961,67618,82348,89014,24046,-89014,18861,-30218,-7192,19708,-18537,25481,-21690,-23903,35083,34470,-29076,88710,-65080,-69025,84659
val nums = intArrayOf(9, 5, 4, 3, 2)
println(subArrayRanges(nums))
