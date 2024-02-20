<template>
    <div class="post-container w-1124 h-896 top-100 left-288 absolute flex flex-col items-start">
      <div class="todo-list w-653 h-768 top-156 left-296 mt-75">
        <div v-for="todo in todos" :key="todo.id" class="todo">
          <div class="checkbox-box">
            <input  
              v-model="todo.completed" 
              @change="updateTodo(todo)" 
              class="checkbox" 
              type="checkbox">
          </div>
          <span class="todo-text">{{ todo.task }}</span>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: "TodoList",
    data() {
      return {
        todos: []
      };
    },
    created() {
        const todosFromLocalStorage = localStorage.getItem('todos');
        if (todosFromLocalStorage) {
            this.todos = JSON.parse(todosFromLocalStorage);
        }
        this.fetchTodos(); 

    },
    methods: {
      fetchTodos() {
        axios.get(`http://127.0.0.1:8000/api/users/${this.$route.params.userId}/todos/`)
          .then(response => {
            this.todos = response.data;
            localStorage.setItem('todos', JSON.stringify(response.data));
          })
          .catch(error => {
            console.error('Error fetching todos:', error);
          });
      },
      updateTodo(todo) {
            axios.put(`http://127.0.0.1:8000/api/todos/${todo.id}/complete/`, {})
            .then(response => {
                console.log('Todo updated successfully:', response.data);
            })
            .catch(error => {
                console.error('Error updating todo:', error);
            });
        }

    }
  }
  </script>
  