<template>
  <div class="HiveGraphs">
    <h1>Graphiques Ruches</h1>
    <br>
    <span class="hiveChoice">
     <label for="checkid"  style="word-wrap:break-word">
        <input id="checkid" checked type="checkbox" value="hive1" />Ruche 1
     </label>
     <label for="checkid"  style="word-wrap:break-word">
        <input id="checkid"  type="checkbox" value="hive2" />Ruche 2
     </label>
     <label for="checkid"  style="word-wrap:break-word">
        <input id="checkid"  type="checkbox" value="hive3" />Ruche 3
     </label>
     <label for="checkid"  style="word-wrap:break-word">
        <input id="checkid"  type="checkbox" value="hive4" />Ruche 4
     </label>
    </span>
    <br/>
    <select class="sel type" name="data" id="data" v-on:change="renderChart($event.target.value)">
      <option class="opt" value="void">Sélectionner</option>
      <option class="opt" value="temp">Température</option>
      <option class="opt" value="weight">Poids</option>
      <option class="opt" value="noise">Bruit</option>
      <option class="opt" value="test">Test</option>
    </select>
    <select class="sel group" name="rend" id="rend" v-show="this.toRender" v-on:change="groupData($event.target.value)">
      <option class="opt" value="all">Toutes les entrées</option>
      <option class="opt" value="year">Moyenne par an</option>
      <option class="opt" value="month">Moyenne par mois</option>
      <option class="opt" value="week">Moyenne par semaine</option>
      <option class="opt" value="day">Moyenne par jour</option>
      <option class="opt" value="hour">Moyenne par heure</option>
    </select>
    <div class="chartdiv" ref="chartdiv"></div>
  </div>
</template>

<script>
import * as am4core from '@amcharts/amcharts4/core'
import * as am4charts from '@amcharts/amcharts4/charts'
import am4themesanimated from '@amcharts/amcharts4/themes/animated'
import am4themeskelly from '@amcharts/amcharts4/themes/kelly'

am4core.useTheme(am4themeskelly)
am4core.useTheme(am4themesanimated)

