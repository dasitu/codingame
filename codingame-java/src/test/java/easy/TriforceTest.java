package easy;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.*;
import java.lang.reflect.Method;

import static org.junit.Assert.assertEquals;

public class TriforceTest {

  private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
  private final ByteArrayOutputStream errContent = new ByteArrayOutputStream();
  private final static String testClassName = "easy.Triforce";

  @Before
  public void setUpStreams() {
    System.setOut(new PrintStream(outContent));
    System.setErr(new PrintStream(errContent));
  }

  @After
  public void restoreStreams() {
    System.setIn(System.in);
    System.setOut(System.out);
    System.setErr(System.err);
  }

  @Test
  public void test1(){
    String[] input = {"1"};
    String[] output = {
            ".*",
            "* *"};
    testWithInputOutput(input, output, testClassName);
  }

  @Test
  public void test3(){
    String[] input = {"3"};
    String[] output = {
            ".    *",
            "    ***",
            "   *****",
            "  *     *",
            " ***   ***",
            "***** *****"};
    testWithInputOutput(input, output, testClassName);
  }

  @Test
  public void test5(){
    String[] input = {"5"};
    String[] output = {
            ".        *",
            "        ***",
            "       *****",
            "      *******",
            "     *********",
            "    *         *",
            "   ***       ***",
            "  *****     *****",
            " *******   *******",
            "********* *********"
    };
    testWithInputOutput(input, output, testClassName);
  }

  @Test
  public void test10(){
    String[] input = {"10"};
    String[] output = {
            ".                  *",
            "                  ***",
            "                 *****",
            "                *******",
            "               *********",
            "              ***********",
            "             *************",
            "            ***************",
            "           *****************",
            "          *******************",
            "         *                   *",
            "        ***                 ***",
            "       *****               *****",
            "      *******             *******",
            "     *********           *********",
            "    ***********         ***********",
            "   *************       *************",
            "  ***************     ***************",
            " *****************   *****************",
            "******************* *******************"
    };
    testWithInputOutput(input, output, testClassName);
  }

  private void testWithInputOutput(String[] input, String[] output, String className){

    StringBuilder lines = new StringBuilder();
    for (int i = 0; i < input.length; i++) {
      lines.append(input[i]);
      if (i + 1 != input.length){
        lines.append(System.getProperty("line.separator"));
      }
    }
    ByteArrayInputStream in = new ByteArrayInputStream(lines.toString().getBytes());
    System.setIn(in);
    try {
      Class<?> testObjectClass = Class.forName(className);
      Method meth = testObjectClass.getMethod("main", String[].class);
      String[] params = null;
      meth.invoke(null, (Object) params);
    }
    catch (Exception e){
      System.out.println(e.getCause().toString());
    }

    StringWriter expectedStringWriter = new StringWriter();
    PrintWriter printWriter = new PrintWriter(expectedStringWriter);

    for (String line: output) {
      printWriter.println(line);
    }
    printWriter.close();

    String expected = expectedStringWriter.toString();
    assertEquals(expected, outContent.toString());
  }

}
