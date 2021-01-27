<template>
  <div class="home">
    <Header/>
    <About id="about"/>
    <Data id="data"/>
    <Team id="team"/>
    <Footer/>
  </div>
</template>

<script>
import Header from './Header.vue'
import About from './About.vue'
import Data from './Data.vue'
import Team from './Team.vue'
import Footer from './Footer.vue'

export default {
  name: 'Home',
  components: {
    Header,
    About,
    Data,
    Team,
    Footer
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
