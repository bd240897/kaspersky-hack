<template>
  <Navbar/>

  <section class="main-page">
    <b-container class="main-page__container">

      <div class="about_us mb-2 border border-primary rounded-2 p-2">
        <div class="about_us__header text-size-header text-center mb-2">
          О нас
        </div>

        <div class="about_us__text text-size-body mb-2">
          Наш проект поможет вашему питомцу всегда быть здоровым и энергичным.
        </div>
      </div>

      <div
          class="video d-flex flex-column justify-content-center align-items-center mb-2 border border-primary rounded-2 p-2">

        <div class="video__header text-size-header text-center mb-2">
          Презентация
        </div>

        <div class="video__iframe mb-2 embed-responsive embed-responsive-4by3">
          <iframe class="embed-responsive-item"
                  width="350" height="196" src="https://www.youtube.com/embed/eeIgIrCFGTs"
                  title="YouTube video player" frameborder="0"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowfullscreen></iframe>
        </div>

        <div class="video__btn d-grid gap-2 w-100 mb-2">
          <b-button v-on:click.prevent="goToRegister" class="video__btn__item" block variant="primary">Присоединиться
          </b-button>
        </div>

        <div class="video__btn d-grid gap-2 w-100 mb-2">
          <b-button v-on:click.prevent="goToLogin" class="video__btn__item" block variant="primary">Войти</b-button>
        </div>
      </div>

      <div class="purpose mb-2 border border-primary rounded-2 p-2">
        <div class="purpose__header text-size-header text-center mb-2">
          Наши цели
        </div>

        <div class="purpose__text text-size-body mb-2">
          <b-list-group>
            <b-list-group-item>
              <b-icon icon="star-fill" variant="success"></b-icon>
              контроль здоровья вашего питомца
            </b-list-group-item>
            <b-list-group-item>
              <b-icon icon="star-fill" variant="success"></b-icon>
              своевременное выявление заболеваний
            </b-list-group-item>
            <b-list-group-item>
              <b-icon icon="star-fill" variant="success"></b-icon>
              консультации со специалистами
            </b-list-group-item>
          </b-list-group>
        </div>
      </div>

      <div class="advantage mb-2 border border-primary rounded-2 p-2">
        <div class="advantage__header text-size-header text-center mb-2">
          Наши достоиснва
        </div>

        <div class="advantage__text text-size-body mb-2">
          <b-list-group>
            <b-list-group-item>
              <b-icon icon="star-fill" variant="success"></b-icon>
              не нужно никуда идти
            </b-list-group-item>
            <b-list-group-item>
              <b-icon icon="star-fill" variant="success"></b-icon>
              мгновенный результат
            </b-list-group-item>
            <b-list-group-item>
              <b-icon icon="star-fill" variant="success"></b-icon>
              консультация со специалистом
            </b-list-group-item>
          </b-list-group>
        </div>
      </div>

      <div class="start mb-2 border border-primary rounded-2 p-2">
        <div class="start__header text-size-header text-center mb-2">
          Быстрый старт
        </div>

        <div class="start__text text-size-body mb-3">
          Если вы не хотите регистрироваться а просто хотите протестировать наш фунционал вам сюда:
        </div>

        <div class="start__btn d-grid gap-2 w-100 mb-2">
          <b-button v-on:click.prevent="goToQuickStart" class="start__btn__item" block variant="primary">Сделать фото и
            получить ответ
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