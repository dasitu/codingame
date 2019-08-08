package codingame.clash;

import java.util.Scanner;

public class LinearFunction {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int x1 = in.nextInt();
    int y1 = in.nextInt();
    int x2 = in.nextInt();
    int y2 = in.nextInt();

    int a = (y2 - y1) / (x2 - x1);
    int b = y1 - (a * x1);
    String s = b > 0 ? "+" + b : String.valueOf(b);
    System.out.println(a + "*x" + s);
  }
}