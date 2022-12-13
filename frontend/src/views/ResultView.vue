<template>
  <Navbar/>

  <section class="results h-100">
    <div class="container">

      <div class="results__header text-center text-size-header mb-4">
        Suggested diagnosis
      </div>

      <div class="diseases">
        <div class="diseases__intro text-size-body mb-4">
          Our model analyzed your photo and identified the following issues.
        </div>
        <div class="diseases__prediction">
          <div class="">
            <div class="text-size-body fw-bold text-center mb-3">
              We thinks that your pet has:
            </div>

            <DiseaseItem
                v-if="diseases.length"
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
          Our recommendations:
        </div>

        <div v-if="diseases.length" class="recommendation__list">
          <div class="recommendation__item text-size-body">
            - Repeat analysis
          </div>
          <div class="recommendation__item text-size-body">
            - Contact vet specialist
          </div>
          <div class="recommendation__item text-size-body">
            - If there is nothing to concern about, be happy
          </div>
        </div>

        <div v-else class="recommendation__list">
          <div class="recommendation__item text-size-body">
            <p class="m-0 p-0 pb-1">You don't need to do anything. Everything is fine with your pet. </p>
            <p class="m-0 p-0 pb-1">But you can see the list of our clinics.</p>
          </div>
        </div>

        <div v-if="diseases.length" class="recommendation__conclusion text-size-body">
          * Please consult a specialist!
        </div>



        <div class="report__btn my-2">
          <button @click="goToDoctors" class="button_item btn btn-primary w-100" type="submit">
            Our partner Clinics
          </button>
        </div>
      </div>

      <!--      <div class="report mb-3">-->
      <!--        <div class="report__header text-size-header fw-bold text-center">-->
      <!--          Отчет-->
      <!--        </div>-->
      <!--        <div class="report__body text-size-body">-->
      <!--          Распечатав данный отчет вы можете показать его ветеринару для уточнения резульатов.-->
      <!--        </div>-->
      <!--        <div class="report__btn  my-2">-->
      <!--          <button class="button_item btn btn-primary w-100" type="submit">Сохранить отчет</button>-->
      <!--        </div>-->
      <!--      </div>-->

      <!--      <div class="wikipedia mb-3">-->
      <!--        <div class="wikipedia__header text-size-header fw-bold text-center">-->
      <!--          Википедия-->
      <!--        </div>-->
      <!--        <div class="wikipedia__body text-size-body">-->
      <!--          Вы модете почитать о выявленных диагнозах более подробно в нашей википедии.-->
      <!--        </div>-->
      <!--        <div class="wikipedia__btn  my-2">-->
      <!--          <button class="button_item btn btn-primary w-100" type="submit">Открыть википедию</button>-->
      <!--        </div>-->
      <!--      </div>-->

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
  name: "ResultView",
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