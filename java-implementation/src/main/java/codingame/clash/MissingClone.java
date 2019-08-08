package codingame.clash;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class MissingClone {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String L = in.nextLine();
    String[] a = L.split(" ");

    int smallest = 9999;
    String rt = "";
    for (String letter : a) {
      int currentCount = Collections.frequency(Arrays.asList(a), letter);
      if (currentCount < smallest) {
        rt = letter;
        smallest = currentCount;
      }
    }
    System.out.println(rt);
  }
}
