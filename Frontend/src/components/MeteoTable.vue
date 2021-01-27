<template>
  <div class="Table">
    <h1>Tableau Météo</h1>
    <br />
    <table id="meteoTable">
      <tr class="line" v-for="row in meteoData" :key="row.a">
        <td>{{ row.a }}</td>
        <td>{{ row.b }}</td>
        <td>{{ row.c }}</td>
        <td>{{ row.d }}</td>
        <td>{{ row.e }}</td>
        <td>{{ row.f }}</td>
      </tr>
    </table>
    <br />
    <button class="btn" v-on:click="json()">
      <i class="fa fa-download"></i> Download meteo data
    </button>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "MeteoTable",
  props: {
    meteoData: Array,
  },
  methods: {
    exportToJsonFile: function (jsonData) {
      let dataStr = JSON.stringify(jsonData);
      let dataUri =
        "data:application/json;charset=utf-8," + encodeURIComponent(dataStr);
      let date = new Date()
      let exportFileDefaultName = "meteo_data" + date.getDate() + date.getHours() + date.getMinutes() +".json";

      let linkElement = document.createElement("a");
      linkElement.setAttribute("href", dataUri);
      linkElement.setAttribute("download", exportFileDefaultName);
      linkElement.click();
    },
    json: function () {
      alert("Le téléchargement va se lancer.");
      const axios = require("axios");
      axios.get("http://localhost:1337/meteos").then((response) => {
        this.exportToJsonFile(response.data);
      });
    },
  },
};
</script>

<style scoped>
div {
  width: 90vw;
  height: 1000px;
  border: 5px rgb(200, 200, 200) solid;
  margin: auto;
}
h1 {
  color: white;
  display: block;
  font-size: 2em;
  font-weight: bold;
  text-align: center;
}
table {
  color: white;
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td,
th {
  color: white;
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: rgb(218, 103, 10);
}

.btn {
  background-color: rgb(218, 103, 10);
  border: none;
  float: right;
  margin: 5px;
}

.btn:hover {
  cursor: pointer;
  background-color: rgb(236, 223, 35);
  transform: scale(1.1, 1.1);
  -webkit-transform: scale(1.1, 1.1);
  -moz-transform: scale(1.1, 1.1);
}
</style>
