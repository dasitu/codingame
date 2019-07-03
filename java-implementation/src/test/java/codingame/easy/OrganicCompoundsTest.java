package codingame.easy;

import org.junit.Test;
import utils.TestUtils;

public class OrganicCompoundsTest extends TestUtils {

  @Test
  public void saturatedHydrocarbon(){
    String[] input = {
            "1",
            "CH3(1)CH2(1)CH3",
    };
    String[] output = {"VALID"};
    testWithInputOutput(input, output);
  }

  @Test
  public void unsaturatedHydrocarbon(){
    String[] input = {
            "1",
            "CH2(2)CH1(1)CH3",
    };
    String[] output = {"VALID"};
    testWithInputOutput(input, output);
  }

  @Test
  public void hydrocarbonWith1Substituent(){
    String[] input = {
            "3",
            "CH3   CH3",
            "(1)   (1)",
            "CH2(1)CH1(1)CH3",
    };
    String[] output = {"VALID"};
    testWithInputOutput(input, output);
  }

  @Test
  public void multipleSubstituents(){
    String[] input = {
            "5",
            "CH3(1)CH1(1)CH2(1)CH1(1)CH3",
            "      (1)         (1)",
            "      CH3         CH1(1)CH1(1)CH3",
            "                  (1)",
            "                  CH3",
    };
    String[] output = {"INVALID"};
    testWithInputOutput(input, output);
  }

  @Test
  public void unsaturatedHydrocarbonWithSubstituents(){
    String[] input = {
            "5",
            "CH2(2)CH0(1)CH1(2)CH0(1)CH3",
            "      (1)         (1)",
            "      CH0         CH1(1)CH2(1)CH3",
            "      (3)         (1)",
            "      CH1         CH3",
    };
    String[] output = {"VALID"};
    testWithInputOutput(input, output);
  }

  @Test
  public void invalid(){
    String[] input = {
            "5",
            "CH2(2)CH0(1)CH1(2)CH0(1)CH3",
            "      (1)         (1)",
            "      CH1         CH1(1)CH2(1)CH3",
            "      (2)         (2)",
            "      CH2         CH3",
    };
    String[] output = {"INVALID"};
    testWithInputOutput(input, output);
  }

  @Test
  public void cyclicHydrocarbon(){
    String[] input = {
            "3",
            "CH2(1)CH2",
            "(1)   (1)",
            "CH2(1)CH2",
    };
    String[] output = {"VALID"};
    testWithInputOutput(input, output);
  }

  @Test
  public void cyclicHydrocarbonWithSubstituents(){
    String[] input = {
            "5",
            "CH2(1)CH2(1)CH2",
            "(1)         (1)",
            "CH2         CH1(2)CH3",
            "(1)         (1)",
            "CH2(1)CH2(1)CH2",
    };
    String[] output = {"INVALID"};
    testWithInputOutput(input, output);
  }

  @Test
  public void twoCarbonCycles(){
    String[] input = {
            "5",
            "CH2(1)CH2(1)CH1(1)CH2",
            "(1)         (1)   (1)",
            "CH2         CH2   CH2",
            "(1)         (1)   (1)",
            "CH2(1)CH2(1)CH1(1)CH2",
    };
    String[] output = {"VALID"};
    testWithInputOutput(input, output);
  }

  @Test
  public void enormousCompound(){
    String[] input = {
            "11",
            "CH2(1)CH1(1)CH1(1)CH2",
            "(1)   (1)   (1)   (1)",
            "CH2   CH3   CH2   CH2",
            "(1)         (1)   (1)",
            "CH2(1)CH1(1)CH1(1)CH1",
            "      (1)         (1)",
            "      CH2   CH1(1)CH1(1)CH3",
            "      (1)   (2)",
            "      CH2   CH1(2)CH1",
            "      (1)         (1)",
            "      CH2(1)CH1(2)CH4",
    };
    String[] output = {"INVALID"};
    testWithInputOutput(input, output);
  }

  @Test
  public void codingame(){
    String[] input = {
            "7",
            "CH2(1)CH1(1)CH1(1)CH3",
            "(1)         (1)",
            "CH2         CH2",
            "(1)         (1)",
            "CH2         CH2   CH3",
            "(1)         (1)   (1)",
            "CH2(1)CH3   CH2(1)CH2",
    };
    String[] output = {"INVALID"};
    testWithInputOutput(input, output);
  }
}
