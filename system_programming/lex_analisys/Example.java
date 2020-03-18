import java.io.BufferedWriter;
import java.io.FileWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.ArrayList;

public class Example {

    private static class PatternWithColor {

        private Pattern pattern;
        private String color;
        int a = 5;
        double b = 4.5 + 0xfabcdef1;
        boolean t = true;
        ArrayList<Integer> ar = new ArrayList<Integer>(5);

        void f(){
            this.ar.add(5);
        }

        private PatternWithColor(String pattern, String color) {
            this.pattern = Pattern.compile(pattern);
            this.color = color;
        }
    }

    private static void writeToFile(String content, String fileName) {
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));

            writer.write(content);

            writer.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }


    private static void createHtml(String source, String out_file_name) {
        StringBuilder builder = new StringBuilder();

        /*
        String[] colors = colorText(source);

        for (int i = 0; i < source.length(); i++)
            builder.append(String.format("<span style='color:%s;'>%c</span>", colors[i], source.charAt(i)));

        builder.append(
                "</body>\n" +
                        "</html>"
        );
        */

        writeToFile(builder.toString(), out_file_name);
    }

    public static void main(String[] args) {
        for (String s : Arrays.asList("Main")) {

            String source = "hey handsome)";
        }
    }
}
