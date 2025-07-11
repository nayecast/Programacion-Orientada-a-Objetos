package empleados; 
public class TipGerente implements Empleado {
    private String nombre;
    private int horas;
    public TipGerente(String nombre, int horas) {
        this.nombre = nombre; 
        this.horas = horas;   
    }

    // Implementacion del metodo calcularSalario definido en la interfaz Empleado
    @Override
    public double calcularSalario() {
        return horas * 50.0; // El salario se calcula multiplicando las horas por $50
    }

    // Implementacion del metodo obtenerRol definido en la interfaz Empleado
    @Override
    public String obtenerRol() {
        return "Gerente"; // Devuelve el rol del empleado
    }

    // Implementacion del metodo getNombre definido en la interfaz Empleado
    @Override
    public String getNombre() {
        return nombre; // Devuelve el nombre del gerente
    }
}


