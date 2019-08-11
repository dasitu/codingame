package codingame.clash;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class PrintFormat {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    String A = in.nextLine();
    int L = in.nextInt();
    int sum = 0;
    for (char c: String.valueOf(L).toCharArray()){
      sum *= Character.getNumericValue(c) + 1;
    }
    System.out.println(sum);
    StringBuilder f = new StringBuilder();
    for (int i = 0; i < A.length() + 4; i++) {
      f.append("*");
    }
    String a = f.toString();
    f.append(System.lineSeparator());
    f.append("* ");
    f.append(A);
    f.append(" *");
    f.append(System.lineSeparator());
    f.append(a);
    System.out.println(f.toString());
  }
}
