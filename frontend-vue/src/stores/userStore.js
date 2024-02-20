// store/user.js

import { defineStore } from 'pinia';
import axios from 'axios';
export const useUserStore = defineStore({
  id: 'user',
  state: () => ({
    users: []
  }),
  actions: {
    async fetchUsers() {
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
     
                this.users = response.data;
                localStorage.setItem('users', JSON.stringify(response.data));
            })
            .catch(error => {
                console.error('Error fetching users:', error);
            });
        
    },
    setUsers(users) {
      this.users = users;
    },
    saveUsersToLocal() {
      localStorage.setItem('users', JSON.stringify(this.users));
    },
    loadUsersFromLocal() {
        const localUsers = localStorage.getItem('users');
        console.log("Local Users:", localUsers);
        if (localUsers) {
          this.setUsers(JSON.parse(localUsers));
        }
      }
      
  }
});
