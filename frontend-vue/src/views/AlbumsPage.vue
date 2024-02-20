<template>
      <SidebarTodo />
      <GoHome />
      <AlbumList />
</template>
<script>
import SidebarTodo from '@/components/SidebarTodo.vue';
import GoHome from '@/components/GoHome.vue';
import AlbumList from '@/components/AlbumList.vue';

export default{
    name: 'AlbumsPage',
    components:{
        SidebarTodo,
        GoHome,
        AlbumList
    }
}
</script>