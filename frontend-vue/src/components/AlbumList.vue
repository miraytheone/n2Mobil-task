<template>
    <div class="container mx-auto mt-100 ml-260 grid grid-cols-3 gap-32">
        <div v-for="album in albums" :key="album.id" class="card w-full h-370 p-24 border border-gray-300 rounded flex flex-col">
            <router-link :to="{ name: 'PhotosPage', params: {  userId: userId, albumId: album.id }}" class="router-link">
                <div class="images">
                    <div v-for="photo in getPhotos(album.id)" :key="photo.id" class="image">
                        <img  :src="photo.url"/> 
                    </div>
                </div>
                <p class="image-header">{{ album.title }}</p>
            </router-link>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "AlbumList",
    data() {
        return {
            albums: [],
            photos: {},
            userId: this.$route.params.userId
        };
    },
    created() {
        const albumsFromLocalStorage = localStorage.getItem('albums');
        if (albumsFromLocalStorage) {
   
            this.albums = JSON.parse(albumsFromLocalStorage);
        } 

        this.fetchAlbums();
    },
    methods: {
        fetchAlbums() {
            axios.get(`http://127.0.0.1:8000/api/users/${this.$route.params.userId}/albums`)
                .then(response => {
                    this.albums = response.data;
                })
                .catch(error => {
                    console.error('Error fetching albums:', error);
                });
        },
        getPhotos(albumId) { // fetchPhotos yerine getPhotos kullanıldı
            if (!this.photos[albumId]) { // Eğer zaten fotoğraflar yüklenmişse tekrar yükleme
                axios.get(`http://127.0.0.1:8000/api/users/${this.$route.params.userId}/albums/${albumId}/photos`)
                    .then(response => {
                        this.photos[albumId] = response.data.slice(0, 4);
                    })
                    .catch(error => {
                        console.error('Error fetching photos:', error);
                    });
            }
            return this.photos[albumId] || []; // Eğer fotoğraflar henüz yüklenmemişse boş bir dizi döndür
        }
    },
    watch: {
        '$route.params.albumId': function(newAlbumId, oldAlbumId) {
            if (newAlbumId !== oldAlbumId) {
                this.getPhotos(newAlbumId); // Albüm değiştiğinde yeni fotoğrafları al
            }
        }
    },
}
</script>
