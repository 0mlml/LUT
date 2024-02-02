package main;

import java.util.ArrayList;

public class Zoo {
    private final String name;
    private final ArrayList<Animal> animals;

    public Zoo(String name) {
        this.name = name;
        this.animals = new ArrayList<Animal>();
    }

    public void addAnimal(Animal animal) {
        this.animals.add(animal);
    }

    public void runAnimals(int laps) {
        for (Animal animal : this.animals) {
            animal.run(laps);
        }
    }

    public void listAnimals() {
        System.out.println(name + " contains the following animals:");
        for (Animal animal : this.animals) {
            System.out.println(animal);
        }
    }
}
