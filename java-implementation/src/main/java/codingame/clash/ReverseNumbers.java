package codingame.clash;

import java.util.Scanner;

public class ReverseNumbers {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int t = 0;
    int l = 0;
    for (int i = 0; i < n; i++) {
      int number = in.nextInt();
      if (number >= 10) {
        t += number / 10;
        l += number % 10;
      } else {
        t += number;
      }
    }

    StringBuilder a = new StringBuilder();
    if (l != 0) {
      a.append(l / 10);
    }
    a.append(t);
    System.out.println(a.toString());
  }
}
