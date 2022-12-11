<template>
  <router-view/>
</template>

<style>

  html, body {
    height: 100%;
  }

  #app{
    height: 100%;
  }

</style>

<script>
import PageLoader from './components/PageLoader'
export default {
  name: 'App',
  components: {
    PageLoader
  },
  created() {
  }
}
</script>

