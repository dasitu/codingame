package codingame.clash;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Reverse {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int factor = in.nextInt();
    int bound1 = in.nextInt();
    int bound2 = in.nextInt();

    List<String> a = new ArrayList<>();
    for (int i = 0; i < bound2; i++) {
      if (factor * i > bound1) {
        a.add(String.valueOf(factor * i));
      }
    }
    System.out.println(String.join(" ", a));
  }
}
