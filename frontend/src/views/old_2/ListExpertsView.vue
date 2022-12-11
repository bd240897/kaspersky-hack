<template>
  <section class="">
    <div class="container ">

      <h1 class="text-center my-5">Рекомендуемые Вам эксперты</h1>

      <div class="row">

        <div class="col-6 mb-2">
          <div class="card text-center">
            <img class="card-img-top p-4 pb-0" src="../assets/img/mama.jpg" alt="Card image cap">
            <div class="card-body">
              <h5 class="card-title mb-3">Иванов Иван Иванович</h5>
              <p class="card-text mb-2"><b>Специализация:</b> Трейдинг</p>
              <p class="card-text"><b>Сектор::</b> Банковский</p>
              <a v-on:click.prevent="goToChat" class="btn btn-primary w-100">Выбрать</a>
            </div>
          </div>
        </div>

        <div class="col-6 mb-2">
          <div class="card text-center">
            <img class="card-img-top p-4 pb-0" src="../assets/img/papa.jpg" alt="Card image cap">
            <div class="card-body">
              <h5 class="card-title mb-3">Олегов Олег Олегович</h5>
              <p class="card-text mb-2"><b>Специализация:</b> Инвестиции</p>
              <p class="card-text"><b>Сектор::</b> Услуг</p>
              <a v-on:click.prevent="goToChat" class="btn btn-primary w-100">Выбрать</a>
            </div>
          </div>
        </div>

        <div class="col-6 mb-2">
          <div class="card text-center">
            <img class="card-img-top p-4 pb-0" src="../assets/img/mama.jpg" alt="Card image cap">
            <div class="card-body">
              <h5 class="card-title mb-3">Иванов Иван Иванович</h5>
              <p class="card-text mb-2"><b>Специализация:</b> Трейдинг</p>
              <p class="card-text"><b>Сектор::</b> Банковский</p>
              <a v-on:click.prevent="goToChat" class="btn btn-primary w-100">Выбрать</a>
            </div>
          </div>
        </div>

        <div class="col-6 mb-2">
          <div class="card text-center">
            <img class="card-img-top p-4 pb-0" src="../assets/img/papa.jpg" alt="Card image cap">
            <div class="card-body">
              <h5 class="card-title mb-3">Олегов Олег Олегович</h5>
              <p class="card-text mb-2"><b>Специализация:</b> Инвестиции</p>
              <p class="card-text"><b>Сектор::</b> Услуг</p>
              <a v-on:click.prevent="goToChat" class="btn btn-primary w-100">Выбрать</a>
            </div>
          </div>
        </div>

        <div class="col-6 mb-2">
          <div class="card text-center">
            <img class="card-img-top p-4 pb-0" src="../assets/img/papa.jpg" alt="Card image cap">
            <div class="card-body">
              <h5 class="card-title mb-3">Павлов Пал Палыч</h5>
              <p class="card-text mb-2"><b>Специализация:</b> Ивестиции</p>
              <p class="card-text"><b>Сектор::</b> Промышленный</p>
              <a v-on:click.prevent="goToChat" class="btn btn-primary w-100">Выбрать</a>
            </div>
          </div>
        </div>

        <div class="col-6 mb-2">
          <div class="card text-center">
            <img class="card-img-top p-4 pb-0" src="../assets/img/papa.jpg" alt="Card image cap">
            <div class="card-body">
              <h5 class="card-title mb-3">Сережин Сергей Сергеевич</h5>
              <p class="card-text mb-2"><b>Специализация:</b> Трейдинг</p>
              <p class="card-text"><b>Сектор::</b> Инф. технологий</p>
              <a v-on:click.prevent="goToChat" class="btn btn-primary w-100">Выбрать</a>
            </div>
          </div>
        </div>

      </div>
    </div>

  </section>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "ListExpertsView",
  created() {
    this.scrollToTop()
  },
  methods: {
    goToChat() {
      // переход в чат
      this.$router.push({name: 'ChatView'})
    },
    scrollToTop() {
      // при открытии страницы пролистывание вверх
      window.scrollTo(0, 0);
    }
  },
}
</script>

<style scoped>
.card-img-top {
  border-radius: 50%;
}

.card {
  background-color: #D8F0FB;
  border-radius: 10px;
}

.card-text {
  font-size: 14px;
}
</style>