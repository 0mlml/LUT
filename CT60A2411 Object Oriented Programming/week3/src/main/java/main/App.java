package main;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Please, name the zoo:");
        String zooName = scanner.nextLine();
        Zoo zoo = new Zoo(zooName);

        while (true) {
            System.out.println(
                    "1) Create a new animal, 2) List all animals, 3) Run animals, 0) End the program");
            int choice = Integer.parseInt(scanner.nextLine());

            switch (choice) {
                case 1:
                    System.out.println("What species?");
                    String species = scanner.nextLine();
                    System.out.println("Enter the name of the animal:");
                    String name = scanner.nextLine();
                    System.out.println("Enter the age of the animal:");
                    int age = Integer.parseInt(scanner.nextLine());
                    zoo.addAnimal(new Animal(species, name, age));
                    break;
                case 2:
                    zoo.listAnimals();
                    break;
                case 3:
                    System.out.println("How many laps?");
                    int laps = Integer.parseInt(scanner.nextLine());
                    zoo.runAnimals(laps);
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
