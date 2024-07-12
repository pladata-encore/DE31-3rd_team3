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
import com.example.minip3.service.WordService;
import io.swagger.v3.oas.annotations.media.Schema;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.http.HttpStatus;

@RestController
@RequestMapping("/word")
public class WordController {
    private final WordService wordService;
    @Autowired
    public WordController(WordService wordService){
        this.wordService = wordService;
    }
    // urls = [
    //         ['100','264','265','268','266','267','269'],
    //         ['101','259','258','261','771','260','262','310','263'],
    //         ['102','249','250','251','254','252','59b','255','256','276','257'],
    //         ['103','241','239','240','237','238','276','242','243','244','248','245'],
    //         ['105','731','226','227','230','732','283','229','228'],
    //         ['104','231','232','233','234','322'],
    // ]
    @GetMapping("/range")
    public ResponseEntity<List<Word>> getNews_rangenews(
        // client에게 입력해야할 설명
        // RETURN 값이 여러개이므로 <LIST<WORD>>
        @Schema (description = "ex)yyyy-mm-dd 입력(2024-05-01 ~ 2024-05-28)")
        @RequestParam @DateTimeFormat(pattern = "yyyy-MM-dd") LocalDate startDate,
        @Schema (description = "ex)yyyy-mm-dd 입력(2024-05-01 ~ 2024-05-28)")
        @RequestParam @DateTimeFormat(pattern = "yyyy-MM-dd") LocalDate endDate
        ) {
        // 날짜 A와 날짜 B 
        List<Word> newsResponseDtoList = wordService.getNews_rangenews(startDate.atStartOfDay(), endDate.atStartOfDay());
        return ResponseEntity.status(HttpStatus.OK).body(newsResponseDtoList);
    }

    @GetMapping("/searchnews")
    //keyword: str, date: str
    public ResponseEntity<List<Word>> getNews_searchnews(
        @Schema (description = "궁금한 keyword입력")
        @RequestParam String param1,
        @Schema (description = "ex)yyyy-mm-dd 입력(2024-05-01 ~ 2024-05-28)")
        @RequestParam @DateTimeFormat(pattern = "yyyy-MM-dd") LocalDate Date
        ) {
        // 궁금한 STRING과 날짜 A 인자
        List<Word> newsResponseDtoList = wordService.getNews_searchnews(param1, Date.atStartOfDay());
        return ResponseEntity.status(HttpStatus.OK).body(newsResponseDtoList);
    }
    
}