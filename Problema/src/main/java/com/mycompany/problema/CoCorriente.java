package com.mycompany.problema;

public class CoCorriente extends Cuenta {

    double saldo;
    double interes = 0.07;

    public CoCorriente(String titular, double saldoInicial) {
        super(titular);
        this.saldo = saldoInicial;
    }

    public void saldoEInteres() {
        System.out.println("Saldo actual cuenta corriente: $" + saldo);
        System.out.println("Interes aplicado: " + (interes * 100) + "%");
    }

    public void interes() {
        saldo += saldo * interes;
        System.out.println("Saldo aplicando el interés: $" + saldo);
    }
}
