package codingame.clash;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class AverageNumber {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int L = in.nextInt();
    int W = in.nextInt();
    List<Integer> all = new ArrayList<>();
    for (int i = 0; i < L; i++) {
      int S = in.nextInt();
      all.add(S);
    }

    List<String> answer = new ArrayList<>();
    for (int i = 0; i <= L - W; i++) {
      float sumValue = 0;
      for (int j = 0; j < W; j++) {
        sumValue += all.get(i + j);
      }
      answer.add(String.format("%.1f", sumValue / W));
    }
    System.out.println(String.join(" ", answer));
  }
}
