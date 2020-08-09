import java.io.IOException;

public class mainClass {

    public static void main (String [] args)
    {
        //run finalScrape.py
        Process p;
        String[] runPy = {"python3", " finalScrape.py"};
        try {
            p = Runtime.getRuntime().exec(runPy);

        } catch (IOException e){
            System.err.println(e);
        }

        parser.parse();


    }
    
}