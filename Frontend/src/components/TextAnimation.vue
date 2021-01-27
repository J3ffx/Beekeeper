<template>
  <div class="container has-text-centered">
    <h1 class="title">
      ensisa
    </h1>
    <h2 id="toAnimate"> </h2>
  </div>
</template>

<script>
export default {
  name: 'text-animation',
  data: function () {
    return {
      i: 0,
      sens: 'right',
      index: 0,
      forwardSpeed: 75,
      backwardSpeed: 50,
      waitTime: 500
    }
  },
  props: {
    strings: Array
  },
  mounted: function () {
    this.goForward()
  },
  methods: {
    goForward () {
      if (this.i < this.strings[this.index].length) {
        document.getElementById('toAnimate').innerHTML += this.strings[this.index].charAt(this.i)
        this.i++
        setTimeout(this.goForward, this.forwardSpeed)
      } else {
        setTimeout(this.goBackward, this.waitTime)
      }
    },

    goBackward () {
      if (this.i > 0) {
        document.getElementById('toAnimate').innerHTML = document.getElementById('toAnimate').innerHTML.slice(0, -1)
        this.i--
        setTimeout(this.goBackward, this.backwardSpeed)
      } else {
        this.index++
        if (this.index >= this.strings.length) {
          this.index = 0
        }
        setTimeout(this.goForward, this.waitTime)
      }
    }
  }
}
</script>

<style scoped>
.title:not(:last-child) {
  text-align: center;
  text-transform: uppercase;
  font-size: 7em;
  margin-bottom: 0;
  padding-bottom: 0;
  font-weight: bold;
  -webkit-text-stroke: 2px black;
}

h2 {
  text-transform: uppercase;
  margin-top: 0;
  padding-top: 0;
  font-size: 2em;
  font-weight: bold;
  height: 100px;
  -webkit-text-stroke: 2px black;
}
</style>
