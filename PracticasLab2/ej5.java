package edu.utvt;
import java.util.Scanner;

public class ej5 {

    public static void main(String[] args) {
        int loops = 0;
        Scanner sc = new Scanner(System.in);

        System.out.println("Ingresa el número de ciclos requeridos: ");
        loops = sc.nextInt();

        for (int count = 1; count <= loops; count++) {
            System.out.println("Número actual de iteración: " + count);
        }

        sc.close();
    }
}
