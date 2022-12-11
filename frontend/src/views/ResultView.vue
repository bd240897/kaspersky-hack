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
                v-if="diseases"
                v-for="disease in diseases"
                :disease="disease"
            />

            <DiseaseItemHealthy
                v-else
            />

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
          <button @click="goToDoctors" class="button_item btn btn-primary w-100" type="submit">Ближайшие клиники</button>
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

  </section>


</template>

<script>
import goToSomewhere from "@/mixins/goToSomewhere";
import {mapActions, mapState} from "vuex";
import DiseaseItem from "@/components/DiseaseItem";
import DiseaseItemHealthy from "@/components/DiseaseItemHealthy";

export default {
  name: "ResultView",
  mixins: [goToSomewhere],
  components: {
    DiseaseItem,
    DiseaseItemHealthy,
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