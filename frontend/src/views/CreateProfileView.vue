<template>
    <Navbar/>

    <section class="create_profile h-100">
        <div class="container d-flex flex-column align-items-center justify-content-center h-100">

            <div class="create_profile__header text-center text-size-header">
                Анкета владельца
            </div>

            <div class="create__form w-100">

                <div class="form__email form-group my-2 border border-primary p-2 rounded">
                    <label for="exampleInputEmail1" class="form-label">Имя</label>
                    <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
                           placeholder="Имя">
                </div>

                <div class="form__gender  form-group mb-2 border border-primary p-2 rounded">
                    <label class="form-label">Пол</label>

                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                        <label class="form-check-label" for="flexRadioDefault1">
                            Мужской
                        </label>
                    </div>

                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2"
                               checked>
                        <label class="form-check-label" for="flexRadioDefault2">
                            Женский
                        </label>
                    </div>

                </div>

                <div class="form__avatar mb-2 border border-primary p-2 rounded">
                    <label for="formFile" class="form-label">Аватар</label>
                    <input class="form-control" type="file" id="formFile">
                </div>

                <div class="form__button my-2">
                    <button class="button_item btn btn-primary w-100" type="submit">Отправить</button>
                </div>

            </div>
        </div>
    </section>
</template>

<script>
import Navbar from "@/components/Navbar";

export default {
  name: "CreateProfileView",
    components: {
    Navbar
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
</style>