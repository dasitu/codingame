package codingame.clash;

import org.junit.Test;
import utils.StdInOutTestUtils;

public class FileModeCalTest extends StdInOutTestUtils {
  @Test
  public void test() {
    String[] input = {
            "3",
            "-rw-rwxr-x",
            "-rwxrwxrwx",
            "-r--------",
    };
    String[] output = {"675","777","400"};
    testWithInputOutput(input, output);
  }
}
