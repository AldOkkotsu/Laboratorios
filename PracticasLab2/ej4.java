package edu.utvt;

public class ej4 {
    public static void main(String[] args) {
        int age = 34;

        if (age <= 12) {
            System.out.println("Eres un niño");
        } else if (age < 17) {
            System.out.println("Eres un adolescente");
        } else if (age < 35) {
            System.out.println("Eres un adulto joven");
        } else {
            System.out.println("Eres un adulto");
        }
    }
}
