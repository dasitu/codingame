package codingame.clash;

import org.junit.Test;
import utils.StdInOutTestUtils;

public class ChangeLetterTest extends StdInOutTestUtils {

  @Test
  public void test() {
    String[] input = {"ABCDEFG"};
    String[] output = {"BADCFEG"};
    testWithInputOutput(input, output);
  }
}