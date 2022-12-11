<template>
  <div class="hystmodal" id="myModal">
    <div class="hystmodal__window">
      <button data-hystclose class="hystmodal__close">Close</button>
      Текст модального окошка.
      <img src="img/photo.jpg" alt="Изображение в окне"/>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModalWindow2",
  data: function () {
    return {
      show: false
    }
  },
  methods: {}
}
</script>

<style scoped lang="scss">
  .hystmodal {
    position: fixed;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    overflow: hidden;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
    display: flex;
    flex-flow: column nowrap;
    justify-content: center; /* см. ниже */
    align-items: center;
    z-index: 99;
    /* Чтобы окно не прилипало к границе
    браузера установим отступы */
    padding: 30px 0;
    background: rgba(0, 0, 0, 0.5);
  }
</style>