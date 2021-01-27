<template>
  <div class="graph">
    <table id="meteoTable">
      <tr>
      <h1>SmartUHA</h1>
      </tr>
      <tr class="line" v-for="row in meteo" :key="row.key">
        <td>{{row.a}}</td>
        <td>{{row.b}}</td>
        <td>{{row.c}}</td>
        <td>{{row.d}}</td>
        <td>{{row.e}}</td>
        <td>{{row.f}}</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Graphs',
  props: {
    meteo: Array
  }
}
</script>

<style scoped>
div {
  width: 90vw;
  height: 600px;
  border: 5px rgb(200, 200, 200) solid;
  margin: auto;
}
h1 {
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
</style>
