<template>
  <div class="hero-head">
    <header class="navbar">
    <div class="container">
      <div class="navbar-brand">
        <a class="navbar-item">
          <img src="../assets/beekeeper_white_solo.png" alt="Logo">
        </a>
        <span class="navbar-burger burger" data-target="navbarMenuHeroC">
            <span></span>
            <span></span>
            <span></span>
          </span>
      </div>
      <div id="navbarMenuHeroC" class="navbar-menu">
        <div class="navbar-end">
          <a href="/" class="navbar-item is-active">
            Accueil
          </a>
          <a href="#about" class="navbar-item">
            Description
          </a>
          <a href="#data" class="navbar-item">
            Données
          </a>
          <a href="#team" class="navbar-item">
            Équipe
          </a>
        </div>
      </div>
    </div>
  </header>
  </div>
</template>

<script>
export default {
  name: 'nav-bar'
}
</script>

<style>
.hero.is-success a.navbar-item, .hero.is-success a.navbar-item.is-active {
  background-color: transparent;
  color: rgba(255, 255, 255, 0.5);
  font-size: 1.2em;
}

.hero.is-success a.navbar-item.is-active, .hero.is-success a.navbar-item:hover {
  border-bottom: 4px solid white;
  color: white;
  background-color: transparent;
}

</style>
