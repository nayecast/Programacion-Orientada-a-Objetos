package com.mycompany.proyecto02;

public class Perro extends Animal {
    String raza;
    public Perro (String tipo, String raza) {

        super(tipo);
        this.raza = raza;
    }

    public void ladrar() {
        System.out.println("Guau guau-Soy un " + raza);

    }
    
    public void vacunas(){
        if (edad >3) {
            System.out.println("Es un adulto, necesita 7 vacunas");
        } else {
            System.out.println("Es un cachorro, necesita 4 vacunas.");
        }
    
    
      
    }

}
