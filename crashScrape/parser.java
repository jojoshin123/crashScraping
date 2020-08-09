import java.io.File;
import java.io.FileNotFoundException;  // to handle errors
import java.io.FileWriter; //to write to output file
import java.io.IOException;
import java.util.Scanner; // to read text files

public class parser {

    public static void parse(){

        try {
            
            //open crashData file from finalScrape.py output
            File f = new File("/Users/jonahshin/Side Projects/crashScrape/crashData.txt");

            //define output file and define FileWriter
            File output = new File("/Users/jonahshin/Side Projects/crashScrape/output.txt");
            FileWriter writer = new FileWriter(output);

            //set delimiter
            Scanner scan = new Scanner(f).useDelimiter("<div class=\"jss108\"><button class=\"MuiButtonBase-root MuiButton-root MuiButton-text jss109 jss11");

            //TODO: eliminate delimiter to make code more effective?

            while (scan.hasNext()) {
                String ex = scan.next();
                String sub = ex.substring(ex.indexOf("label")+7, ex.indexOf("label")+11);

                //String parsed = ex.substring(startIndex, endIndex);

                //Write to output.txt
                writer.write(sub + "\n");


                //System.out.println(sub);
            }
            scan.close();
            writer.close();

        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

    }
}
