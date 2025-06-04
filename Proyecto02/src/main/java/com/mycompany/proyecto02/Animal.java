
package com.mycompany.proyecto02;

import java.util.Scanner;

public class Animal {
    int edad;
    String tipo;
    Animal(String tipo){
        this.tipo=tipo;
        this.edad=edad;
        
    }
    public void describir(){
        System.out.println("tipo:"+tipo);
    }
    
    public void EdadPerro(){
        Scanner teclado=new Scanner(System.in);
        System.out.println("Ingrese la edad de su mascota");
        this.edad= teclado.nextInt();
        
        if (edad<=3) {
            System.out.println("Su mascota es Cachorro");
            
            
        }else{
            System.out.println("Su mascota es un Adulto");
        }
        
    }
   
}
