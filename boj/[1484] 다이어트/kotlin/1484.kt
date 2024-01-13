import kotlin.math.pow

fun main() {
    val G = readln().toInt()
    var start = 1.0
    var end = 2.0
    val answer = mutableListOf<Int>()

    while (start != end) {
        when {
            (end.pow(2) - start.pow(2)) > G.toDouble() -> start++
            (end.pow(2) - start.pow(2)) == G.toDouble() -> {
                answer.add(end.toInt())
                start++
            }
            else -> end++
        }
    }
    if (answer.isEmpty()) {
        println(-1)
    } else {
        answer.forEach { println(it) }
    }
}
