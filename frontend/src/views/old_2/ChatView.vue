<template>
  <section class="chat h-100">
    <div class="container d-flex h-100 flex-column">

      <div v-on:click.prevent="goToProfile"  class="chat_name row align-items-center pt-3">
        <div class="name__arrow col-2">
          &lt;
        </div>
        <div class="name__username col-8">
          Иванов Иван Иванович
        </div>
        <div class="name__img col-2">
          <img class="name__img__item" src="../assets/img/mama.jpg">
        </div>
      </div>


      <div class="chat_body d-flex flex-column align-items-start mt-5">
        <div v-for="msg in chatHistory" class="massage_item"
             v-bind:class="[ isMyMassage(msg.sender) ? 'massage_item--client' : 'massage_item--expert']">
          {{ msg.text }}
        </div>
      </div>

      <div class="chat_send pb-3">
        <div class="form-group">
          <div class="row">
            <div class="col-9 me-0 pe-0">
              <textarea v-model="massage" class="form-control" id="exampleFormControlTextarea1" rows="1"
                        placeholder="Напишите сообщение..."></textarea>

            </div>
            <div class="col-3 ms-0 ps-0">
              <button v-on:click.prevent="sendNewMassage" class="button_item btn btn-primary w-100" type="submit">Send</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import {mapActions, mapState} from "vuex";

export default {
  name: "ChatView",
  data() {
    return {
      massage: '',
    }
  },
  computed: {
    ...mapState('chat', ['chatHistory',]),
    ...mapState('profile', ['id_dialog', "userInfo"]),
  },
  methods: {
    ...mapActions('chat', ['getChatHistory', 'sendMassage']),
    isMyMassage(id) {
      // проверяет являюсь ли я автором сообщения по id
      return parseInt(id) === this.userInfo.userId
    },
    sendNewMassage() {
      // отправляет сообщение
      let data_msg = {
        "message": {
          "dialogId": this.id_dialog,
          "text": this.massage,
          "messageType": "WIDGET",
          "data": "{\"widget\":\"custom data\"}",
          "mediaUrl": "https://cdn-icons-png.flaticon.com/512/945/945244.png"
        }
      }
      this.sendMassage({data: data_msg})
      this.massage = ''
    },
    goToProfile(){
      // переход в профиль
      this.$router.push({ name: 'ProfileView'})
    },

  },
  created() {
    this.getChatHistory({})
    let self = this;
    setInterval(function () {
      self.getChatHistory({})
    }, 5000);
  }
}
</script>

<style scoped>
.name__username, .name__arrow {
  font-size: 14px;
  font-family: Montserrat, sans-serif;
  font-weight: 700;
  cursor: pointer;
}

.name__img__item {
  max-width: 100%;
  height: auto;
  border-radius: 50%;
}

.massage_item {
  border-radius: 20px;
  /*margin-top: 20px;*/
  /*margin-bottom: 20px;*/
  margin: 6px 0;
  /*padding-top: 20px;*/
  /*padding-bottom: 20px;*/
  padding: 16px 10px;
}

.massage_item--client {
  background: #D8F0FB;
  align-self: end;
}

.massage_item--expert {
  background: #3CB5E8;
  align-self: start;
}


/* выравнивание чата */
.chat_name {
  flex: 0 0 auto;
}

.chat_body {
  flex: 1 0 auto;
}

.chat_send {
  /* 0 flex-grow, 0 flex-shrink, auto flex-basis */
  flex: 0 0 auto;
}

</style>