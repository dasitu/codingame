package codingame.clash;

import java.util.*;

class NumberRatio {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int N = in.nextInt();
    int R = in.nextInt();
    StringBuilder s = new StringBuilder();
    for (int i = 0; i < N; i++) {
      int n = (int)Math.pow(R, i);
      //s.append(String.format("%.2f", n));
      s.append(n);
      s.append(" ");
    }
    System.out.print(s.toString().trim());
  }
}