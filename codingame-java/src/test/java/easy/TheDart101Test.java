package easy;

import org.junit.Test;
import utils.TestUtils;

public class TheDart101Test extends TestUtils {

  @Test
  public void test2Players(){
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
  public void test1Win1Loser(){
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
  public void testOneMissed(){
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
  public void testTowMissed(){
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
}
