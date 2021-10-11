const app = Vue.createApp({
    // template: <h1>Hello {{firstName}}</h1>',
    data() {
        return {
            firstName: 'John',
            lastName: 'Doe',
            email: 'johnny@gmail.com',
            gender: 'male',
            picture: 'http://randomuser.me/api/portraits/men/10.jpg',
        }
    },
    methods: {
        // getUser() {
        //     this.firstName = 'Selena'
        //     this.lastName = 'Smith'
        //     this.email = 'selena@gmail.com'
        //     this.gender = 'female'
        //     this.picture = 'http://randomuser.me/api/portraits/women/10.jpg'

        // },
        async getUser() {
            const res = await fetch('https://randomuser.me/api') //can use await only for asynchronous function like fetch
            const { results } = await res.json()

            // console.log(res)

            this.firstName = results[0].name.first
            this.lastName = results[0].name.last
            this.email = results[0].email
            this.gender = results[0].gender
            this.picture = results[0].picture.large
        }
    },
})
app.mount('#app')  

// code to mount this app into the div
// template is an object but data is a function, that's y it has parenthesis
// function will return an object
