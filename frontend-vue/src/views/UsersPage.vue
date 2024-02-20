<template>
    <SidebarComponent/>
    <div class="title">
        <span>All Users</span>
    </div>
        
    <UserList/>
      
           
       
</template>
<script>
import SidebarComponent from '@/components/SidebarComponent.vue';
import UserList from '@/components/UserList.vue';
export default{
    name: 'UsersPage',
    components:{
        SidebarComponent,
        UserList
    },
}
</script>