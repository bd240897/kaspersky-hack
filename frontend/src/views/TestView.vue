<template>
  {{test}}
<div>
  <b-button v-b-toggle.collapse-1 variant="primary">Toggle Collapse</b-button>
  <b-collapse id="collapse-1" class="mt-2">
    <b-card>
      <p class="card-text">Collapse contents Here</p>
      <b-button v-b-toggle.collapse-1-inner size="sm">Toggle Inner Collapse</b-button>
      <b-collapse id="collapse-1-inner" class="mt-2">
        <b-card>Hello!</b-card>
      </b-collapse>
    </b-card>
  </b-collapse>
</div>

  <!--<TestSlot>-->
  <!--  <template v-slot:header>-->
  <!--    <h1>Здесь мог быть заголовок страницы</h1>-->
  <!--  </template>-->

  <!--  <template v-slot:default>-->
  <!--    <p>Параграф для основного контента.</p>-->
  <!--    <p>И ещё один.</p>-->
  <!--  </template>-->

  <!--  <template v-slot:footer>-->
  <!--    <p>Некая контактная информация</p>-->
  <!--  </template>-->
  <!--</TestSlot>-->
      <button сlass="show-modal-button" @click="showModal">Показать модальное окно</button>
  <modal-window ref="modal">
  </modal-window>

  <DiseaseItem :disease="disease_item" />

</template>


<script>
import TestSlot from '../components/TestSlot'
import ModalWindow from "@/components/modal-window";
import DiseaseItem from "@/components/DiseaseItem";

export default {
  name: "TestView",
  components: {
    TestSlot,
    ModalWindow,
    DiseaseItem
  },
  data() {
    return {
      disease_item: {
        name: 'name',
        description: "description",
      },
    }
  },
  created() {
  },
  methods: {
    showModal: function () {
      this.$refs.modal.show = true
    }
  },
  computed:{
    test() {
      return process.env.VUE_APP_ROOT_API
    }
  }
}
</script>

<style scoped>

</style>