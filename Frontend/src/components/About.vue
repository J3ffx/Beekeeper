<template>
  <section class="about is-fullheight">
    <h1> à propos
    </h1>
    <Separator/>
    <div class="columns">
      <div class="column is-one-third">
        <b-image
          :src="require('@/assets/beekeeper_neg.png')"
          alt="Beekeeper Logo"
          :rounded="false"
          :lazy="true"
        ></b-image>
      </div>
      <div class="column is-two-thirds">
        <h2> Projet BeeKeeper </h2>
        <p>
          Le projet BeeKeeper, mis en place en 2019 à l'ENSISA à Mulhouse, est un projet développé et maintenu par des étudiants
          des filières ASE & IR. Il est encadré par Messieurs DUPUIS Raphaël et WEBER Jonathan, tous deux enseignants de cette école.
          L'idée est de développer une ruche connectée, ainsi 4 ruches ont été placées au sein d'un enclos disposé devant l'école
          avec différents capteurs afin de pouvoir récolter et analyser des données sur les abeilles et ainsi étudier leur comportement.
          <br/>
          Le lien avec la ruche étant défectueux, nous avons en guise de remplacement accès à une station météo située sur le campus.
          Cette dernière nous fournira des données avec lesquelles travailler.
        </p>
      </div>
    </div>
  </section>
</template>

<script>
import Separator from './Separator'

export default {
  name: 'About',
  components: {
    Separator
  }
}
</script>

<style scoped>
section {
  background-color: #161726;
  padding-bottom: 50px;
  padding-top: 50px;
}

.columns {
  width: 85%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 0;
}

p {
  margin-top: 15px;
  padding-bottom: 15px;
  border-bottom: 2px grey solid;
  color: rgb(200, 200, 200);
}

h1, h2 {
  font-size: 2em;
  color: white;
}

h1 {
  text-align: center;
  text-transform: uppercase;
}

.b-image-wrapper {
  border: 2px rgb(200, 200, 200) solid;
  padding: 20px;
}
</style>
