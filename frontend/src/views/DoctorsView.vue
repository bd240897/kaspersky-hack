<template>
    <div class="treatment">
        <div class="container">

            <div class="treatment__header text-size-header  fw-bold text-center my-4">
                Ближайшие клиники в г. Москва
            </div>

            <div class="treatment__text text-size-body mb-2">
                Ниже приведен список наших портнеров у которых вы можете получить консультацию
            </div>

            <div class="treatment__doctors mb-2">
                <div class="doctor__item pb-2">

                    <div class="doctor__item__btn text-center text-size-header fw-bold px-3 py-4 rounded rounded-4"
                         v-b-toggle.collapse-1>
                        <spna> Клиника</spna>
                        Планеты животных
                    </div>

                    <b-collapse id="collapse-1" class="doctor__item__collapse mt-2 w-100" visible>
                        <b-card title="Планеты животных" sub-title="Вет. клиника" class="text-center">
                            <b-card-text>
                                <div class="address text-size-body text-center">
                                    <span>Адрес:</span>
                                    Дмитровское ш., 165дк6, Москва
                                </div>
                            </b-card-text>
                            <b-card-text>
                                <div class="map-responsive">
                                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d790.3582035308439!2d37.54216840688408!3d55.92387963415428!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46b539d43babf8db%3A0x6ff97ca09776e189!2z0JLQtdGC0LrQu9C40L3QuNC60LAgItCf0LvQsNC90LXRgtCwINC20LjQstC-0YLQvdGL0YUi!5e0!3m2!1sru!2sru!4v1670765124086!5m2!1sru!2sru"
                                            width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"
                                            referrerpolicy="no-referrer-when-downgrade"></iframe>
                                </div>
                            </b-card-text>

                            <div class="form__button my-2">
                                <b-button
                                        href="https://vet165.ru/"
                                        variant="primary"
                                        class="w-100"
                                >
                                    Записаться
                                </b-button>
                            </div>
                        </b-card>
                    </b-collapse>
                </div>

                <div class="doctor__item pb-2">

                    <div class="doctor__item__btn text-center text-size-header fw-bold px-3 py-4 rounded rounded-4"
                         v-b-toggle.collapse-2>
                        <spna> Клиника</spna>
                        Оберег
                    </div>

                    <b-collapse id="collapse-2" class="doctor__item__collapse mt-2 w-100">
                        <b-card title="Оберег" sub-title="Вет. клиника" class="text-center">
                            <b-card-text>
                                <div class="address text-size-body text-center">
                                    <span>Адрес:</span>
                                    Илимская ул., 5 корпус 1, Москва
                                </div>
                            </b-card-text>
                            <b-card-text>
                                <div class="map-responsive">
                                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d35794.628905222125!2d37.52822598439141!3d55.89450967323737!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46b5374292d03b3f%3A0xab7c07fd090e25a4!2z0J7QsdC10YDQtdCz!5e0!3m2!1sru!2sru!4v1670767264876!5m2!1sru!2sru"
                                            width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"
                                            referrerpolicy="no-referrer-when-downgrade"></iframe>
                                </div>
                            </b-card-text>

                            <div class="form__button my-2">
                                <b-button
                                        href="https://vet165.ru/"
                                        variant="primary"
                                        class="w-100"
                                >
                                    Записаться
                                </b-button>
                            </div>
                        </b-card>
                    </b-collapse>
                </div>

                <div class="doctor__item pb-2">

                    <div class="doctor__item__btn text-center text-size-header fw-bold px-3 py-4 rounded rounded-4"
                         v-b-toggle.collapse-3>
                        <spna> Клиника</spna>
                        Ахилл
                    </div>

                    <b-collapse id="collapse-3" class="doctor__item__collapse mt-2 w-100">
                        <b-card title="Ахилл" sub-title="Вет. клиника" class="text-center">
                            <b-card-text>
                                <div class="address text-size-body text-center">
                                    <span>Адрес:</span>
                                    Дубнинская ул., 32, Москва
                                </div>
                            </b-card-text>
                            <b-card-text>
                                <div class="map-responsive">
                                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d42556.658140072315!2d37.47468925709922!3d55.904143015145195!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46b54b3d00b801bb%3A0xa9eb45e76c065b7e!2z0JDRhdC40LvQuyB8INCS0LXRgtC10YDQuNC90LDRgNC90LDRjyDQutC70LjQvdC40LrQsCDQktC-0YHRgtC-0YfQvdC-0LUg0JTQtdCz0YPQvdC40L3QviB8INCS0LXRgtC60LvQuNC90LjQutCwLCDQstC10YLQsNC_0YLQtdC60LA!5e0!3m2!1sru!2sru!4v1670767438061!5m2!1sru!2sru"
                                            width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"
                                            referrerpolicy="no-referrer-when-downgrade"></iframe>
                                </div>
                            </b-card-text>

                            <div class="form__button my-2">
                                <b-button
                                        href="https://vet165.ru/"
                                        variant="primary"
                                        class="w-100"
                                >
                                    Записаться
                                </b-button>
                            </div>
                        </b-card>
                    </b-collapse>
                </div>
            </div>
        </div>

    </div>

  &#128512;
  &#128512;
  &#128512;
  &#128512;
</template>

<script>
export default {
  name: "DoctorsView"
}
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

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

    .color-header {

    }

    .text-family-header {

    }

    .text-family-body {

    }

    .video iframe {
        /*height: auto;*/
        /*width: 100%;*/
    }


    .map-responsive {
        overflow: hidden;
        padding-bottom: 56.25%;
        position: relative;
        height: 0;
    }

    .map-responsive iframe {
        left: 0;
        top: 0;
        height: 100%;
        width: 100%;
        position: absolute;
    }

    .doctor__item__btn {
        background-color: #a3c0f1;
    }
</style>