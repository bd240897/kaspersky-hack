<template>
  <Navbar/>

  <h1>Profile</h1>
</template>

<script>
import {mapActions, mapState} from "vuex";
import Navbar from "@/components/Navbar";

export default {
  name: "ProfileView",
  components: {
    Navbar
  },
  data: function () {
    return {}
  },
  computed: {
    // ...mapState('profile', ['profile_info', "wallets_list"]),
  },
  methods: {
    // ...mapActions('profile', ["getProfileInfo", "getWalletsList",]),
  },
  created() {
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300&display=swap');
</style>