package main;

public class Animal {
    private final String type;
    private final String name;
    private final int age;

    public Animal(String type, String name, int age) {
        this.type = type;
        this.name = name;
        this.age = age;
    }

    public void run(int laps) {
        for (int i = 0; i < laps; i++) {
            System.out.println(name + " runs really fast!");
        }
    }

    public String toString() {
        return String.format("%s: %s, %d years", type, name, age);
    }
}
