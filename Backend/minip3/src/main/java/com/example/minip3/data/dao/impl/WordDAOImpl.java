package com.example.minip3.data.dao.impl;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Component;

import com.example.minip3.Word;
import com.example.minip3.data.dao.NewsDAO;
import com.example.minip3.data.dao.WordDAO;
import com.example.minip3.data.entity.News;
import com.example.minip3.data.repository.NewsRepository;
import com.example.minip3.data.repository.WordRepository;
import com.google.protobuf.Timestamp;

@Component
public class WordDAOImpl implements WordDAO{ //주키가 없으므로 JPA대신 JDBC 사용
    private final JdbcTemplate jdbcTemplate;
    @Autowired
    public WordDAOImpl(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }
    @Override
    public List<Word> findByDateTimeBetween(LocalDateTime startDate, LocalDateTime endDate) {
        // JDBC를 사용하여 SQL 쿼리 실행
        //WORD_COUNTS 테이블에서 날짜가 atStartOfDay과 atStartOfDay2 사이인 값들중 
        //  WORD로 묶어서 각 나온 개수의 합을 SUM(FREQUENCY) 하여서 내림차순으로
        // 500개가져오기
        String sql = "SELECT word AS name, SUM(frequency) AS value FROM word_counts WHERE datetime BETWEEN ? AND ? GROUP BY word ORDER BY value DESC LIMIT 500 ";
        // OBJECT배열에 ? 에 들어갈 인자 2개 선언하고, RESULTSET라는 RS(테이블 로우행 구조) , ROWNUM은 현재행
        // 각각 JdbcTemplate 이 알아서 rs.next()하면서 Word라는 객체 만듬
        List<Word> words = new ArrayList<>(); //RETURN 할 LIST
        try (Connection conn = jdbcTemplate.getDataSource().getConnection(); //properties에 있는 정보로 db연결
         PreparedStatement ps = conn.prepareStatement(sql)) { //미리 선언된 sql로 동적파라미터 바인딩
            ps.setObject(1, startDate); //첫번째 ?에 input
            ps.setObject(2, endDate); //두번째 ?에 input
            System.out.println(ps); //디버그
            try (ResultSet rs = ps.executeQuery()) { //실행시킨걸 rs객체에 넣기
                while (rs.next()) { //존재할때까지
                    Word word = new Word();
                    // word.setDatetime(rs.getTimestamp("datetime").toLocalDateTime());
                    // word.setMainSec(rs.getString("main_sec"));
                    // word.setSubSub(rs.getString("sub_sub"));
                    word.setWord(rs.getString("name"));
                    word.setFrequency(rs.getInt("value"));
                    words.add(word);
                }
            }
            } catch (SQLException e) {
                e.printStackTrace();
        }
        return words;    










    }

    @Override
    public List<Word> findByDateTimeBetween(String param1, LocalDateTime Date){
        LocalDateTime startDate = Date.minusDays(3);  // Date에서 3일 전의 날짜
        LocalDateTime endDate = Date.plusDays(3);     // Date에서 3일 후의 날짜
        // 입력받은 날짜 DATE에서 +-3일 에 포함되는 애들중 WORD가 입력한 PARAM1이고 DATE와 WORD로 묶고
        // DATETIME순으로 출력
        String sql = "SELECT datetime,word, SUM(frequency) as frequency FROM word_counts WHERE datetime BETWEEN ? AND ? AND word = ? GROUP BY datetime, word ORDER BY datetime ";
        // sql = f"SELECT datetime, word, SUM(frequency) as frequency FROM word_counts 
        // WHERE datetime BETWEEN '{st_datetime}' AND '{ed_datetime}' AND word = '{keyword}' 
        // GROUP BY datetime, word ORDER BY datetime"
        List<Word> words = new ArrayList<>(); //RETURN 할 LIST
        try (Connection conn = jdbcTemplate.getDataSource().getConnection(); //properties에 있는 정보로 db연결
         PreparedStatement ps = conn.prepareStatement(sql)) { //미리 선언된 sql로 동적파라미터 바인딩
            ps.setObject(1, startDate); //첫번째 ?에 input
            ps.setObject(2, endDate); //두번째 ?에 input
            ps.setObject(3, param1); //세번째 ? 에 input
            System.out.println(ps); //디버그
            try (ResultSet rs = ps.executeQuery()) { //실행시킨걸 rs객체에 넣기
                while (rs.next()) { //존재할때까지
                    Word word = new Word();
                    word.setDatetime(rs.getTimestamp("datetime").toLocalDateTime());
                    // word.setMainSec(rs.getString("main_sec"));
                    // word.setSubSub(rs.getString("sub_sub"));
                    word.setWord(rs.getString("word"));
                    word.setFrequency(rs.getInt("frequency"));
                    words.add(word);
                }
            }
            } catch (SQLException e) {
                e.printStackTrace();
        }
        return words;    
    }   
}
