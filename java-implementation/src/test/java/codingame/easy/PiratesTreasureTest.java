package codingame.easy;

import org.junit.Test;
import utils.TestUtils;

public class PiratesTreasureTest extends TestUtils {
  @Test
  public void smallestIsland(){
    String[] input = {
            "2",
            "2",
            "0 1",
            "1 1",
    };
    String[] output = {"0 0"};
    testWithInputOutput(input, output);
  }

  @Test
  public void fullySurrounded(){
    String[] input = {
           "4",
           "4",
           "1 1 1 0",
           "1 0 1 0",
           "1 1 1 1",
           "0 0 1 1",
    };
    String[] output = {"1 1"};
    testWithInputOutput(input, output);
  }

  @Test
  public void smallIsland(){
    String[] input = {
            "5",
            "7",
            "0 0 1 1 0",
            "0 1 0 0 1",
            "0 1 1 1 0",
            "0 1 0 1 1",
            "1 1 1 1 0",
            "0 1 0 0 1",
            "1 0 0 0 0",
    };
    String[] output = {"2 3"};
    testWithInputOutput(input, output);
  }

  @Test
  public void largeIsland(){
    String[] input = {
            "25",
            "25",
            "0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0",
            "1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0",
            "0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
            "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
            "0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 1 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1",
    };
    String[] output = {"23 23"};
    testWithInputOutput(input, output);
  }

  @Test
  public void edge(){
    String[] input = {
            "5",
            "4",
            "0 1 0 1 0",
            "0 1 1 1 0",
            "1 0 1 1 1",
            "0 0 0 0 0",
    };
    String[] output = {"2 0"};
    testWithInputOutput(input, output);
  }

}
