package codingame.clash;

import org.junit.Test;
import utils.StdInOutTestUtils;

public class MuffinMenTest extends StdInOutTestUtils {

  @Test
  public void test(){
    String[] input = {
            "1000 50 10 30 15",
    };
    String[] output = {
            "true",
            "3",
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void test1(){
    String[] input = {
            "0 2 1 4 10",
    };
    String[] output = {
            "true",
            "0",
    };
    testWithInputOutput(input, output);
  }
}
