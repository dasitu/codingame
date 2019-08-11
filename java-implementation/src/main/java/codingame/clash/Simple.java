package codingame.clash;

import java.util.Scanner;

public class Simple {

    public static void main(String args[]) {
      Scanner in = new Scanner(System.in);
      int N = in.nextInt();
      double highest = 0;
      double shortest = 999999;
      for (int i = 0; i < N; i++) {
        String object = in.next();
        float initialVelocity = in.nextFloat();
        double tH = 2 * initialVelocity / 9.8;
        double s = 0.5 * initialVelocity * tH;
        if (s > highest){
          highest = s;
        }
        if (s < shortest){
          shortest = s;
        }
      }
      double sT;

      System.out.println("fastest_object_to_fall time");
      System.out.println("object_with_highest_altitude height");
    }
  }