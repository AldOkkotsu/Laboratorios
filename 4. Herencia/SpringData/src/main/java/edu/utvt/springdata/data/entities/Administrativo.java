package edu.utvt.springdata.data.entities;

import jakarta.persistence.DiscriminatorValue;
import jakarta.persistence.Entity;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@DiscriminatorValue( value = "2")
@AllArgsConstructor
@NoArgsConstructor
@Data

public class Administrativo extends  Usuario{

    private Double salario;

}
