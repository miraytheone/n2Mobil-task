<template>
    <SidebarTodo/>
   <PhotoList></PhotoList>
</template>

<script>
import PhotoList from '@/components/PhotoList.vue';
import SidebarTodo from '@/components/SidebarTodo.vue';

export default{
    name: "PhotosPage",
    components:{
    SidebarTodo,
    PhotoList
}
}
</script>