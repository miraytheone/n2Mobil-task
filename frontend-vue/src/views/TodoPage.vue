<template>
    <SidebarTodo />
    <GoHome/>
    <TodoList :userId="this.$route.params.userId"/>
</template>

<script>
import SidebarTodo from "@/components/SidebarTodo.vue"
import TodoList from "@/components/TodoList.vue";
import GoHome from "@/components/GoHome.vue";
export default{
    name: "TodoPage",
    components:{
        SidebarTodo,
        TodoList,
        GoHome
    },
    
  
}
</script>
