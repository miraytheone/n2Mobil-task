<template>
    <div class="post-container w-1124 h-896 top-100 left-288 absolute flex flex-col items-start">
      <div v-for="post in posts" :key="post.id" class="post-wrap">
        <div class="post">
          <span class="post-title">{{ post.title }}</span>
          <span class="post-summary">{{ post.content }}</span>
        </div>
        <div class="see-more">
          <a @click="openModal(post)" href="#" :id="'modal-btn-' + post.id" class="see-more-button w-131 h-32 absolute top-124 left-850 flex items-center justify-between font-medium text-sm">See More 
            <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-square-rounded-arrow-right" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#4F359B" fill="none" stroke-linecap="round" stroke-linejoin="round">
              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
              <path d="M12 16l4 -4l-4 -4" />
              <path d="M8 12h8" />
              <path d="M12 3c7.2 0 9 1.8 9 9s-1.8 9 -9 9s-9 -1.8 -9 -9s1.8 -9 9 -9z" />
            </svg>
          </a>
        </div>
      </div>
  
      <div v-if="selectedPost" ref="modal" id="modal" class="modal absolute z-10 max-w-1024 max-h-550 top-18 left-18 p-36 bg-white rounded-xl">
        <div ref="overlay" class="overlay fixed z-0 top-0 left-0 w-full h-full bg-black opacity-40"></div>
        <div class="modal-content">
          <span @click="closeModal" class="close">
            <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-square-rounded-x" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#2c3e50" fill="none" stroke-linecap="round" stroke-linejoin="round">
              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
              <path d="M10 10l4 4m0 -4l-4 4" />
              <path d="M12 3c7.2 0 9 1.8 9 9s-1.8 9 -9 9s-9 -1.8 -9 -9s1.8 -9 9 -9z" />
            </svg>
          </span>
          <span class="modal-title">{{ selectedPost.title }}</span>
          <div class="post-content">
            <div class="content">
              <p class="description" v-html="addNewLines(selectedPost.content)"></p>
            </div>
            <div class="comment-section">
              <span class="comment-title">Comments</span>
              <div class="comments">
                <div v-for="comment in selectedPost.comments" :key="comment.id" class="comment-wrap">
                    <img class="comment-img" src="https://img.freepik.com/free-photo/cheerful-curly-business-girl-wearing-glasses_176420-206.jpg?w=1480&t=st=1707381734~exp=1707382334~hmac=8cccad5a62128b680108fc56e887065cf7872ca883413a22b967e36ac91cde2e"/>
                    <div class="comment-content">
                        <span class="comment-name">{{  comment.name }}</span>
                        <p class="comment-dec"> {{  comment.text }}</p>
                    </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: "PostList",
    data() {
      return {
        posts: [],
        selectedPost: null,
        comments: []
      };
    },
    created() {
        const postsFromLocalStorage = localStorage.getItem('posts');
        const commentsFromLocalStorage = localStorage.getItem('comments');
        if (postsFromLocalStorage && commentsFromLocalStorage) {

            this.posts = JSON.parse(postsFromLocalStorage);
        }
        this.fetchPosts();
    
        
    },
 
    methods: {
        openModal(post) {
            console.log("Modal açılıyor");
            this.selectedPost = post;
          
            this.fetchComments(post.id);
            setTimeout(() => {
            this.$refs.modal.style.display = "block";
            this.$refs.overlay.style.display = "block";
            }, 100); // 100 milisaniye gecikme ekleyin
        },
        closeModal() {
            this.selectedPost = null;
            this.$refs.modal.style.display = "none";
            this.$refs.overlay.style.display = "none";
        },
        addNewLines(text) {
            return text.replace(/#COVID19/g, '#COVID19<br><br>');
        },
        fetchPosts() {
            axios.get(`http://127.0.0.1:8000/api/users/${this.$route.params.userId}/posts`)
            .then(response => {
                this.posts = response.data;
                localStorage.setItem('posts', JSON.stringify(response.data));
            })
            .catch(error => {
                console.error('Error fetching posts:', error);
            });
        },
        fetchComments(postId) {
            axios.get(`http://127.0.0.1:8000/api/posts/${postId}/comments/`)
                .then(response => {
                    this.selectedPost.comments = response.data;
                    localStorage.setItem('comments', JSON.stringify(response.data));

                })
                .catch(error => {
                    console.error('Error fetching comments:', error);
                });
        }
    }
  };
  </script>
  
  <style scoped>
  /* Gerekli stillendirme buraya eklenebilir */
  </style>
  