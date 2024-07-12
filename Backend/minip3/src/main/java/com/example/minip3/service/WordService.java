package com.example.minip3.service;

import java.time.LocalDateTime;
import java.util.List;

import com.example.minip3.Word;
import com.example.minip3.data.dto.NewsDto;
import com.example.minip3.data.dto.NewsResponseDto;


public interface WordService {
    List<Word> getNews_rangenews(LocalDateTime atStartOfDay, LocalDateTime atStartOfDay2);
    List<Word> getNews_searchnews(String param1, LocalDateTime Date);

}
