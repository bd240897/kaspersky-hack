<template>
  <div class="page_nav mb-2">
    <b-navbar toggleable type="dark" variant="primary">
      <b-navbar-brand v-on:click="goToMain" class="ms-2 text-white fw-bold" href="#">Tail app</b-navbar-brand>

      <b-navbar-toggle class="me-2" target="navbar-toggle-collapse">


        <template #default="{ expanded }">
          &#128523;
<!--          <b-icon v-if="expanded" icon="chevron-bar-up">&#128559;</b-icon>-->
<!--          <b-icon v-else icon="chevron-bar-down">&#128523;</b-icon>-->
        </template>
      </b-navbar-toggle>

      <b-collapse id="navbar-toggle-collapse" is-nav>
        <b-navbar-nav class="ms-auto text-white">
          <b-nav-item to="/" class="ms-2 text-white" active-class="white" href="#">Main</b-nav-item>
          <b-nav-item to="/quick/" class="ms-2" href="#">Quick start</b-nav-item>
          <b-nav-item to="/doctors/" class="ms-2" href="#">Clinics</b-nav-item>
<!--          <b-nav-item to="/team/" class="ms-2" href="#">About team</b-nav-item>-->
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>


<script>
import goToSomewhere from "@/mixins/goToSomewhere";

export default {
  name: "Navbar",
  mixins: [goToSomewhere],
}
</script>

<style scoped>
.nav-item a {
  color: white !important;
}
</style>