package com.mycompany.problema;

public class Cuenta {

    String titular;

    public Cuenta(String titular) {
        this.titular = titular;
    }

    public void mostrarTitular() {
        System.out.println("Titular de la cuenta: " + titular);
    }
}
