package edu.utvt.springdata.data.entities;

import jakarta.persistence.DiscriminatorValue;
import jakarta.persistence.Entity;

@Entity
@DiscriminatorValue(value = "1")
public class Alumno extends Usuario {
}
