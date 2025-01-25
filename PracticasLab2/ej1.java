package edu.utvt;
import java.util.Scanner;

public class ej1 {

    public static void main(String[] args) {
        String name;
        int age;
        String message = "hola %s, tu edad es %s";

        Scanner sc = new Scanner(System.in);

        System.out.print("ingrese nombre: ");
        name = sc.nextLine();

        System.out.print("ingrese edad: ");
        age = Integer.parseInt(sc.nextLine());

        sc.close();
        String finalMessage = String.format(message, name, age);
        System.out.print(finalMessage);
    }
}
