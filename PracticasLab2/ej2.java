package edu.utvt;

public class ej2 {

    public static void main(String[] args) {
        String name = "John Doe";
        int age = 40;

        // Concatenación simple de cadenas en Java
        String message = "Hola " + name + " con tu edad actual " + age + ", ya eres mayor de edad.";
        System.out.println(message);

        // Uso de StringBuffer
        StringBuffer sb = new StringBuffer();
        sb.append("Hola ");
        sb.append(name);
        sb.append(" con tu edad actual ");
        sb.append(age);
        sb.append(", ya eres mayor de edad.");
        System.out.println(sb.toString());

        // Uso de String.format
        String defaultMessage = "Hola %s con tu edad actual %d, ya eres mayor de edad.";
        String newMessage = String.format(defaultMessage, name, age);
        System.out.println(newMessage);
    }













}
