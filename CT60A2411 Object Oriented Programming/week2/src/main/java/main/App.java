package main;

import java.util.Scanner;

public class App {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    Hedgehog hog = new Hedgehog();

    while (true) {
      System.out.println("1) Make hedgehog talk, 2) Create new hedgehog, 3) Make hedgehog run, 0) Quit");
      int choice = Integer.parseInt(scanner.nextLine());

      switch (choice) {
        case 1:
          System.out.println("What does hedgehog say?");
          String text = scanner.nextLine();
          hog.speak(text);
          break;
        case 2:
          System.out.println("What is the name of the hedgehog:");
          String name = scanner.nextLine();
          System.out.println("What is the age of the hedgehog:");
          int age = Integer.parseInt(scanner.nextLine());
          hog = new Hedgehog(name, age);
          break;
        case 3:
          System.out.println("How many laps?");
          int laps = Integer.parseInt(scanner.nextLine());
          hog.run(laps);
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
