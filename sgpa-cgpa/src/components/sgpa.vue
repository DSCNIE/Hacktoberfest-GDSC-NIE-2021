<template>
  <div class="container">
    
    <div class="scroll">
      <table class="center table is-hoverable is-striped">
        <tr>
          <th>
            Course Code:
          </th>
          <th>
            Semester:
          </th>
          <th>credits:</th>
          <th>grade:</th>
        </tr>
        <tr v-for="(row, index) in subjects" :key="index">
          <td>
            <input
              v-model="subjects[index].course"
              class="input"
              type="text"
              placeholder="Enter course code"
            />
          </td>
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
              placeholder="Enter course credits"
              max="4"
              min="0"
            />
          </td>
          <td>
            <select v-model="subjects[index].grade" class="input">
              <option value="#"></option>
              <option value="S">S</option>
              <option value="A">A</option>
              <option value="B">B</option>
              <option value="C">C</option>
              <option value="D">D</option>
              <option value="F">F</option>
            </select>
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
        <i class="fas fa-plus"></i>Add Subject
      </button>
    </div>
    <div class="calculate">
      <button
        @click.once="calculateSgpa"
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
        SGPA:
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
          course: null,
          sem: null,
          credits: null,
          grade: null,
          perGrade: null,
        },
      ],
    };
  },
  methods: {
    addRow: function() {
      this.subjects.push({
        course: null,
        sem: null,
        credits: null,
        grade: null,
      });
    },
    deleteRow: function(index) {
      this.subjects.splice(index, 1);
      console.log(this.deleteRow);
    },
    calculateSgpa: function() {
      this.subjects.forEach((ele) => {
        switch (ele.grade) {
          case "S":
            ele.perGrade = 10;
            break;
          case "A":
            ele.perGrade = 9;
            break;
          case "B":
            ele.perGrade = 8;
            break;
          case "C":
            ele.perGrade = 7;
            break;
          case "D":
            ele.perGrade = 6;
            break;
          case "F":
            ele.perGrade = 0;
            break;
        }
        if (ele.sem == this.subjects[0].sem) {
          this.totalCreds += parseFloat(ele.credits);
          this.result += parseFloat(
            (ele.credits * ele.perGrade)
          );
          
        } else {
          this.totalCreds = NaN;
          this.result = NaN;
        }
      });
      this.result = parseFloat(this.result / this.totalCreds).toFixed(2);
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
