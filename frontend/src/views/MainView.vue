<template>
  <Navbar/>

  <section class="main-page">
    <b-container class="main-page__container">

      <div class="about_us mb-2 border border-primary rounded-2 p-2">
        <div class="about_us__header text-size-header text-center mb-2">
          About us
        </div>

        <div class="about_us__text text-size-body mb-2">
          Our project will help your pet to always be healthy and energetic.
        </div>
      </div>

      <div
          class="video d-flex flex-column justify-content-center align-items-center mb-2 border border-primary rounded-2 p-2">

        <div class="video__header text-size-header text-center mb-2">
          Our video
        </div>

        <div class="video__iframe mb-2 embed-responsive embed-responsive-4by3">
          <iframe class="embed-responsive-item"
                  width="350" height="196" src="https://www.youtube.com/embed/eeIgIrCFGTs"
                  title="YouTube video player" frameborder="0"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowfullscreen></iframe>
        </div>

<!--        <div class="video__btn d-grid gap-2 w-100 mb-2">-->
<!--          <b-button v-on:click.prevent="goToRegister" class="video__btn__item" block variant="primary">-->
<!--            Join our community-->
<!--          </b-button>-->
<!--        </div>-->

<!--        <div class="video__btn d-grid gap-2 w-100 mb-2">-->
<!--          <b-button v-on:click.prevent="goToLogin" class="video__btn__item" block variant="primary">-->
<!--            Sign in-->
<!--          </b-button>-->
<!--        </div>-->
      </div>

      <div class="purpose mb-2 border border-primary rounded-2 p-2">
        <div class="purpose__header text-size-header text-center mb-2">
          Our goals
        </div>

        <div class="purpose__text text-size-body mb-2">
          <b-list-group>
            <b-list-group-item>
<!--              <b-icon icon="star-fill" variant="success"></b-icon>-->
              monitoring your pet's health
            </b-list-group-item>
            <b-list-group-item>
<!--              <b-icon icon="star-fill" variant="success"></b-icon>-->
              timely detection of diseases
            </b-list-group-item>
            <b-list-group-item>
<!--              <b-icon icon="star-fill" variant="success"></b-icon>-->
              consultations with specialists
            </b-list-group-item>
          </b-list-group>
        </div>
      </div>

      <div class="advantage mb-2 border border-primary rounded-2 p-2">
        <div class="advantage__header text-size-header text-center mb-2">
          Our advantages
        </div>

        <div class="advantage__text text-size-body mb-2">
          <b-list-group>
            <b-list-group-item>
<!--              <b-icon icon="star-fill" variant="success"></b-icon>-->
              no need to go anywhere
            </b-list-group-item>
            <b-list-group-item>
<!--              <b-icon icon="star-fill" variant="success"></b-icon>-->
              instant result
            </b-list-group-item>
            <b-list-group-item>
<!--              <b-icon icon="star-fill" variant="success"></b-icon>-->
              consultation with a specialist
            </b-list-group-item>
          </b-list-group>
        </div>
      </div>

      <div class="start mb-2 border border-primary rounded-2 p-2">
        <div class="start__header text-size-header text-center mb-2">
          Quick start
        </div>

        <div class="start__text text-size-body mb-3">
          Our system will analyze your photo, just send it to us.
        </div>

        <div class="start__btn d-grid gap-2 w-100 mb-2">
          <b-button v-on:click.prevent="goToQuickStart" class="start__btn__item" block variant="primary">
            Take a photo and get a diagnosis
          </b-button>
        </div>
      </div>

    </b-container>
  </section>
</template>

<script>
import goToSomewhere from "@/mixins/goToSomewhere";
import {mapActions} from "vuex";
import TestSlot from "@/components/TestSlot";
import Navbar from "@/components/Navbar";

export default {
  name: "MainView",
  components: {
    Navbar
  },
  mixins: [goToSomewhere],
  data() {
    return {}
  },
  methods: {},
  created() {
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

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

.video iframe {
  /*height: auto;*/
  /*width: 100%;*/
}
</style>