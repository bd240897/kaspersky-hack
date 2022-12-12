<template>
  <modal-window ref="modal">
    <template v-slot:title>
      <h3 class="">{{ disease.name }}</h3>
    </template>
    <template v-slot:body>
      <p class="" v-html="disease.more_information"></p>
    </template>
  </modal-window>

  <div @click="showModal" class="prediction__element border border-3 border-primary rounded p-2 mb-3">
    <div class="row">
      <div class="element__icon col-2 h1 d-flex justify-content-center align-items-center">
<!--        <b-icon icon="exclamation-circle-fill" variant="warning"></b-icon>-->
        <img class="w-100" src="../assets/icons/warning.png" style="">
      </div>
      <div class="element__icon__body col-10 d-flex flex-column justify-content-center align-items-center">
        <div class="element__icon__body__disease fw-bold h2">
          {{ disease.name }}
        </div>
        <div class="element__icon__body__description col-12">
          {{ disease.description }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ModalWindow from "@/components/modal-window";

export default {
  name: "DiseaseItem",
  components: {
    ModalWindow,
  },
  props: {
    disease: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  methods: {
    showModal: function () {
      this.$refs.modal.show = true
    }
  }
}
</script>

<style scoped>
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

.element__icon__body {
  border-left: solid blue;
}

.prediction__element{
  cursor: pointer;
}

</style>