<template>
  <div class="container">
    <div class="scroll">
      <table class="center table is-hoverable is-striped">
        <tr>
          <th>
            Semester:
          </th>
          <th>Total credits:</th>
          <th>SGPA:</th>
        </tr>
        <tr v-for="(row, index) in subjects" :key="index">
          <td>
            <select
              v-model="subjects[index].sem"
              class="input"
              placeholder="Enter sem"
            >
              <option value="#" disabled selected hidden></option>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
              <option value="6">6</option>
              <option value="7">7</option>
              <option value="8">8</option>
            </select>
          </td>
          <td>
            <input
              v-model="subjects[index].credits"
              class="input"
              type="number"
              placeholder="Enter sem credits"
              min="0"
            />
          </td>
          <td>
            <input
              v-model="subjects[index].sgpa"
              class="input"
              type="number"
              placeholder="Enter sem sgpa"
              min="0"
            />
          </td>
          <td>
            <button
              @click="deleteRow(index)"
              class="button is-danger is-outlined"
            >
              <i class="fas fa-trash"></i>
            </button>
          </td>
        </tr>
      </table>
    </div>
    <div class="addBtn">
      <button
        @click="addRow"
        class="add button is-fullwidth  is-info is-outlined"
      >
        <i class="fas fa-plus"></i>Add Semester
      </button>
    </div>
    <div class="calculate">
      <button
        @click.once="calculateCgpa"
        class="calc button is-fullwidth  is-info"
      >
        Calculate
      </button>
    </div>
    <div class="final">
      <div class="result">
        Total Credits:
        <div class="ans">
          {{ this.totalCreds }}
        </div>
      </div>
      <div class="result">
        CGPA:
        <div class="ans">
          {{ this.result }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      result: null,
      totalCreds: null,
      subjects: [
        {
          sem: null,
          credits: null,
          sgpa: null,
        },
      ],
    };
  },
  methods: {
    addRow: function() {
      this.subjects.push({
        sem: null,
        credits: null,
        sgpa: null,
      });
    },
    deleteRow: function(index) {
      this.subjects.splice(index, 1);
      console.log(this.deleteRow);
    },
    calculateCgpa: function() {
        this.subjects.forEach((ele) => {
            this.totalCreds += parseFloat (ele.credits);
            this.result += ele.credits*ele.sgpa;
        })
        this.result = parseFloat (this.result/this.totalCreds).toFixed(2);
    },
  },
};
</script>

<style scoped>
.scroll {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 100%;
  max-height: 40vh;
  overflow-y: scroll;
  font: bold 16px arial;
}
.add {
  max-width: 60vh;
}
.addBtn {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding-top: 20px;
}
.calculate {
  padding-top: 20px;
  display: flex;
  justify-content: center;
}
.calc {
  max-width: 20vh;
}
.final {
  margin-top: 5vh;
  padding-top: 20px;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  background-color: rgb(235, 238, 240);
}
.result {
  font: bold 18px arial;
}
.ans {
  padding: 0.5em 0.5em 0.5em 0.5em;
  text-align: center;
  color: rgb(58, 101, 180);
  font-size: 1.5em;
}
</style>
