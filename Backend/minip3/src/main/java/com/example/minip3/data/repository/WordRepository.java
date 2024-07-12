package com.example.minip3.data.repository;

import com.example.minip3.Word;
import com.example.minip3.data.entity.News;
import java.time.LocalDateTime;
import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface WordRepository  {
    //필요없는 WORDREPOSITRY
    // List<Word> findByDatetimeBetween(LocalDateTime atStartOfDay, LocalDateTime atStartOfDay2, int param1, int param2);
 
} 