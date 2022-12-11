<template>
  <div v-if="show" class="modal_show" @click.self="closeModal">
    <div class="disease_modal">
      <div class="disease_modal__close" @click="closeModal">&#10006;</div>
      <slot name="title">
        <h3 class="disease_modal__title">Дефолтный Заголовок</h3>
      </slot>
      <slot name="body">
        <div class="disease_modal__body">
          Дефолтный контент модального окна
        </div>
      </slot>
      <slot name="footer">
        <div class="disease_modal__footer">
          <button class="disease_modal__footer__button" @click="closeModal">
            Ок
          </button>
        </div>
      </slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModalWindow",
  data: function () {
    return {
      show: false
    }
  },
  methods: {
    closeModal: function () {
      this.show = false
    }
  }
}
</script>

<style scoped
       lang="scss">
.modal_show {
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

.disease_modal {
  background: #fff;
  border-radius: 8px;
  padding: 15px;
  min-width: 85%;
  max-width: 85%;
  position: absolute;

  &__close {
    border-radius: 50%;
    color: #fff;
    background: #2a4cc7;
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    top: 7px;
    right: 7px;
    width: 30px;
    height: 30px;
    cursor: pointer;
  }

  &__title {
    color: #0971c7;
  }

  &__body {
    margin-bottom: 20px
  }

  &__footer {
    &__button {
      background-color: #0971c7;
      color: #fff;
      border: none;
      text-align: center;
      padding: 8px;
      font-size: 17px;
      font-weight: 500;
      border-radius: 8px;
      min-width: 150px;
    }
  }
}
</style>