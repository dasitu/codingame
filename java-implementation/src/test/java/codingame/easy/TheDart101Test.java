package codingame.easy;

import org.junit.Test;
import utils.StdInOutTestUtils;

public class TheDart101Test extends StdInOutTestUtils {

  @Test
  public void twoPlayers(){
    String[] input = {
            "2",
            "Hugo",
            "Guillaume",
            "10 5 3*18 15 5 4 8",
            "5 5 10 2*19 5 6 2*5 1 20 1",
    };
    String[] output = {"Hugo"};
    testWithInputOutput(input, output);
  }

  @Test
  public void oneWinOneLose(){
    String[] input = {
            "2",
            "Lisa",
            "Emma",
            "10 5 3*18 15 5 4 8",
            "5 5 2*18 9 3 2 8 1 3",
    };
    String[] output = {"Lisa"};
    testWithInputOutput(input, output);
  }

  @Test
  public void oneMissed(){
    String[] input = {
            "2",
            "Candice",
            "Elise",
            "10 5 3*18 20 X 2*14 4",
            "5 5 10 2*19 5 6 2*5 1 20 1",
    };
    String[] output = {"Candice"};
    testWithInputOutput(input, output);
  }

  @Test
  public void twoMissed(){
    String[] input = {
            "2",
            "Fred",
            "Charles",
            "10 6 3*18 X 19 X 2*25 2",
            "5 5 10 2*19 5 6 2*5 1 20 1",
    };
    String[] output = {"Fred"};
    testWithInputOutput(input, output);
  }

  @Test
  public void OverTheScore(){
    String[] input = {
            "2",
            "Noemie",
            "Nicolas",
            "2 5 5 19 5 6 10 1 20 1 2 5",
            "3*17 5 12 5 2 3 15 9 20 3",
    };
    String[] output = {"Nicolas"};
    testWithInputOutput(input, output);
  }

  @Test
  public void twoPlayersAndLotOfShoots(){
    String[] input = {
           "2",
           "Yoan",
           "Ludo",
           "20 1 5 2*5 3*18 X X 19 11 10 12 16 7 2*11 X 3*17 3*7",
           "3*20 3*19 3*17 25 20 X X X 2*25 3*14 X X X 3*20 X 5 X 3*18",
    };
    String[] output = {"Ludo"};
    testWithInputOutput(input, output);
  }

  @Test
  public void fourPlayers(){
    String[] input = {
            "4",
            "Eric",
            "Delphine",
            "Patricia",
            "Yan",
            "6 2 7 15 2*10 8 2 3 6 15 2 1 3 11",
            "4 3 2 1 1 1 X X 10 2 3 5",
            "X X X X X X X X X 2*25 3*17",
            "3*15 2*10 3*5 2*12 2*7 2*7 3*15",
    };
    String[] output = {"Patricia"};
    testWithInputOutput(input, output);
  }

  @Test
  public void eightPlayers(){
    String[] input = {
           "8",
           "Eric",
           "Delphine",
           "Patricia",
           "Yan",
           "David",
           "Hugo",
           "Ludo",
           "Yoan",
           "4 3 2 1 1 1 X X 10",
           "X X X X X X X X X 2*25 3*17",
           "6 2 7 15 2*10 8 2 3 6 15 2 1 3 11",
           "3*15 2*10 3*5 2*12 2*7 2*7 3*15",
           "2*25 3*17",
           "10 5 3*18 20 X 2*14 4",
           "5 5 10 2*19 5 6 2*5 1 20 1",
           "10 5 3*18 20 X 2*14 10",
    };
    String[] output = {"David"};
    testWithInputOutput(input, output);
  }

}
