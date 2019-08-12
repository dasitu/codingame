//https://www.codingame.com/ide/puzzle/hunger-games

package codingame.easy;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.SortedSet;
import java.util.TreeMap;
import java.util.TreeSet;

public class HungerGames {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    Map<String, List<List<String>>> board = new TreeMap<>();

    int tributes = in.nextInt();
    if (in.hasNextLine()) {
      in.nextLine();
    }
    for (int i = 0; i < tributes; i++) {
      String playerName = in.nextLine();
      List<String> killer = new ArrayList<>(1);
      killer.add("Winner");
      List<String> killed = new ArrayList<>();
      List<List<String>> killerAndKilled = new ArrayList<>();
      killerAndKilled.add(killed);
      killerAndKilled.add(killer);
      board.put(playerName, killerAndKilled);
    }
    int turns = in.nextInt();
    if (in.hasNextLine()) {
      in.nextLine();
    }
    for (int i = 0; i < turns; i++) {
      String info = in.nextLine();
      String[] infos = info.split("killed");
      String killer = infos[0].replace(" ","");
      String killed = infos[1].replace(" ","");

      if (killed.contains(",")) {
        // add killed
        String[] killeds = killed.split(",");
        Arrays.sort(killeds);
        board.get(killer).get(0).addAll(Arrays.asList(killeds));

        // add corresponding killer
        for (String k : killeds) {
          board.get(k).get(1).set(0, killer);
        }
      } else {
        board.get(killer).get(0).add(killed);
        board.get(killed).get(1).set(0, killer);
      }
    }

    SortedSet<String> keys = new TreeSet<>(board.keySet());
    int i = 0;
    for (String k : keys) {
      System.out.println("Name: " + k);
      String killedNames = "None";
      Collections.sort(board.get(k).get(0));
      if (board.get(k).get(0).size() != 0){
        killedNames = String.join(", ", board.get(k).get(0));
      }
      System.out.println("Killed: " + killedNames);
      System.out.println("Killer: " + board.get(k).get(1).get(0));
      if (i < board.size() - 1){
        System.out.println("");
      }
      i++;
    }
  }
}
