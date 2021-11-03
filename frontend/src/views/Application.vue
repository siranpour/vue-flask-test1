<template>
<div id="app">
<div class="p-5 mb-2 bg-primary text-dark"></div>


    <div class="mb-3">
      <label for="title" class="form-label">Please choose your course:</label>
        <select name="category_id" @change="onChange($event)" class="form-control">
          <option>--- Select Course ---</option>
            <option value="1">W261</option>
            <option value="2">W271</option>
        </select>
    </div>

    <b-form @submit="submit">
      <b-form-group id="input-group-2" label="Please enter your question" label-for="input-2">
        <b-form-textarea
          id="input-2"
          type="text"
          v-model="dataentry.question"
          placeholder="Type your question here"
        ></b-form-textarea>
      </b-form-group>
    <b-button pill v-on:click.prevent="submit" id="button-1" type="submit" variant="dark">Search</b-button>

     <b-form-group id="input-group-3" label="Answer" label-for="input-3">
       <b-form-textarea
         id="input-3"
         type="text"
         v-model="dataentry.answer"
         placeholder="Here is answer"

       ></b-form-textarea>
     </b-form-group>
  </b-form>

  </div>

</template>
<script>
import axios from 'axios';

export default{

  data(){
    return {
       dataentry:{
        question:"",
        answer:"",
      },
    };
  },
  methods:{
    submit:function(){
      const path = 'http://127.0.0.1:5000/dataentry'
      axios.post(path, {
        question:this.dataentry.question,
        answer:this.dataentry.answer,
        }
      )
      .then((response) => {
         console.log(response)
         this.dataentry.answer = response.data.result;
      })
      .catch(err =>{
        console.log(err);
      });
    },
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Castoro&display=swap');
#app {
  font-family: 'Lato', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
#input-group-1 {
  margin-left:25%;
  margin-bottom: 20px;
  width: 50%;
  padding-left: 80px;
  margin-top: 50px;
  font-weight:bold;

}
h3{
  margin-left:40%;
  font-family: 'Castoro', serif;
}
#input-group-2{
  margin-left:25%;
  margin-bottom: 20px;
  margin-top: 50px;
  width:50%;
  padding-left:80px;
  font-weight:bold;
}
#input-group-3{
  margin-left: 20px;
  margin-right: 20px;
}
#button-1{
margin-left:50%;
}
.nav-bar{
  padding-left: 50px;;
}
.link{
  padding-right:100px;
  font-size: 20px;
  color:white;
}

.mb-3{
  margin-left: 20px;
  margin-right: 20px;
}

.p-3 mb-2 bg-info text-dark{
  font-size: 100px;
}
</style>