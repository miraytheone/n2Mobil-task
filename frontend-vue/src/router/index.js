import { createRouter, createWebHistory } from 'vue-router'

import TodoPage from '@/views/TodoPage.vue'
import UsersPage from '@/views/UsersPage.vue'
import PostsPage from '@/views/PostsPage.vue'
import AlbumsPage from '@/views/AlbumsPage.vue'
import PhotosPage from '@/views/PhotosPage.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: UsersPage
    },
    {
      path: '/users/:userId/todos',
      name: 'TodoPage',
      component: TodoPage,
      props: true
    },
    {
      path: '/users/:userId/posts',
      name: 'PostPage',
      component: PostsPage,
      
    },
    {
      path: '/users/:userId/albums',
      name: 'AlbumsPage',
      component: AlbumsPage,
      props: true
    },
    {
      path: '/users/:userId/albums/:albumId/photos',
      name: 'PhotosPage',
      component: PhotosPage,
      props: true
    }
  ]
})


router.beforeEach((to, from, next) => {
  const userId = localStorage.getItem('userId');
  const albumId = localStorage.getItem('albumId');

  // Eğer userId veya albumId localStorage'da yoksa ve hedef rotaya gitmiyorsak, 
  // parametreleri tekrar ata ve yeniden yönlendir
  if ((!userId || !albumId) && to.name !== 'PhotosPage') {
    localStorage.setItem('userId', to.params.userId);
    localStorage.setItem('albumId', to.params.albumId);
    next({ ...to, replace: true });
  } else {
    next();
  }
});

export default router
