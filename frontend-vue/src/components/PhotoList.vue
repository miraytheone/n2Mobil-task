<template>
    <div>
      <router-link :to="{ name: 'AlbumsPage', params: { userId: userId }}">
        <div class="title">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="icon icon-tabler icon-tabler-square-rounded-arrow-left"
            width="44"
            height="44"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="#2c3e50"
            fill="none"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <path stroke="none" d="M0 0h24v24H0z" fill="none" />
            <path d="M12 8l-4 4l4 4" />
            <path d="M16 12h-8" />
            <path d="M12 3c7.2 0 9 1.8 9 9s-1.8 9 -9 9s-9 -1.8 -9 -9s1.8 -9 9 -9z" />
          </svg>
          <span>Go Albums</span>
        </div>
      </router-link>
      <div class="container">
        <div class="album-images">
          <img v-for="photo in photos" :key="photo.id" :src="photo.url" alt="Photo" />
        </div>
      </div>
    </div>
  </template>
  
 <script>
import axios from "axios";

export default {
  name: "PhotoList",
  components:{

  },
  data() {
    return {
      photos: [],
      userId: null,
    };
  },
  created() {
    // Check if user ID is available in local storage
    const storedUserId = localStorage.getItem('userId');
    
    if (storedUserId) {
        this.userId = storedUserId;
    } else {
        // If not available in local storage, check route parameters
        this.userId = this.$route.params.userId;
        localStorage.setItem('userId', this.userId);
    }

    if (this.userId) {
        this.fetchPhotos();
    }
},

  methods: {
    fetchPhotos() {
      axios
        .get(
          `http://127.0.0.1:8000/api/users/${this.$route.params.userId}/albums/${this.$route.params.albumId}/photos`
        )
        .then((response) => {
          this.photos = response.data;
          localStorage.setItem('userId', this.userId); 

        })
        .catch((error) => {
          console.error("Error fetching photos:", error);
        });
    },
  },
};
</script>
