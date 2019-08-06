package codingame.clash;

import java.util.Scanner;

public class MuffinMen {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    float m = in.nextInt();
    float b = in.nextInt();
    float t = in.nextInt();
    float mb = in.nextInt();
    float bt = in.nextInt();

    int neededBox = (int) Math.ceil(m / mb);
    float actualBox = b;
    if (neededBox <= b) {
      actualBox = neededBox;
    }
    int neededTrucks = (int) Math.ceil(actualBox / bt);
    if (neededTrucks <= t) {
      System.out.println("true");
      System.out.println(neededTrucks);
    } else {
      System.out.println("false");
      System.out.println((int) (bt * t * actualBox * m));
    }
  }
}
