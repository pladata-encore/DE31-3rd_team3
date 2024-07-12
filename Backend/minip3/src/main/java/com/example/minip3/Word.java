package com.example.minip3;


import java.time.LocalDateTime;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;

@Getter
@Table(name = "word_counts")
public class Word {

  
    @Column(name = "datetime", columnDefinition = "DATETIME")
    private LocalDateTime datetime;

    @Column(name = "main_sec", nullable = false, length = 255)
    private String mainSec;

    @Column(name = "sub_sub", length = 255)
    private String subSub;

    @Column(name = "word", columnDefinition = "TEXT")
    private String word;

    @Column(name = "frequency", columnDefinition = "int")
    private int frequency;
    


    public LocalDateTime getDatetime() {
        return datetime;
    }

    public String getMainSec() {
        return mainSec;
    }

    public String getSubSub() {
        return subSub;
    }

    public String getWord() {
        return word;
    }

    public int getFrequency() {
        return frequency;
    }

    public void setDatetime(LocalDateTime localDateTime) {
        this.datetime=localDateTime;
    }

    public void setMainSec(String string) {
        this.mainSec=string;
    }

    public void setSubSub(String string) {
        this.subSub=string;
    }

    public void setWord(String string) {
        this.word=string;
    }

    public void setFrequency(int int1) {
        this.frequency=int1;
    }

    

    
}