export default {
  name: 'MeteoGraphs',
  components: {
  },
  props: {
    render: Boolean,
    type: String,
    data: []
  },
  data () {
    return {
      toRender: this.render,
      displayed: this.type,
      dispData: this.data
    }
  },
  methods: {
    getWeekNumber (d) {
      d = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()))
      d.setUTCDate(d.getUTCDate() + 4 - (d.getUTCDay() || 7))
      var yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1))
      var weekNo = Math.ceil((((d - yearStart) / 86400000) + 1) / 7)
      return weekNo
    },
    getDateOfWeek (y, w) {
      return new Date(y, 0, (1 + (w - 1) * 7))
    },
    groupData (type) {
      (!this.dispData) ? this.dispData = this.chart.data : this.chart.data = this.dispData
      if (type) {
        let data = this.chart.data
        let groups, date, newData
        switch (type) {
          case 'year' :
            groups = data.reduce((groups, line) => {
              date = line.date.toLocaleDateString('fr-FR').split('/')[2]
              if (!groups[date]) {
                groups[date] = []
              }
              groups[date].push(line.value)
              return groups
            }, {})
            newData = Object.keys(groups).map((date) => {
              return {
                date: new Date('01/01/' + date),
                value: (groups[date].reduce((a, b) => a + b, 0) / groups[date].length).toFixed(2)
              }
            })
            this.chart.data = newData
            break
          case 'month' :
            groups = data.reduce((groups, line) => {
              date = line.date.toLocaleDateString('fr-FR').split('/')[1] + '/' + line.date.toLocaleDateString('fr-FR').split('/')[2]
              if (!groups[date]) {
                groups[date] = []
              }
              groups[date].push(line.value)
              return groups
            }, {})
            newData = Object.keys(groups).map((date) => {
              return {
                date: new Date(date.split('/')[0] + '/01/' + date.split('/')[1]),
                value: (groups[date].reduce((a, b) => a + b, 0) / groups[date].length).toFixed(2)
              }
            })
            this.chart.data = newData
            break
          case 'week' :
            groups = data.reduce((groups, line) => {
              date = line.date.toLocaleDateString('fr-FR').split('/')[2] + '|' + this.getWeekNumber(line.date)
              if (!groups[date]) {
                groups[date] = []
              }
              groups[date].push(line.value)
              return groups
            }, {})
            newData = Object.keys(groups).map((date) => {
              console.log(date.split('|')[1])
              if (date.split('|')[1] < 52) {
                return {
                  date: this.getDateOfWeek(date.split('|')[0], date.split('|')[1]),
                  value: (groups[date].reduce((a, b) => a + b, 0) / groups[date].length).toFixed(2)
                }
              }
            })
            this.chart.data = newData
            console.log(newData)
            break
          case 'day' :
            groups = data.reduce((groups, line) => {
              date = line.date.toDateString()
              if (!groups[date]) {
                groups[date] = []
              }
              groups[date].push(line.value)
              return groups
            }, {})
            newData = Object.keys(groups).map((date) => {
              return {
                date: new Date(date),
                value: (groups[date].reduce((a, b) => a + b, 0) / groups[date].length).toFixed(2)
              }
            })
            this.chart.data = newData
            break
          case 'hour' :
            groups = data.reduce((groups, line) => {
              date = line.date.toDateString() + ' ' + line.date.toLocaleTimeString('fr-FR', {hour: '2-digit'})
              if (!groups[date]) {
                groups[date] = []
              }
              groups[date].push(line.value)
              return groups
            }, {})
            newData = Object.keys(groups).map((date) => {
              return {
                date: new Date(date.replace(' h', ':00:00')),
                value: (groups[date].reduce((a, b) => a + b, 0) / groups[date].length).toFixed(2)
              }
            })
            this.chart.data = newData
            break
          default :
            break
        }
      }
    },
    renderDefault () {
      this.renderChart(this.displayed)
    },
    renderChart (type) {
      if (this.chart) {
        this.chart.dispose()
      }
      let chart = am4core.create(this.$refs.chartdiv, am4charts.XYChart)
      let xText = ''
      let yText = ''
      chart.paddingRight = 50
      chart.paddingLeft = 20
      if (type) {
        this.toRender = true
        this.displayed = type
        switch (type) {
          case 'temp' :
            chart.dataSource.url = 'http://localhost:1337/hives'
            chart.dataSource.adapter.add('parsedData', function (data) {
              let newData = []
              for (let i = 0; i < data.length; i++) {
                let row = data[i]
                newData.push({
                  date: new Date(row.published_at),
                  name: 'temperature' + i,
                  value: parseInt(row.Batch[5].b.split(' °')[0])
                })
              }
              data = newData
              return data
            })
            yText = 'Température (°C)'
            xText = 'Date'
            break
          case 'weight' :
            chart.dataSource.url = 'http://localhost:1337/hives'
            chart.dataSource.adapter.add('parsedData', function (data) {
              let newData = []
              for (let i = 0; i < data.length; i++) {
                let row = data[i]
                newData.push({
                  date: new Date(row.published_at),
                  name: 'weight' + i,
                  value: parseInt(row.Batch[6].b.split(' g')[0])
                })
              }
              data = newData
              return data
            })
            yText = 'Poids (g)'
            xText = 'Date'
            break
          case 'noise' :
            chart.dataSource.url = 'http://localhost:1337/hives'
            chart.dataSource.adapter.add('parsedData', function (data) {
              let newData = []
              for (let i = 0; i < data.length; i++) {
                let row = data[i]
                newData.push({
                  date: new Date(row.published_at),
                  name: 'noise' + i,
                  value: parseInt(row.Batch[11].b.split(' dB')[0])
                })
              }
              data = newData
              return data
            })
            yText = 'Bruit (dB)'
            xText = 'Date'
            break
          case 'test' :
            let data = []
            let value = 10
            for (let i = 1; i < 366; i++) {
              value += Math.round((Math.random() < 0.5 ? 1 : -1) * Math.random() * 1)
              data.push({ date: new Date(2020, 0, i), name: 'name' + i, value: value })
            }
            chart.data = data
            yText = 'Value'
            xText = 'Date'
            break
          default :
            chart.data = []
            this.toRender = false
            break
        }
      }

      let dateAxis = chart.xAxes.push(new am4charts.DateAxis())
      dateAxis.title.text = xText

      let valueAxis = chart.yAxes.push(new am4charts.ValueAxis())
      valueAxis.title.text = yText

      let series = chart.series.push(new am4charts.LineSeries())
      series.dataFields.dateX = 'date'
      series.dataFields.valueY = 'value'
      series.tooltipText = '{valueY.value}'
      series.minBulletDistance = 100
      chart.cursor = new am4charts.XYCursor()

      let scrollbarX = new am4charts.XYChartScrollbar()
      scrollbarX.series.push(series)
      chart.scrollbarX = scrollbarX

      var bullet = series.bullets.push(new am4charts.CircleBullet())
      bullet.circle.radius = 1
      bullet.circle.fill = am4core.color('#fff')
      bullet.circle.strokeWidth = 0

      this.chart = chart

      this.dispData = null

      document.getElementById('rend').value = 'all'
    }
  },
  mounted () {
    let event = new Event('render')
    event.value = this.displayed
    this.renderChart(event)
  },

  beforeDestroy () {
    if (this.chart) {
      this.chart.dispose()
    }
  }
}
</script>

<style scoped>
div {
  width: 90vw;
  height: 635px;
  border: 5px rgb(200, 200, 200) solid;
  margin: auto;
  text-align: center;
}
h1 {
  color: white;
  display: block;
  font-size: 2em;
  font-weight: bold;
  text-align:center;
}
table {
  color: white;
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  color: white;
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: rgb(218, 103, 10);
}

.btn{
  background-color: rgb(218, 103, 10);
  border: none;
  float: right;
  margin: 5px;
}

.btn:hover{
  cursor: pointer;
  background-color: rgb(236, 223, 35);
  transform:scale(1.1,1.1);
    -webkit-transform:scale(1.1,1.1);
    -moz-transform:scale(1.1,1.1);
}

select {
  appearance: none;
  margin: 0;

}

.sel{
  width: 50%;
  min-width: 15ch;
  max-width: 20ch;
  border: 1px solid var(--select-border);
  border-radius: 0.25em;
  padding: 0.25em 0.5em;
  font-size: 1.25rem;
  cursor: pointer;
  line-height: 1.1;
  background-color: #fff;
}

.type{
  background: url(https://image.flaticon.com/icons/png/512/263/263827.png) 96% / 15% no-repeat #EEE;
}

.group{
  background: url(https://cdn4.iconfinder.com/data/icons/small-n-flat/24/calendar-512.png) 96% / 15% no-repeat #EEE;
}

.chartdiv {
  width: 100%;
  height: 500px;
}

[type="checkbox"]{
  vertical-align:middle;
}

.hiveChoice{
  color:white;
  text-align:center;
}

label{
  margin-right: 10px;
}

input{
  margin-right:5px;
}

</style>
