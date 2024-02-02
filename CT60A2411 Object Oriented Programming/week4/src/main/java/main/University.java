package main;

import java.util.ArrayList;
import java.util.List;
import java.io.*;

public class University {
    private List<Student> students;

    public University() {
        this.students = new ArrayList<>();
    }

    public void addStudent(Student s) {
        this.students.add(s);
    }

    public void listStudents() {
        System.out.println("Students:");
        for (Student s : this.students) {
            System.out.println(s);
        }
    }

    public void addStudentDialogue() {
        System.out.println("What is the name of the student?");
        String name = App.scanner.nextLine();
        System.out.println("What is the student number of the student?");
        String studentNumber = App.scanner.nextLine();
        Student s = new Student(name, studentNumber);
        this.addStudent(s);
    }

    private Student selectStudentDialogue(String message) {
        int i = 0;
        for (Student s : this.students) {
            System.out.printf("%d: %s%n", i++, s.getName());
        }
        System.out.println(message);
        int choice = Integer.parseInt(App.scanner.nextLine());
        return this.students.get(choice);
    }

    public void addCourseCompletionDialogue() {
        Student s = selectStudentDialogue("Which student do you want to add course completion for?");
        System.out.println("What is the name of the course?");
        String course = App.scanner.nextLine();
        System.out.println("What is the grade of the course?");
        int grade = Integer.parseInt(App.scanner.nextLine());
        s.addGrade(course, grade);
    }

    public void calculateAverageGradeDialogue() {
        Student s = selectStudentDialogue("Which student do you want to calculate the average for?");
        System.out.printf("Average is %.1f%n", Calculator.getAverageGrade(s));
    }

    public void calculateMedianGradeDialogue() {
        Student s = selectStudentDialogue("Which student do you want to calculate the median for?");
        System.out.printf("Median is %.1f%n", Calculator.getMedianGrade(s));
    }

    public void listCourseCompletionsDialogue() {
        Student s = selectStudentDialogue("Which student do you want to list course completions for?");
        for (String course : s.getCourses().keySet()) {
            System.out.printf("%s: %d%n", course, s.getCourses().get(course));
        }
    }

    public void saveToFile() {
        File f = new File("students.bin");
        try {
            FileOutputStream fos = new FileOutputStream(f);
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            oos.writeObject(this.students);
            oos.close();
        } catch (Exception ignored) {
        }
    }

    @SuppressWarnings("unchecked")
    public void readFromFile() {
        File f = new File("students.bin");
        try {
            FileInputStream fis = new FileInputStream(f);
            ObjectInputStream ois = new ObjectInputStream(fis);
            this.students = (ArrayList<Student>) ois.readObject();
            ois.close();
        } catch (Exception ignored) {
        }
    }
}
