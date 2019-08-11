package codingame.clash;

import java.util.Scanner;

public class TimeFormat {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    String duration = in.next();
    String a[] = duration.split(":");
    System.out.println(Integer.parseInt(a[0]) * 60 + Integer.parseInt(a[1]));
  }
}
