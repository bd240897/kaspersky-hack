<template>
  <section class="">
    <div class="container">

      <div class="profile d-flex flex-column">

        <div class="profile__avatar d-flex justify-content-center my-3">
          <img v-if="userInfo.avatar" class="img_item w-50" v-bind:src="userInfo.avatar">
          <img v-else class="img_item w-50" src="../assets/img/mama.jpg">
        </div>

        <div class="profile__name d-flex justify-content-center mb-3">
          <div class="profile__name w-25 d-flex justify-content-center text-center">
            {{ userInfo.surname }} {{ userInfo.middleName }} {{ userInfo.name }}
          </div>
        </div>

        <div class="profile__edit flex-column mb-3">
          <button class="edit__button_item btn btn-primary w-100" type="submit">Редактировать профиль</button>
        </div>

        <div class="profile__bag flex-column mb-3">
          <button class="bag__button_item btn btn-primary w-100" type="submit">Портфель</button>
        </div>

      </div>

      <div class="expert d-flex flex-column">

        <h1 class="poll__name text-center mb-3">Опрос</h1>

        <div class="poll__deals mb-3">
          <label for="exampleFormControlInput1" class="form-label">Введите количество совершенных сделок</label>
          <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="15">
        </div>

        <div class="poll__risk_profile mb-3">
          <select class="form-select" aria-label="Disabled select example" disabled>
            <option selected>Выберите ваш риск профиль</option>
            <option value="1">Консервативный</option>
            <option value="2">Умеренный</option>
            <option value="3">Агрессивный</option>
          </select>
        </div>

      </div>

    </div>
  </section>

  <section class="expert">
    <div class="container h-100 d-flex flex-column">
      <h1 class="text-center mb-3">Ваш текущий эксперт</h1>

      <div class="profile__avatar d-flex justify-content-center my-3">
        <img class="img_item w-50" src="../assets/img/papa.jpg">
      </div>

      <div class="profile__name d-flex justify-content-center mb-3">
        <div class="profile__name w-25 d-flex justify-content-center text-center">
          Иванов Иван Иванович
        </div>
      </div>

      <div class="profile__bag flex-column mb-3">
        <button v-on:click.prevent="goToExperts" class="bag__button_item btn btn-primary w-100" type="submit">Карточка эксперта</button>
      </div>

      <div class="profile__bag flex-column mb-3">
        <button class="bag__button_item btn btn-primary w-100" type="submit">Сменить эксперта</button>
      </div>

      <div class="profile__go_to_chat mb-3">
        <button v-on:click.prevent="goToChat" class="login__button btn btn-primary w-100" type="submit">
          Перейти к чатам
        </button>
      </div>
    </div>
  </section>

</template>

<script>
import {mapActions, mapState} from "vuex";

export default {
  name: "ProfileView",
  computed: {
    ...mapState('profile', ['userInfo',]),
  },
  methods: {
    ...mapActions('profile', ["getUserInfo", "getIdDialog"]),
    goToChat() {
      // перейти в чат
      this.$router.push({name: 'ChatView'})
    },
    goToExperts() {
      // перейти на страницу экспертов
      this.$router.push({name: 'ListExpertsView'})
    },
  },
  created() {
    this.getUserInfo({})
    this.getIdDialog({})
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

html, body {
  height: 100%;
}

.img_item {
  width: 100%;
  height: 100%;
  border-radius: 50%;
}

.profile__name {
  font-size: 36px;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  line-height: 30px;
}

.profile__button {
  width: 100%;
}

.button_item {
  background-color: #0275D8;
  font-size: 20px;
  font-family: Montserrat, sans-serif;
  font-weight: 400;
}
</style>