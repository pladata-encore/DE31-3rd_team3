"use client";
import * as React from 'react';
import styles from '@/styles/page.module.css';

import { DateRange } from 'react-date-range';
import { addDays } from "date-fns"
import 'react-date-range/dist/styles.css'; // main style file
import 'react-date-range/dist/theme/default.css'; // theme css file

import * as d3 from 'd3';
import cloud from 'd3-cloud';

function Home() {

  const [state, setState] = React.useState([
    {
      startDate: Date.parse("2024-05-01"),
      endDate: addDays(Date.parse("2024-05-01"), 1),
      key: "selection",
    },
  ])

  const [wordData, setWordData] = React.useState([{ text: "데이터를", value: 90 }, { text: "입력하세요", value: 70 },]);

  React.useEffect(() => {
    cloud()
      .size([400, 550])
      .words(wordData)
      .padding(5)
      .rotate(function () { // -90도, 0도, 90도 중 하나
        return (~~(Math.random() * 3) - 1) * 90;
      })
      .font("Impact")
      .fontSize((d) => d.value)
      .on("end", end)
      .start();

    function end(words) {
      d3.select("#word-cloud").selectAll("svg").remove();
      d3.select("#word-cloud")
        .append("svg")
        .attr("width", 400)
        .attr("height", 550)
        .append("g")
        .attr("transform", "translate(" + 500 / 2 + "," + 500 / 2 + ")")
        .attr("class", "value")
        .selectAll("text")
        .data(words)
        .enter()
        .append("text")
        .style("font-size", function (d) {
          return d.value + "px";
        })
        .style("font-family", "Impact")
        .attr("text-anchor", "middle")
        .attr("transform", function (d) {
          return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function (d) {
          return d.text;
        })
        .on("mouseover", onMouseOver)
        .on("mouseout", onMouseOut);
    }

    function onMouseOver(d, i) {
      d3.select(this).transition().duration(300).style("fill", "red");
      // display value text bottom left corner
      d3.select("#word-cloud").append("valueText")
        .attr("x", 10)
        .attr("y", 500)
        .text(d.value);
    }

    function onMouseOut(d, i) {
      d3.select(this).transition().duration(300).style("fill", "black");
      // remove value text
      d3.select("#word-cloud").selectAll("valueText").remove();
    }
  }, [wordData]);

  function handleClick() {
    console.log(state[0].startDate);
    console.log(state[0].endDate);
    setWordData([{ text: "버튼", value: 90 }, { text: "눌렀다", value: 70 },]);
  }

  return (
    <main className={styles.main}>
      <div id='mainContainer' className={styles.horizontal}>
        <div className={styles.container}>
          <h1>rangeView Page</h1>
          <p>Welcome to the rangeView page</p>
          <br />
          {/* only display calendar when click on the input */}
          {/* if selection is end close calander view */}
          <DateRange
            editableDateInputs={true}
            onChange={item => setState([item.selection])}
            moveRangeOnFirstSelection={false}
            ranges={state}
            direction="horizontal"
            showDateDisplay={true}
            showMonthAndYearPickers={false}
            dateDisplayFormat='yyyy-MM-dd'
            minDate={new Date(Date.parse("2024-05-01"))}
            maxDate={new Date(Date.parse("2024-07-09"))}
          />
          <input className={styles.button} type='button' value='검색' onClick={handleClick} />
        </div>
        <div className={styles.container}>
          <div id="word-cloud"></div>
        </div>
      </div>
    </main>
  );
}

export default Home;