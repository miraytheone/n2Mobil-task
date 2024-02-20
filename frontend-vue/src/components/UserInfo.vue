<template>
    <div v-if="user" class="person w-228 h-68 mx-auto mb-20 border border-gray-300 rounded flex items-center">
                <img class="person-image" src="https://img.freepik.com/free-photo/cheerful-curly-business-girl-wearing-glasses_176420-206.jpg?w=1480&t=st=1707381734~exp=1707382334~hmac=8cccad5a62128b680108fc56e887065cf7872ca883413a22b967e36ac91cde2e"/>
                <div class="person-info">
                    <span class="person-name"> {{ user.name }} </span>
                    <div class="person-email">
                        <a :href="'mailto:' + user.email" > {{ user.email }} </a>
                    </div>
                </div>
            <div class="person-line w-228 border border-gray-300 transform rotate-0 mt-100 absolute"></div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            user: null,
        };
    },
    methods: {
        fetchUser() {
        const userId = this.$route.params.userId;
        axios.get(`http://127.0.0.1:8000/api/users/${userId}`)
            .then(response => {
            this.user = response.data;
            })
            .catch(error => {
            console.error('Kullanıcı bilgileri alınamadı:', error);
            });
        },
    },
    beforeRouteUpdate(to, from, next) {
        this.fetchUser();
        next();
    },
    created() {
        this.fetchUser();
    },
}
</script>
