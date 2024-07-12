package com.example.minip3.data.dao.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import com.example.minip3.data.dao.NewsDAO;
import com.example.minip3.data.entity.News;
import com.example.minip3.data.repository.NewsRepository;

@Component
public class NewsDAOImpl implements NewsDAO{
    private NewsRepository newsRepository;
    @Autowired
    public NewsDAOImpl(NewsRepository newsRepository){
        this.newsRepository=newsRepository;
    }
    @Override
    public News selectNews(int id) { //JPA이므로 REPOSITORY를 
        News selectedNews = newsRepository.getReferenceById(id);
        return selectedNews;
    }
}
