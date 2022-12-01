import java.io.*;
import java.util.Scanner;


public class Problem1 {
    public static void main(String[] args) {
        
        try {
            File file = new File("\\Users\\Nemesis\\Repositories\\adventofcode2022\\problem1\\samplse.txt");

            Scanner reader = new Scanner(file);

            int highestCalories = 0;
            int currentCalories = 0;
            while(reader.hasNextLine()) {
                String stringVal = reader.nextLine();
                if (stringVal == "\n") {
                    if (highestCalories < currentCalories) {
                        highestCalories = currentCalories
                    }
                }
            }
        } catch(Exception e) {
            System.out.println("ERROR: " + e.toString());
        }
    }
}