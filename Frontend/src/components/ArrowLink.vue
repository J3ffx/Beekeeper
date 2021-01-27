<template>
  <div>
    <a class="scroll-link" v-on:click="scroll" :href="this.href"> > </a>
  </div>
</template>

<script>

export default {
  name: 'arrow-link',
  props: {
    href: String
  },
  methods: {
    scroll (event) {
      let link = document.getElementsByClassName('scroll-link')[0]
      let target = link.hash.slice(1) ? document.getElementById(link.hash.slice(1)) : document.body
      event.preventDefault()
      this.smoothScroll(target.getBoundingClientRect().top)
      setTimeout(function () {
        location.hash = link.hash
      }, 600)
    },

    smoothScroll (distance) {
      let steps = 20
      let stepInterval = 10
      let i = 0
      let stepLength = distance / steps
      let currentPos = window.pageYOffset || document.documentElement.scrollTop
      let interval = setInterval(function () {
        currentPos += stepLength
        window.scrollTo(0, currentPos)
        if (++i >= steps) clearInterval(interval)
      }, stepInterval)
    }
  }
}
</script>

<style scoped>
a {
  font-size: 2em;
  transform: rotate(90deg);
  position: absolute;
  bottom: 0;
  right: 48%;
  padding-bottom: 0;
  margin-bottom: 0;
  color: grey;
}

div {
  width: 10%;
  padding-bottom: 6%; /* = width / 1.41 */
  position: absolute;
  bottom: 0;
  left: 45%;
  overflow: hidden;
}

div:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #161726;
  transform-origin: 0 100%;
  transform: rotate(45deg);
}

a:hover {
  color: white;
}
</style>
