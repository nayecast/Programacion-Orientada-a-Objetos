package empleados; 

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.util.Scanner;

public class Empresass { 

    public static void main(String[] args) { 
        Scanner sc = new Scanner(System.in); 
        String url = "jdbc:sqlite:empresa.db"; // El URL que conecta  a la base de datos SQLite

        try (Connection conn = DriverManager.getConnection(url)) { // Intenta conectar a la base de datos

            if (conn != null) { // Si la conexion se establece correctamente sale un
                System.out.println("Conexion correcta en la base de datos SQLite"); // Mensaje de confirmación
            } else { // Si no se conecta
                System.out.println("No se pudo conectar con la base de datos");
                return; // Sale del programa
            }

            Statement stmt = conn.createStatement(); // Objeto para ejecutar sentencias SQL

            // Crea la tabla empleados si no existe
            stmt.execute("CREATE TABLE IF NOT EXISTS empleados (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, rol TEXT, salario REAL)");

            // Pide cuantos empleados se van a ingresar
            System.out.print("Cuantos empleados desea ingresar? ");
            int n = Integer.parseInt(sc.nextLine()); // Convierte la entrada a un numero

            for (int i = 0; i < n; i++) { //Se ingresar cada empleado
                System.out.print("Nombre: ");
                String nombre = sc.nextLine(); // Lee el nombre del empleado

                System.out.print("Tipo (gerente/desarrollador): ");
                String tipo = sc.nextLine().toLowerCase(); // Lee el tipo de empleado y lo convierte a minusculas

                System.out.print("Horas trabajadas: ");
                int horas = Integer.parseInt(sc.nextLine()); // Lee las horas trabajadas

                Empleado emp; // Variable para el objeto empleado

                // Aqui verifica el tipo y crea el objeto que es
                if (tipo.equals("gerente")) {
                    emp = new TipGerente(nombre, horas); // crea un gerente
                } else if (tipo.equals("desarrollador")) {
                    emp = new TipDesarrollador(nombre, horas); // crea un desarrollador
                } else {
                    // Si el tipo es invalido lo omite
                    System.out.println(" Tipo de empleado invalido, lo  omitira\n");
                    continue; // Pasa al siguiente ciclo sin guardar nada
                }

                double salario = emp.calcularSalario(); // Calcula el salario del empleado

                // Guarda los datos del empleado en la base de datos
                PreparedStatement ps = conn.prepareStatement("INSERT INTO empleados (nombre, rol, salario) VALUES (?, ?, ?)");
                ps.setString(1, emp.getNombre()); // Establece el nombre
                ps.setString(2, emp.obtenerRol()); // Establece el rol
                ps.setDouble(3, salario); // Establece el salario
                ps.executeUpdate(); // Ejecuta el insert

                // Muestra mensaje de empleado ingresado con su salario
                System.out.println(emp.getNombre() + " (" + emp.obtenerRol() + ") → $" + salario + "\n");
            }

            // Consulta todos los empleados guardados en la base de datos
            ResultSet rs = stmt.executeQuery("SELECT * FROM empleados");
            System.out.println("\nLista Empleados"); // Encabezado

            while (rs.next()) { // Recorre los resultados
                // Imprime los datos del empleado como ID | Nombre | Rol | Salario
                System.out.println(rs.getInt("id") + " | " + rs.getString("nombre") + " | " +
                        rs.getString("rol") + " | $" + rs.getDouble("salario"));
            }

        } catch (SQLException e) { 
            System.out.println("Error: " + e.getMessage()); 
        }

    } 
} 
