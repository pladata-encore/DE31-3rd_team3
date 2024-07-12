package com.example.minip3.service.impl;

import com.example.minip3.Word;
import com.example.minip3.data.dao.NewsDAO;
import com.example.minip3.data.dao.WordDAO;
import com.example.minip3.data.dto.NewsDto;
import com.example.minip3.data.dto.NewsResponseDto;
import com.example.minip3.service.NewsService;
import com.example.minip3.service.WordService;
import com.example.minip3.data.entity.News;
import com.example.minip3.data.repository.NewsRepository;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


@Service
public class WordServiceImpl  implements WordService{
    private final WordDAO wordDAO;

    @Autowired
    public WordServiceImpl(WordDAO wordDAO) {
        this.wordDAO = wordDAO;
    }
    //service이므로 함수 로직만 선언!!! -> worddao interface 에 선언 -> 이것이 word dao imp에서 구현
    @Override
    public List<Word> getNews_rangenews(LocalDateTime atStartOfDay, LocalDateTime atStartOfDay2) {
        return wordDAO.findByDateTimeBetween(atStartOfDay, atStartOfDay2);
    }
    @Override
    public List<Word> getNews_searchnews(String param1, LocalDateTime Date) {
        return wordDAO.findByDateTimeBetween(param1, Date);
    }

    

    
   

    

    

    


}
