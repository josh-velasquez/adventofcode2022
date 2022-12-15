import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Problem8 {
    public static void main(String[] args) {
    //    partOne();
        partTwo();

    }

    private static void partTwo() {
        Scanner input = new Scanner(System.in);
        ArrayList<List<Integer>> trees = new ArrayList<List<Integer>>();
        while(input.hasNextLine()) {
            String[] treeRow = input.nextLine().split("");
            List<Integer> row = new ArrayList<Integer>();
            for(String tree : treeRow) {
                row.add(Integer.valueOf(tree));
            }
            trees.add(row);
        }

        int highestScenicScore = 0;

        for (int i = 0; i < trees.size(); i++) {
            for (int j = 0; j < trees.get(0).size(); j++) {
                int tree = trees.get(i).get(j);

                // search left
                // decrement in column
                int leftVisibleTrees = 0;
                for (int k = (j - 1); k >= 0; k--){
                    if (tree > trees.get(i).get(k)) {
                        leftVisibleTrees++;
                    } else {
                        leftVisibleTrees++;
                        break;
                    }
                }

                // search top
                // decrement row
                int topVisibleTrees = 0;                
                for (int k = (i - 1); k >= 0; k--) {
                    if (tree > trees.get(k).get(j)) {
                        topVisibleTrees++;
                    } else {
                        topVisibleTrees++;
                        break;
                    }
                }
                
                // search right
                // increment column
                int rightVisibleTrees = 0;
                for(int k = (j + 1); k < trees.size(); k++) {
                    if (tree > trees.get(i).get(k)) {
                        rightVisibleTrees++;
                    } else {
                        rightVisibleTrees++;
                        break;
                    }
                }

                // search bottom
                // increment row
                int bottomVisibleTrees = 0;
                for (int k = (i + 1); k < trees.get(i).size(); k++) {
                    if (tree > trees.get(k).get(j)) {
                        bottomVisibleTrees++;
                    } else {
                        bottomVisibleTrees++;
                        break;
                    }
                }

                int treeScenicScore = leftVisibleTrees * topVisibleTrees * rightVisibleTrees * bottomVisibleTrees;
                if (treeScenicScore > highestScenicScore) {
                    highestScenicScore = treeScenicScore;
                }
            }
        }
        System.out.println("\nHighest Scenic Score: " + highestScenicScore);

    }

    private static void partOne() {
        Scanner input = new Scanner(System.in);
        ArrayList<List<Integer>> trees = new ArrayList<List<Integer>>();
        while(input.hasNextLine()) {
            String[] treeRow = input.nextLine().split("");
            List<Integer> row = new ArrayList<Integer>();
            for(String tree : treeRow) {
                row.add(Integer.valueOf(tree));
            }
            trees.add(row);
        }

        int totalVisibleTrees = (trees.size() * 2) + (trees.get(0).size() * 2) - 4;

        // Ignore the surrounding trees already
        for (int i = 1; i < trees.size() - 1; i++) {
            for (int j = 1; j < trees.get(0).size() - 1; j++) {
                int tree = trees.get(i).get(j);
                
                // search left
                // decrement in column
                boolean leftFound = true;
                for (int k = (j - 1); k >= 0; k--){

                    if (tree <= trees.get(i).get(k)) {
                        leftFound = false;
                    }
                }

                // search top
                // decrement row
                boolean topFound = true;
                for (int k = (i - 1); k >= 0; k--) {
                    if (tree <= trees.get(k).get(j)) {
                        topFound = false;
                    }
                }
                
                // search right
                // increment column
                boolean rightFound = true;
                for(int k = (j + 1); k < trees.size(); k++) {
                    if (tree <= trees.get(i).get(k)) {
                        rightFound = false;
                    }
                }

                // search bottom
                // increment row
                boolean bottomFound = true;
                for (int k = (i + 1); k < trees.get(i).size(); k++) {
                    if (tree <= trees.get(k).get(j)) {
                        bottomFound = false;
                    }
                }

                if (leftFound || topFound || rightFound || bottomFound) {
                    totalVisibleTrees++;
                }
            }
        }

        System.out.println("Total Visible Trees: " + totalVisibleTrees);
        input.close();
    }
}