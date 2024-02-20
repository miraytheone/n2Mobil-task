<template>
    <SidebarTodo />
    <GoHome />
    <PostList />
</template>

<script>
import SidebarTodo from "@/components/SidebarTodo.vue"
import GoHome from "@/components/GoHome.vue"
import PostList from "@/components/PostList.vue";
export default{
    name: "PostsPage",
    components: {
        SidebarTodo,
        GoHome,
        PostList
    },
    metaInfo: {
      script: [
        { src: '../custom.js', async: true, defer: true }
      ],
    }
}
</script>
