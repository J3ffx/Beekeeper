<template>
  <section class="team">
    <h1> équipe </h1>
    <Separator/>
    <Hexagons :members="team"/>
  </section>
</template>

<script>
import Separator from './Separator'
import Hexagons from './Hexagons'

export default {
  name: 'Team',
  components: {
    Separator,
    Hexagons
  },
  data: function () {
    return {
      team: []
    }
  },
  methods: {
    formatName (first, last) {
      return first.charAt(0).toUpperCase() + first.slice(1) + ' ' + last.toUpperCase()
    },
    formatSpecialty (code) {
      return code.toString() === 'ir' ? 'Informatique & Réseaux ' : 'Automatique & Systèmes embarqués'
    },
    formatPromo (start, end) {
      return start + ' - ' + end
    }
  },
  created: function () {
    const axios = require('axios')
    const apiUrl = 'http://localhost:1337'
    axios
      .get(apiUrl + '/membres')
      .then(response => {
        for (const member of response.data) {
          this.team.push({
            src: 'http://localhost:1337' + member.picture[0].url,
            alt: this.formatName(member.first_name, member.last_name),
            name: this.formatName(member.first_name, member.last_name),
            desc: this.formatSpecialty(member.specialty),
            promo: this.formatPromo(member.promo1, member.promo2),
            link: member.link
          })
        }
      })
  }
}
</script>

<style scoped>
section {
  background: #161726;
  padding-top: 50px;
  padding-bottom: 50px;
}

h1 {
  text-transform: uppercase;
  text-align: center;
  font-size: 2em;
  color: white;
}
</style>
