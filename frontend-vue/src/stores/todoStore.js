import { defineStore } from 'pinia';
import axios from 'axios';

export const useTodoStore = defineStore({
  id: 'todo',
  state: () => ({
    todos: []
  }),
  actions: {
    async fetchTodos(userId) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/users/${userId}/todos/`);
        this.todos = response.data;
        localStorage.setItem('todos', JSON.stringify(response.data));
        console.log('Todos fetched successfully:', this.todos);
      } catch (error) {
        console.error('Error fetching todos:', error);
      }
    },
    async updateTodo(todo) {
      try {
        const response = await axios.put(`http://127.0.0.1:8000/api/todos/${todo.id}/complete/`, {});
        const updatedTodo = response.data;
        const index = this.todos.findIndex(item => item.id === updatedTodo.id);
        if (index !== -1) {
          this.todos.splice(index, 1, updatedTodo);
        }
        console.log('Todo updated successfully:', updatedTodo);
      } catch (error) {
        console.error('Error updating todo:', error);
      }
    }
  }
});
