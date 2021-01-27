<template>
  <div class="separator">
    <div class="square"/>
    <div class="square"/>
    <div class="square"/>
    <div class="square"/>
    <div class="square"/>
    <div class="square"/>
    <div class="square"/>
    <div class="square"/>
    <div class="square"/>
    <div class="square"/>
  </div>
</template>

<script>
export default {
  name: 'Separator'
}
</script>

<style scoped>
.separator {
  margin-top: 25px;
  margin-bottom: 25px;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.square {
  width: 20px;
  height: 20px;
  border: 2px white solid;
  transform: rotate(45deg);
}
</style>
