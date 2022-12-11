export default {
    data() {
        return {}
    },
    created() {

    },
    methods: {
        goToLogin() {
            this.$router.push({name: 'LoginView'})
        },
        goToRegister() {
            this.$router.push({name: 'RegisterView'})
        },
        goToProfile(id) {
            console.log(id)
            // перейти на страницу экспертов
            this.$router.push({name: 'ProfileView'})
        },
        goToQuickStart() {
            this.$router.push({name: 'QuickStartView'})
        },
        goToDoctors() {
            this.$router.push({name: 'DoctorsView'})
        },
    }
}