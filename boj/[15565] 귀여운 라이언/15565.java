import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        final int N = Integer.parseInt(st.nextToken());
        final int K = Integer.parseInt(st.nextToken());
        final int[] dolls = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            dolls[i] = Integer.parseInt(st.nextToken());
        }

        int start = 0;
        int end = 0;
        final Map<Integer, Integer> count = new HashMap<>();
        count.put(dolls[end], 1);
        int answer = 1000001;
        while (end < N) {
            if (count.getOrDefault(1, 0) == K) {
                answer = Math.min(answer, end - start + 1);
                count.put(dolls[start], count.getOrDefault(dolls[start], 0) - 1);
                start += 1;
            } else {
                end += 1;
                if (end >= N) {
                    break;
                }
                count.put(dolls[end], count.getOrDefault(dolls[end], 0) + 1);
            }
        }

        if (answer == 1000001) {
            answer = -1;
        }
        System.out.println(answer);
    }
}
