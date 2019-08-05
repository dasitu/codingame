package codingame.clash;

import org.junit.Test;
import utils.StdInOutTestUtils;

public class AverageNumberTest extends StdInOutTestUtils {

  @Test
  public void test() {
    String[] input = {
            "8",
            "3",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
    };
    String[] output = {"2.0 3.0 4.0 5.0 6.0 7.0"};
    testWithInputOutput(input, output);
  }
}