<template>
  <section class="data">
    <h1> Données </h1>
    <Separator/>
    <MeteoGraphs/>
    <Separator/>
    <MeteoTable :meteoData="data"/>
  </section>
</template>

<script>
import Separator from './Separator'
import MeteoGraphs from './MeteoGraphs'
import MeteoTable from './MeteoTable'

export default {
  name: 'Data',
  components: {
    Separator,
    MeteoGraphs,
    MeteoTable
  },
  data: function () {
    return {
      data: []
    }
  },
  created: function () {
    const axios = require('axios')
    const apiUrl = 'http://localhost:1337'
    axios
      .get(apiUrl + '/meteos')
      .then(response => {
        for (const row of response.data[response.data.length - 1].Batch) {
          this.data.push({
            a: row.a,
            b: row.b,
            c: row.c,
            d: row.d,
            e: row.e,
            f: row.f
          })
        }
      })
  }
}

</script>

<style scoped>
section {
  background: #484856;
  padding-top: 50px;
  padding-bottom: 50px;
}

h1 {
  text-align: center;
  font-size: 2em;
  color: white;
  text-transform: uppercase;
}
</style>
