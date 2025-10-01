import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class StudentsScholarshipTest {
    public static void main(String[] args) {
        String csvFile = "students_test.csv"; // Path to your CSV file
        String line = "";
        String csvSplitBy = ","; // CSV is comma-separated

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            // Read the header line first
            String header = br.readLine();
            System.out.println("Header: " + header);

            // Read each subsequent line
            while ((line = br.readLine()) != null) {
                // Split line into columns using comma as separator
                String[] columns = line.split(csvSplitBy);

                // Print each column for demonstration
                System.out.println("Student:");
                for (int i = 0; i < columns.length; i++) {
                    System.out.println("  Column " + (i + 1) + ": " + columns[i]);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
few;l,
