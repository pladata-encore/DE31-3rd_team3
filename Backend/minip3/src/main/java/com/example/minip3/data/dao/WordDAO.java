package com.example.minip3.data.dao;

import java.time.LocalDateTime;
import java.util.List;

import com.example.minip3.Word;

public interface WordDAO {
    // 함수 원형선언
    List<Word> findByDateTimeBetween(LocalDateTime atStartOfDay, LocalDateTime atStartOfDay2);
    // findByDateTimeBetween
    //  sql = f"SELECT datetime, word, SUM(frequency) as frequency FROM word_counts 
    // WHERE datetime BETWEEN '{st_datetime}' AND '{ed_datetime}' AND word = '{keyword}' 
    // GROUP BY datetime, word ORDER BY datetime"
    List<Word> findByDateTimeBetween(String param1, LocalDateTime Date);
    
}