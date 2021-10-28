<template>
  <div class="container">
    <div class="result">
      <span class="answer">{{ calciResult || 0 }}</span>
    </div>
    <div class="grid">
      <div class=" column" v-for="(op, index) in elements" :key="index">
        <p
          class="allElements is-clickable is-hovered"
          :class="{
            'bg-green': ['C', '*', '/', '-', '+', '%', '='].includes(op), //include keyword to check available in array or not
          }"
          @click="action(op)"
        >
          {{ op }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      calciResult: "",
      operator: null,
      prevValue: "",
      elements: [
        "C",
        "*",
        "/",
        "-",
        "7",
        "8",
        "9",
        "+",
        "4",
        "5",
        "6",
        "%",
        "1",
        "2",
        "3",
        "=",
        "0",
        ".",
      ],
    };
  },
  methods: {
    action: function(op) {
      if (!isNaN(op) || op == ".") {
        // isNaN is not a number
        this.calciResult = this.calciResult + op + "";
        //empty string to convert it to string
      }
      if (op == "C") {
        this.calciResult = "";
      }
      if (op == "%") {
        this.calciResult = this.calciResult / 100 + "";
      }
      if (["*", "/", "+", "-"].includes(op)) {
        this.operator = op;
        this.prevValue = this.calciResult;
        this.calciResult = "";
        this.calciResult = this.prevValue + this.operator + this.calciResult;
      }
      if (op === "=") {
        this.calciResult = eval(
          this.calciResult
        );
        // eval keyword to evaluate operations passed as strings
        this.prevValue = "";
        this.operator = "";
        this.nextValue = "";
      }
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: rgb(46, 47, 49);
  margin: 50px 100px 50px 100px;
  padding: 10px 10px 10px 10px;
}
.result {
  display: flex;
  justify-content: flex-end;
  background-color: rgb(93, 97, 104);
  margin: 10px 10px 10px 10px;
  padding: 20px 20px 20px 20px;
  max-width: 60%;
  min-width: 400px;
}
.answer {
  font-size: 40px;
  color: rgb(213, 236, 211);
}
.grid {
  display: grid;
  grid-template-columns: repeat(4, 100px);
  /* grid-gap: 30px; */
  justify-content: center;
}
.allElements {
  font-size: 30px;
  text-align: center;
  background-color: rgb(107, 101, 101);
  border-radius: 10%;
  color: rgb(204, 230, 223);
}
.allElements:hover {
  background-color: rgb(165, 162, 162);
}
.bg-green {
  background-color: rgb(56, 139, 56);
}
</style>
