package com.example.minip3.service;

import java.time.LocalDateTime;
import java.util.List;

import com.example.minip3.Word;
import com.example.minip3.data.dto.NewsDto;
import com.example.minip3.data.dto.NewsResponseDto;


public interface NewsService {
    NewsResponseDto getNews(int id);
}
