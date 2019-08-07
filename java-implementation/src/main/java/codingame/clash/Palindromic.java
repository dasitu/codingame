package codingame.clash;

import java.util.Scanner;

public class Palindromic {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long N = in.nextLong();
    int b = in.nextInt();
    String o = Long.toString(N, b);
    int i = Integer.parseInt( "f", 16 );
    char a = 'a';
    System.out.println((int)a);

    int c = 99;
    System.out.println((char)c);
    StringBuilder g = new StringBuilder(o);
    g.reverse();
    System.out.println(g.toString().equals(o));
  }
}