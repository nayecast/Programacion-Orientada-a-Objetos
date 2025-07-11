package empleados; 

// La clase TipDesarrollador implementa la interfaz Empleado
public class TipDesarrollador implements Empleado  {
    private String nombre;
    private int horas;
    public TipDesarrollador(String nombre, int horas) {
        this.nombre = nombre; 
        this.horas = horas;   
    }

    // Implementacion del metodo calcularSalario definido en la interfaz Empleado
    @Override
    public double calcularSalario() {
        return horas * 30.0; // El salario se calcula multiplicando las horas por $30
    }

    // Implementacion del metodo obtenerRol definido en la interfaz Empleado
    @Override
    public String obtenerRol() {
        return "Desarrollador"; // Devuelve el rol del empleado
    }

    // Implementacion del metodo getNombre definido en la interfaz Empleado
    @Override
    public String getNombre() {
        return nombre; // Devuelve el nombre del desarrollador
    }
}
