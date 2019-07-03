// https://www.codingame.com/ide/puzzle/the-dart-101

package codingame.easy;

import java.util.Scanner;
import java.util.regex.Pattern;

public class TheDart101 {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int playerCount = in.nextInt();
    String[] players = new String[playerCount];
    String[] shoots = new String[playerCount];
    int winnerIndex = 0;
    int winnerScore = 0;
    int winnerRound = 0;
    if (in.hasNextLine()) {
      in.nextLine();
    }
    for (int i = 0; i < playerCount; i++) {
      players[i] = in.nextLine();
    }
    for (int i = 0; i < playerCount; i++) {
      shoots[i] = in.nextLine();
      int[] playerScoreAndRound = calculateScore(shoots[i]);
      int playerScore = playerScoreAndRound[0];
      int playerRound = playerScoreAndRound[1];
      if (playerScore > winnerScore) {
        winnerScore = playerScore;
        winnerRound = playerRound;
        winnerIndex = i;
      } else if (playerScore == winnerScore && playerRound < winnerRound) {
        winnerRound = playerRound;
        winnerIndex = i;
      }
    }

    System.out.println(players[winnerIndex]);
  }

  private static int[] calculateScore(String shoots) {
    String[] shoot = shoots.split(" ");
    int[] totalScoreAndRound = {0, 0};
    int shootIndex;
    int shootIndexInRound;
    for (shootIndex = 0; shootIndex < shoot.length; shootIndex += shootIndexInRound) {
      System.err.println("round:" + totalScoreAndRound[1]);
      int roundScore = 0;
      StringBuilder missState = new StringBuilder();
      for (shootIndexInRound = 0;
           shootIndexInRound < 3 && (shootIndexInRound + shootIndex) < shoot.length;
           shootIndexInRound++) {
        String singleShoot = shoot[shootIndex + shootIndexInRound];
        System.err.println(singleShoot);

        if (singleShoot.contains("*")) { // * situation
          String[] multipleValue = singleShoot.split(Pattern.quote("*"));
          roundScore += Integer.parseInt(multipleValue[0]) * Integer.parseInt(multipleValue[1]);
          missState.append("O");
        } else if (singleShoot.equals("X")) { // X handling
          roundScore -= 20;
          missState.append("X");
          if (missState.toString().equals("XXX")) {
            totalScoreAndRound[0] = 0;
            roundScore = 0;
          } else if (missState.toString().contains("XX")) {
            roundScore -= 10;
          }
        } else { // just add the number
          roundScore += Integer.parseInt(singleShoot);
          missState.append("O");
        }

        // handle the exceed situation, round is end
        int total = totalScoreAndRound[0] + roundScore;
        if (total > 101) {
          System.err.println("totalScore:" + total + " Exceed 101.");
          roundScore = 0;
          shootIndexInRound++;
          break;
        }
      }
      totalScoreAndRound[1]++;
      totalScoreAndRound[0] += roundScore;
      System.err.println("roundScore:" + roundScore);
      System.err.println("totalScore:" + totalScoreAndRound[0]);
    }
    return totalScoreAndRound;
  }
}