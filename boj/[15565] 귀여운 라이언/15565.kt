import kotlin.math.min

fun main(args: Array<String>) {
    val (N, K) = readln().split(" ").map { it.toInt() }
    val dolls = readln().split(" ").map { it.toInt() }

    var start = 0
    var end = 0
    var answer = Int.MAX_VALUE
    val count = mutableMapOf<Int, Int>().withDefault { 0 }
    count[dolls[end]] = 1

    while (end < N) {
        if (count[1] == K) {
            answer = min(answer, end - start + 1)
            count[dolls[start]] = count.getValue(dolls[start]).minus(1)
            start++
        } else {
            end++
            if (end < N) {
                count[dolls[end]] = count.getValue(dolls[end]).plus(1)
            }
        }
    }

    if (answer == Int.MAX_VALUE) {
        answer = -1
    }
    println(answer)
}
