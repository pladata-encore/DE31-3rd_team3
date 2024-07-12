package com.example.minip3.service.impl;

import com.example.minip3.Word;
import com.example.minip3.data.dao.NewsDAO;
import com.example.minip3.data.dto.NewsDto;
import com.example.minip3.data.dto.NewsResponseDto;
import com.example.minip3.service.NewsService;
import com.example.minip3.data.entity.News;
import com.example.minip3.data.repository.NewsRepository;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


@Service
public class NewsServiceImpl  implements NewsService{
    private final NewsDAO newsDAO;
    
    @Autowired
    public NewsServiceImpl(NewsDAO newsDAO) {
        this.newsDAO = newsDAO;
    }
    
    @Override
    public NewsResponseDto getNews(int id){ //return 타입이 newsResonsdto지면
        News news = newsDAO.selectNews(id); //newsdao의 selectnews 호출
        NewsResponseDto newsResponseDto = new NewsResponseDto();
        newsResponseDto.setId(news.getId());
        newsResponseDto.setMainSection(news.getMainSection());
        newsResponseDto.setSubSection(news.getSubSection());
        newsResponseDto.setTitle(news.getTitle());
        newsResponseDto.setDatetime(news.getDatetime());
        newsResponseDto.setContent(news.getContent());
        newsResponseDto.setImageSrc(news.getImageSrc());
        newsResponseDto.setByline(news.getByline());
        return newsResponseDto; 
    }

    

    
   

    

    

    


}
