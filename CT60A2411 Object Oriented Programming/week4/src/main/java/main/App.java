package main;

import java.util.Scanner;

public class App {
    public static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        University uni = new University();

        while (true) {
            System.out.println("1) Add student, 2) List students, 3) Add course completion for student, 4) List course completions of student, 5) Calculate the average of course completions, 6) Calculate median of course completions, 7) Save students to file, 8) Load students from file, 0) End the program");
            int choice = Integer.parseInt(scanner.nextLine());

            switch (choice) {
                case 1:
                    uni.addStudentDialogue();
                    break;
                case 2:
                    uni.listStudents();
                    break;
                case 3:
                    uni.addCourseCompletionDialogue();
                    break;
                case 4:
                    uni.listCourseCompletionsDialogue();
                    break;
                case 5:
                    uni.calculateAverageGradeDialogue();
                    break;
                case 6:
                    uni.calculateMedianGradeDialogue();
                    break;
                case 7:
                    uni.saveToFile();
                    break;
                case 8:
                    uni.readFromFile();
                    break;
                case 0:
                    System.out.println("Thank you for using the program.");
                    scanner.close();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Wrong input value");
                    break;
            }
        }
    }
}
