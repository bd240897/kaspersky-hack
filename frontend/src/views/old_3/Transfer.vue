<template>

  <section class="transfer h-100">
    <div class="transfer__container container christmas-tree h-100">
      <div class="header py-3">
        <div class="row">

          <div v-on:click="goToProfile" class="header__arrow col-3 d-flex align-items-center justify-content-center">
            <div class="header__arrow__item">&larr;</div>
          </div>

          <div class="header__text col-9 d-flex align-items-center justify-content-center">
            Перевод между счетами
          </div>
        </div>

      </div>

      <div class="wallet">

        <div class="choose text-center my-2">
          С какого счета переводить?
        </div>

        <div class="wallet__element d-flex flex-column align-items-center py-2 mb-4">
          <div class="wallet_name">
            cо счета: {{ wallet_info.name }}
          </div>
          <div class="wallet_value">
            {{ wallet_info.value }} {{ wallet_info.currency }}
          </div>
          <div class="wallet_currency">
            Валюта счёта: {{ wallet_info.currency }}
          </div>
        </div>

        <div class="choose text-center my-2">
          На какой счет переводить?
        </div>



        <div v-for="wallet in wallets_list" v-on:click="setWalletTo(wallet.id)" :class="{ wallet__element_red: wallet_to === wallet.id }" class="wallet__element d-flex flex-column align-items-center py-2 mb-4">
          <div class="wallet_name">
            {{wallet.name}}
          </div>
          <div class="wallet_value">
            {{wallet.value}} {{wallet.currency}}
          </div>
          <div class="wallet_currency">
            Валюта счёта: {{wallet.currency}}
          </div>
        </div>

      </div>

      <div class="value form-group mt-4">
        <input v-model="value" class="value__item form-control" type="text" id="exampleInputPassword1"
               placeholder="Сумма">
      </div>

      <div class="send mb-4">
        <button v-on:click="tryMakeTransfer" class="send_item btn btn-primary w-100" type="submit">Перевести</button>
      </div>
    </div>

  </section>
</template>

<script>
import {mapActions, mapState} from "vuex";

export default {
  name: "Transfer",
  data: function () {
    return {
      USD: "USD",
      RUB: "RUB",
      EUR: "EUR",
      wallet_to: '',
      value: '',
    }
  },
  computed: {
    ...mapState(['BASE_URL']),
    ...mapState('transfer', ["wallet_info"]),
    ...mapState('profile', ["wallets_list"]),
    wallet_from() {
      return this.wallet_info.id
    }
  },
  methods: {
    ...mapActions('transfer', ["getWalletInfo", "makeTransfer"]),
    goToProfile() {
      // перейти на страницу экспертов
      this.$router.push({name: 'ProfileView'})
    },
    setWalletTo(id) {
      console.log(id)
      this.wallet_to = id
    },
    tryMakeTransfer() {
      let data_msg = {
        "from_account": this.wallet_from,
        "to_account": this.wallet_to,
        "value": this.value,
      }
      this.makeTransfer({data: data_msg})
      this.goToHistory()
    },
    goToHistory() {
      this.$router.push({name: 'History'})
    },
  },
  created() {
    this.getWalletInfo({id: this.$route.params.id})
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

.choose {
  /* тексt */
  font-size: 26px;
  font-family: Rubik, sans-serif;
  font-weight: 600;
  color: white;
}

.wallet__element {
  background-color: #1C0542;
  border-radius: 20px;
  border: 3px solid white;
  cursor: pointer;
}

.wallet__element:hover{
    border: 3px solid red;
}

.wallet__element_red{
    border: 3px solid red;
}


.wallet_name, .wallet_value, .wallet_currency {
  color: white;

}

.wallet_name {
  font-size: 15px;
  font-family: Rubik, sans-serif;
  font-weight: 600;
}

.wallet_value {
  font-size: 20px;
  font-family: Rubik, sans-serif;
  font-weight: 600;
}

.wallet_currency {
  font-size: 14px;
  font-family: Rubik, sans-serif;
  font-weight: 300;
}

.value__item {
  border-radius: 20px;
  border: 2px solid #5c636a;
}

.send {
  margin-top: 80px;
}


.send_item {
  /* фон */
  background-color: white;
  border-radius: 15px;
  border: 2px solid #5c636a;

  /* тексt */
  font-size: 30px;
  font-family: Rubik, sans-serif;
  font-weight: 600;
  color: black;
}

</style>