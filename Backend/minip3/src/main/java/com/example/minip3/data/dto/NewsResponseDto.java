package com.example.minip3.data.dto;

import java.time.LocalDateTime;
import java.util.List;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class NewsResponseDto {
    private int id;
    private String mainSection;
    private String subSection;
    private String title;
    private LocalDateTime datetime;
    private String content;
    private String imageSrc;
    private String byline;
   
}
