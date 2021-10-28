<template>
  <div class="container">
    <h1>TIC TAC TOE</h1>
    <div class="grid">
      <div @click="action1(index)" class="cells is-clickable" v-for="(n, index) in arr" :key="index" >
          <span id="visible">{{ n }}</span>
      </div>
    </div>
    <div class="buttons">
      <button class=" is-clickable" @click="reset">RESET</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      arr: ['', '', '', '', '', '', '', '', ''],
      task: ["X","O"],
      flag: false,
    };
  },
  methods: {
    action1: function(index) {
      this.arr[index] = this.task[this.flag? 1 : 0];
      this.flag = !this.flag;
      this.arr.push('hi');
      this.arr.pop();
    },
    reset: function() {
      this.arr = ['', '', '', '', '', '', '', '', ''];
    },
  },
};
</script>

<style scoped>
.container {
  background-color: rgb(88, 80, 80);
  margin: 50px 50px 50px 50px;
}
.grid {
  display: grid;
  grid-template-columns: repeat(3, 100px);
  grid-template-rows: repeat(3, 100px);
  justify-content: center;
  padding: 50px 50px 50px 50px;
}
.cells {
  border: 2px solid black;
  background-color: rgb(68, 63, 63);
  display: flex;
  justify-content: center;
  align-items: center;
}
.cells:hover {
  background-color: rgb(107, 106, 106);
}
h1 {
  font-size: 30px;
  text-align: center;
  color: white;
}
.buttons {
  margin-top: 40px;
  display: flex;
  justify-content: center;
}
button {
  padding: 10px 10px 10px 10px;
  margin: 10px 10px 10px 10px;
  min-width: 100px;
  border-radius: 20%;
}
#visible {
  font-size: 40px;
  color: white;
}
</style>
