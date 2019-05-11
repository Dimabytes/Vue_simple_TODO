<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <Todos/>
  </div>
</template>

<script>
import Todos from './components/Todos.vue'

export default {
  name: 'app',
  components: {
    Todos
  }
}
</script>

<style lang="scss">

  *:active,*:focus  {
  outline: none;
  }


#app {
  font-family: 'Titillium Web', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
