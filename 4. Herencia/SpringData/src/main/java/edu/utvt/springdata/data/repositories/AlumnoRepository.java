package edu.utvt.springdata.data.repositories;
import edu.utvt.springdata.data.entities.Alumno;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;
public interface AlumnoRepository extends JpaRepository<Alumno, UUID> {
}
