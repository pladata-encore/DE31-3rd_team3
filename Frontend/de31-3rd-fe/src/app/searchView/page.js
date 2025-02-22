"use client";
import * as React from 'react';
import styles from '@/styles/page.module.css';

import { Calendar } from 'react-date-range';
import { addDays } from "date-fns"
import 'react-date-range/dist/styles.css'; // main style file
import 'react-date-range/dist/theme/default.css'; // theme css file

import * as d3 from 'd3';

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

  return (
    <main className={styles.main}>
      <div id='mainContainer' className={styles.horizontal}>
        <div className={styles.container}>
          <h1>searchView Page</h1>
          <p>Welcome to the searchView page</p>
          <br />
          <input className={styles.searchbox} type="text" placeholder="검색어를 입력하세요" />
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
          <input className={styles.button} type='button' value='검색' />
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