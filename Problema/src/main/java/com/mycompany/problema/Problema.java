package com.mycompany.problema;

import java.util.Scanner;

public class Problema {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.println("Sistema");
        System.out.print("Ingrese el nombre del titular: ");
        String nombre = teclado.nextLine();

        System.out.print("Ingrese su saldo: ");
        double saldo = teclado.nextDouble();
        teclado.nextLine();

        System.out.print("¿Que tipo de cuenta desea crear? ahorro/corriente: ");
        String tipo = teclado.nextLine().toLowerCase();

        if (tipo.equals("ahorro")) {
            CoAhorro ca = new CoAhorro(nombre, saldo);
            ca.mostrarTitular();
            ca.saldoEInteres();
            ca.interes();
        } else if (tipo.equals("corriente")) {
            CoCorriente cc = new CoCorriente(nombre, saldo);
            cc.mostrarTitular();
            cc.saldoEInteres();
            cc.interes();
        } else {
            System.out.println("Tipo de cuenta no valido ingrese correctamente");
        }

    }
}
