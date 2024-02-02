package main;

import java.util.stream.Stream;

public class Calculator {
    public static double getAverageGrade(Student s) {
        if (s.getCourses().size() == 0) {
            return 0;
        }

        double sum = s.getCourses().values().stream().reduce(0, Integer::sum);
        return sum / s.getCourses().size();
    }

    public static double getMedianGrade(Student s) {
        if (s.getCourses().size() == 0) {
            return 0;
        }

        int[] grades = s.getCourses().values().stream().mapToInt(i -> i).sorted().toArray();
        int middle = grades.length / 2;
        if (grades.length % 2 == 0) {
            return (grades[middle - 1] + grades[middle]) / 2.0;
        } else {
            return grades[middle];
        }
    }
}
