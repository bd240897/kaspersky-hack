<template>
  <section class="transfer h-100">
    <div class="transfer__container container christmas-tree h-100">
      <div class="header py-3">
        <div class="row">

          <div v-on:click="goToProfile" class="header__arrow col-3 d-flex align-items-center justify-content-center">
            <div class="header__arrow__item">&larr;</div>
          </div>

          <div class="header__text col-9 d-flex align-items-center justify-content-center">
            История операций
          </div>
        </div>

      </div>

      <div class="wallet">

        <div v-for="history_item in history" class="wallet__element p-3 mb-2">
          <div>
            <div class="row mb-2">
              <div class="name__img col-3 d-flex align-items-center justify-content-center">
                <img class="name__img__item" src="../assets/img/transfer.png">
              </div>

              <div class="col-4 text-white d-flex align-items-center justify-content-center" style="font-size: 21px">
                {{ history_item.from_account_currency }} &rarr; {{ history_item.to_account_currency }}
              </div>
              <div class="col-5 text-white d-flex align-items-center justify-content-center" style="font-size: 21px">
                {{ history_item.value }} {{ history_item.from_account_currency }}
              </div>
            </div>

            <div class="text-white text-left" style="font-size: 14px">
              Перевод между счетами
            </div>
            <div class="text-white text-left" style="font-size: 12px">
              {{ setDataFormat(history_item.date) }}
            </div>

          </div>
        </div>

      </div>

    </div>

  </section>
</template>

<script>
import {mapActions, mapState} from "vuex";
import moment from 'moment'

export default {
  name: "History",
  data: function () {
    return {
      USD: "USD",
      RUB: "RUB",
      EUR: "EUR",
    }
  },
  computed: {
    ...mapState(['BASE_URL']),
    ...mapState('history', ['history',]),
  },
  methods: {
    ...mapActions('profile', ["getProfileInfo", "getWalletsList",]),
    ...mapActions('history', ["getHistory",]),
    getAvatar(url) {
      return this.BASE_URL + url
    },
    goToProfile(id) {
      console.log(id)
      // перейти на страницу экспертов
      this.$router.push({name: 'ProfileView'})
    },
    setDataFormat(data) {
      return moment(data).format('MM.DD.YYYY HH:mm')
    }
  },
  created() {
    this.getHistory({})
    setTimeout(() => {
      this.getHistory({})
      console.log("setTimeout")
    }, (3000));
  }
}
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300&display=swap');

html, body {
  height: 100%;
}

.transfer {
  background: #26065A;
}

.christmas-tree {
  background: url(../assets/img/christmas-tree.png);
  background-repeat: no-repeat;
  background-size: 800px;
}

.header__text {
  font-size: 20px;
  font-family: Rubik, sans-serif;
  font-weight: 600;
  color: white;
}

.header__arrow__item {
  /* тексt */
  font-size: 30px;
  font-family: Rubik, sans-serif;
  font-weight: 600;
  color: white;
  padding: 0 20px;

  border-radius: 20px;
  border: 2px solid #5c636a;
  cursor: pointer;
}


.header__arrow__item:hover {
  border: 2px solid red;
}


.wallet__element {
  background-color: #1C0542;
  border-radius: 20px;
  border: 3px solid white;
}


.name__img__item {
  max-width: 40px;
  height: auto;
  border-radius: 50%;
  border: 3px solid white;
}
</style>