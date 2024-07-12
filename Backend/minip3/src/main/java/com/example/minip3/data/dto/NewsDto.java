package com.example.minip3.data.dto;

import java.time.LocalDateTime;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

@Builder
@Data
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class NewsDto {

    private int id;
    private String mainSection;
    private String subSection;
    private String title;
    private LocalDateTime datetime;
    private String content;
    private String imageSrc;
    private String byline;
    public int getId() {
        return id;
    }


    public String getMainSection() {
    return mainSection;
    }

    public String getSubSection() {
        return subSection;
    }
     
    public String getTitle() {
        return title;
    }
    public LocalDateTime getDatetime() {
        return datetime;
    }
    public String getContent() {
        return content;
    }
    public String getImageSrc() {
        return imageSrc;
    }
    public String getByline() {
        return byline;
    }
}   
