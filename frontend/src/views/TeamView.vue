<template>
  <Navbar/>

  <section class="results h-100">
    <div class="container">

      <div class="results__header text-center text-size-header mb-4">
        О нашей команде
      </div>

    </div>

  </section>


</template>

<script>
import goToSomewhere from "@/mixins/goToSomewhere";
import {mapActions, mapState} from "vuex";
import DiseaseItem from "@/components/DiseaseItem";
import DiseaseItemHealthy from "@/components/DiseaseItemHealthy";
import Navbar from "@/components/Navbar";

export default {
  name: "TeamView",
  mixins: [goToSomewhere],
  components: {
    DiseaseItem,
    DiseaseItemHealthy,
    Navbar
  },
  data() {
    return {}
  },
  computed: {
    ...mapState('quick_start', ['diseases',]),
  },
  methods: {
    // ...mapActions("quick_start", ["SEND_PHOTO"]),
    showModal: function () {
      this.$refs.modal.show = true
    }
  },
  created() {
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

html, body {
  height: 100%;
}

.text-size-header {
  font-size: 30px;
  font-family: Montserrat, sans-serif;
  font-weight: 400;
}

.text-size-body {
  font-size: 21px;
  font-family: Montserrat, sans-serif;
  font-weight: 400;
}


</style>