"use client";
import * as React from 'react';
import styles from '@/styles/page.module.css';

import { Calendar } from 'react-date-range';
import { addDays } from "date-fns"
import 'react-date-range/dist/styles.css'; // main style file
import 'react-date-range/dist/theme/default.css'; // theme css file

import * as d3 from 'd3';

import axios from 'axios';

function Home() {

  const [date, setDate] = React.useState(new Date(Date.parse("2024-05-01")));
  const [wordData, setWordData] = React.useState(
    {
      label: "데이터를 입력하세요",
      data: [
        { "date": "2024-05-01", "value": 90 },
        { "date": "2024-05-02", "value": 70 },
        { "date": "2024-05-03", "value": 50 },
        { "date": "2024-05-04", "value": 30 },
        { "date": "2024-05-05", "value": 20 },
        { "date": "2024-05-06", "value": 10 },
        { "date": "2024-05-07", "value": 5 }
      ]
    });

  React.useEffect(() => {
    // Clear the existing chart before rendering a new one
    d3.select("#barchart").selectAll("svg").remove();

    // Code for Barchart
    const margin = { top: 20, right: 20, bottom: 30, left: 40 };
    const width = 960 - margin.left - margin.right;
    const height = 500 - margin.top - margin.bottom;

    const x = d3.scaleBand()
      .range([0, width])
      .padding(0.1);
    const y = d3.scaleLinear()
      .range([height, 0]);

    const svg = d3.select("#barchart")
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

    // add title
    svg.append("text")
      .attr("x", (width / 2))
      .attr("y", 0 + (margin.top / 2))
      .attr("text-anchor", "middle")
      .style("font-size", "20px")
      .style("text-decoration", "underline")
      .text("Frequency of " + wordData.label);

    x.domain(wordData.data.map(function (d) { return d.date; }));
    y.domain([0, d3.max(wordData.data, function (d) { return d.value; })]);

    svg.selectAll(".bar")
      .data(wordData.data)
      .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function (d) { return x(d.date); })
      .attr("width", x.bandwidth())
      .attr("y", function (d) { return y(d.value); })
      .attr("height", function (d) { return height - y(d.value); })
      .on("mouseover", onMouseOver)
      .on("mouseout", onMouseOut);

    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

    svg.append("g")
      .call(d3.axisLeft(y));

    function onMouseOver(d, i) {
      d3.select(this).transition().duration(300).style("fill", "red");
      // display value text bottom left corner
      d3.select("#barchart").append("valueText")
        .attr("x", 10)
        .attr("y", 10)
        .text(d.value);
    }

    function onMouseOut(d, i) {
      d3.select(this).transition().duration(300).style("fill", "black");
      // remove value text
      d3.select("#barchart").selectAll("valueText").remove();
    }
  }, [wordData]);

  function handleClick() {
    // parse date to string ( yyyy-MM-dd )
    const st_date = date.toISOString().split('T')[0];
    const searchBoxValue = document.getElementById('searchBox').value;

    axios.get('http://140.238.153.4:22000/word/searchnews', {
      params: {
        param1: searchBoxValue,
        Date: st_date
      }
    })
      .then((response) => {
        console.log(response.data);
        // only get "datetime" as "date" and "frequency" as "value"
        const resData = response.data.map((item) => {
          return { date: item.datetime.split("T")[0], value: item.frequency };
        });
        setWordData({ label: searchBoxValue, data: resData });
      })
      .catch((error) => {
        console.log(error);
      });
  }


  return (
    <main className={styles.main}>
      <div id='mainContainer' className={styles.horizontal}>
        <div className={styles.container}>
          <h1>토픽별 뉴스 검색</h1>
          <p style={{ textAlign: "center" }}>검색어를 입력하고 날짜를 선택해주세요.<br />선택한 날로부터 7일간의 뉴스 키워드 빈도수를 시각화합니다.</p>
          <br />
          <input id='searchBox' className={styles.searchbox} type="text" placeholder="검색어를 입력하세요" />
          <Calendar
            onChange={item => setDate(item)}
            direction="horizontal"
            showDateDisplay={true}
            showMonthAndYearPickers={false}
            dateDisplayFormat='yyyy-MM-dd'
            minDate={new Date(Date.parse("2024-05-01"))}
            maxDate={new Date(Date.parse("2024-07-09"))}
            date={date}
          />
          <input className={styles.button} type='button' value='검색' onClick={handleClick} />
        </div>
        <div className={styles.container}>
          {/* Code for Barchart */}
          <div id="barchart"></div>
        </div>
      </div>
    </main>
  );
}

export default Home;