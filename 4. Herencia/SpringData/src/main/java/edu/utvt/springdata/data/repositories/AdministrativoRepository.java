package edu.utvt.springdata.data.repositories;

import edu.utvt.springdata.data.entities.Administrativo;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface AdministrativoRepository extends JpaRepository<Administrativo, UUID> {
}
