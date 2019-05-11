<template>
  <div class="todo">
    <form class="new_todo" v-on:submit.prevent="add_todo">
      <textarea required v-model="new_todo_text"/>
      <button>Add new todo</button>
    </form>
    <h1>Things to do:</h1>
    <ul>
      <li v-for="(todo, index) in todos" v-bind:key="index">
        <p>{{todo.date | moment("MM.DD, HH:mm")}}<br>{{todo.title | FirstUpper}}</p>
        <br>
        <div class="btn_cont">
          <button class="remove_btn" v-on:click="remove_todo(todo.id, index)">Remove</button>
          <button class="change_btn" v-on:click="change_btn(todo.id)">Change</button>
        </div>
        <form class="form_change" v-if="show_change.includes(todo.id)" v-on:submit.prevent="change_todo(index, todo.id)">
          <textarea v-model="todo.title" required/>
          <button>Confirm changes</button>
        </form>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Todos',
  data: function () {
    return {
      change_texts: [],
      show_change: [],
      new_todo_text: '',
      todos: []
    }
  },
  filters: {
    FirstUpper: function (value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    }
  },
  methods: {
    remove_todo: function (todoId, index) {
      axios.delete(this.$BASE_URL + 'note/' + todoId + '/')
      this.todos.splice(index, 1)
    },
    add_todo: function () {
      axios.post(this.$BASE_URL + 'notes/', {
        title: this.new_todo_text
      })
        .then(response => {
          this.new_todo_text = ''
          this.todos.unshift(response.data)
        })
    },
    update_todos: function () {
      axios.get(this.$BASE_URL + 'notes/')
        .then(response => {
          this.todos = response.data
          console.log(response.data)
        })
    },
    change_btn (id) {
      if (this.show_change.includes(id)) {
        this.show_change.splice(this.show_change.indexOf(id), 1)
      } else {
        this.show_change.push(id)
      }
    },
    change_todo (index, id) {
      axios.put(this.$BASE_URL + 'note/' + id + '/', {
        title: this.todos[index].title
      })
        .then(response => {
          for (let k in response.data) {
            this.todos[index][k] = response.data[k]
          }
        })
    }
  },
  created () {
    this.update_todos()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  $dark-blue: #191d21;
  $salt: #41b883;
  .todo{
    .new_todo{
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      textarea{
        width: 800px;
        max-width: 100%;
        height: 60px;
        border-radius: 6px;
        font-size: 16px;
      }

      & > button{
        width: 300px;
        height: 60px;
        border-radius: 30px;
        border: none;
        margin-top: 30px;
        font-size: 30px;
        color: $dark-blue;
        background: $salt;
        cursor: pointer;
      }
    }
    h1{
      font-size: 35px;
    }
    justify-content: center;
    align-items: center;
    display: flex;
    flex-direction: column;
    ul{
      text-align: left;
      max-width: 600px;
      list-style: none;
      padding-inline-start: 0;
      width: 100%;

      p{
        margin: 0 0 -14px 0;
        font-size: 26px;
        color: $dark-blue;
        word-break: break-word;
      }
      .btn_cont{
        display: flex;
        justify-content: space-between;
      }
      .btn_cont > button{
        width: 120px;
        height: 40px;
        border-radius: 15px;
        border: none;
        font-size: 20px;
        cursor: pointer;
        color: $dark-blue;
      }
      .remove_btn{
        background: #e64f3f;
      }
      .change_btn{
        background: #f7c34b;

      }

      .form_change{
        textarea{
        margin-top: 15px;
        width: 100%;
        height: 60px;
        border-radius: 6px;
        font-size: 16px;
      }
        button{
          width: 200px;
          height: 40px;
          border-radius: 10px;
          border: none;
          margin-top: 15px;
          font-size: 20px;
          color: $dark-blue;
          background: $salt;
          cursor: pointer;
        }
      }
    }
  }
</style>
