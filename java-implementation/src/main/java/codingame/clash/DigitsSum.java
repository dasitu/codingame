package codingame.clash;

import java.util.Scanner;

public class DigitsSum {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int N = in.nextInt();
    String binStr = Integer.toBinaryString(N);
    int sum = 0;
    for (char b : binStr.toCharArray()) {
      sum += Integer.parseInt(String.valueOf(b));
    }
    System.out.println(sum);
    // System.out.println(N + " in Base 8 : " + Integer.toOctalString(N));
    // System.out.println(N + " in Base 16 : " + Integer.toHexString(N));
  }
}