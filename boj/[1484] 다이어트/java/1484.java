import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int G = Integer.parseInt(br.readLine());

        double start = 1.0;
        double end = 2.0;
        final List<Integer> answer = new ArrayList<>();
        while (start != end) {
            if ((Math.pow(end, 2.0) - Math.pow(start, 2.0)) > G) {
                start++;
            } else if ((Math.pow(end, 2.0) - Math.pow(start, 2.0)) == G) {
                answer.add((int) end);
                start++;
            } else {
                end++;
            }
        }

        if (answer.isEmpty()) {
            System.out.println(-1);
        } else {
            for (final int a : answer) {
                System.out.println(a);
            }
        }
    }
}
