package codingame.clash;

import org.junit.Test;
import utils.StdInOutTestUtils;

public class NumberIncreaseTest extends StdInOutTestUtils {

  @Test
  public void test1() {
    String[] input = {
            "10",
            "-64",
            "71",
            "-98",
            "-60",
            "-18",
            "41",
            "88",
            "-2",
            "-24",
            "63",
    };
    String[] output = {
           "-63",
           "71",
           "-97",
           "-59",
           "-17",
           "41",
           "89",
           "-1",
           "-23",
           "63",
    };
    testWithInputOutput(input, output);
  }
}