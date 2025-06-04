package com.mycompany.problema;

public class CoAhorro extends Cuenta {

    double saldo;
    double interes = 0.05;

    public CoAhorro(String titular, double saldoInicial) {
        super(titular);
        this.saldo = saldoInicial;
    }

    public void saldoEInteres() {
        System.out.println("Saldo actual de la cuenta de ahorro: $" + saldo);
        System.out.println("Interes aplicado: " + (interes * 100) + "%");
    }

    public void interes() {
        saldo += saldo * interes;
        System.out.println("Saldo aplicando el interes: $" + saldo);
    }
}
