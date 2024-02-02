package main;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.io.Serializable;

public class Student implements Serializable {
    private static final long serialVersionUID = 1L;

    private final HashMap<String, Integer> courses;
    private final String name;
    private final String studentNumber;

    public Student(String name, String studentNumber) {
        this.name = name;
        this.studentNumber = studentNumber;
        this.courses = new LinkedHashMap<>();
    }

    public HashMap<String, Integer> getCourses() {
        return this.courses;
    }

    public void addGrade(String course, int grade) {
        if (this.courses.containsKey(course) && this.courses.get(course) >= grade) {
            return;
        }

        this.courses.put(course, grade);
    }

    public String getName() {
        return this.name;
    }

    public String toString() {
        return String.format("%s: %s", this.studentNumber, this.name);
    }
}
