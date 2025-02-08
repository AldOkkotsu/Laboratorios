package edu.utvt.springdata;

import edu.utvt.springdata.data.entities.Student;
import edu.utvt.springdata.data.repositories.studentRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class SpringDataApplicationTests {

    @Autowired
    private studentRepository studentRepository;

    @Test
    void contextLoads() {
        // Creación del estudiante utilizando el constructor adecuado
        Student student = new Student("Yerely", "Martinez");
        studentRepository.save(student);
    }
}
