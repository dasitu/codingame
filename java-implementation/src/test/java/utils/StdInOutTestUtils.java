package utils;

import org.junit.After;
import org.junit.Before;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.lang.reflect.Method;

import static org.junit.Assert.assertEquals;

public class StdInOutTestUtils {

  private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
  private final ByteArrayOutputStream errContent = new ByteArrayOutputStream();
  private final String testClassName = this.getClass().getName().replaceFirst("Test$","");

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

  protected void testWithInputOutput(String[] input, String[] output){

    StringBuilder lines = new StringBuilder();
    for (String line: input){
      lines.append(line);
      lines.append(System.getProperty("line.separator"));
    }
    ByteArrayInputStream in = new ByteArrayInputStream(lines.toString().getBytes());
    System.setIn(in);
    try {
      Class<?> testObjectClass = Class.forName(testClassName);
      Method meth = testObjectClass.getMethod("main", String[].class);
      String[] params = null;
      meth.invoke(null, (Object) params);
    }
    catch (Exception e){
      System.out.println(e.getCause().toString());
    }

//    StringWriter expectedStringWriter = new StringWriter();
//    PrintWriter printWriter = new PrintWriter(expectedStringWriter);
//    for (String line: output) {
//      printWriter.println(line);
//    }
//    printWriter.close();
//    String expected = expectedStringWriter.toString();

    StringBuilder expected = new StringBuilder();
    for (String line: output){
      expected.append(line);
      expected.append(System.getProperty("line.separator"));
    }

    assertEquals(expected.toString(), outContent.toString());
  }
}
