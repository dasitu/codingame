package codingame.clash;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Porker {

  private static int calculateValue(List<Integer> cards, String type) {
    int returnValue = 0;
    int weight = 1;
    switch (type) {
      case "triple": {
        weight = 1000000;
        break;
      }
      case "straight": {
        weight = 10000;
        break;
      }
      case "pair": {
        weight = 100;
        break;
      }
      default: { }
    }
    for (Integer card : cards) {
      returnValue += card * weight;
    }
    return returnValue;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int N = in.nextInt();
    int biggestValue = 0;
    String output = "";
    for (int i = 0; i < N; i++) {
      String name = in.next();
      List<Integer> cards = new ArrayList<>();
      int X = in.nextInt();
      int Y = in.nextInt();
      int Z = in.nextInt();
      cards.add(X);
      cards.add(Y);
      cards.add(Z);
      Collections.sort(cards);
      String type = "";
      if (X == Y && Y == Z) {
        type = "triple";
      } else if (X == Y || Y == Z || Z == X) {
        type = "pair";
      } else if (Z - Y == 1 && Y - X == 1) {
        type = "straight";
      } else {
        type = "highCard";
      }

      int cardValue = calculateValue(cards, type);
      if (cardValue > biggestValue) {
        output = name;
        biggestValue = cardValue;
      } else if (cardValue == biggestValue) {
        output += " " + name;
      }
    }
    System.out.println(output);
  }
}
