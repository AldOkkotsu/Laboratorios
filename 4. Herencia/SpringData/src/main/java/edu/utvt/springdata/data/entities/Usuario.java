package edu.utvt.springdata.data.entities;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;
import java.time.LocalDate;
import java.util.UUID;

@Entity(name = "te_users")
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)
@DiscriminatorColumn(name = "tipo", discriminatorType = DiscriminatorType.INTEGER)
@AllArgsConstructor
@NoArgsConstructor
@Data
public abstract class Usuario implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;
    private String nombre;
    private String apellidos;
    private String email;
    private LocalDate fechaNacimiento; // Cambiado a LocalDate
}
