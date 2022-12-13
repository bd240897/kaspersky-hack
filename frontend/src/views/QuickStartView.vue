<template>
  <Navbar/>

  <section class="make_photo">
    <div class="container ">

      <div class="make__header text-center text-size-header mb-4">
        How to take pictures
      </div>

      <div class="make__body text-size-body  mb-4">
        Take a photo of your pet's poops. The photo must be of good quality, and also not have unnecessary items.
        Then upload a photo to the form below and click the submit button.
      </div>

      <div class="make__img mb-2">
        <div class="img__header text-size-body text-center fw-bold">
          Preview of photo
        </div>
        <div class="img__container d-flex justify-content-center">
          <img v-if="!file" class="img__container__item w-100" src="../assets/img/poop_example.png"/>
          <img v-else v-bind:src="imagePreview" v-show="showPreview" class="img__container__item w-100"/>
        </div>
      </div>

      <div class="login__error w-100 mb-2">
        <b-alert v-if="error_massage" show dismissible>
          <div>{{ error_massage }}</div>
        </b-alert>
      </div>


      <div class="make__form w-100 mb-2 border border-primary p-2 rounded">
        <div class="form__photo mb-2">
          <label for="file" class="form-label">
            Upload photo
          </label>
          <input v-on:change="handleFileUpload()" class="create_body__file form-control" type="file" id="file"
                 ref="file" multiple>
        </div>

        <div class="form__button my-2">
          <button v-on:click="submitFile()" class="button_item btn btn-primary w-100" type="submit">
            Upload
          </button>
        </div>


      </div>
    </div>
  </section>
</template>

<script>
import goToSomewhere from "@/mixins/goToSomewhere";
import {mapActions} from "vuex";
import Navbar from "@/components/Navbar";

export default {
  name: "QuickStartView",
  components: {
    Navbar
  },
  mixins: [goToSomewhere],
  data() {
    return {
      file: '',
      error_massage: '',
      imagePreview: '',
      showPreview: true,
    }
  },
  methods: {
    ...mapActions("quick_start", ["SEND_PHOTO"]),

    // handleFileUpload() {
    //   this.file = this.$refs.file.files[0];
    // },

    handleFileUpload() {
      this.file = this.$refs.file.files[0];
      let reader = new FileReader();

      reader.addEventListener("load", function () {
        this.showPreview = true;
        this.imagePreview = reader.result;
      }.bind(this), false);

      if (this.file) {
        if (/\.(jpe?g|png|gif)$/i.test(this.file.name)) {
          reader.readAsDataURL(this.file);
        }
      }
    },
    submitFile() {
      let formData = new FormData();
      formData.append('file', this.file);


      // обнулим ошибки
      this.error_massage = '';

      this.SEND_PHOTO({formData: formData})
          .catch(err => {
            console.log(err)
            if (err.response) {
              console.log("client received an error response (5xx, 4xx)")
              this.error_massage = err.response.data.detail
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
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

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

.img__container__item {
  max-width: 350px;
  height: auto;
}
</style>