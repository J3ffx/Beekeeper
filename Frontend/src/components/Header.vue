<template>
  <section class="hero is-success is-fullheight">
    <nav-bar/>

    <!-- Hero content: will be in the middle -->
    <div class="hero-body">
      <text-animation v-bind:strings="this.subtitleAnimation"/>
    </div>

    <!-- Hero footer: will stick at the bottom -->
    <div>
      <arrow-link href="#about"/>
    </div>
  </section>
</template>

<script>
import NavBar from './NavBar.vue'
import TextAnimation from './TextAnimation'
import ArrowLink from './ArrowLink'

export default {
  name: 'Header',
  components: {
    ArrowLink,
    NavBar,
    TextAnimation
  },
  data: function () {
    return {
      subtitleAnimation: [
        'École Nationale Supérieure d\'Ingénieurs Sud-Alsace',
        'Projet BeeKeePer',
        'Busra DAGLI',
        'Jérôme FANFAN']
    }
  }
}
</script>

<style scoped>
.hero {
  background-image: url('../assets/hero-image.jpg');
  background-position: center;
  background-size: cover;
}
</style>
