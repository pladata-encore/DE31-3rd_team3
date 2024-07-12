package com.example.minip3.data.entity;

import java.time.LocalDateTime;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;
//JPA 이므로 ENTITIY 선언 --> 주키 필수
@Entity
@Getter
@Setter
@Table(name = "news")
public class News {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "main_section", nullable = false, length = 255)
    private String mainSection;

    @Column(name = "sub_section", length = 255)
    private String subSection;

    @Column(name = "title", columnDefinition = "TEXT")
    private String title;

    @Column(name = "datetime", columnDefinition = "DATETIME")
    private LocalDateTime datetime;

    @Column(name = "content", columnDefinition = "LONGTEXT")
    private String content;

    @Column(name = "image_src", columnDefinition = "TEXT")
    private String imageSrc;

    @Column(name = "byline", columnDefinition = "TEXT")
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
