package edu.utvt.springdata;
import edu.utvt.springdata.data.entities.Administrativo;
import edu.utvt.springdata.data.entities.Alumno;
import edu.utvt.springdata.data.repositories.AdministrativoRepository;
import edu.utvt.springdata.data.repositories.AlumnoRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import java.time.LocalDate;

@SpringBootTest
public class lolTest {
    @Autowired
    private AlumnoRepository alumnoRepository;
    @Test
    void insertAlumno() {
        Alumno alumno = new Alumno();
        alumno.setNombre("Yerely");
        alumno.setApellidos("Martinez");
        alumno.setEmail("yerely@example.com");
        alumno.setFechaNacimiento(LocalDate.of(2000, 5, 25));
        alumnoRepository.save(alumno);
    }

    @Autowired
    private AdministrativoRepository administrativoRepository;

    @Test
    void insertAdministrativo() {
        Administrativo administrativo = new Administrativo();
        administrativo.setNombre("Aldo");
        administrativo.setApellidos("Gonzalez");
        administrativo.setEmail("aldo@gmail.com");
        administrativo.setFechaNacimiento(LocalDate.of(2004, 11, 23));
        administrativo.setSalario(Double.parseDouble("2020"));
        administrativoRepository.save(administrativo);
    }
}

