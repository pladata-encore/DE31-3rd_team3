package com.example.minip3.controller;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import com.example.minip3.Word;
import com.example.minip3.data.dto.NewsResponseDto;
import com.example.minip3.service.NewsService;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.http.HttpStatus;

@RestController
@RequestMapping("/news")
public class NewsController {
    private final NewsService newsService;
    @Autowired
    public NewsController(NewsService newsService){
        this.newsService = newsService;
    }
    @GetMapping("/id")
    // 주소가 ip:8000/id
    public ResponseEntity<NewsResponseDto> getNews(int id){
        // client가 execute하면 실행되는거 ->service의 getnews호출 id는 mysql의 index번호
        NewsResponseDto newsResponseDto = newsService.getNews(id);
        return ResponseEntity.status(HttpStatus.OK).body(newsResponseDto);
    }

    

   

}