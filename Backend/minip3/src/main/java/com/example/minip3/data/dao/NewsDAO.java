package com.example.minip3.data.dao;

import com.example.minip3.data.entity.News;


public interface NewsDAO {
    // interface 에서 가볍게 함수원형선언
    News selectNews(int id);
}
