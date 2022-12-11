<template>
  <section class="results h-100">
    <div class="container">

      <div class="results__header text-center text-size-header mb-4">
        Предполагаемый диагноз
      </div>

      <div class="diseases">
        <div class="diseases__intro text-size-body mb-4">
          Наша модель проанализировала вашу фотогафию и выявила следующие проблеммы. дполагаемый диагноз.
        </div>
        <div class="diseases__prediction">
          <div class="">
            <div class="text-size-body fw-bold text-center mb-3">Мы считаем что у вашего питомца:</div>

            <DiseaseItem
                v-for="disease in diseases"
                :disease="disease"
            />


<!--            <div v-for="disease in diseases"-->
<!--                 class="prediction__element border border-3 border-primary rounded p-2 mb-3">-->
<!--              <div class="row">-->
<!--                <div class="element__icon col-2 h1 d-flex justify-content-center align-items-center">-->
<!--                  <b-icon icon="exclamation-circle-fill" variant="warning"></b-icon>-->
<!--                </div>-->
<!--                <div class="element__icon__body col-10 d-flex flex-column justify-content-center align-items-center">-->
<!--                  <div class="element__icon__body__disease fw-bold h2">-->
<!--                    {{ disease.name }}-->
<!--                  </div>-->
<!--                  <div class="element__icon__body__description col-12">-->
<!--                    {{ disease.description }}-->
<!--                  </div>-->
<!--                </div>-->

<!--              </div>-->
<!--              <div>-->

<!--              </div>-->

<!--            </div>-->
          </div>
        </div>
      </div>

      <div class="recommendation mb-3">
        <div class="recommendation__header text-size-header fw-bold text-center mb-2">
          Наши рекомендации:
        </div>

        <div class="recommendation__list">
          <div class="recommendation__item text-size-body">
            - сменить корм
          </div>
          <div class="recommendation__item text-size-body">
            - сдать анализы у ветеринара
          </div>
        </div>

        <div class="recommendation__conclusion text-size-body">
          * Пожалуйста прокунсултируейтесь со специалистом.
        </div>

        <div class="report__btn  my-2">
          <button class="button_item btn btn-primary w-100" type="submit">Ближайшие клиники</button>
        </div>
      </div>

      <div class="report mb-3">
        <div class="report__header text-size-header fw-bold text-center">
          Отчет
        </div>
        <div class="report__body text-size-body">
          Распечатав данный отчет вы можете показать его ветеринару для уточнения резульатов.
        </div>
        <div class="report__btn  my-2">
          <button class="button_item btn btn-primary w-100" type="submit">Сохранить отчет</button>
        </div>
      </div>

      <div class="wikipedia mb-3">
        <div class="wikipedia__header text-size-header fw-bold text-center">
          Википедия
        </div>
        <div class="wikipedia__body text-size-body">
          Вы модете почитать о выявленных диагнозах более подробно в нашей википедии.
        </div>
        <div class="wikipedia__btn  my-2">
          <button class="button_item btn btn-primary w-100" type="submit">Открыть википедию</button>
        </div>
      </div>
    </div>


    <!--    <div class="page">-->
    <!--      <button сlass="show-modal-button" @click="showModal">Показать модальное окно</button>-->
    <!--      <modal-window-2 ref="modal"></modal-window-2>-->
    <!--    </div>-->

    <div class="page">
      <button сlass="show-modal-button" @click="showModal">Показать модальное окно</button>
<!--      <modal-window ref="modal"></modal-window>-->
      <modal-window ref="modal">
        <template v-slot:title>
          <h3 class="modal-title">Добавить отзыв</h3>
        </template>
        <template v-slot:body>
                <textarea class="modal-textarea"
                          placeholder="Добавьте отзыв">
                </textarea>
        </template>

      </modal-window>


    </div>


  </section>


</template>

<script>
import goToSomewhere from "@/mixins/goToSomewhere";
import {mapActions, mapState} from "vuex";
import ModalWindow from '../components/modal-window.vue'
import ModalWindow2 from '../components/modal-window-2.vue'
import DiseaseItem from "@/components/DiseaseItem";

export default {
  name: "ResultView",
  mixins: [goToSomewhere],
  components: {
    ModalWindow,
    ModalWindow2,
    DiseaseItem,
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

.bg-green {
  background-color: #00A88E;
}

.element__icon__body {
  border-left: solid blue;
}

.description_disease {

}

.page {
  position: relative;
  width: 100%;
  min-height: 100%;
}

.modal {
  position: fixed; /* фиксированное положение */
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.5); /* цвет фона */
  z-index: 1050;
  opacity: 0; /* по умолчанию модальное окно прозрачно */
  -webkit-transition: opacity 200ms ease-in;
  -moz-transition: opacity 200ms ease-in;
  transition: opacity 200ms ease-in; /* анимация перехода */
  pointer-events: none; /* элемент невидим для событий мыши */
  margin: 0;
  padding: 0;
}


</style>