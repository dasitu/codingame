package codingame.clash;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class FileModeCal {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    Map<String, Integer> values = new HashMap<>();
    values.put("r", 4);
    values.put("w", 2);
    values.put("x", 1);
    values.put("-", 0);
    int N = in.nextInt();
    for (int i = 0; i < N; i++) {
      String word = in.next();
      char[] fileMode = word.substring(1).toCharArray();
      for (int j = 0; j < fileMode.length; j += 3) {
        int sum = 0;
        for (int k = 0; k < 3; k++) {
          sum += values.get(String.valueOf(fileMode[k + j]));
        }
        System.out.print(sum);
      }
      System.out.println("");
    }
  }
}
