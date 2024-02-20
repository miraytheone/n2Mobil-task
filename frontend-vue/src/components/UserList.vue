<template>
    <div class="container mx-auto mt-100 ml-260 grid grid-cols-3 gap-32">
         <div v-for="user in users" :key="user.id" class="card w-full h-370 p-24 border border-gray-300 rounded flex flex-col">
        <router-link :to="{ name: 'TodoPage', params: { userId: user.id } }">
            <div class="card-wrap">
                <div class="user-header">
                    <img class="user-photo" src="https://img.freepik.com/free-photo/cheerful-curly-business-girl-wearing-glasses_176420-206.jpg?w=1480&t=st=1707381734~exp=1707382334~hmac=8cccad5a62128b680108fc56e887065cf7872ca883413a22b967e36ac91cde2e"/>
                    <div class="user-general">
                        <p class="name">{{ user.name }}</p>
                        <p class="text">{{ user.email }}</p>
                        <p class="text">{{  user.phone }}</p>
                    </div>
                </div>
                <div class="user-info">
                    <div class="user-wrap">
                        <div class="icon-head"><svg  xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-map-pin-heart" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2c3e50" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                            <path d="M15 11a3 3 0 1 0 -3.973 2.839" />
                            <path d="M11.76 21.47a1.991 1.991 0 0 1 -1.173 -.57l-4.244 -4.243a8 8 0 1 1 13.657 -5.588" />
                            <path d="M18 22l3.35 -3.284a2.143 2.143 0 0 0 .005 -3.071a2.242 2.242 0 0 0 -3.129 -.006l-.224 .22l-.223 -.22a2.242 2.242 0 0 0 -3.128 -.006a2.143 2.143 0 0 0 -.006 3.071l3.355 3.296z" />
                            </svg>
                        <span class="info-header">Location</span></div>
                        <p class="text">{{  user.address.street }} {{ user.address.suite }} </p>
                        <p class="text">{{ user.address.zipcode }} / {{ user.address.city }}</p>

                    </div>
                    
                    <div class="user-wrap">
                        <div class="icon-head"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-building-skyscraper" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2c3e50" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                            <path d="M3 21l18 0" />
                            <path d="M5 21v-14l8 -4v18" />
                            <path d="M19 21v-10l-6 -4" />
                            <path d="M9 9l0 .01" />
                            <path d="M9 12l0 .01" />
                            <path d="M9 15l0 .01" />
                            <path d="M9 18l0 .01" />
                            </svg>
                        <span class="info-header">Company</span></div>
                        <p class="text">{{user.company.name}}</p>

                    </div>
                
                    <div class="user-wrap">
                        <div class="icon-head"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-world-share" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2c3e50" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                            <path d="M20.94 13.045a9 9 0 1 0 -8.953 7.955" />
                            <path d="M3.6 9h16.8" />
                            <path d="M3.6 15h9.4" />
                            <path d="M11.5 3a17 17 0 0 0 0 18" />
                            <path d="M12.5 3a16.991 16.991 0 0 1 2.529 10.294" />
                            <path d="M16 22l5 -5" />
                            <path d="M21 21.5v-4.5h-4.5" />
                            </svg>
                        <span class="info-header">Website</span></div>
                        <p class="text">{{ user.website }}</p>
                    </div>

                </div>
            </div>
        </router-link>
    </div>
          
    </div>
   
</template>
<script>
import axios from 'axios';

export default {
    name: "UserList",
    data() {
        return {
            users: []
        };
    },
    created() {
  
        const usersFromLocalStorage = localStorage.getItem('users');
        if (usersFromLocalStorage) {
   
            this.users = JSON.parse(usersFromLocalStorage);
        } 

            this.fetchUsers();
        
    },
    methods: {
        fetchUsers() {
            axios.get('http://127.0.0.1:8000/api/users/')
                .then(response => {
         
                    this.users = response.data;
                    localStorage.setItem('users', JSON.stringify(response.data));
                })
                .catch(error => {
                    console.error('Error fetching users:', error);
                });
            
        }
    }
}
</script>
