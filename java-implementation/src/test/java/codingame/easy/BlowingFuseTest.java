package codingame.easy;

import org.junit.Test;
import utils.StdInOutTestUtils;

public class BlowingFuseTest extends StdInOutTestUtils {

  @Test
  public void Blown() {
    String[] input = {
            "5 2 10",
            "11 6 11 10 10",
            "3 3",
    };
    String[] output = {"Fuse was blown."};
    testWithInputOutput(input, output);
  }

  @Test
  public void notBlown() {
    String[] input = {
            "5 8 82",
            "18 20 3 1 20",
            "2 4 3 3 5 4 2 3",
    };
    String[] output = {"Fuse was not blown.", "Maximal consumed current was 41 A."};
    testWithInputOutput(input, output);
  }

  @Test
  public void singleDevice() {
    String[] input = {
            "1 10 1",
            "9",
            "1 1 1 1 1 1 1 1 1 1",
    };
    String[] output = {"Fuse was blown."};
    testWithInputOutput(input, output);
  }

  @Test
  public void moreDevices() {
    String[] input = {
            "6 24 71",
            "10 10 14 14 14 15",
            "4 3 3 5 4 1 5 5 5 4 1 5 5 4 2 3 3 3 1 6 2 1 5 5",
    };
    String[] output = {"Fuse was not blown.", "Maximal consumed current was 49 A."};
    testWithInputOutput(input, output);
  }

  @Test
  public void moreClicksMoreDevices() {
    String[] input = {
            "11 20 72",
            "11 10 13 19 15 9 20 10 16 12 5",
            "6 8 3 4 8 6 10 3 6 5 2 4 10 2 6 6 4 2 4 5",
    };
    String[] output = {"Fuse was not blown.", "Maximal consumed current was 65 A."};
    testWithInputOutput(input, output);
  }

  @Test
  public void powerHungry() {
    String[] input = {
            "20 20 200",
            "3 12 5 8 15 12 12 10 11 16 10 19 17 15 11 9 17 6 14 5",
            "1 3 5 7 5 9 2 4 6 8 10 11 13 15 2 17 12 14 16 18",
    };
    String[] output = {"Fuse was not blown.", "Maximal consumed current was 181 A."};
    testWithInputOutput(input, output);
  }

}
