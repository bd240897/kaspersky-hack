<template>

  <section class="login h-100">
    <div class="container d-flex flex-column align-items-center justify-content-center h-100">
      <div class="login__header text-center text-size-header">
        Tail app (Регистрация)
      </div>

      <div class="login__error w-100">
        <b-alert v-for="field in error_massage" show dismissible>
          <div v-for="error in field">{{ error }}</div>
        </b-alert>
      </div>

      <div class="login__form w-100">
        <div class="form__email form-group my-2">
          <input v-model="form.username" type="email" class="form-control" id="exampleInputEmail1"
                 aria-describedby="emailHelp"
                 placeholder="Логин">
        </div>

        <div class="form__password form-group mb-2">
          <input v-model="form.password" type="password" class="form-control" id="exampleInputPassword1"
                 placeholder="Пароль">
        </div>

        <div class="form__repeat_password form-group mb-2">
          <input v-model="password_repeat" type="password" class="form-control" id="exampleInputPassword2"
                 placeholder="Повторите пароль">
        </div>

        <div class="form__button mb-2">
          <button v-on:click.prevent="getRegister" class="button_item btn btn-primary w-100" type="submit">
            Зарегистрироваться
          </button>
        </div>

        <p class="form_text_or text-center mb-2">или</p>

        <div class="form__button mb-2">
          <button v-on:click.prevent="goToLogin" class="button_item btn btn-primary w-100" type="submit">Войти</button>
        </div>
      </div>
    </div>
  </section>

  {{ error_massage }}
</template>

<script>
import goToSomewhere from "@/mixins/goToSomewhere";
import {mapActions} from "vuex";

export default {
  name: "RegisterView",
  mixins: [goToSomewhere],
  data() {
    return {
      form: {
        username: 'test1',
        password: '1234qwerS+',
        password_repeat: '1234qwerS+',
      },
      error_massage: ''
    }
  },
  methods: {
    ...mapActions('register', ["REGISTER"]),
    getRegister() {
      // залогиниться
      let data_login = {
        "username": this.form.username,
        "password": this.form.password
      }
      this.REGISTER({data: data_login})
          .catch(err => {
            console.log(err)
            if (err.response) {
              console.log("client received an error response (5xx, 4xx)")
              this.error_massage = err.response.data
            } else if (err.request) {
              console.log("client never received a response, or request never left")
            } else {
              console.log("anything else ")
            }
            return err
          })
    },
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

.bg-green {
  background-color: #00A88E;
}
</style>