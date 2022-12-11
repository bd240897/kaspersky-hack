<template>

  <section class="profile h-100">
    <div class="christmas-tree h-100">

      <div class="profile__container container d-flex flex-column h-100">
        <div class="user mb-3">
          <div class="user__name row align-items-center pt-3">
            <div class="name__username col-9">
              <p class="ms-3">{{profile_info.first_name}}</p>
            </div>
            <div class="name__img col-3">
              <img class="name__img__item" v-bind:src="getAvatar(profile_info.avatar)">
            </div>
          </div>
        </div>


        <div class="compliment mb-3">
          <div class="compliment__container d-flex justify-content-center">
            <div class="compliment__container__container d-flex w-75 align-items-center">
              <div class="compliment__icon pe-3">
                <img class="compliment__icon__item" src="../assets/img/fortune-cookie.png">
              </div>
              <div class="compliment__text">
                Комиссия за хранение валюты на брокерских счетах не взимается
              </div>
              т
            </div>
          </div>
        </div>

        <div class="currency container mb-3">

          <div v-for="wallet in wallets_list" v-on:click="goToTransfer(wallet.id)" class="currency__element mb-3 row align-items-center">

            <div class="element__icon col-3 p-3">
              <img v-if="wallet.currency===RUB" class="element__icon__item ms-2" src="../assets/img/ruble.png">
              <img v-if="wallet.currency===USD" class="element__icon__item ms-2" src="../assets/img/dollar-coin.png">
              <img v-if="wallet.currency===EUR" class="element__icon__item ms-2" src="../assets/img/yuan.png">
            </div>

            <div class="element__text col-9">
              <div class="ms-5">
                <div class="element__text__price">
                  {{wallet.value}} {{wallet.currency}}
                </div>
                <div class="element__text__name">
                  {{wallet.name}}
                </div>
              </div>
            </div>
          </div>

        </div>

        <div class="open-wallet d-flex justify-content-center mb-3">
          <button class="button_item btn btn-primary py-3 p" type="submit">Создать счет</button>
        </div>

        <div class="open-wallet d-flex justify-content-center mb-3">
          <button v-on:click="goToHistory" class="button_item btn btn-primary py-3 p" type="submit">goToHistory</button>
        </div>

      </div>
    </div>
  </section>

</template>

<script>
import {mapActions, mapState} from "vuex";

export default {
  name: "ProfileView",
    data: function () {
    return {
      USD: "USD",
      RUB: "RUB",
      EUR: "EUR",
    }
  },
  computed: {
    ...mapState(['BASE_URL']),
    ...mapState('profile', ['profile_info', "wallets_list"]),
  },
  methods: {
    ...mapActions('profile', ["getProfileInfo", "getWalletsList",]),
    getAvatar(url) {
      return this.BASE_URL + url
    },
    goToTransfer(id) {
      console.log(id)
      // перейти на страницу экспертов
      this.$router.push({name: 'Transfer', params: { id: id }})
    },
    goToHistory() {
      this.$router.push({name: 'History'})
    },

  },
  created() {
    this.getProfileInfo({})
    this.getWalletsList({})
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300&display=swap');

html, body {
  height: 100%;
}

.profile {
  background: #26065A;
}

.christmas-tree {
  background: url(../assets/img/christmas-tree.png);
  /*background-position: 5vw 0; !* Положение фона *!*/
  background-repeat: no-repeat;
  background-size: 800px;
}

.name__username {
  font-size: 30px;
  font-family: Montserrat, sans-serif;
  font-weight: 700;
  color: white;
}

.name__img__item {
  max-width: 65px;
  height: auto;
  border-radius: 50%;
}

.compliment__icon__item {
  max-width: 65px;
  height: auto;
  border-radius: 50%;
}


.compliment__text {
  color: white;
  font-size: 16px;
}

.currency__element {
  background-color: #1C0542;
  border-radius: 20px;
  border: 2px solid #5c636a;
  cursor: pointer;

}

.currency__element:hover {
  border: 2px solid red;
}

.element__icon__item {
  max-width: 65px;
  height: auto;
  border-radius: 50%;
}

.element__text__price {
  color: white;
  font-size: 24px;
  font-family: Rubik, sans-serif;
  font-weight: 600;
}

.element__text__name {
  color: white;
  font-size: 20px;
  font-family: Rubik, sans-serif;
  font-weight: 300;
}

.button_item {
  /* фон */
  background-color: white;
  border-radius: 18px;
  border: 2px solid #5c636a;

  /* тексt */
  font-size: 16px;
  font-family: Rubik, sans-serif;
  font-weight: 600;
  color: black;
}
</style>