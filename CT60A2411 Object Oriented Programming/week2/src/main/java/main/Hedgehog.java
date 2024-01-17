package main;

public class Hedgehog {
  private String name = "Pikseli";
  private int age = 5;

  public Hedgehog(String name, int age) {
    this.name = name;
    this.age = age;
  }

  public Hedgehog() {
  }

  public void speak(String message) {
    if (message.length() <= 0) {
      System.out
          .println(String.format("I am %s and my age is %d, but could you still give me input values?", name, age));
    } else {
      System.out.println(String.format("%s: %s", name, message));
    }
  }

  public void run(int laps) {
    for (int i = 0; i < laps; i++) {
      System.out.println(name + " runs really fast!");
    }
  }
}
