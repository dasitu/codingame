package codingame.clash;

import java.util.Scanner;

public class DigitCount {

  public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      String s = in.nextLine();
      double t = 0.0;
      double m = 0.0;
      for (char c: s.toCharArray()){
        if (Character.isDigit(c)){
          t++;
        }
        if(Character.isLetter(c)){
          m++;
        }
      }
      System.out.println((int)Math.round(m/t));
    }
  }