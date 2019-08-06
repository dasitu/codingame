package codingame.clash;

import java.util.Scanner;

public class NumberIncrease {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int count = in.nextInt();
    for (int i = 0; i < count; i++) {
      int s = in.nextInt();
      int out = s % 2 == 0 ? s + 1 : s ;
      System.out.println(out);
    }
  }
}
