<template>
  <section class="login h-100">
    <div class="container d-flex flex-column h-100">

        <div class="snowflake h-25 mb-2">

        </div>

        <div class="block">
            <div class="login__header text-center mx-0 px-0 text-size-header">
               Tail app (Вход)
            </div>

            <div class="login__form w-100">
                <div class="form__email form-group my-4">
                    <input v-model="username" class="form__password__item form-control" type="text" id="exampleInputEmail1"
                           aria-describedby="emailHelp" placeholder="Логин">
                </div>

                <div class="form__password form-group my-4">
                    <input v-model="password" class="form__password__item form-control" type="password" id="exampleInputPassword2"
                           placeholder="Пароль">
                </div>

                <div class="login__button mb-4">
                    <button v-on:click.prevent="getLogin" class="button_item btn btn-primary w-100" type="submit">Войти</button>
                </div>

                <div class="login__button mb-4">
                    <button v-on:click.prevent="IS_PROFILE_EXISTS" class="button_item btn btn-primary w-100" type="submit">IS_PROFILE_EXISTS</button>
                </div>

                <p class="login_text_or text-center">или</p>

                <div class="login__button">
                    <button v-on:click.prevent="goToRegister" class="button_item btn btn-primary w-100" type="submit">Зарегистрироваться</button>
                </div>
            </div>
        </div>


    </div>
</section>
</template>

<script>
import {mapActions} from "vuex";
import goToSomewhere from "@/mixins/goToSomewhere";
export default {
  name: "LoginView",
  mixins: [goToSomewhere],
  data() {
    return {
      username: 'amid',
      password: '1',
    }
  },
  methods: {
    ...mapActions('login', ["LOGIN", "IS_PROFILE_EXISTS"]),
    getLogin() {
      // залогиниться
      let data_login = {
        "username": this.username,
        "password": this.password
      }
      this.LOGIN({data: data_login})
      // this.getUserInfo({})
    },

    // goToRegister() {
    //   this.$router.push({ name: 'Register'})
    // }
  },
  created() {
  },
}
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Oswald&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Cabin:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Rubik:wght@600&display=swap');

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